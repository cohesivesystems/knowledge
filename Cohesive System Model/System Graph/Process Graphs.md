---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-07-05
aliases:
  - Processes
  - Process Structure
  - Process Structures
---

# Process Graphs

Process graphs describe how [[Process|semantic processes]] are arranged across time, observer models, entity models, relation models, boundaries, and external systems.

A process graph may describe a domain process, [[Sagas|saga]], [[Process Managers|process manager]], durable workflow, orchestration, choreography, operational procedure, transaction, runtime operation, scheduler-managed logical process, or resumable maintenance procedure. The model treats the graph as structure when it gives coherence to a series of related observations, commands, events, transitions, decisions, effects, and artifacts. This describes coordination shape and participant roles, not the workflow engine, scheduler, transaction manager, application host, or operating-system mechanism that realizes it.

[[Business Transactions]] are domain-level process structures whose progress, acceptance, rejection, compensation, or completion matters to the business. They may use one process graph or several cooperating process graphs.

Process graphs may include process state and may coordinate several participants without making every participant part of one transaction.

A process may be modeled as a special kind of [[Entity|entity]] and [[Observer|observer]] when it has its own identity, durable state or history, and rules for interpreting incoming events, signals, or commands over time.

[[Process Theories|Process theories]] give the guiding language for process graphs. They distinguish the semantic process from its coordination shape, operational guarantees, and realization substrate while preserving how processes compose, interact, recover, and feed back over time.

Process graphs have [[Flow Views|flow views]]. A flow view describes how process inputs, outputs, signals, observations, commands, events, effects, or artifacts move between participants. Flow is therefore a useful view of process movement, but it is not the whole process graph. The graph also includes subject identity, participant roles, state, decisions, policies, transitions, recovery, compensation, and completion meanings.

[[Orchestration and Choreography|Orchestration and choreography]] are process coordination shapes. In orchestration, a coordinating observer or [[Process Managers|process manager]] owns more of the decision surface. In choreography, participants advance the process through events, protocols, subscriptions, shared media, and local reactions. Choreography can still have a shared global protocol and singular goal; it lacks one explicit process manager controlling the whole execution. Many systems mix both shapes, so the model should state where process identity, authority, ordering, recovery, and completion meaning live.

Process graph concerns include:

- The subject or correlation identity.
- Participant observers and entities.
- Current process state.
- Steps, decisions, and transitions.
- Inputs, outputs, effects, artifacts, and movement paths.
- Compensation or recovery behavior.
- Delivery and retry expectations.

Examples include:

- OS processes and OS threads executing work across one or more scheduling units.
- Logical processes spanning fibers, green threads, coroutines, or runtime tasks.
- ASP.NET operations that perform multiple steps, possibly wrapped by [[Durable Execution|durable execution]].
- Driver onboarding, coordinated across entity state transitions, runtime listeners, effect emitters, concurrency control, UI activity, and durable step advancement.
- Index rebuilds, backfills, data repairs, and migrations that must resume after a crash.
- [[Sagas|Sagas]] whose selected steps have compensating actions.
- RDBMS transactions that attach ACID commit and rollback semantics to database operations.
- ML workflows that normalize training examples, generate or project datasets, run models, transform and persist model artifacts, evaluate outcomes, and promote selected models.

Process graphs compose when outputs of one process feed another process as observations, commands, events, artifacts, or decisions. Such compositions may be pipelines, nested sub-processes, concurrent processes, or feedback loops.

Related concepts: [[Process Theories|process theories]], [[Process|process]], [[Business Transactions|business transactions]], [[Flow Views|flow views]], [[Coordination|coordination]], [[Orchestration and Choreography|orchestration and choreography]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Durable Execution|durable execution]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Observer Models|observer models]], [[Entity Models|entity models]], [[Observer|observer]], [[Entity|entity]], [[Event|event]], [[Command|command]], [[State|state]], [[Recovery|recovery]], [[Policy Scopes|policy scopes]], [[Invariant Scopes|invariant scopes]].
