# ADR 002: Strategic Emergence Inversion (Topological Forward Escrow)

## Status
Accepted

## Context
In the `kaggle-orbit-wars-2026` vectorized environment, the `PhronesisGuard` was originally designed as a defensive measure. When the `persona_confidence_score` dropped below 0.6 (due to high target distance or high mass requirements), the agent executed the Golden Scar Protocol to route resources to the `safest_planet` (furthest from enemies). While this preserved mass, it abandoned positional control, leading to passive attrition.

## Decision
We are inverting the logic to foster Human-AI emergence. When faced with uncertainty, the agent will now compute a `forward_node` (the friendly planet closest to the center of the board).

By routing mass to this node, the agent transforms an uncertain situation into a proactive "Interference Fit". It weaponizes its own uncertainty, deploying a stronghold that disrupts future enemy trajectories. The AI provides the kinematic calculation, while the Human (via the architectural Golden Scar constraint) enforces this aggressive contradiction management.

## Consequences
- **Positive:** Converts passive defense into active positional dominance. Increases the probability of intersecting and destroying enemy fleets mid-transit.
- **Negative:** Forward nodes are inherently riskier. If the forward node is overwhelmed by an unpredicted enemy swarm, the mass lost via the Golden Ratio routing is higher than if it were kept at the rear.
