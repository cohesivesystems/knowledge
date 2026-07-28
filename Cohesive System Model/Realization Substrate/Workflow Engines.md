---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-07-27
---

# Workflow Engines

Workflow Engines are runtimes for defining, coordinating, and operating multi-step workflows across time.

They commonly provide workflow identity, workflow state or history, timers, activity scheduling, retries, compensation, signals, [[Query|queries]], inspection, and operational controls. Many workflow engines also provide [[Durable Execution|durable execution]], but durable execution is an architecture practice, not the definition of a workflow engine.

In the model, workflow engines often [[Realization|realize]] [[Process Graphs|process graphs]], [[Coordination|coordination]], [[Durability|durability]] of workflow material, [[Recovery|recovery]], [[Durable Execution|durable execution]], and long-lived [[Observer|observer]] behavior.

A workflow engine is a candidate interpreter of a process graph, not the authority that defines process meaning. Engine-native definitions, delegates, task registrations, workflow names, and histories are valid realization artifacts only when their correspondence to the authored or canonical process graph is explicit and compatible.

A workflow activation may realize an observer for a process step. The process itself may also be modeled as an entity-observer when it has identity, durable state/history, and rules for interpreting incoming events or signals over time.

A workflow engine may also be a [[Durable Execution Engines|durable execution engine]] when it persists enough execution material to resume, replay, retry, or recover coherent execution. A saga runtime, [[Process Managers|process manager]], DAG runner, human-workflow system, or state-machine engine may be a workflow engine without exposing the same durable execution semantics.

Workflow engine concerns include:

- Workflow identity.
- Workflow state or history.
- Durability and durable execution guarantees, if provided.
- Replay, resume, or continuation behavior.
- Activity execution.
- Timer and signal handling.
- Retry and compensation.
- External interaction boundaries.

A workflow history is a persistence choice. It must still be related back to entity versions, committed events, projection models, policy scopes, and invariant scopes.

Long-lived workflow state should pin the exact process definition identity, semantic revision, and normalized content identity. Replaying a different definition under the same name is not compatible by default. A definition change requires exact compatibility evidence or an explicit migration of continuation state.

A workflow engine that claims [[Execution Kernel|execution-kernel]] conformance must preserve finite activation and durable-cut semantics, complete token and join state where parallelism is supported, wait registration and arbitration, stable effect identity, retry and ambiguous-outcome rules, and the distinction among replay, retry, recovery, restart, pause, cancellation, termination, and migration.

An engine may offer stronger native guarantees, but unavailable atomicity, ordering, durability, response, idempotency, or recovery requirements must remain explicit rather than degrade to engine defaults.

Related concepts: [[Execution Kernel|execution kernel]], [[Realization|realization]], [[Process Graphs|process graphs]], [[Process|process]], [[Transition Models|transition models]], [[Effect|effect]], [[Durability|durability]], [[Durable Execution|durable execution]], [[Durable Execution Engines|durable execution engines]], [[Observer|observer]], [[Entity|entity]], [[Query|query]], [[Coordination|coordination]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Retry|retry]], [[Recovery|recovery]], [[Ordering|ordering]].
