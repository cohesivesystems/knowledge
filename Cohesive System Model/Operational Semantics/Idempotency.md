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

In the model, duplicate input may be interpreted as a nil endogenous event for the target [[Entity]]: the observer saw the input, but no new domain transition was committed.

Related concepts: [[Retry]], [[Delivery Semantics]], [[Command]], [[Transition]], [[Version]], [[Recovery]].
