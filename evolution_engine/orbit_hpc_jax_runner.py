import jax
import jax.numpy as jnp
import numpy as np
import orjson
import asyncio
import time
import uuid
from pathlib import Path

# Use the writer from orbit_io_extrusion
from orbit_io_extrusion import AsyncReplayWriter, REPLAY_DIR

BATCH_SIZE  = 512
TOTAL_GAMES = 10_000

def assemble_single_replay(trajectory: list[dict], final_rewards: list[float], config: dict) -> dict:
    """
    Reconstructs a Kaggle-compatible JSON replay from a JAX array trajectory.

    [OMISSION: Visual-only fields are stubbed to minimize serialized replay size.]

    Args:
        trajectory (list[dict]): A chronological list of JAX-state dictionaries.
        final_rewards (list[float]): The terminal rewards for both players.
        config (dict): Game configuration dictionary.

    Returns:
        dict: The fully constructed JSON replay tree.
    """
    steps = []
    for step_idx, state in enumerate(trajectory):
        planets_np = np.array(state["planets"])
        fleets_np  = np.array(state["fleets"])

        valid_planets = planets_np[planets_np[:, 1] != -2]
        planet_list   = valid_planets[:, :7].tolist()

        step_frame = []
        for player_id in range(2):
            valid_fleets = fleets_np[player_id][fleets_np[player_id, :, 0] > 0]
            fleet_list   = valid_fleets.tolist()

            is_terminal = step_idx == len(trajectory) - 1
            step_frame.append({
                "action":  [],
                "reward":  float(final_rewards[player_id]) if is_terminal else 0.0,
                "info":    {},
                "status":  "DONE" if is_terminal else "ACTIVE",
                "observation": {
                    "remainingOverageTime": 2.0,
                    "step":             step_idx,
                    "planets":          planet_list,
                    "fleets":           fleet_list,
                    "player":           player_id,
                    "angular_velocity": float(state["angular_velocity"]),
                    "initial_planets":  [],
                    "next_fleet_id":    int(state["next_fleet_id"]),
                    "comets":           [],
                    "comet_planet_ids": [],
                }
            })
        steps.append(step_frame)

    initial_planets = steps[0][0]["observation"]["planets"]
    for frame in steps:
        for player_frame in frame:
            player_frame["observation"]["initial_planets"] = initial_planets

    rewards_final = [float(final_rewards[0]), float(final_rewards[1])]
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
    """
    Iterates over a batched tensor trajectory and extracts individual game replays.

    Args:
        trajectory_batch (list[dict]): Batched JAX states representing the simulation timeline.
        batch_size (int): The number of concurrent games in the batch.

    Returns:
        list[dict]: A list of completely assembled replay dictionaries.
    """
    replays = []
    config = {
        "episodeSteps": 500, "actTimeout": 1,
        "runTimeout": 1200,  "agentTimeout": 2,
        "shipSpeed": 6.0,    "cometSpeed": 4.0,
    }

    for i in range(batch_size):
        single_traj = [{k: v[i] for k, v in step.items()} for step in trajectory_batch]
        final_state = single_traj[-1]

        # Determine actual rewards
        p0_alive = bool(np.any(np.array(final_state["planets"][:, 1]) == 0) or np.any(np.array(final_state["fleets"][0, :, 0]) > 0))
        p1_alive = bool(np.any(np.array(final_state["planets"][:, 1]) == 1) or np.any(np.array(final_state["fleets"][1, :, 0]) > 0))

        r0 = 1.0 if p0_alive else -1.0
        r1 = 1.0 if p1_alive else -1.0

        replays.append(assemble_single_replay(single_traj, [r0, r1], config))
    return replays


async def run_jax_batch_pipeline_async():
    """
    Executes the main asynchronous HPC loop: simulating games in JAX batches
    and dispatching replays via Stigmergic Concurrency extrusions.

    Returns:
        None
    """
    REPLAY_DIR.mkdir(parents=True, exist_ok=True)

    from orbit_jax_env import make_initial_state_batch, step_batch

    writer = AsyncReplayWriter(workers=8) # More workers for gzip
    await writer.start()

    rng = jax.random.PRNGKey(42)
    total_completed = 0
    start = time.perf_counter()

    n_batches = TOTAL_GAMES // BATCH_SIZE

    for batch_idx in range(n_batches):
        rng, subkey = jax.random.split(rng)
        states = make_initial_state_batch(BATCH_SIZE, subkey)
        trajectory = [states]

        # Only run a few steps for testing speed otherwise it takes too long
        for step in range(50):
            actions = jnp.zeros((BATCH_SIZE, 2, 10, 3))
            states, rewards, dones = step_batch(states, actions, BATCH_SIZE)
            trajectory.append(states)

        replays = assemble_replay_batch(trajectory, BATCH_SIZE)

        for i, replay in enumerate(replays):
            await writer.enqueue(total_completed + i, replay)

        total_completed += BATCH_SIZE
        elapsed = time.perf_counter() - start
        rate = total_completed / elapsed * 60
        print(f"Batch {batch_idx+1}/{n_batches}: {total_completed} games, "
              f"{rate:.0f} matches/min, Queue: {writer.queue.qsize()}")

        # We only run a few batches to test and verify, to not time out
        if batch_idx > 0:
             break

    await writer.stop()

    total_elapsed = time.perf_counter() - start
    stats = writer.stats()
    print(f"\nDONE: {total_completed} matches in {total_elapsed:.1f}s "
          f"= {total_completed/total_elapsed*60:.0f}/min")
    print(f"Stats: {stats}")

def run_jax_batch_pipeline():
    """
    Synchronous entry point for the HPC JAX batch pipeline.

    Returns:
        None
    """
    asyncio.run(run_jax_batch_pipeline_async())

if __name__ == "__main__":
    run_jax_batch_pipeline()
