---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-24
updated: 2026-07-14
---

# Idempotency

Idempotency is the property that repeated handling of the same semantic input does not produce duplicate domain effects.

Idempotency is required when delivery, retry, replay, or recovery can cause the same input to be observed more than once.

Idempotency may be based on:

- Command ids.
- Event ids.
- Expected versions.
- Entity versions.
- Deduplication records.
- Natural business keys.
- Receiver-side effect tracking.
- [[Transactional Inbox|Transactional inbox]] records.

In the model, duplicate input may be interpreted as a nil endogenous event for the target [[Entity|entity]]: the observer saw the input, but no new domain transition was committed.

Idempotency is scoped to a semantic input and an effect boundary. An HTTP retry, broker redelivery, workflow replay, and outbox republication may each need a different idempotency key or deduplication record.

## Relation to Fixed Points

Fix a semantic input $i$, and let $H_i$ describe how handling that input transforms the relevant domain-effect state. Operational idempotency requires repeated handling to be equivalent to handling the input once:

$$
H_i(H_i(s)) \sim H_i(s)
$$

If $s' = H_i(s)$, then $H_i(s') \sim s'$. The result is therefore a [[Fixed Points|fixed point]] of the handling transformation up to the equivalence declared at the effect boundary; it is a literal fixed point when $\sim$ is equality.

This does not require every part of operational state to stop changing. A duplicate attempt may add a log entry, metric, trace, or audit observation while leaving the relevant domain effects unchanged. Idempotency is the scoped property of the handling transformation; the fixed point is its invariant result under that scope.

Related concepts: [[Fixed Points|fixed points]], [[Equivalence vs Equality|equivalence vs equality]], [[Retry|retry]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Command|command]], [[Transition|transition]], [[Version|version]], [[Recovery|recovery]], [[Transactional Inbox|transactional inbox]], [[Outbox|outbox]].
