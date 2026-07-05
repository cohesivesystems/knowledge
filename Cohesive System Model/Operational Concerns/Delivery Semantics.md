---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-24
updated: 2026-07-01
---

# Delivery Semantics

Delivery Semantics answers: what guarantees does an interaction edge provide?

Delivery guarantees are always scoped to a defined boundary, key, stream, partition, actor, transaction, or protocol. They do not automatically mean that a business transition committed.

Delivery semantics may specify:

- At-most-once, at-least-once, or effectively-once delivery within a defined boundary.
- Ordered delivery per key.
- Durable or volatile delivery.
- Replayable or retained delivery.
- Deduplicated delivery.
- Whether the receiver must be idempotent.
- What [[Acknowledgments|acknowledgments]] mean.

For [[CRDTs]], delivery requirements depend on the CRDT family. State-based CRDTs can tolerate duplicated state delivery when merge is idempotent. Operation-based CRDTs require the delivery assumptions under which concurrent operations commute, such as causal, reliable, or exactly-once operation delivery within the relevant boundary.

The meaning of an [[Acknowledgments|acknowledgment]] must be defined explicitly. It may mean accepted, persisted, processed, committed, responsibility transferred, or something narrower.

Delivery semantics are one way [[Synchrony and Asynchrony|asynchronous]] interaction gains stronger structure. Ordered delivery, durable delivery, acknowledgment, replay, and deduplication do not necessarily make the interaction synchronous, but they define which independent occurrences are later related, joined, or observed as coherent.

Related concepts: [[Interaction|interaction]], [[Acknowledgments|acknowledgments]], [[Ordering|ordering]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Idempotency|idempotency]], [[Recovery|recovery]], [[CRDTs]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Observer|observer]], [[Brokers|brokers]], [[Network|network]].
