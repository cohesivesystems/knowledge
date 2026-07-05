---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-24
updated: 2026-07-01
---

# Retry

Retry is the controlled repetition of an operation after a transient failure, timeout, conflict, or unavailable dependency.

Retry changes the operational shape of a system because the same input may be observed more than once by the same or different [[Observer|observers]].

Retry is one recovery strategy: it re-drives incomplete or transiently failed work when the original input remains valid and duplicate effects are controlled.

## Time Replication

Retry can be read suggestively as **time replication**: the same operational intent is preserved and re-presented across successive moments. It does not replicate the resulting [[State|state]]; it replicates the opportunity for a [[Command|command]] or operation to take effect when failure may be transient.

In this sense, retry is a replication of time rather than state. State-machine replication uses [[Consensus|consensus]] or another ordering mechanism to replicate an agreed sequence of operations across space, so multiple replicas apply the same [[Transition|transition]] rules and produce equivalent state. Retry repeats an attempt across time, so a boundary may eventually observe, reject, or commit the intent. State-machine replication asks which replica or log position counts; retry asks which attempt counts.

When failure is deterministic, the input is invalid, or the required dependency cannot become available under the system assumptions, time replication does not add resilience. It only repeats work.

A retry policy should define:

- Which failures are retryable.
- Retry limits and backoff.
- Whether retries preserve ordering.
- Which idempotency key, command id, event id, or version check prevents duplicate effects.
- How exhausted retries are surfaced for recovery.

Retries are safe only when paired with explicit [[Idempotency|idempotency]], appropriate [[Delivery Semantics|delivery semantics]], and clear recovery behavior.

Related concepts: [[Idempotency|idempotency]], [[Rate Limiting|rate limiting]], [[Ordering|ordering]], [[Recovery|recovery]], [[Delivery Semantics|delivery semantics]], [[Command|command]], [[Time|time]], [[State|state]], [[Consensus|consensus]], [[Transition|transition]].
