---
realm: Operational Semantics
---

# Ordering

Realm: Operational Semantics

Ordering defines the scope within which events, commands, observations, or effects are sequenced.

Ordering is always relative to a space:

- A key.
- A stream.
- A partition.
- An actor identity.
- A transaction.
- A workflow history.
- An entity version history.

An ordered delivery edge does not necessarily mean the domain transition has committed. It only means the delivery mechanism preserves order within its stated boundary.

Ordering supports version histories, replay, projection updates, concurrency control, and coherent behavior over time.

For [[CRDTs]], ordering requirements are type-specific. Some merge functions are insensitive to message order, while operation-based CRDTs may require causal ordering or explicit causal metadata.

Related concepts: [[Delivery Semantics]], [[Version]], [[Event]], [[Concurrency Control]], [[CRDTs]], [[Enrichment and Order]], [[Brokers]], [[Workflow Engines]], [[Actor Systems]].
