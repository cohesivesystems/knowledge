---
realm: Architecture Practices
kind: pattern
created: 2026-06-29
updated: 2026-06-29
aliases:
  - Inbox
  - Inbox Pattern
  - Idempotent Receiver
  - Transactional Inbox Pattern
---

# Transactional Inbox

The transactional inbox addresses the consumer-side problem of processing a delivered input exactly once in domain meaning when the delivery substrate may redeliver it.

## Cohesive Formulation

A transactional inbox commits input receipt, deduplication state, and local effects in one local persistence boundary:

```txt
receive input
  -> check inbox or deduplication record
  -> interpret as event, command, or signal
  -> commit local transition + inbox record + optional outbox record
  -> acknowledge input
```

If the same input is delivered again, the receiving observer can recognize it and produce no duplicate domain transition for the target entity.

## In the Model

The inbox complements [[Transactional Outbox|transactional outbox]]. Outbox records durable responsibility to publish after a local transition. Inbox records durable responsibility for having consumed or processed an input before acknowledging it as complete at the delivery boundary.

Together they support reliable handoff across asynchronous boundaries:

```txt
producer state + outbox commit
  -> publish, maybe more than once
  -> consumer inbox + local state commit
```

This composition is often called effectively-once processing, but the guarantee is not global magic. It is a combination of local atomic commits, stable input identifiers, idempotent interpretation, explicit acknowledgment timing, retry, and recovery.

## Failure Modes

The pattern fails when the consumer acknowledges before committing the inbox and local state, when deduplication is not in the same commit boundary as the effects it protects, when the deduplication key does not identify the semantic input, or when non-idempotent external effects happen before the local commit.

Related concepts: [[Transactional Outbox|transactional outbox]], [[Outbox|outbox]], [[Idempotency|idempotency]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Recovery|recovery]], [[Retry|retry]], [[Interaction|interaction]], [[Dual-Write Problem|dual-write problem]], [[Weak Isolation Patterns|weak isolation patterns]].
