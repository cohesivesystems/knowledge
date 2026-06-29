---
realm: Operational Semantics
kind: operational-semantics
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

In the model, duplicate input may be interpreted as a nil endogenous event for the target [[Entity]]: the observer saw the input, but no new domain transition was committed.

Idempotency is scoped to a semantic input and an effect boundary. An HTTP retry, broker redelivery, workflow replay, and outbox republication may each need a different idempotency key or deduplication record.

Related concepts: [[Retry]], [[Delivery Semantics]], [[Acknowledgments]], [[Commit Boundaries]], [[Effects]], [[Command]], [[Transition]], [[Version]], [[Recovery]], [[Transactional Inbox]], [[Outbox]].
