---
realm: Operational Semantics
---

# Retry

Retry is the controlled repetition of an operation after a transient failure, timeout, conflict, or unavailable dependency.

Retry changes the operational shape of a system because the same input may be observed more than once by the same or different [[Observer|Observers]].

Retry is one recovery strategy: it re-drives incomplete or transiently failed work when the original input remains valid and duplicate effects are controlled.

A retry policy should define:

- Which failures are retryable.
- Retry limits and backoff.
- Whether retries preserve ordering.
- Which idempotency key, command id, event id, or version check prevents duplicate effects.
- How exhausted retries are surfaced for recovery.

Retries are safe only when paired with explicit [[Idempotency]], appropriate [[Delivery Semantics]], and clear recovery behavior.

Related concepts: [[Idempotency]], [[Rate Limiting]], [[Ordering]], [[Recovery]], [[Delivery Semantics]], [[Command]].
