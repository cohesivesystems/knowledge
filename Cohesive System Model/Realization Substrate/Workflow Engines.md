---
realm: Realization Substrate
kind: realization-substrate
---

# Workflow Engines

Workflow Engines are runtimes for defining, coordinating, and operating multi-step workflows across time.

They commonly provide workflow identity, workflow state or history, timers, activity scheduling, retries, compensation, signals, [[Query|queries]], inspection, and operational controls. Many workflow engines also provide [[Durable Execution]], but durable execution is a guarantee, not the definition of a workflow engine.

In the model, workflow engines often [[Realization|realize]] [[Processes]], [[Coordination]], [[Durable Execution]], [[Recovery]], and long-lived [[Observer]] behavior.

A workflow activation may realize an observer for a process step. The process itself may also be modeled as an entity-observer when it has identity, durable state/history, and rules for interpreting incoming events or signals over time.

A workflow engine may also be a [[Durable Execution Engines|durable execution engine]] when it persists enough execution material to resume, replay, retry, or recover coherent execution. A saga runtime, process manager, DAG runner, human-workflow system, or state-machine engine may be a workflow engine without exposing the same durable execution semantics.

Workflow engine concerns include:

- Workflow identity.
- Workflow state or history.
- Durable execution guarantees, if provided.
- Replay, resume, or continuation behavior.
- Activity execution.
- Timer and signal handling.
- Retry and compensation.
- External interaction boundaries.

A workflow history is a persistence choice. It must still be related back to entity versions, committed events, projections, policies, and invariants.

Related concepts: [[Realization]], [[Processes]], [[Process]], [[Durable Execution]], [[Durable Execution Engines]], [[Observer]], [[Entity]], [[Query]], [[Coordination]], [[Persistence]], [[Reconstitution]], [[Retry]], [[Recovery]], [[Ordering]].
