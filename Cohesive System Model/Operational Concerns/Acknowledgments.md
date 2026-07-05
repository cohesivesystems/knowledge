---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-29
updated: 2026-07-04
aliases:
  - Acknowledgment
  - Ack
  - Acks
---

# Acknowledgments

Acknowledgments answer: what does a participant or substrate claim has happened?

An acknowledgment is a signal that some boundary accepted responsibility, persisted data, processed input, advanced a cursor, committed a transition, or completed a narrower protocol step. Its meaning is defined by the protocol and boundary that emit it.

Acknowledgment is not the same as domain commitment. A transport acknowledgment may only mean bytes were received. A broker acknowledgment may mean the broker accepted a message or that a consumer advanced an offset. A workflow acknowledgment may mean a checkpoint committed. A command response may mean an entity transition committed. These claims should not be treated as interchangeable.

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
- Responsibility transferred to another participant.

The model should state which one applies.

## Failure Modes

Acknowledging too early can lose work. For example, a consumer that commits an offset before committing its local transition may not receive the input again after a crash.

Acknowledging too late can duplicate work. For example, a consumer that commits local state but crashes before acknowledging the broker may receive the same input again and must rely on [[Idempotency|idempotency]], expected versions, or a [[Transactional Inbox|transactional inbox]].

Acknowledgment therefore belongs with [[Delivery Semantics|delivery semantics]], [[Commit Boundaries|commit boundaries]], [[Durability|durability]], [[Recovery|recovery]], and [[Effects|effect]] design.

Related concepts: [[Delivery Semantics|delivery semantics]], [[Interaction|interaction]], [[Boundaries|boundaries]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Durability|durability]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Brokers|brokers]], [[Network|network]].
