# orbit_jax_env.py — JAX-native Orbit Wars batch stepper
# Replaces kaggle_environments entirely for the hot simulation loop.
# Replay JSON is re-assembled from recorded state arrays at the end.

import jax
import jax.numpy as jnp
from jax import jit, vmap, lax
import numpy as np
from functools import partial

# =========================================================
# GAME CONSTANTS (from orbit_wars.py source)
# =========================================================
BOARD_SIZE           = 100.0
CENTER               = 50.0
SUN_RADIUS           = 10.0
ROTATION_RADIUS_LIMIT= 50.0
SHIP_SPEED           = 6.0
MAX_PLANETS          = 64     # Upper bound for fixed-size arrays
MAX_FLEETS           = 128    # Upper bound per player
N_PLAYERS            = 2

# =========================================================
# GAME STATE AS PYTREE (JAX-compatible fixed-size arrays)
# =========================================================
# Orbit Wars uses variable-length planet/fleet lists.
# JAX requires fixed shapes. We pad with a sentinel owner=-2.

def make_initial_state_batch(batch_size: int, rng_key):
    """
    Initializes a batch of games simultaneously using vmap over random keys.

    [⊘] Contradiction: Dynamic game lengths mapped to fixed-size JAX tensors.

    Args:
        batch_size (int): The number of games to initialize in parallel.
        rng_key (jax.random.PRNGKey): The JAX pseudorandom number generator key.

    Returns:
        dict: A Pytree of batched JAX arrays representing initial states.
    """
    keys = jax.random.split(rng_key, batch_size)
    # Each game's initial state — vectorized via vmap
    return vmap(init_single_game)(keys)

def init_single_game(rng_key):
    """
    Initializes a single game, returning a dictionary of fixed-size JAX arrays.

    Args:
        rng_key (jax.random.PRNGKey): The PRNG key for randomizing initial state.

    Returns:
        dict: The initial game state.
    """
    # Planet state: [id, owner, x, y, radius, ships, production, is_orbiting]
    # Pad to MAX_PLANETS with is_valid=False
    planets = jnp.zeros((MAX_PLANETS, 8))  # 8 features per planet
    # ... (generation logic translated from generate_planets())

    state = {
        "planets":          planets,          # (MAX_PLANETS, 8)
        "fleets":           jnp.zeros((N_PLAYERS, MAX_FLEETS, 7)),  # (2, MAX_FLEETS, 7)
        "step":             jnp.int32(0),
        "angular_velocity": jax.random.uniform(rng_key, minval=0.01, maxval=0.05),
        "next_fleet_id":    jnp.int32(0),
        "done":             jnp.bool_(False),
    }
    return state


@partial(jit, static_argnums=(2,))
def step_batch(states: dict, actions: jnp.ndarray, batch_size: int) -> tuple:
    """
    Steps a batch of games forward simultaneously using JIT compilation.
    
    Args:
        states (dict):  Pytree of arrays, each shape (B, ...).
        actions (jnp.ndarray): Shape (B, N_PLAYERS, MAX_MOVES, 3). Each move is [from_planet_id, angle, num_ships].
        batch_size (int): The number of games in the batch.

    Returns:
        tuple: (new_states, rewards, dones)
            new_states: Updated Pytree of arrays.
            rewards: Shape (B, N_PLAYERS).
            dones: Shape (B,) bool.
    """
    # vmap the single-game step over the batch dimension
    new_states, rewards, dones = vmap(step_single)(states, actions)
    return new_states, rewards, dones


def step_single(state: dict, action: jnp.ndarray) -> tuple:
    """
    Advances a single game state by one frame. Pure JAX, JIT-compilable.

    Args:
        state (dict): The current game state.
        action (jnp.ndarray): The action tensor for all players.

    Returns:
        tuple: (new_state, rewards, done)
    """
    planets = state["planets"]      # (MAX_PLANETS, 8)
    fleets  = state["fleets"]       # (N_PLAYERS, MAX_FLEETS, 7)
    step    = state["step"]
    omega   = state["angular_velocity"]

    # 1. ROTATE ORBITING PLANETS
    # Determine which planets orbit: orbital_radius + radius < ROTATION_RADIUS_LIMIT
    px = planets[:, 2]
    py = planets[:, 3]
    orbital_r = jnp.sqrt((px - CENTER)**2 + (py - CENTER)**2)
    is_orbiting = (orbital_r + planets[:, 4]) < ROTATION_RADIUS_LIMIT

    # Rotate by angular_velocity
    angles = jnp.arctan2(py - CENTER, px - CENTER)
    new_angles = angles + omega
    new_x = jnp.where(is_orbiting, CENTER + orbital_r * jnp.cos(new_angles), px)
    new_y = jnp.where(is_orbiting, CENTER + orbital_r * jnp.sin(new_angles), py)
    planets = planets.at[:, 2].set(new_x).at[:, 3].set(new_y)

    # 2. PROCESS ACTIONS — launch fleets
    # (Translation of process_moves() from orbit_wars.py)
    # For each valid move in action[player_id], add fleet to state
    fleets = _launch_fleets(planets, fleets, action, step)

    # 3. MOVE FLEETS
    fleets = _advance_fleets(fleets)

    # 4. FLEET-PLANET COLLISIONS → ownership changes
    planets, fleets = _resolve_collisions(planets, fleets)

    # 5. PRODUCTION — owned planets generate ships
    is_owned = planets[:, 1] >= 0
    new_ships = planets[:, 5] + jnp.where(is_owned, planets[:, 6], 0.0)
    planets = planets.at[:, 5].set(jnp.clip(new_ships, 0, 999))

    # 6. CHECK TERMINAL CONDITION
    # A player loses if they own 0 planets AND 0 fleets
    p0_alive = jnp.any((planets[:, 1] == 0)) | jnp.any((fleets[0, :, 0] > 0))
    p1_alive = jnp.any((planets[:, 1] == 1)) | jnp.any((fleets[1, :, 0] > 0))
    done = (~p0_alive) | (~p1_alive) | (step >= 499)

    rewards = jnp.where(
        done,
        jnp.array([jnp.where(p0_alive, 1.0, -1.0),
                   jnp.where(p1_alive, 1.0, -1.0)]),
        jnp.zeros(N_PLAYERS)
    )

    new_state = {**state, "planets": planets, "fleets": fleets,
                 "step": step + 1, "done": done}
    return new_state, rewards, done


# Helper: advance fleet positions
def _advance_fleets(fleets):
    """
    Advances fleet positions based on velocity and ship count constraints.

    Args:
        fleets (jnp.ndarray): The current fleets tensor.

    Returns:
        jnp.ndarray: The updated fleets tensor.
    """
    # Speed formula: min(SHIP_SPEED, SHIP_SPEED / sqrt(ships))
    ships = fleets[:, :, 6]
    speed = jnp.minimum(SHIP_SPEED, SHIP_SPEED / jnp.sqrt(jnp.maximum(ships, 1)))
    dx = speed * jnp.cos(fleets[:, :, 4])
    dy = speed * jnp.sin(fleets[:, :, 4])
    fleets = fleets.at[:, :, 2].add(dx)
    fleets = fleets.at[:, :, 3].add(dy)
    return fleets

# Stub helpers to make the module valid since they are omitted from the markdown
def _launch_fleets(planets, fleets, action, step):
    """
    Processes fleet launch actions and adds them to the active state.

    Args:
        planets (jnp.ndarray): The current planets tensor.
        fleets (jnp.ndarray): The current fleets tensor.
        action (jnp.ndarray): The action tensor.
        step (int): The current simulation step.

    Returns:
        jnp.ndarray: Updated fleets.
    """
    return fleets

def _resolve_collisions(planets, fleets):
    """
    Resolves fleet-planet collisions and handles ownership transfers.

    Args:
        planets (jnp.ndarray): The current planets tensor.
        fleets (jnp.ndarray): The current fleets tensor.

    Returns:
        tuple: (updated_planets, updated_fleets)
    """
    return planets, fleets
