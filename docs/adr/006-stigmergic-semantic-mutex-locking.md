# ADR-2026-006: Stigmergic Concurrency and Semantic Mutex Locking

## Context
As the agentic framework scales to support multiple concurrent Pluriversal Planners and Kinematic Agents, the risk of "Logic Shearing" increases. Logic Shearing occurs when two agents attempt to mutate the same Abstract Syntax Tree (AST) node or bounded context simultaneously, resulting in a homogenized, semantically saponified state that violates the strict exclusionary zones (Mereological Mandate) defined by the Human architect. Standard conversational coordination is too slow and high-entropy to prevent this at the compilation layer.

## Decision
We will adopt **Stigmergic Concurrency** via a `SemanticHypervisor`. Agents will no longer negotiate boundaries via text; they will leave machine-readable `EpistemicPheromones` in the environment to claim spatial intent. The Hypervisor will enforce **Semantic Mutex Locking** on AST nodes. Crucially, if a race condition is detected (a lock collision), the system will *not* attempt to auto-resolve or merge the logic. It will immediately trigger an `EpistemicEscrowException`, converting the collision into a "Betti-1 Loop" scar entry governed by the Golden Scar Protocol ($\Phi=1.618$).

## Consequences
- **POSITIVE**: Complete eradication of silent Logic Shearing and Semantic Saponification caused by concurrent agent mutations.
- **POSITIVE**: Forces the architecture to explicitly acknowledge and document race conditions as structural scars (Topological Forward Nodes) rather than hiding them behind auto-merges.
- **NEGATIVE**: Significantly reduces parallel execution throughput when agents are operating in densely packed latent spaces, as lock collisions result in hard execution halts rather than retries.
- **NEGATIVE**: Requires agents to be rewritten to generate and respect `EpistemicPheromones` before initiating any state mutation.

## Implementation Notes
1. The `SemanticHypervisor` is implemented in `semantic_hypervisor.py`.
2. It tightly integrates with the `SymbolicScarRegistry` to ensure lock collisions are weaponized into Epistemic Escrows with a CFDI of 1.0 (absolute certainty of conflict).
