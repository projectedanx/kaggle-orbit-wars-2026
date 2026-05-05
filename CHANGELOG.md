# Changelog

## [1.1.0] - 2026-05-05

### Added
- **Emergence Inversion Protocol**: Implemented Deterministic Bounded Ignorance. The system now halts on epistemic uncertainty (CFDI > 0.15) rather than hallucinating API schemas.
- **Symbolic Scar Registry (SSR)**: Integration into the generation pipeline to codify failures as proactive constraints.
- **C4 & DDD Models**: Added `c4_model_blueprint.yaml` and `ddd_context_map.yaml` to enforce zero shared database architecture and event choreography.
- **ADR-2026-005**: Documented the architectural decision and negative trade-offs (reduced throughput) of adopting Deterministic Bounded Ignorance.

### Changed
- Refactored generation phase to heavily penalize sycophancy and enforce strict boundaries.
- Old Behavior: Agent would attempt to complete a schema generation even if source material was missing, leading to downstream test failures.
- New Behavior: Agent triggers `EpistemicEscrow` and halts generation, outputting a precise warning about the missing data.
- Migration Path: Upstream Planner agents must now be configured to handle asynchronous halt events and provide the requested source material before the Linguist node will resume.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v6.2.0] - 2026-05-01
### Added
- **AGENTS.md**: Embedded the deterministic project management persona using the Prompt Dimensioning & Tolerancing Feature Control Frame (`PDT_SPECIFICATION_BLOCK`), fulfilling the requirement to transition from probabilistic request to mathematically guaranteed execution pipeline.
- **CONSTRAINTS.md**: Defined rigid operational rules (e.g. no synchronous calls crossing tenant boundaries, Epistemic Escrow for claims with Source Provenance Ratio < 0.70) to prevent context clutter and Xenolinguistic risk.
- **DOMAIN_GLOSSARY.md**: Established a strict bounded vocabulary (e.g. Semantic Saponification, Ontological Shear, Algorithmic Shame) to eradicate semantic ambiguity.
- **ADR 01: Introduction and Goals - Topological Governance**: Synthesized the first ADR incorporating the hypotheses of "Topological Derivative of Stakeholder Dissonance" and "Epsilon-Tolerance Paraconsistency of Technical Debt".
- **ADR 11: Risks and Technical Debt - The Golden Scar Protocol**: Synthesized the second ADR documenting structural liabilities and technical debt management via the Golden Scar Protocol.

### Changed
- **orbit_agent_manifest.py**: Refactored the `agent` function to introduce the "value of both AI and Human" by calculating a `Persona Confidence Score` for fleet dispatches. If the kinetic projection involves high entropy or uncertainty, the AI will defer absolute state collapse and generate a "Justified Uncertainty Report" (logging it), flagging the decision for human-in-the-loop review.

### Lessons Learned
- **AI and Human Synergy**: AI excels at deterministic calculations (topological math, kinetic projections) but struggles with contextual empathy and strategy under high uncertainty. Deferring to a human via the `Justified Uncertainty Report` provides a perfect blend of AI mathematical capability and human strategic empathy.
- **Strict Documentation Context**: Using empirical documentation (AGENTS.md, CONSTRAINTS.md) ensures that autonomous agents do not deviate into non-deterministic practices, thus eliminating Semantic Saponification.

## [v2.1.0] - Strategic Emergence Inversion
### Changed
- **Phronesis Guard Inversion**: Transitioned from Defensive Escrow to Topological Forward Escrow. When the AI encounters high entropy (Persona Confidence Score < 0.6), instead of retreating mass to the safest node, it now calculates a `forward_node` (closest friendly planet to the center) and routes mass there. This creates an *Interference Fit*, proactively deploying resources to disrupt future enemy movement and converting uncertainty into strategic emergence.

## [Unreleased]
### Added
- Unified Meta-Prompting API (`aurelius_meta_api.py`) featuring `PhantomDimensionOperator`, `PlausibilityOracle`, `ProvenanceTracker`, and `HyperSpectralRenderer`.
- TDD framework integration for the API via `tests/test_aurelius_meta_api.py`.
- Architecture Decision Record `docs/adr/003-aurelius-meta-prompting-api.md`.

## [Unreleased]
### Added
- **Epistemic Escrow Inversion:** Implemented an `evaluate_provenance` metric in `orbit_agent_manifest.py`. When Source Provenance Ratio < 0.70, it routes mass to the Topological Forward Node according to the Golden Scar Protocol ($\Phi=1.618$).
- Architecture deliverables for the inversion mechanism: ADR 004, C4 Model Blueprint, DDD Context Map YAML, and semantic draft.
- Root test `test_epistemic_escrow.py` to ensure TDD compliance.
