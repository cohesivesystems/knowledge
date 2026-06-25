---
realm: Realization Substrate
---

# Workflow Engines

Realm: Realization Substrate

Workflow Engines are runtimes for durable, multi-step execution across time.

They commonly provide persisted workflow histories, timers, activity scheduling, retries, compensation, signals, [[Query|queries]], and replay or resume behavior.

In the model, workflow engines often [[Realization|realize]] [[Processes]], [[Coordination]], [[Recovery]], and long-lived [[Observer]] behavior.

A workflow activation may realize an observer for a process step. The process itself may also be modeled as an entity-observer when it has identity, durable state/history, and rules for interpreting incoming events or signals over time.

Workflow engine concerns include:

- Workflow identity.
- Durable history.
- Deterministic replay or resume.
- Activity execution.
- Timer and signal handling.
- Retry and compensation.
- External interaction boundaries.

A workflow history is a persistence choice. It must still be related back to entity versions, committed events, projections, policies, and invariants.

Related concepts: [[Realization]], [[Processes]], [[Observer]], [[Entity]], [[Query]], [[Coordination]], [[Persistence]], [[Reconstitution]], [[Retry]], [[Recovery]], [[Ordering]].
