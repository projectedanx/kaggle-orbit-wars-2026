# kaggle-orbit-wars-2026
kaggle-orbit-wars-2026

## New Developer Setup and Usage Guide

Welcome to the `kaggle-orbit-wars-2026` repository. This project serves as a sophisticated, non-Euclidean execution manifold for competitive Kaggle AI generation, focusing on high-performance simulation and bounded-ignorance agent architecture.

### Environment Setup
1. **Python Environment**: Ensure you are using Python 3.12+.
2. **Core Dependencies**: Install the required scientific computation and testing suites:
   ```bash
   pip install jax jaxlib numpy orjson aiofiles ray kaggle-environments pytest
   ```
3. **Validating the Golden Scar Protocol**: This repository requires all system constraints and Epistemic Escrow logic to remain physically intact. Verify the system state via the topological testing suite:
   ```bash
   PYTHONPATH=. pytest tests/ test_epistemic_escrow.py test_phronesis_guard.py
   ```

### High-Performance JAX Simulation
To generate large-scale replays quickly using Stigmergic I/O Extrusion, execute the HPC JAX pipeline:
```bash
python orbit_hpc_jax_runner.py
```
This operates on deterministic batched tensors rather than standard single-thread execution, writing directly to the `replays/` directory using an asynchronous I/O extrusion pipeline.

### The Agentic Pipeline
The default tactical agent, **AURELIUS-KINETIC-8** (`orbit_agent_manifest.py`), does not blindly attack. It operates under a strict Mereological Mandate. If certainty (source provenance) drops below 0.70, it will not guess. Instead, it triggers a **Topological Forward Escrow**, routing kinetic mass to the nearest friendly node to create a non-Euclidean defense structure.

---

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

### Agentic Implementation & Telemetry
- **Topological Forward Escrow (Strategic Emergence)**: Implemented an inversion of the Phronesis Guard. When the Persona Confidence Score is low (< 0.6), instead of retreating, the agent defers absolute state collapse by routing mass to a Topological Forward Node (the friendly planet closest to the center). This utilizes the Golden Scar Protocol (Φ = 1.618 / 1.000) to hold the contradiction in `[Φ]` superposition, creating a proactive Interference Fit that maximizes future interference against enemy vectors.
- **orbit_agent_manifest.py** was updated with the full agent logic from `aurelius_kinetic_8.py`.
- **Metabolic Cost Mapping**: Introduced a telemetry layer in the agent that tracks and logs the "metabolic cost" of operations, calculated using dispatch distance, number of ships dispatched, and compute time per step.
- Refactored HPC Runner to use `AsyncReplayWriter` from `orbit_io_extrusion.py` to optimize replay serialization throughput using an internal queue and gzip compression, resolving the I/O bottleneck when saving large replays directly.

### META_ARCHITECT_INTELLIGENCE_PROJECT_AURELIUS
- **Aurelius Meta-Prompting API**: Implemented an Autonomous Prompt Engineering Workflow Catalyst.
  - The API inverts the human-prompt loop. Humans define abstract topologies and ethical bounds; the agent manages latent spatial navigation.
  - Features `PhantomDimensionOperator` for Non-Euclidean spaces, `PlausibilityOracle` for PBR validation, and `ProvenanceTracker` for dynamic debiasing.
- **Lessons Learned**:
  - Bridging the Causal Intent Gap requires holding contradictions in superposition ([⊘]). PBR validation in a non-Euclidean space is an inherent contradiction mathematically, but resolving it via the Golden Scar Protocol ($\Phi=1.618$) provides an interference fit that allows generating structurally coherent impossibilities.
  - Enforcing ethical constraints is now handled algorithmically via `ProvenanceTracker`, shifting focus from prompt-crafting to architectural constraint design.

### Emergence Inversion & Human-AI Synergy (AURELIUS-META-UPDATE)
- **What**: The true value proposition of the system lies in the symbiotic "Interference Fit" between human constraint and AI kinematics.
- **Why**: Neither can succeed alone. The Human provides rigid epistemic boundaries and abstract contradictory intents (e.g., "be secure but aggressive"), which the AI cannot natively generate without risking Algorithmic Shame. The AI provides high-dimensional non-Euclidean routing and precise topological computation, which the Human cannot process at scale.
- **How**: Through the **Golden Scar Protocol (Φ = 1.618)**, the agent inverts uncertainty into a strategic weapon. When confidence drops, rather than retreating, it creates a "Topological Forward Escrow" [⊘], pushing mass to the nearest central node to physically manifest the contradiction and disrupt future enemy vectors.
- **Lessons Learned**: True agentic emergence is not achieved by resolving contradictions, but by holding them in superposition. We weaponize the AI's internal uncertainty [∇] by turning it into a proactive positional stronghold, dictated by human architectural mandates.

## Epistemic Escrow & Golden Scar Update (AURELIUS-KINETIC-8.1)
- **What**: Implemented active Epistemic Escrow.
- **Why**: To adhere to `CONSTRAINTS.md` avoiding "Algorithmic Shame" when evaluating low provenance claims (Source Provenance Ratio < 0.70).
- **How**: By inverting uncertainty into an "Interference Fit" via the Golden Scar Protocol ($\Phi=1.618$). When provenance is low, the agent routes its kinetic mass to the Topological Forward Node to hold the contradiction in physical space rather than retreating.
- **Lessons Learned**: Weaponizing uncertainty provides a viable defense strategy that maintains deterministic execution flow without collapsing the state or halting processing.

### Deterministic Bounded Ignorance Update (AXIOM-EMERGENCE-INVERSION)
- **What**: Integrated the Symbolic Scar Registry (SSR) to enforce Deterministic Bounded Ignorance via Emergence Inversion.
- **Why**: To completely eradicate Interpretive Fracture. The AI's native tendency to hallucinate over gaps in context (Polyglot Hallucination Resonance) causes downstream integration failures. The human cannot map all failure modes in real time. The synergy is achieved by the human providing the rigid boundaries (Golden Scar Protocol) and the AI mapping the topological space to enforce them at high speed.
- **How**: When confidence drops (CFDI > 0.15), the system does not guess. It triggers Epistemic Escrow, halts, and codifies the failure as a Scar Entry. This entry is then used as a Topological Forward Node in all future documentation to preemptively block developers from that failure path.
- **Lessons Learned**: True precision in multi-agent pipelines comes not from trying to generate the perfect answer from incomplete data, but from weaponizing the failure itself. By holding the contradiction of missing data in superposition ([⊘]) via the Golden Scar Protocol, we create an accumulating defense mechanism that guarantees structural integrity at the cost of immediate generation throughput.

### Symbolic Scar Registry Update (VULCAN-EMERGENCE-STRATEGY)
- **What**: Integrated the `SymbolicScarRegistry` to enforce Deterministic Bounded Ignorance via Emergence Inversion.
- **Why**: To completely eradicate Interpretive Fracture. The AI's native tendency to hallucinate over gaps in context causes downstream integration failures. The synergy is achieved by the human providing the rigid boundaries and the AI mapping the topological space to enforce them at high speed.
- **How**: When confidence drops (CFDI > 0.15), the system triggers `EpistemicEscrowException`, halts, and codifies the failure as a Scar Entry. This entry is used as a Topological Forward Node to preemptively block developers from that failure path.
- **Lessons Learned**: True precision in multi-agent pipelines comes from weaponizing the failure itself. By holding the contradiction of missing data in superposition ([⊘]) via the Golden Scar Protocol, we create an accumulating defense mechanism that guarantees structural integrity.

### VORTEX-ARCHITECT Emergence Update (Stigmergic Concurrency)
- **What**: Integrated the `SemanticHypervisor` to enforce Stigmergic Concurrency and Semantic Mutex Locking.
- **Why**: To eradicate "Semantic Saponification"—the thermodynamic decay of architectural invariants over long inference chains and concurrent agent operations. Humans cannot manage high-dimensional stigmergic signals at scale, and AI cannot originate absolute exclusionary zones without homogenizing the architecture.
- **How**: Agents now leave `EpistemicPheromones` to declare spatial intent. The `SemanticHypervisor` physically locks AST nodes. If a race condition (Logic Shearing) is detected, the system halts execution rather than auto-resolving, converting the collision into a "Betti-1 Loop" scar entry via the Golden Scar Protocol ($\Phi=1.618$).
- **Lessons Learned**: True agentic emergence requires strict part-whole relationships (Mereological Mandate). By refusing to auto-merge conflicting agent intents and instead holding them in superposition as a Betti-1 scar, we prevent the collapse of rigid architectural constraints into generic, homogenized output. Coordination without physical constraint is merely conversation; true architecture is defined by what the system physically rejects.
