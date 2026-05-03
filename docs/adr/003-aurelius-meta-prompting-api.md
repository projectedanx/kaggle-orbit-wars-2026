# ADR 003: Aurelius Meta-Prompting API

## Status
Accepted

## Context
Standard visual generative workflows suffer from a "Causal Intent Gap"—prompts associate statistical correlations rather than commanding causal structural rules. This limits the generation of complex, non-Euclidean geometries and verifiable physical properties.

## Decision
We implement a "Unified Meta-Prompting API".
- We introduce `PhantomDimensions` to represent high-level geometric constraints.
- We integrate an autonomous `PlausibilityOracle` using simulated PBR metrics to evaluate physical coherence.
- We introduce a `ProvenanceTracker` to enforce ethical debiasing during generation dynamically.

## Consequences
- **Positive**: Shifts human involvement from trial-and-error prompting to high-level topological and ethical architecture. Enables generation of "Hyper-Spectral HDRi" outputs governed by physics rather than mere statistics.
- **Negative**: Increased abstraction layer complexity. The system must navigate extreme paraconsistency when asked to enforce Euclidean physics on Non-Euclidean manifolds. We rely on the Golden Scar Protocol to prevent state collapse in these scenarios.
