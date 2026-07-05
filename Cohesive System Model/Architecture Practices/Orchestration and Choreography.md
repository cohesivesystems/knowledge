---
realm: Architecture Practices
kind: pattern
aliases:
  - Orchestration
  - Choreography
---

# Orchestration and Choreography

Orchestration and choreography are forms of [[Coordination|coordination]] that differ by where process control lives in the realization.

Both forms can have a shared goal, a shared protocol, a process boundary, and durable state. The distinction is a matter of degree: how much one logical node or role controls execution of the protocol.

## Orchestration

Orchestration coordinates a process through an explicit [[Process Managers|process manager]]. One logical role owns process execution state, decides next steps, directs participants, observes enough replies or events to advance, and handles timeout, retry, cancellation, compensation, or completion.

The physical node holding the role may change across leases, failover, restarts, or durable execution recovery. The design remains orchestrated when one logical process manager controls the run.

Examples include:

- A [[Sagas|saga]] orchestrator that sends commands and compensating commands to participants.
- A durable workflow that records workflow history, schedules activities, observes signals, and resumes after host failure.
- An index rebuild coordinator that tracks partitions, assigns ranges to workers, monitors progress, retries failed work, and decides completion.
- A CI pipeline controller that schedules jobs, waits for results, applies dependencies, and marks the run failed or complete.
- A human approval workflow that records pending approvals, sends reminders, handles expiry, and escalates exceptions.

## Choreography

Choreography coordinates a process without one explicit process manager controlling the whole execution. Process progress emerges from participants following local rules over shared messages, events, logs, topics, membership state, or protocols.

Choreography does not mean there is no process or no global protocol. The global protocol may be implicit in aligned configurations, topic contracts, schemas, command/event meanings, subscription rules, quorum rules, or shared state-machine specifications. What is absent, or weaker, is a single node that monitors and controls execution of the process.

Examples include:

- Event-driven order fulfillment where payment, inventory, shipping, notification, and projection services react to published events and local state.
- Pub/sub projection pipelines where consumers independently follow committed event streams and update their own read models.
- Gossip protocols where peers exchange local observations and converge without a central coordinator.
- [[CRDTs|CRDT]] replication where replicas accept compatible local updates and merge by algebraic rules.
- Domain event choreography where each participant owns its own transition and emits events for others to interpret.

## Middle Ground

Many distributed protocols sit between pure choreography and classic orchestration.

Paxos can be seen as more choreographed than an index rebuild. Paxos implements a single replicated state machine and coordinates participants toward a shared decision, but no single node "runs the algorithm" in the way an index rebuild coordinator runs a rebuild. Proposers, acceptors, and learners follow protocol-local rules. A leader or proposer may coordinate a round and make global proposals, but it cannot unilaterally authorize the history; quorum intersection and acceptor state determine which value is chosen. The leader role can change, and the authority to decide is distributed through the protocol.

An index rebuild may also have a leader that changes across runs or after restart. It is still more orchestrated when one logical process manager records execution state, assigns work to workers, directly observes their progress, retries failed work, and decides completion for the rebuild process.

[[Consensus Protocols|Consensus protocols]] such as Paxos, Multi-Paxos, Raft, Zab, and Viewstamped Replication often use leader-mediated choreography: a leader coordinates proposals, but correctness is constrained by distributed participant rules, quorum state, durable metadata, and recovery behavior.

[[Two-Phase Commit|Two-phase commit]] has a stronger coordinator shape than Paxos because one coordinator drives prepare and commit or abort for a fixed transaction boundary. It is still a narrow atomic-commit protocol, not a general process manager for the business process around the transaction.

## Design Questions

When classifying a process, ask:

- Where does process execution state live?
- Which role decides the next step?
- Which role observes progress or failure?
- Are participants commanded by a process manager, or do they follow local protocol rules?
- Is authority centralized, leader-mediated, quorum-mediated, or distributed?
- Can the controller role change without changing the process identity?
- Which state is durable enough to recover the process?

Related concepts: [[Coordination|coordination]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Process|process]], [[Processes|processes]], [[Observer|observer]], [[Event-Driven Architecture|event-driven architecture]], [[Durable Execution|durable execution]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Consensus|consensus]], [[Consensus Protocols|consensus protocols]], [[Two-Phase Commit|two-phase commit]], [[CRDTs]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Recovery|recovery]], [[Boundaries|boundaries]].
