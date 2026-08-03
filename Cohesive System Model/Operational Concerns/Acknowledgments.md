---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-29
updated: 2026-08-02
aliases:
  - Acknowledgment
  - Ack
  - Acks
---

# Acknowledgments

Acknowledgments answer: what does a participant or substrate claim has happened?

An acknowledgment is a signal that some boundary accepted responsibility, persisted data, processed input, advanced a cursor, committed a transition, or completed a narrower protocol step. Its meaning is defined by the protocol and boundary that emit it.

Acknowledgment is not the same as domain commitment. A transport acknowledgment may only mean bytes were received. A broker acknowledgment may mean the broker accepted a message or that a consumer advanced an offset. A workflow acknowledgment may mean a checkpoint committed. A command response may mean an entity transition committed. These claims should not be treated as interchangeable.

Acknowledgment is also not a generic synonym for [[Delivery Progress and Settlement|provider settlement]], replay position, or durable application progress. Settlement is the narrower operation that changes provider-managed delivery state. A replay cursor selects retained input. Application progress proves which input and effects the application durably accounted for. An acknowledgment can report any of those facts only when its protocol and boundary state that precise meaning.

## Common Meanings

An acknowledgment may mean:

- Accepted for transmission.
- Accepted by a broker or channel.
- Persisted by a broker or store.
- Delivered to a consumer process.
- Processed by an application handler.
- Committed by an entity transition.
- Recorded as a workflow checkpoint.
- Offset, cursor, or claim advanced.
- Provider delivery state settled, released, deferred, or quarantined.
- Responsibility transferred to another participant.

The model should state which one applies.

## Failure Modes

Acknowledging too early can lose work. For example, a consumer that commits an offset before committing its local transition may not receive the input again after a crash.

Acknowledging too late can duplicate work. For example, a consumer that commits local state but crashes before acknowledging the broker may receive the same input again and must rely on [[Idempotency|idempotency]], expected versions, or a [[Transactional Inbox|transactional inbox]].

Acknowledgment therefore belongs with [[Delivery Semantics|delivery semantics]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Commit Boundaries|commit boundaries]], [[Durability|durability]], [[Recovery|recovery]], and [[Effect Models|effect-structure]] design.

For a consuming channel, the model should distinguish the acknowledgment signal from the authority used to settle current provider state and from the durable progress that justifies settlement. A failed settlement call can be ambiguous after provider dispatch; recovery may need to reconcile provider state rather than assume either delivery or non-delivery.

Related concepts: [[Delivery Semantics|delivery semantics]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Interaction|interaction]], [[Interaction Protocols|interaction protocols]], [[Interaction Channels|interaction channels]], [[Boundaries|boundaries]], [[Commit Boundaries|commit boundaries]], [[Effect Models|effects]], [[Durability|durability]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Brokers|brokers]], [[Network Channels|network channels]], [[Network|network]].
