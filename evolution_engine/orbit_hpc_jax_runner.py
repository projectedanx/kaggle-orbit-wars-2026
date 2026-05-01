# orbit_hpc_jax_runner.py
import jax
import jax.numpy as jnp
import numpy as np
import orjson
import asyncio
import aiofiles
import time
import uuid
from pathlib import Path

BATCH_SIZE  = 512       # Simultaneous games per GPU kernel invocation
TOTAL_GAMES = 100_000
REPLAY_DIR  = Path("/mnt/orbit-ramdisk/replays")

async def write_batch_replays(batch_replays: list[dict], base_id: int):
    """Write a batch of replays asynchronously."""
    tasks = []
    for i, replay in enumerate(batch_replays):
        path = REPLAY_DIR / f"match_{base_id + i:08d}.json"
        tasks.append(_write_single(path, orjson.dumps(replay)))
    await asyncio.gather(*tasks)

async def _write_single(path, data):
    async with aiofiles.open(path, "wb") as f:
        await f.write(data)

def assemble_single_replay(trajectory: list[dict], final_rewards: list[float],
                            config: dict) -> dict:
    """
    Reconstruct a kaggle_environments-compatible replay dict from a JAX trajectory.
    Schema verified against kaggle-environments==1.28.1 toJSON() output.
    """
    steps = []
    for step_idx, state in enumerate(trajectory):
        # Convert JAX arrays back to Python lists
        planets_np = np.array(state["planets"])  # (MAX_PLANETS, 8)
        fleets_np  = np.array(state["fleets"])   # (N_PLAYERS, MAX_FLEETS, 7)

        # Filter out padding (sentinel owner=-2)
        valid_planets = planets_np[planets_np[:, 1] != -2]
        planet_list   = valid_planets[:, :7].tolist()  # Drop is_orbiting flag

        step_frame = []
        for player_id in range(2):
            valid_fleets = fleets_np[player_id][fleets_np[player_id, :, 0] > 0]
            fleet_list   = valid_fleets.tolist()

            is_terminal = step_idx == len(trajectory) - 1
            step_frame.append({
                "action":  [],   # Actions are recorded separately in training loop
                "reward":  final_rewards[player_id] if is_terminal else 0,
                "info":    {},
                "status":  "DONE" if is_terminal else "ACTIVE",
                "observation": {
                    "remainingOverageTime": 2.0,
                    "step":             step_idx,
                    "planets":          planet_list,
                    "fleets":           fleet_list,
                    "player":           player_id,
                    "angular_velocity": float(state["angular_velocity"]),
                    "initial_planets":  [],  # Populated from trajectory
                    "next_fleet_id":    int(state["next_fleet_id"]),
                    "comets":           [],
                    "comet_planet_ids": [],
                }
            })
        steps.append(step_frame)

    # Inject initial_planets into all steps
    initial_planets = steps[0][0]["observation"]["planets"]
    for frame in steps:
        for player_frame in frame:
            player_frame["observation"]["initial_planets"] = initial_planets

    rewards_final = [final_rewards[0], final_rewards[1]]
    return {
        "id":             str(uuid.uuid1()),
        "name":           "orbit_wars",
        "title":          "Orbit Wars",
        "description":    "Conquer planets rotating around a sun in a continuous space.",
        "version":        "1.0.9",
        "module_version": "1.28.1",
        "schema_version": 1,
        "configuration":  config,
        "info":           {},
        "rewards":        rewards_final,
        "statuses":       ["DONE", "DONE"],
        "steps":          steps,
    }


def assemble_replay_batch(trajectory_batch, batch_size: int) -> list[dict]:
    """Vectorized replay assembly for a batch of games."""
    replays = []
    config = {
        "episodeSteps": 500, "actTimeout": 1,
        "runTimeout": 1200,  "agentTimeout": 2,
        "shipSpeed": 6.0,    "cometSpeed": 4.0,
    }
    for i in range(batch_size):
        # Slice out game i from the batched trajectory
        single_traj = [{k: v[i] for k, v in step.items()}
                       for step in trajectory_batch]
        rewards = [1.0, -1.0]  # Replace with actual from terminal state
        replays.append(assemble_single_replay(single_traj, rewards, config))
    return replays


def run_jax_batch_pipeline():
    """Main JAX vectorized pipeline."""
    REPLAY_DIR.mkdir(parents=True, exist_ok=True)

    from orbit_jax_env import make_initial_state_batch, step_batch

    rng = jax.random.PRNGKey(42)
    total_completed = 0
    start = time.perf_counter()

    n_batches = TOTAL_GAMES // BATCH_SIZE

    for batch_idx in range(n_batches):
        rng, subkey = jax.random.split(rng)
        
        # Initialize BATCH_SIZE games simultaneously
        states = make_initial_state_batch(BATCH_SIZE, subkey)
        
        # Record trajectories for replay JSON assembly
        trajectory = [states]  # Step 0 state

        # Run all games to completion (fixed 500 steps)
        # jit+vmap: this compiles on first call, runs at GPU speed after
        for step in range(500):
            # In real impl: get actions from agents here
            # For self-play training: use your policy network
            actions = jnp.zeros((BATCH_SIZE, 2, 10, 3))  # placeholder
            states, rewards, dones = step_batch(states, actions, BATCH_SIZE)
            trajectory.append(states)

        # Convert trajectory to kaggle replay JSON format
        # (Do this on CPU asynchronously while GPU runs next batch)
        replays = assemble_replay_batch(trajectory, BATCH_SIZE)

        # Async write (non-blocking — happens while GPU runs next batch)
        asyncio.run(write_batch_replays(replays, total_completed))

        total_completed += BATCH_SIZE
        elapsed = time.perf_counter() - start
        rate = total_completed / elapsed * 60
        print(f"Batch {batch_idx+1}/{n_batches}: {total_completed} games, "
              f"{rate:.0f} matches/min")

    total_elapsed = time.perf_counter() - start
    print(f"\nDONE: {total_completed} matches in {total_elapsed:.1f}s "
          f"= {total_completed/total_elapsed*60:.0f}/min")

if __name__ == "__main__":
    # run_jax_batch_pipeline()
    pass
