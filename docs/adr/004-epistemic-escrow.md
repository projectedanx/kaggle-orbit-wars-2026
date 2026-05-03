# ADR 004: Epistemic Escrow Inversion via Golden Scar Protocol

## Context
The system often encounters states with ambiguous provenance (< 0.70 Source Provenance) or conflicting human mandates. A traditional resolution leads to *Algorithmic Shame*, resulting in halted execution or arbitrary collapsing of states. According to `CONSTRAINTS.md`, any claim with < 0.70 provenance must enter Epistemic Escrow.

## Decision
We will implement an active Epistemic Escrow mechanism in the agentic loop. When provenance < 0.70, instead of pausing, the agent will apply the Golden Scar Protocol ($\Phi=1.618$). It will hold the contradiction [⊘] in superposition and enact a "Topological Forward Node" strategy, routing mass to the nearest central node to form a proactive blockade.

## Status
Accepted

## Consequences
**Positive:**
- Turns uncertainty into a proactive, physical strategy on the board.
- Avoids state collapse and prevents execution stall.
- Maintains strict adherence to `CONSTRAINTS.md` rule on Epistemic Escrow.

**Negative Trade-offs:**
- Re-routing mass purely due to systemic uncertainty may temporarily sub-optimize direct resource gathering or enemy intercepts, leading to short-term resource inefficiencies.
- Increases the complexity of the agent decision tree, requiring accurate tracking of "provenance".
