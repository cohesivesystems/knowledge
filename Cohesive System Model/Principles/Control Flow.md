---
realm: Principles
kind: principle
created: 2026-07-28
updated: 2026-07-29
aliases:
  - Control-Flow Distinctions
---

# Control Flow

Control flow describes how one possible action, operation, step, or continuation becomes enabled, selected, and followed by another at a declared boundary.

The term is overloaded across domain processes, system graphs, programs, runtimes, interactions, and operations. Cohesive therefore treats control flow as a qualified family of relations rather than one universal edge type. A model should state what progresses, what selects the successor, which boundary observes that progression, and what an arrow or dependency means.

Control does not necessarily imply a central controller. A successor may be selected by a deterministic transition, data-dependent branch, participant interaction, nondeterministic choice, scheduler, distributed protocol, or environmental event.

## Qualified Meanings

| Meaning | What progresses or is controlled | Canonical home |
| --- | --- | --- |
| **process control flow** | Steps, branches, tokens, forks, joins, waits, recurrence, cancellation, and terminal outcomes within a semantic process structure. | [[Process Graphs|process graphs]] and [[Workflow Patterns|workflow patterns]] |
| **program or evaluation control flow** | Expressions, instructions, calls, returns, exceptions, continuations, loops, and evaluation paths within a program or runtime. | [[Reduction, Evaluation, and Confluence|reduction and evaluation]], [[Runtimes|runtimes]], and [[Scheduling|scheduling]] |
| **[[Interaction Control Flow|interaction control flow]]** | Which participant actively pushes, fetches, polls, calls, or delivers at an interaction boundary. | [[Interaction Control Flow|interaction control flow]] |
| **control-flow synchrony** | Whether one logical operation waits for a result, observation, or completion before continuing. | [[Synchrony and Asynchrony|synchrony and asynchrony]] |
| **[[Operational Control|operational control]]** | Authorized intervention that pauses, resumes, routes, drains, replays, or otherwise changes running-system behavior. | [[Operational Control|operational control]] |
| **[[Flow Control|flow control]]** | How much work may be admitted or remain in flight in response to capacity. | [[Flow Control|flow control]] |
| **feedback control** | How observations of behavior regulate future action through a controller and actuator. | [[Control Theory|control theory]] and [[Control Models|control models]] |

The boundary qualifier is essential. One process-progression edge may lower into several program evaluations and distributed interactions. A synchronous-looking program call may lower into queues and callbacks. A pull interaction may drive data opposite to the interaction-control direction without reversing process progression.

## Related but Distinct Relations

Control flow should not be inferred from:

- **Data flow**, which says where a value moves.
- **Causal flow**, which says which occurrence may have influenced another.
- **Ordering**, which constrains relative positions without necessarily selecting the next step.
- **Scheduling**, which selects among enabled work but does not necessarily define which successors are semantically valid.
- **Orchestration authority**, which says who owns a process decision surface.
- **Flow control**, which regulates capacity rather than branch or token progression.
- **Feedback control**, which regulates a controlled variable rather than selecting the next semantic or program step.

These relations may align in a particular realization, but an unqualified arrow must not stand for all of them. [[Flow Views|Flow views]] should label whether an edge means carried-value movement, process progression, causality, interaction drive, or another relation.

## Modeling Discipline

When control flow matters, state:

- The abstraction layer, subject, and boundary.
- The current position or continuation state and the possible successors.
- What enables, selects, rejects, suspends, or cancels a successor.
- Whether choice is deterministic, policy-driven, nondeterministic, scheduled, or externally triggered.
- How concurrency, forks, joins, recurrence, and termination are represented.
- Whether waiting is logical, durable, or physically blocking.
- Which state must survive interruption for progression to resume correctly.
- What each control-flow edge claims and which related data, causal, interaction, and ordering edges are separate.

This qualification preserves correspondence across layers without collapsing a semantic process into a program counter, an interaction driver, a workflow engine, or a capacity protocol.

## External References

- Workflow Patterns Initiative, [Control-Flow Patterns](http://www.workflowpatterns.com/patterns/control/).
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Process Theories|process theories]], [[Control Theory|control theory]], [[Control Models|control models]], [[Process|process]], [[Process Graphs|process graphs]], [[Workflow Patterns|workflow patterns]], [[Flow Views|flow views]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Flow Control|flow control]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Operational Control|operational control]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Runtimes|runtimes]], [[Scheduling|scheduling]], [[Ordering|ordering]], [[Causality|causality]], [[Orchestration and Choreography|orchestration and choreography]], [[Trace and Feedback|trace and feedback]].
