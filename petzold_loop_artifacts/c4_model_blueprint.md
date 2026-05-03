# C4 Model Blueprint: Orbit Wars Agentic Framework

## System Context Diagram
- **User (Human):** Provides strategic objectives and epistemic constraints.
- **Orbit Wars Agent:** Receives environment states, computes topological routing, and outputs moves.
- **Kaggle Environment Engine:** Simulates the continuous 2D non-Euclidean board and physics.

## Container Diagram
- **Meta-Architect API:** Handles prompt engineering and constraints.
- **JAX/XLA HPC Engine:** Manages vectorized simulations and thermodynamic efficiency.
- **Agent Manifest (orbit_agent_manifest.py):** Core decision loop implementing the Phronesis Guard and Epistemic Escrow.
- **IO Extrusion Pipeline:** Asynchronous replay writing.

## Component Diagram (Agent Manifest)
- **Provenance Evaluator:** Checks the Source Provenance Ratio of current states/claims.
- **Kinematic Calculator:** Computes distance, fleet speeds, and intercepts.
- **Epistemic Escrow Router [∇]:** Activated when Provenance < 0.70. Calculates the Topological Forward Node and routes mass to it.
- **Standard Router:** Handles standard intercepts and production maximization.

## Code Diagram
*(Implied by standard Python structures inside orbit_agent_manifest.py)*
