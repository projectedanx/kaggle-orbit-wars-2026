# kaggle-orbit-wars-2026
kaggle-orbit-wars-2026

## High-Performance Computation Updates (AURELIUS-KINETIC-8)

To support thermodynamic efficiency and large-scale replay generation (~10,000 matches/minute), this repository has been updated with:

- **aurelius_kinetic_8.py**: Implements zero-sum thermodynamic principles to identify optimal mass for capture considering angular velocity and travel time. Includes precise interception calculations.
- **orbit_jax_env.py**: A fully vectorized environment using JAX and XLA, allowing multiple Orbit Wars simulations on a single GPU.
- **orbit_hpc_jax_runner.py**: A runner that integrates JAX-batched game stepping with replay generation, reconstructing the Kaggle replay JSON from state snapshots.
- **orbit_io_extrusion.py**: An asynchronous replay-saving pipeline, using Python's `asyncio` and `aiofiles` for high-throughput disk writes.

### Lessons Learned
- Writing small replays directly to WSL-mounted Windows drives (`/mnt/c`) is a massive I/O bottleneck. The current `orbit_io_extrusion.py` script mitigates this using `aiofiles` and gzip compression. A RAM disk (`tmpfs`) is recommended for the fastest throughput.
- JAX handles dynamic operations poorly. Pre-allocation of planet and fleet states to fixed sizes (`MAX_PLANETS=64`, `MAX_FLEETS=128`) heavily optimized our simulation steps.
- Kaggle `toJSON()` schema validation relies heavily on exact structural parsing. When reconstructing replays from JAX snapshots, ensure proper injection of `initial_planets`.
