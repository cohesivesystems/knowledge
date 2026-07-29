---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-07-28
aliases:
  - Process Structure
  - Process Structures
---

# Process Graphs

Process graphs describe how [[Process|semantic processes]] are arranged across time, observer models, entity models, relation models, boundaries, and external systems.

A process graph may describe a domain process, [[Sagas|saga]], [[Process Managers|process manager]], durable workflow, orchestration, choreography, operational procedure, transaction, runtime operation, scheduler-managed logical process, or resumable maintenance procedure. The model treats the graph as structure when it gives coherence to a series of related observations, commands, events, transitions, decisions, effects, and artifacts. This describes coordination shape and participant roles, not the workflow engine, scheduler, transaction manager, application host, or operating-system mechanism that realizes it.

[[Business Transactions]] are domain-level process structures whose progress, acceptance, rejection, compensation, or completion matters to the business. They may use one process graph or several cooperating process graphs.

Process graphs may include process state and may coordinate several participants without making every participant part of one transaction.

A process may be modeled as a special kind of [[Entity|entity]] and [[Observer|observer]] when it has its own identity, durable state or history, and rules for interpreting incoming events, signals, or commands over time.

A process graph should distinguish its definition from execution material:

- The **process definition** gives stable typed nodes, edges, ports, branches, regions, outcomes, recovery policy, and semantic revision.
- A **process instance** is one durable logical journey through the definition.
- A **process attempt** is one recovery or continuity epoch within the instance.
- An **activation** is one finite execution slice.
- A **token** represents one active [[Control Flow|control-flow]] branch.
- Continuation state, checkpoints, inboxes, outboxes, and operation ledgers persist enough material to resume or recover execution.

A display name or source position is not sufficient compatibility evidence for long-lived process state. A persisted continuation must identify the exact definition identity, semantic revision, and normalized content it interprets, unless an explicit migration establishes another correspondence.

[[Process Theories|Process theories]] give the guiding language for process graphs. They distinguish the semantic process from its coordination shape, operational guarantees, and realization substrate while preserving how processes compose, interact, recover, and feed back over time.

Process graphs have [[Flow Views|flow views]]. A flow view describes how process inputs, outputs, signals, observations, commands, events, effects, or artifacts move between participants. Flow is therefore a useful view of process movement, but it is not the whole process graph. The graph also includes subject identity, participant roles, state, decisions, policies, transitions, recovery, compensation, and completion meanings.

[[Orchestration and Choreography|Orchestration and choreography]] are process coordination shapes. In orchestration, a coordinating observer or [[Process Managers|process manager]] owns more of the decision surface. In choreography, participants advance the process through events, protocols, subscriptions, shared media, and local reactions. Choreography can still have a shared global protocol and singular goal; it lacks one explicit process manager controlling the whole execution. Many systems mix both shapes, so the model should state where process identity, authority, ordering, recovery, and completion meaning live.

Process graph concerns include:

- The subject or correlation identity.
- Participant observers and entities.
- Current process state.
- Steps, decisions, and transitions.
- Stable typed branch, fork, join, wait, timer, recurrence, and terminal-outcome structure.
- Inputs, outputs, effects, artifacts, and movement paths.
- Explicit durable cuts at which one finite activation may yield and later continue.
- Compensation or recovery behavior.
- Delivery and retry expectations.

Process graphs own coordination state: active branches, waits, correlation, interaction results, replies, compensation progress, recovery progress, and terminal outcomes. They do not own duplicated aggregate business state. Entity observations and [[Transition Models|transition models]] remain governed by their own entity and authority boundaries.

Free graph cycles and arbitrary recursion hide progress and recovery obligations. Long-lived or recurrent processes should use explicit recurrence, feedback, polling, timers, signals, or scheduled reactivation with declared progress, cancellation, durable-cut, deadline, and failure meanings.

Forks and joins should identify stable branches, join mode, failure and cancellation behavior, and whether completion order is semantically observable. Durable waits should define registration, buffering, identity, admission, claim, consumption, arbitration, timeout, late-input, stale-input, and retention meanings before a realization chooses a workflow engine, database, broker, or actor mechanism.

A join that waits for a branch that was never enabled, was cancelled without changing the completion set, or can no longer produce its token creates a structural [[Deadlock and Livelock|workflow deadlock]]. Process-graph validation should distinguish such unreachable completion from a runtime wait on a slow or failed external participant.

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

## External References

- Gregor Hohpe and Bobby Woolf, [Process Manager](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html), *Enterprise Integration Patterns*, 2003.
- Enterprise Integration Patterns, [Message Routing patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html), including Routing Slip, Scatter-Gather, and Composed Message Processor.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Process Theories|process theories]], [[Process|process]], [[Control Flow|control flow]], [[Execution Kernel|execution kernel]], [[Business Transactions|business transactions]], [[Flow Views|flow views]], [[Routing Models|routing models]], [[Flow Operators|flow operators]], [[Correlation and Conversations|correlation and conversations]], [[Coordination|coordination]], [[Deadlock and Livelock|deadlock and livelock]], [[Orchestration and Choreography|orchestration and choreography]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Durable Execution|durable execution]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Observer Models|observer models]], [[Entity Models|entity models]], [[Transition Models|transition models]], [[Observer|observer]], [[Entity|entity]], [[Event|event]], [[Effect|effect]], [[Command|command]], [[State|state]], [[Commit Boundaries|commit boundaries]], [[Recovery|recovery]], [[Policy Scopes|policy scopes]], [[Invariant Scopes|invariant scopes]].
