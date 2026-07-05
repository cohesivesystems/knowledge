---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-28
updated: 2026-07-04
---

# Process

A process is coherent work unfolding over time.

A process gives semantic unity to a related sequence of [[Observation|observations]], [[Command|commands]], [[Query|queries]], [[Event|events]], [[Transition|transitions]], decisions, effects, and participant activity. It is not defined by any particular runtime, workflow engine, scheduler, thread, transaction manager, or broker. Those belong to [[Realization|realization]].

A process is characterized by:

- A subject, purpose, or correlation [[Identity|identity]].
- Participants such as [[Observer|observers]], [[Entity|entities]], people, agents, services, stores, models, or external systems.
- Inputs it observes or receives.
- Decisions, policies, and invariants that govern progression.
- Steps, phases, or transitions that describe meaningful progress.
- Outputs, effects, artifacts, or signals emitted as it progresses.
- Completion, rejection, cancellation, timeout, compensation, rollback, promotion, or failure meanings.
- Optional process state, history, or checkpoints.
- Flows that describe how process inputs, outputs, signals, and effects move between participants.

The same semantic process may have several executions and several realizations. A long-running domain process may be advanced by many short [[Durable Execution|durable executions]]. A request operation may execute a short-lived process inside an application host. A database transaction may realize rollback semantics for a bounded sequence of database operations. An OS process, OS thread, fiber, workflow activation, actor turn, scheduler task, or HTTP request handler may realize part of a process without being identical to the semantic process.

Processes may be modeled as [[Entity|entities]] when they have identity, durable state, versioned history, or lifecycle transitions. Processes may be modeled as [[Observer|observers]] when they interpret inputs relative to their own state, history, policies, and boundary.

Examples include:

- OS processes and OS threads executing work across one or more operating-system scheduling units.
- Logical processes spanning fibers, green threads, coroutines, or tasks managed by a scheduler.
- ASP.NET operations that perform multiple steps, possibly wrapped by [[Durable Execution|durable execution]].
- Driver onboarding, where a domain lifecycle is backed by entity transitions and coordinated by runtime listeners, effect emitters, concurrency control, UI activity, and durable step advancement.
- UI wizards or sessions that coordinate with a domain process without being the same process.
- Index rebuilds, backfills, data repairs, migrations, and other resumable maintenance work.
- [[Process Managers|Process managers]] that explicitly orchestrate process progress.
- [[Sagas|Sagas]], where selected steps have compensating actions.
- RDBMS transactions, which attach ACID commit and rollback semantics to a bounded sequence of database operations.
- ML workflows such as normalizing training examples, generating or projecting datasets, running models, transforming and persisting model artifacts, evaluating outcomes, and promoting selected models.
- Human approval, escalation, exception-handling, compliance, or review procedures.
- Control loops that observe state, decide, emit corrective commands, and observe the resulting changes.


## Process Composition
Processes compose. One process may produce outputs, artifacts, observations, commands, or events consumed by another process. Compositions may be linear pipelines, branching protocols, nested sub-processes, concurrent processes over the same subject, or feedback loops where later outputs become future inputs.

Process composition requires attention to boundary, identity, ordering, idempotency, persistence, retry, recovery, and compensation. Without those semantics, individually valid process steps may fail to compose into coherent work.

[[Process Theories|Process theories]] provide the broader discipline for this composition. They ask what a process exposes at its interface, which observations and effects cross boundaries, how sequential, concurrent, nested, choice, and feedback compositions are formed, and which realization obligations must be preserved by workflows, [[Process Managers|process managers]], [[Sagas|sagas]], durable executions, actors, transactions, brokers, or lower physical processes.

## Related Concepts

Related concepts: [[Process Theories|process theories]], [[Behavior|behavior]], [[Observer|observer]], [[Entity|entity]], [[Observation|observation]], [[Event|event]], [[Command|command]], [[Query|query]], [[Transition|transition]], [[Identity|identity]], [[State|state]], [[Processes|processes]], [[Coordination|coordination]], [[Orchestration and Choreography|orchestration and choreography]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Durable Execution|durable execution]], [[Recovery|recovery]], [[Realization|realization]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Trace and Feedback|trace and feedback]], [[Compositionality|compositionality]].
