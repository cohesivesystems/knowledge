---
realm: Principles
kind: principle
created: 2026-07-04
updated: 2026-07-15
status: draft
aliases:
  - Process Theory
  - Categorical Process Theory
  - Process Language
  - Process Semantics
---

# Process Theories

Process theories are modeling disciplines for work, interaction, change, and behavior that unfold over time.

In Cohesive, process theories provide a shared language for [[Process|processes]], [[Process Graphs|process graphs]], workflows, [[Process Managers|process managers]], [[Sagas|sagas]], durable executions, choreographies, orchestrations, feedback loops, control loops, and physical processes without making all of those things identical.

The goal is not to choose one universal formalism. Open systems, Petri nets, process calculi, session types, string diagrams, compositional games, dynamical systems, control theory, quantum processes, and compositional concurrency each emphasize different structure. Cohesive uses them as sources of discipline for asking what composes, what is observed, what crosses a boundary, and what must be preserved by realization.

## Cohesive Formulation

A process theory makes these elements explicit:

- The units treated as processes.
- The interfaces or [[Boundaries|boundaries]] through which processes interact.
- The observations, events, commands, queries, signals, artifacts, and effects that may cross those boundaries.
- The allowed composition operations: sequential composition, parallel composition, nesting, [[Nondeterminism and Choice|choice]], synchronization, hiding, restriction, merge, and feedback.
- The state, history, trace, run, schedule, or behavior used to describe process evolution.
- The equivalence or refinement relation used to say when two process descriptions are the same enough.
- The failure, cancellation, compensation, retry, timeout, and recovery meanings.
- The realization obligations that make the process executable without changing its intended meaning.

This makes process language compositional. A process is not merely a named blob of activity. It has an interface, internal progression, observable effects, and composition rules.

## Layered Process Meaning

The word "process" is overloaded. Cohesive keeps the layers separate:

- A semantic [[Process|process]] is coherent work unfolding over time.
- [[Process Graphs|Process graphs]] arrange semantic processes across observer models, entity models, flow views, states, decisions, and external systems.
- [[Coordination]] describes how multi-participant process work is made coherent.
- [[Durability]] and [[Recovery|recovery]] describe how process execution material survives failure and is used after interruption.
- [[Durable Execution|Durable execution]] is an architecture practice that applies those concerns to logical execution.
- [[Workflow Engines|Workflow engines]], [[Durable Execution Engines|durable execution engines]], actors, brokers, [[Scheduling|schedulers]], transaction managers, and operating-system processes are realization substrate.
- Physical processes are lower-layer behavior through which the infrastructure itself is ultimately realized.

These layers can be related, but they should not be collapsed. An operating-system process may realize part of a runtime. A runtime task may realize one observer turn. A workflow activation may realize one process step. None of those mechanisms is automatically identical to the semantic process being modeled.

## Process Managers, Sagas, Workflows, and Durable Execution

Process theories give tighter language for common architecture terms:

- A [[Process Managers|process manager]] is an orchestration role with process identity. It observes inputs, records progress or history, decides next steps, and emits commands, events, signals, or effects across boundaries.
- A [[Sagas|saga]] is a business-recovery process manager. It handles business failure, partial completion, compensation, alternate paths, negotiation, escalation, or human intervention.
- [[Durable Execution|Durable execution]] is an execution-recovery practice. It resumes the same logical computation after interruption through persisted progress, history, timers, signals, checkpoints, retry state, or pending work.
- A workflow is an authored or runtime-managed process description. A workflow engine may realize workflow execution, durable execution, inspection, timers, signals, activities, retries, and compensation, but the engine is not the semantic process itself.

This distinction is practical. A saga implemented on durable execution still contains business recovery logic. Durable execution can keep the computation running; it does not decide whether a completed business action should be compensated. A hand-written process manager can be a valid realization when it preserves identity, ordering, persistence, idempotency, delivery, and recovery requirements.

## Orchestration and Choreography

[[Orchestration and Choreography|Orchestration and choreography]] are coordination shapes, not claims that one style is inherently better than the other.

In orchestration, a coordinating observer or [[Process Managers|process manager]] owns more of the decision surface. It observes process state, issues commands, waits for replies or events, handles timeouts, and decides next steps. Orchestration makes control explicit, but can concentrate [[Authority|authority]], coupling, and failure impact.

In choreography, participants advance the process through published events, protocols, subscriptions, shared logs, shared media, and local reactions. Choreography does not mean there is no process or no global protocol. It means the process is not controlled by one explicit process manager. Choreography distributes control and can reduce central coupling, but it can also hide the process boundary, make global progress harder to observe, and leave compensation or timeout behavior implicit.

The distinction is a matter of degree. [[Consensus Protocols|Consensus protocols]] such as Paxos use a shared global protocol and may use a leader or proposer, but the leader is a dynamic protocol role constrained by quorum rules rather than a process manager that owns the whole execution.

Both shapes need the same basic questions answered:

- What is the process identity?
- Which participant can observe which state?
- Which events, commands, and effects advance the process?
- Where are ordering, idempotency, retry, and acknowledgment meanings defined?
- Who can decide completion, rejection, cancellation, timeout, or compensation?
- Which process state is durable enough to support recovery?

Many real systems mix both shapes. A process may be orchestrated inside one boundary and choreographed across another.

## Feedback and Physical Reconciliation

Process theories must account for feedback. Outputs may become future inputs through event loops, control loops, retries, projections, workflow timers, actor messages, human review, or physical response. [[Trace and Feedback|Trace and feedback]] gives the vocabulary for these loops, while [[Ordering]], [[Idempotency]], [[Recovery]], and [[Rate Limiting|rate limiting]] keep them operationally honest.

This matters because Cohesive should reconcile software processes with physical process theories rather than only with application architecture vocabulary. Dynamical systems emphasize state evolution over time. Control theory emphasizes observation, decision, actuation, and feedback. Petri-net style models emphasize concurrency, resources, and enabling conditions. Quantum and categorical process theories emphasize compositional interfaces, interaction, observation, and diagrammatic reasoning.

Cohesive does not identify these physical and mathematical theories with distributed-system workflows. It uses them as compatibility checks: if the language for a workflow, saga, or process manager cannot say what state evolves, what crosses the boundary, how processes compose, and how feedback works, the language is too weak.

## Compiler Discipline for Processes

A process realization preserves:

- Process identity and correlation.
- Participant roles and [[Authority|authority]].
- Interface boundaries and carried semantic roles.
- [[Causality]], ordering, and synchronization requirements.
- State, history, trace, checkpoint, or behavior needed for progress.
- Commit, acknowledgment, and effect boundaries.
- Retry, timeout, cancellation, recovery, and compensation meanings.
- Observable progress and completion meanings.

A process compiler may lower one description into workflow histories, actor reminders, event streams, broker subscriptions, database records, timers, transactional outboxes, inbox deduplication records, state machines, or runtime tasks. It should also name what it cannot preserve. For example, a broker topic may preserve publication order only within a partition; a process manager may recover its own state without knowing whether an external participant completed an irreversible action.

## Design Checks

When modeling a process, ask:

- What is the process boundary, subject, or correlation identity?
- What are the process inputs, outputs, observations, and effects?
- Which parts are sequential, concurrent, nested, optional, compensating, or feedback-shaped?
- Which participant interprets each event, command, signal, or observation?
- What must be synchronized, and what may remain asynchronous?
- What state or history is needed to recover coherently?
- What is the equivalence relation between two executions of the process?
- Which realization mechanisms preserve the process theory, and where do they weaken it?

## External References

- C. A. R. Hoare, [Communicating Sequential Processes](https://doi.org/10.1145/359576.359585), *Communications of the ACM* 21(8):666-677, 1978.
- Robin Milner, [A Calculus of Communicating Systems](https://doi.org/10.1007/3-540-10235-3), LNCS 92, Springer, 1980.
- Robin Milner, Joachim Parrow, and David Walker, [A Calculus of Mobile Processes, I](https://doi.org/10.1016/0890-5401(92)90008-4) and [II](https://doi.org/10.1016/0890-5401(92)90009-5), *Information and Computation* 100(1):1-77, 1992.
- Robin Milner, [Communication and Concurrency](https://www.research.ed.ac.uk/en/publications/communication-and-concurrency/), Prentice Hall, 1989.

Related concepts: [[System Language and Realization|system language and realization]], [[Process|process]], [[Process Graphs|process graphs]], [[State Machines|state machines]], [[Behavior|behavior]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Compositionality|compositionality]], [[Trace and Feedback|trace and feedback]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Coordination|coordination]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Causality|causality]], [[Authority|authority]], [[Orchestration and Choreography|orchestration and choreography]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Interaction|interaction]], [[Durability|durability]], [[Durable Execution|durable execution]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Recovery|recovery]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Effects|effects]], [[Boundaries|boundaries]], [[Realization|realization]].
