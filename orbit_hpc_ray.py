# orbit_hpc_ray.py — Ray-based parallel match runner
import ray
import asyncio
import orjson
import aiofiles
import kaggle_environments as ke
from pathlib import Path
import time

RAY_WORKERS = 32          # Tune to CPU core count
REPLAY_DIR  = Path("./replays")
REPLAY_DIR.mkdir(parents=True, exist_ok=True)

@ray.remote(num_cpus=0.5)   # Each worker uses 0.5 CPUs → pack 2× per core
class OrbitMatchWorker:
    """Stateless Ray actor: runs one match, returns replay dict."""

    def __init__(self, agent_a="random", agent_b="random"):
        """
        Initializes the stateless OrbitMatchWorker.

        Args:
            agent_a (str|callable, optional): The first agent identifier. Defaults to "random".
            agent_b (str|callable, optional): The second agent identifier. Defaults to "random".

        Returns:
            None
        """
        self.agent_a = agent_a
        self.agent_b = agent_b
        # Pre-instantiate env once per worker to avoid re-import overhead
        self._env = None

    def _get_env(self):
        """
        Retrieves or initializes the Kaggle environment for the worker.

        Returns:
            kaggle_environments.core.Environment: The active environment.
        """
        if self._env is None:
            self._env = ke.make(
                'orbit_wars',
                configuration={"episodeSteps": 500},
                debug=False
            )
        return self._env

    def run_match(self, match_id: int) -> dict:
        """
        Executes a single simulation match synchronously within the worker.

        Args:
            match_id (int): The unique identifier for this simulation instance.

        Returns:
            dict: The complete JSON replay of the simulated match.
        """
        env = self._get_env()
        env.reset()  # Reset state without re-initializing
        env.run([self.agent_a, self.agent_b])
        replay = env.toJSON()
        replay["_match_id"] = match_id  # Inject for file naming
        return replay


async def write_replay(replay: dict, match_id: int):
    """
    Asynchronously writes replay data to disk utilizing orjson and aiofiles.

    Args:
        replay (dict): The complete match replay dictionary.
        match_id (int): The match identifier for file naming.

    Returns:
        None
    """
    path = REPLAY_DIR / f"match_{match_id:08d}.json"
    data = orjson.dumps(replay)   # orjson is 5-8x faster than json.dumps
    async with aiofiles.open(path, "wb") as f:
        await f.write(data)


async def run_batch_pipeline(total_matches: int = 10_000):
    """
    Orchestrates the Ray parallelization loop and asynchronous I/O extrusion.

    Args:
        total_matches (int, optional): The target number of matches to simulate. Defaults to 10000.

    Returns:
        None
    """
    ray.init(num_cpus=RAY_WORKERS * 2, ignore_reinit_error=True)

    workers = [OrbitMatchWorker.remote() for _ in range(RAY_WORKERS)]

    start = time.perf_counter()
    pending = {}
    match_id = 0
    write_tasks = []

    # Fill the Ray task queue
    for i, worker in enumerate(workers):
        ref = worker.run_match.remote(match_id)
        pending[ref] = match_id
        match_id += 1

    completed = 0
    while completed < total_matches:
        ready, _ = ray.wait(list(pending.keys()), num_returns=1, timeout=30)
        if not ready:
            break

        ref = ready[0]
        mid = pending.pop(ref)
        replay = ray.get(ref)

        # Schedule async write (non-blocking)
        write_tasks.append(asyncio.create_task(write_replay(replay, mid)))
        completed += 1

        if completed % 100 == 0:
            elapsed = time.perf_counter() - start
            rate = completed / elapsed * 60
            print(f"[{completed}/{total_matches}] Rate: {rate:.0f} matches/min")

        # Refill worker queue
        if match_id < total_matches + RAY_WORKERS:
            worker = workers[mid % RAY_WORKERS]
            ref = worker.run_match.remote(match_id)
            pending[ref] = match_id
            match_id += 1

    # Drain all pending writes
    if write_tasks:
        await asyncio.gather(*write_tasks)

    elapsed = time.perf_counter() - start
    print(f"\nFINAL: {completed} matches in {elapsed:.1f}s = {completed/elapsed*60:.0f}/min")
    ray.shutdown()


if __name__ == "__main__":
    asyncio.run(run_batch_pipeline(10_000))
