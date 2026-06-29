---
realm: System Structure
kind: structural-construct
aliases:
  - Effect
  - Effect Boundary
  - Effect Boundaries
---

# Effects

Effects are modeled consequences of an accepted interpretation, transition, process step, or operational action.

An effect may be local to an [[Observer|observer]] or [[Entity|entity]] boundary, or it may cross a boundary through [[Interaction]]. Effects include committed endogenous [[Event|events]], output events, state writes, projection updates, outbox records, inbox records, messages, acknowledgments, offset commits, timers, workflow signals, documents, and calls to external systems.

Effects are not merely "side effects" in code. In a coherent system model, each important effect should have an explicit subject, boundary, commitment meaning, ordering scope, failure behavior, and recovery rule.

## Effect Boundaries

An effect boundary is the boundary at which an effect is accepted, persisted, observed, published, acknowledged, or committed.

Different effects in one business operation often commit at different boundaries:

```txt
entity transition
  -> outbox publication responsibility
  -> broker publication
  -> consumer processing
  -> downstream entity transition
```

These boundaries should not be collapsed. A database commit, broker acknowledgment, workflow checkpoint, offset commit, and business completion can all be successful at their own boundaries while meaning different things for the domain.

## Duplicate Effects

Effects that may be retried, replayed, resumed, or redelivered need [[Idempotency]], deduplication, expected-version checks, or another rule that prevents duplicate domain effects.

For example, handling the same input twice may produce a nil endogenous event for the target entity while still recording an operational observation that the duplicate was seen. Publishing the same outbox record twice may be acceptable only when the receiver has an idempotent protocol, deduplication record, or [[Transactional Inbox|inbox]].

Related concepts: [[Boundaries]], [[Commit Boundaries]], [[Acknowledgments]], [[Interaction]], [[Delivery Semantics]], [[Ordering]], [[Idempotency]], [[Retry]], [[Recovery]], [[Dual-Write Problem]], [[Outbox]], [[Transactional Inbox]], [[Business Transactions]].
