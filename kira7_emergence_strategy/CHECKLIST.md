# [WRITE PHASE — KIRA-7 ACTIVE]
+++ContextLock(anchor="FEISHU_OPEN_API_INVARIANTS", refresh_interval=2048)
+++DCCDSchemaGuard(schema="Feishu_Card_JSON_v2", enforcement="draft_conditioned")
+++SagaRecovery(strategy="compensating_transaction", mode="token_refresh_first")

# [KIRA-7 JUR ESCALATION GATEWAY CHECKLIST]

## Phase 1: Webhook Sovereignty Perimeter (Ingress)
- [ ] Implement URL Verification Challenge (`type: 'url_verification'`) immediately to prevent silent subscription death (SCAR-002).
- [ ] Implement AES-256-CBC decryption utilizing the `LARK_ENCRYPT_KEY` for payload parsing. Never attempt raw JSON parsing if encrypted (SCAR-003).
- [ ] Implement signature validation: `SHA256(timestamp + nonce + encrypt_key + raw_body)` matching `x-lark-signature` (SCAR-004).
- [ ] Implement Timestamp Freshness Check: Reject requests where `|Date.now() - timestamp| > 300` to mitigate replay attacks.

## Phase 2: Token Primacy Layer (Egress)
- [ ] Implement robust token caching (in-memory lock/mutex for single-process, or Redis) with a TTL of 6900 seconds (100s buffer before the actual 7200s expiration) to avoid token throttling/expiration crashes (SCAR-001).
- [ ] Ensure `tenant_access_token` is dynamically fetched and cached, never hardcoded.

## Phase 3: Adaptive Card Formulation (DCCDSchemaGuard)
- [ ] Formulate a Justified Uncertainty Report (JUR) using exactly Feishu Card JSON v2.0 structure (`msg_type: "interactive"` with nested card object).
- [ ] Implement explicit phase transitions between THINK/WRITE (Gritty persona active) and CODE (Sterile execution).
- [ ] Include interactive fallback action buttons representing the human constraint resolution for the Topological Forward Escrow.

## Phase 4: Scope & Documentation Finalization
- [ ] Update `README.md` to articulate the Emergence Inversion strategy and human-in-the-loop fallback topology.
- [ ] Update `CHANGELOG.md` to record the KIRA-7 Emergence Strategy updates.
- [ ] Create `docs/adr/005-kira7-jur-escalation-gateway.md` mapping out the structural integration of the gateway.
- [ ] Generate explicit `Scope Declaration Block` mapping required Feishu scopes (`im:message`, `im:message:send_as_bot`, `im:message:receive_v1`).
