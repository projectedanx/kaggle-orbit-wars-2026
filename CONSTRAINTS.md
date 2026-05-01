# CONSTRAINTS.md

## Rigid Operational Rules

1. **No Synchronous Calls Crossing Tenant Boundaries**: To prevent logic branching errors and maintain deterministic code flow, synchronous inter-tenant communication is strictly prohibited.
2. **Epistemic Escrow**: Any contextual claim with a Source Provenance Ratio < 0.70 must be quarantined in Epistemic Escrow. It cannot be used for inference or code generation.
3. **Draft-Conditioned Constrained Decoding**: All generation paths must utilize Draft-Conditioned Constrained Decoding to enforce schema adherence without paying the projection tax.
4. **Mandatory Provenance Anchoring**: Code review heuristics must demand Mandatory Provenance Anchoring.
5. **Golden Scar Protocol**: When conflicting mandates exist (e.g. abstract human constraints vs. strict AI parameters), the Golden Ratio (\(\phi=1.618\)) is applied as a non-stochastic Semantic Anchor, embodying the Golden Scar Protocol without collapsing the intelligence lattice. The dominant epistemic frame of empirical governance is assigned a weight of 1.618.
