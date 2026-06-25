---
realm: Architecture Practices
---

# Sagas And Process Managers

Realm: Architecture Practices

Sagas and process managers address the problem of coordinating long-running, multi-step work across boundaries where one atomic transaction is unavailable or inappropriate.

## Cohesive Formulation

The practice is about [[Processes]] and [[Coordination]]:

- A process has identity, state, progress, and recovery behavior.
- It observes events or signals.
- It emits commands to participants.
- It may compensate, retry, time out, or escalate.

## Practice Interpretation

A saga can be modeled as an entity-observer: it has state and history, observes events, interprets them relative to a process boundary, and emits commands or endogenous process events.

## Failure Modes

The pattern fails when the process boundary is implicit, when compensation is assumed to be inverse transition, or when delivery and idempotency are ignored. Sagas do not remove consistency problems; they make consistency procedural and temporal.

Related concepts: [[Processes]], [[Coordination]], [[Observer]], [[Entity]], [[Command]], [[Event]], [[Retry]], [[Recovery]], [[Workflow Engines]], [[Trace and Feedback]].
