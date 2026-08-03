---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-24
updated: 2026-08-02
---

# Delivery Semantics

Delivery Semantics answers: what guarantees does an interaction edge provide?

Delivery guarantees are always scoped to a defined boundary, key, stream, partition, actor, transaction, or protocol. They do not automatically mean that a business transition committed.

Delivery guarantee and transport reliability are distinct dimensions. A reliable byte stream can still leave an application request outcome ambiguous after connection failure. An unreliable datagram can still carry an idempotent observation whose loss is acceptable. Partial reliability can bound age or retransmission without establishing at-most-once application effects. The model should state both the delivery occurrence being guaranteed and the reliability or timeliness behavior of the channel that carries it.

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

## Delivery and Effect Occurrences

One interaction can produce several distinct occurrences:

```txt
emitted
  -> admitted by a channel
  -> delivered to a receiver
  -> processed by a handler
  -> committed at a local boundary
  -> acknowledged
  -> made externally visible or effective
  -> discharged as the intended semantic obligation
```

The sequence is descriptive rather than universal: an acknowledgment may occur before or after local commitment, visibility may lag commitment, and an external effect may remain ambiguous after the handler returns. A guarantee must identify which occurrence it covers and which identities relate retries or repeated observations across the boundaries.

A broker offset, delivery tag, handler attempt, local transaction, external operation, and business interaction have different identities and commitment rules. Exactly one occurrence in one space does not imply exactly one occurrence in another.

## At-Most-Once, At-Least-Once, and Effectively-Once

At-most-once delivery avoids redelivery after selected failures by tolerating possible loss. At-least-once delivery retries or replays until the receiver or sender observes the required acknowledgment, so duplicate delivery is an admitted outcome. Neither property alone determines whether the receiver's semantic effect occurs zero, one, or several times.

An effectively-once semantic effect is usually a composed property rather than a transport feature. It may require:

- Stable semantic operation or emission identity.
- Retryable at-least-once delivery.
- Receiver-side idempotency or deduplication.
- Atomic commitment of local effects with receipt or progress evidence.
- Durable recovery of the prior result for a repeated request.
- Target-side identity when an external non-idempotent effect is involved.

Even this composition is boundary-relative. A transaction can atomically update local state and a consumer cursor while a payment, email, or other external effect remains outside that boundary. The external target must participate in the identity and recovery protocol, or the larger outcome remains possibly duplicated or ambiguous.

Replay also differs from redelivery. Redelivery repeats an interaction occurrence under its delivery protocol. Replay intentionally reads retained history again, often for a new consumer, repaired projection, or changed interpretation. Replay needs its own effect, version, compatibility, and provenance policy.

Replay position, durable application progress, and provider settlement are likewise separate. A cursor can select retained input that the application has not yet applied. Durable progress can cover applied input while provider settlement remains pending after a crash. [[Delivery Progress and Settlement|Delivery progress and settlement]] defines the evidence and recovery cuts among those states.

Delivery semantics are one way [[Synchrony and Asynchrony|asynchronous]] interaction gains stronger structure. Ordered delivery, durable delivery, acknowledgment, replay, and deduplication do not necessarily make the interaction synchronous, but they define which independent occurrences are later related, joined, or observed as coherent.

## Modeling Checks

- Which emitted, admitted, delivered, processed, committed, acknowledged, visible, or semantic occurrence does the guarantee describe?
- Which identity relates duplicates, retries, replays, and recovered results?
- Can acknowledgment happen before or after local commitment, and what loss or duplication follows from each gap?
- Which effects share an atomic commit with receipt or progress evidence?
- Which external effects remain outside the local boundary?
- What retained material, schema, and handler interpretation make replay safe?
- Which replay position, application-progress record, and provider settlement evidence exist, and how are they related?
- Does "exactly once" name a transport occurrence, local state transition, external effect, or semantic obligation?

Related concepts: [[Interaction|interaction]], [[Interaction Channels|interaction channels]], [[Interaction Protocols|interaction protocols]], [[Acknowledgments|acknowledgments]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Ordering|ordering]], [[Commit Boundaries|commit boundaries]], [[Effect Models|effects]], [[Idempotency|idempotency]], [[Transactional Inbox|transactional inbox]], [[Outbox|outbox]], [[Recovery|recovery]], [[Compatibility and Evolution|compatibility and evolution]], [[Observability and Provenance|observability and provenance]], [[Temporal Completeness|temporal completeness]], [[CRDTs]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Observer|observer]], [[Brokers|brokers]], [[Network Channels|network channels]], [[Network|network]].
