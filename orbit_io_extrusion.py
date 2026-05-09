import asyncio
import aiofiles
import orjson
import gzip
from pathlib import Path
from dataclasses import dataclass

REPLAY_DIR  = Path("./replays")
COMPRESS    = True
BUFFER_SIZE = 1000

@dataclass
class ReplayWriteTask:
    """
    Data structure representing a single replay serialization job.
    """
    match_id: int
    replay:   dict

class AsyncReplayWriter:
    """
    High-throughput asynchronous replay extrusion pipeline for HPC JAX execution.
    Mitigates massive I/O bottlenecks when writing directly to disk or WSL mounts.
    """
    def __init__(self, replay_dir: Path = REPLAY_DIR, workers: int = 4):
        """
        Initializes the AsyncReplayWriter with target directory and worker pool.

        Args:
            replay_dir (Path, optional): Target directory for replay files. Defaults to REPLAY_DIR.
            workers (int, optional): Number of asynchronous worker tasks. Defaults to 4.

        Returns:
            None
        """
        self.replay_dir = replay_dir
        self.replay_dir.mkdir(parents=True, exist_ok=True)
        self.queue: asyncio.Queue = None
        self.workers = workers
        self._bytes_written = 0
        self._files_written = 0
        self._worker_tasks = []

    async def start(self):
        """
        Starts the internal queue and spins up the asynchronous worker tasks.

        Returns:
            None
        """
        self.queue = asyncio.Queue(maxsize=BUFFER_SIZE)
        self._worker_tasks = [
            asyncio.create_task(self._worker(i))
            for i in range(self.workers)
        ]

    async def enqueue(self, match_id: int, replay: dict):
        """
        Enqueues a replay serialization task.

        Args:
            match_id (int): The unique identifier for the match.
            replay (dict): The complete state/action replay dictionary.

        Returns:
            None
        """
        await self.queue.put(ReplayWriteTask(match_id, replay))

    async def _worker(self, worker_id: int):
        while True:
            task = await self.queue.get()
            if task is None:
                break
            await self._write(task)
            self.queue.task_done()

    async def _write(self, task: ReplayWriteTask):
        data = orjson.dumps(task.replay)

        if COMPRESS:
            data = gzip.compress(data, compresslevel=1)
            suffix = ".json.gz"
        else:
            suffix = ".json"

        path = self.replay_dir / f"match_{task.match_id:08d}{suffix}"
        async with aiofiles.open(path, "wb") as f:
            await f.write(data)

        self._bytes_written += len(data)
        self._files_written += 1

    async def stop(self):
        """
        Blocks until the queue is empty, then shuts down all worker tasks gracefully.

        Returns:
            None
        """
        await self.queue.join()
        for _ in self._worker_tasks:
            await self.queue.put(None)
        await asyncio.gather(*self._worker_tasks)

    def stats(self) -> dict:
        """
        Retrieves metabolic I/O metrics indicating extrusion performance.

        Returns:
            dict: Extrusion statistics (files, bytes, queue depth).
        """
        return {
            "files_written":  self._files_written,
            "bytes_written":  self._bytes_written,
            "queue_depth":    self.queue.qsize() if self.queue else 0,
        }

async def main_simulation_loop():
    """
    Demonstrates the integration of the async pipeline for replay generation.

    Returns:
        None
    """
    writer = AsyncReplayWriter()
    await writer.start()

    # Stub loop to demonstrate integration
    for match_id in range(100):
        replay = {"test": "data"}
        await writer.enqueue(match_id, replay)

    await writer.stop()
    print(writer.stats())

if __name__ == "__main__":
    asyncio.run(main_simulation_loop())
