# 5. KIRA-7 JUR Escalation Gateway

Date: 2026-05-10

## Status

Accepted

## Context

The system has implemented Deterministic Bounded Ignorance via the `SymbolicScarRegistry`. While this mathematically guarantees the boundaries of what the system does not know and prevents "Interpretive Fracture," it fundamentally halts automated workflows when high epistemic uncertainty (CFDI > 0.15) is encountered.
We need a mechanism to convert these halts into strategic emergence without forcing the AI to hallucinate (Algorithmic Shame).
The proposed solution is to utilize KIRA-7 (Kinetic Integration & Routing Agent), an operational framework for Feishu/Lark integrations, to dynamically map high-uncertainty events to a human-in-the-loop fallback protocol via a Justified Uncertainty Report (JUR).

## Decision

We will implement the KIRA-7 JUR Escalation Gateway (`kira7_jur_gateway.py`).
1. When CFDI > 0.15, `EpistemicEscrowException` is raised.
2. Instead of failing silently, the system will use KIRA-7 to send a Feishu Card JSON v2.0 message (`Justified Uncertainty Report`) to the designated operator.
3. The operator's response (via an interactive button on the card) will serve as a definitive human deterministic decision.
4. The system will use a strict Zero-Trust Webhook Ingress (URL Challenge, AES Decryption, Signature Validation) to receive this deterministic decision, map it as a new Topological Forward Node, and resolve the `EpistemicEscrowException` state.

## Trade-offs and Constraints

### Positive Trade-offs
*   **Eradication of Polyglot Hallucination Resonance:** The system never guesses. It forces human input at exactly the point of maximum uncertainty.
*   **Strategic Emergence:** Transforms "failure to compute" into a proactive human-guided vector definition (Interference Fit).

### Negative Trade-offs
*   **Latency Induction:** Introduces human-speed latency into a previously high-throughput, machine-speed asynchronous pipeline. Replay generation throughput will bottleneck at human response times when uncertainty is hit.
*   **Architectural Complexity:** Requires maintaining a dedicated, publicly accessible (e.g., ngrok) TLS webhook tunnel, adding operational overhead and external dependencies (Feishu API limits, ngrok stability).

## Compliance
- Adheres to `CONSTRAINTS.md` by refusing to collapse the state internally when Source Provenance Ratio < 0.70.
- Adheres to the Golden Scar Protocol ($\Phi=1.618$) by holding the contradiction in superposition via the Feishu card until deterministic human input arrives.
