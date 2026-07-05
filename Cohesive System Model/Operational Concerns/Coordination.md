---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-24
updated: 2026-07-04
---

# Coordination

Coordination answers: how is multi-step or multi-participant work made coherent across [[Observer|observers]]?

Coordination defines how multiple transitions, observers, stores, processes, projections, or external systems are made to move together without losing the semantic meaning of the work.

[[Interaction]] provides the edges through which participants affect, observe, or signal one another. Coordination asks whether the resulting multi-participant behavior is coherent with the intended invariants, ordering, failure handling, and commitment boundaries.

[[Business Transactions]] are a common reason coordination is needed: business-level work often composes several local transitions, interactions, persistence boundaries, retries, and recovery paths into one domain outcome.

Coordination mechanisms include:

- Local transactions.
- Distributed transactions.
- [[Two-Phase Commit]].
- [[Consensus]] and [[Consensus Protocols|consensus protocols]].
- [[Transactional Outbox]] and [[Outbox|outbox]].
- [[Transactional Inbox]] and idempotent receivers.
- [[CRDTs]].
- [[Sagas|Sagas]] with compensation.
- [[Durable Execution|Durable execution]] with resume.
- [[Orchestration and Choreography|Choreography]] through events, protocols, or shared media.
- [[Process Managers|Process managers]] as orchestration.
- Projection update protocols.

## Orchestration and Choreography

[[Orchestration and Choreography|Orchestration and choreography]] describe where process control lives.

In orchestration, one logical [[Process Managers|process manager]] owns enough process execution state to decide next steps, direct participants, observe progress, retry, compensate, or complete the process. A [[Sagas|saga]] orchestrator, durable workflow, index rebuild coordinator, backfill controller, or approval workflow is orchestrated when that logical process manager controls the run, even if the physical node holding the role changes after restart or failover.

In choreography, no single process manager controls the whole execution. Participants follow local rules over shared events, messages, logs, topics, membership state, or protocols. Choreography can still have a shared global protocol and a singular goal; the process exists, but its execution is distributed across participant behavior.

Paxos is closer to choreography than an orchestrated index rebuild. It has a shared replicated-state-machine goal and often a leader or proposer, but no node simply runs the whole algorithm. Proposers, acceptors, and learners follow protocol-local rules, and a value is authorized by quorum state rather than by a process manager's private execution state. An index rebuild coordinator, by contrast, commonly assigns work, monitors workers, records progress, retries failed ranges, and decides completion for one logical rebuild process.

## Ordering, Intent, and Coordination Avoidance

[[Ordering]] preserves distinctions that may matter semantically. If `A then B` and `B then A` collapse into the same result, the model may lose intent, causality, auditability, or invariant context. Ordered, non-commutative histories are therefore valuable when the domain needs to preserve what happened before what.

Preserving order across distributed boundaries usually requires coordination. Coordination may add latency, reduce availability under partitions, constrain throughput, or create operational coupling. The design question is whether the domain invariant really requires the order being preserved.

[[Consensus]] is the coordination primitive for agreeing on one decision, value, or ordered position at a boundary. It can be used to construct linearizable replicated state by deciding a common sequence of operations and applying the same sequential transition rules at each replica. This makes consensus powerful, but also makes its costs explicit: quorum communication, persistence, membership, failure handling, and timing assumptions become part of the boundary's operational concerns.

In terms of [[Synchrony and Asynchrony|synchrony and asynchrony]], coordination is the work of synchronizing: it joins otherwise independent events, observations, transitions, or participants into a shared boundary such as a transaction, barrier, actor turn, consensus decision, or process step.

The [[Safety and Liveness|safety and liveness]] view explains this cost. Coordination often preserves safety by delaying, rejecting, or serializing work until enough information is available. Those choices may weaken liveness unless the system also supplies recovery, retry, failure detection, or partial synchrony assumptions that restore progress.

[[Progress Conditions]] make this tradeoff operational. A blocking coordination mechanism may allow one stalled participant to prevent others from finishing. Lock-free, wait-free, monotone, or commutative designs can reduce that dependency, but only when their assumptions and weaker guarantees fit the domain.

Coordination avoidance designs move work into structures where concurrent updates can be accepted without synchronously agreeing on one global order. [[CRDTs]] do this with monotonic merge or commutative operations when the domain can tolerate temporary divergence and the invariants are compatible with the data type. Probabilistic data structures can play a similar role when approximate answers are acceptable and their update or merge operations compose without central serialization.

The [[CALM Theorem|CALM theorem]] gives a sharper criterion for this choice: monotone programs can be consistently distributed without coordination, while non-monotone programs require coordination or a model change that makes incompleteness, exclusion, reservation, or eventual repair explicit.

The tradeoff is not "ordered" versus "unordered" in general. It is choosing which distinctions must be preserved and which can be safely forgotten, merged, approximated, or made commutative. Those choices determine the [[Consistency Models|consistency model]], [[Isolation|isolation]] level, and weak-isolation patterns the system can honestly claim.

[[CRDTs]] coordinate replicated state by making the merge or operation algebra converge under concurrent updates. This reduces the need for synchronous coordination for each update, but only for data types and invariants compatible with the CRDT's convergence semantics.

In [[CQRS]], coordination often centers on consistency under asynchrony: propagating write-side commits to read-side projections while preserving the required ordering, idempotency, freshness, and recovery semantics.

[[Outbox]] and [[Event Sourcing|event sourcing]] are important because they couple accepted local state change to downstream coordination through durable material. An outbox commits publication responsibility with the local transition. Event sourcing can make the committed event history the shared basis for persistence, projection, and orchestration. In both cases, the consistency claim depends on avoiding an unprotected [[Dual-Write Problem|dual write]] between authoritative state and the effect that tells other observers to act.

The right mechanism depends on the failure boundaries, persistence choices, delivery semantics, and invariants involved.

## External References

- Peter Bailis, Alan Fekete, Ali Ghodsi, Joseph M. Hellerstein, and Ion Stoica, [Coordination Avoidance in Database Systems](https://www.vldb.org/pvldb/vol8/p185-bailis.pdf), PVLDB 8(3):185-196, 2014.

Related concepts: [[Interaction|interaction]], [[Ordering|ordering]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Orchestration and Choreography|orchestration and choreography]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Consensus|consensus]], [[Consensus Protocols|consensus protocols]], [[Safety and Liveness|safety and liveness]], [[Progress Conditions|progress conditions]], [[CAP Theorem|CAP theorem]], [[CALM Theorem|CALM theorem]], [[Version Histories|version histories]], [[Consistency Models|consistency models]], [[Isolation|isolation]], [[ACID]], [[Two-Phase Commit|two-phase commit]], [[Weak Isolation Patterns|weak isolation patterns]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Durable Execution|durable execution]], [[Recovery|recovery]], [[Dual-Write Problem|dual-write problem]], [[Business Transactions|business transactions]], [[Process Graphs|process graphs]], [[CRDTs]], [[CQRS]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Brokers|brokers]], [[Invariant|invariants]].
