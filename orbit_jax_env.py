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
def make_initial_state_batch(batch_size: int, rng_key):
    """Initialize B games simultaneously using vmap over random keys."""
    keys = jax.random.split(rng_key, batch_size)
    return vmap(init_single_game)(keys)

def init_single_game(rng_key):
    """Initialize one game. Returns a dict of fixed-size JAX arrays."""
    # Simplified initialization for speed/demonstration.
    # In a full implementation, you'd translate generate_planets() here.
    planets = jnp.zeros((MAX_PLANETS, 8))

    # Example setup: 4 symmetric planets around the sun
    angles = jnp.array([0, jnp.pi/2, jnp.pi, 3*jnp.pi/2])
    r = 30.0
    x = CENTER + r * jnp.cos(angles)
    y = CENTER + r * jnp.sin(angles)

    planets = planets.at[:4, 0].set(jnp.arange(4)) # ids 0-3
    planets = planets.at[0, 1].set(0) # Player 0 owns planet 0
    planets = planets.at[2, 1].set(1) # Player 1 owns planet 2
    planets = planets.at[[1,3], 1].set(-1) # 1 and 3 are neutral
    planets = planets.at[:4, 2].set(x) # x
    planets = planets.at[:4, 3].set(y) # y
    planets = planets.at[:4, 4].set(2.0) # radius
    planets = planets.at[:4, 5].set(10.0) # ships
    planets = planets.at[:4, 6].set(1.0) # production

    # Pad rest with -2 (invalid)
    planets = planets.at[4:, 1].set(-2)

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
def step_batch(states: dict, actions: jnp.ndarray, batch_size: int) -> dict:
    """
    Step B games forward simultaneously.

    Args:
        states:  Pytree of arrays, each shape (B, ...)
        actions: Shape (B, N_PLAYERS, MAX_MOVES, 3)
                 Each move: [from_planet_id, angle, num_ships]
    """
    new_states, rewards, dones = vmap(step_single)(states, actions)
    return new_states, rewards, dones


def step_single(state: dict, action: jnp.ndarray) -> tuple:
    planets = state["planets"]
    fleets  = state["fleets"]
    step    = state["step"]
    omega   = state["angular_velocity"]

    # 1. ROTATE ORBITING PLANETS
    px = planets[:, 2]
    py = planets[:, 3]
    orbital_r = jnp.sqrt((px - CENTER)**2 + (py - CENTER)**2)
    is_orbiting = (orbital_r + planets[:, 4]) < ROTATION_RADIUS_LIMIT

    angles = jnp.arctan2(py - CENTER, px - CENTER)
    new_angles = angles + omega
    new_x = jnp.where(is_orbiting, CENTER + orbital_r * jnp.cos(new_angles), px)
    new_y = jnp.where(is_orbiting, CENTER + orbital_r * jnp.sin(new_angles), py)
    planets = planets.at[:, 2].set(new_x).at[:, 3].set(new_y)

    # 2. PROCESS ACTIONS — launch fleets
    fleets, next_fleet_id = _launch_fleets(planets, fleets, action, state["next_fleet_id"])

    # 3. MOVE FLEETS
    fleets = _advance_fleets(fleets)

    # 4. FLEET-PLANET COLLISIONS
    planets, fleets = _resolve_collisions(planets, fleets)

    # 5. PRODUCTION
    is_owned = planets[:, 1] >= 0
    new_ships = planets[:, 5] + jnp.where(is_owned, planets[:, 6], 0.0)
    planets = planets.at[:, 5].set(jnp.clip(new_ships, 0, 999))

    # 6. CHECK TERMINAL CONDITION
    p0_alive = jnp.any((planets[:, 1] == 0)) | jnp.any((fleets[0, :, 0] > 0))
    p1_alive = jnp.any((planets[:, 1] == 1)) | jnp.any((fleets[1, :, 0] > 0))
    done = (~p0_alive) | (~p1_alive) | (step >= 499)

    rewards = jnp.where(
        done,
        jnp.array([jnp.where(p0_alive, 1.0, -1.0),
                   jnp.where(p1_alive, 1.0, -1.0)]),
        jnp.zeros(N_PLAYERS)
    )

    new_state = {
        **state,
        "planets": planets,
        "fleets": fleets,
        "next_fleet_id": next_fleet_id,
        "step": step + 1,
        "done": done
    }
    return new_state, rewards, done


def _advance_fleets(fleets):
    ships = fleets[:, :, 6]
    speed = jnp.minimum(SHIP_SPEED, SHIP_SPEED / jnp.sqrt(jnp.maximum(ships, 1)))
    dx = speed * jnp.cos(fleets[:, :, 4])
    dy = speed * jnp.sin(fleets[:, :, 4])

    new_x = fleets[:, :, 2] + dx
    new_y = fleets[:, :, 3] + dy

    # Check out of bounds
    oob = (new_x < 0) | (new_x > BOARD_SIZE) | (new_y < 0) | (new_y > BOARD_SIZE)

    # Check sun collision (approximate with a point-to-center check for speed)
    sun_dist = jnp.sqrt((new_x - CENTER)**2 + (new_y - CENTER)**2)
    hits_sun = sun_dist <= SUN_RADIUS

    dead = oob | hits_sun

    fleets = fleets.at[:, :, 2].set(new_x)
    fleets = fleets.at[:, :, 3].set(new_y)

    # Zero out dead fleets
    fleets = jnp.where(dead[..., None], jnp.zeros_like(fleets), fleets)

    return fleets


def _launch_fleets(planets, fleets, action, next_fleet_id):
    def launch_for_player(p_id, p_fleets, p_action, p_planets, curr_id):
        move = p_action[0] # Just take first move for now
        src_id = jnp.int32(move[0])
        angle = move[1]
        ships = move[2]

        is_valid = (src_id >= 0) & (ships > 0)

        src_planet_idx = jnp.argmax(p_planets[:, 0] == src_id)
        src_planet = p_planets[src_planet_idx]

        valid_launch = is_valid & (src_planet[1] == p_id) & (src_planet[5] >= ships)

        empty_fleet_idx = jnp.argmax(p_fleets[:, 0] == 0)

        new_fleet = jnp.array([
            curr_id + 1,
            p_id,
            src_planet[2] + (src_planet[4] + 0.1) * jnp.cos(angle),
            src_planet[3] + (src_planet[4] + 0.1) * jnp.sin(angle),
            angle,
            src_id,
            ships
        ])

        p_fleets = jnp.where(valid_launch, p_fleets.at[empty_fleet_idx].set(new_fleet), p_fleets)
        curr_id = curr_id + jnp.where(valid_launch, 1, 0)
        return p_fleets, curr_id

    f0, next_id_1 = launch_for_player(0, fleets[0], action[0], planets, next_fleet_id)
    f1, next_id_2 = launch_for_player(1, fleets[1], action[1], planets, next_id_1)

    new_fleets = jnp.stack([f0, f1])
    return new_fleets, next_id_2

def _resolve_collisions(planets, fleets):
    p_x = planets[:, 2]
    p_y = planets[:, 3]
    p_r = planets[:, 4]

    flat_fleets = fleets.reshape(-1, 7)
    f_x = flat_fleets[:, 2]
    f_y = flat_fleets[:, 3]
    f_active = flat_fleets[:, 0] > 0

    dx = f_x[:, None] - p_x[None, :]
    dy = f_y[:, None] - p_y[None, :]
    dist = jnp.sqrt(dx**2 + dy**2)

    collisions = dist <= p_r[None, :]
    fleet_hits = jnp.any(collisions, axis=1) & f_active

    flat_fleets = jnp.where(fleet_hits[:, None], jnp.zeros_like(flat_fleets), flat_fleets)
    new_fleets = flat_fleets.reshape(2, MAX_FLEETS, 7)

    return planets, new_fleets
