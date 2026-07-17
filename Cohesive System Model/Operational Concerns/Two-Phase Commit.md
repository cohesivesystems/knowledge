---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-28
updated: 2026-07-04
---

# Two-Phase Commit

Two-Phase Commit is a coordination protocol for atomic commit across multiple participants.

It attempts to make several resource managers act like one commitment boundary. A coordinator first asks participants to prepare. If every participant votes to commit, the coordinator records and sends the commit decision. If any participant votes to abort or fails before prepare succeeds, the coordinator aborts.

## Semantics

Two-phase commit provides atomic agreement about commit or abort for the participants covered by the protocol. It is a realization mechanism for a distributed transaction boundary, not a business guarantee by itself.

The protocol does not eliminate the need to define [[Isolation|isolation]], [[Durability|durability]], recovery behavior, participant membership, timeout meaning, idempotency, or what external observers may see while the protocol is in progress.

## Costs and Failure Modes

Two-phase commit is coordination-heavy. It adds synchronous dependency between participants, increases latency, and can reduce availability when participants or the coordinator are unreachable.

Classic two-phase commit can block: a prepared participant may be unable to unilaterally decide commit or abort if it loses contact with the coordinator. Recovery requires durable logs and careful replay of coordinator and participant decisions.

## Difference from Consensus

Two-phase commit is not the same as [[Consensus|consensus]] or a [[Consensus Protocols|consensus protocol]] such as Paxos.

Two-phase commit solves atomic commit for a known transaction boundary. The coordinator asks fixed participants whether they can commit, then records and broadcasts commit or abort. The participants are resource managers for that transaction, and the question is whether all covered effects commit as one unit.

Paxos solves agreement on a value or log position for a replicated state machine. A proposer or leader may coordinate a round, but the chosen value is authorized by quorum intersection, acceptor state, ballots, and recovery rules. A failed proposer can be replaced while preserving safety, whereas classic two-phase commit can leave prepared participants blocked if they cannot learn the coordinator's decision.

In [[Orchestration and Choreography|orchestration and choreography]] terms, two-phase commit has a stronger coordinator shape than Paxos, but it is still a narrow atomic-commit protocol rather than a general [[Process Managers|process manager]] for a business process.

## Alternatives

When a single distributed transaction boundary is unavailable or too costly, systems often use [[Cohesive System Model/Operational Concerns/Weak Isolation Patterns|weak isolation patterns]] such as transactional outbox, [[Sagas|sagas]], compensation, idempotent retry, escrow, reservations, reconciliation, or [[CRDTs|CRDT]]-compatible updates.

These alternatives do not provide the same semantics as two-phase commit. They replace one atomic boundary with explicit process, recovery, and invariant-preservation rules.

## External References

- Jim Gray and Andreas Reuter, [Transaction Processing: Concepts and Techniques](https://www.microsoft.com/en-us/research/publication/transaction-processing-concepts-and-techniques/), Morgan Kaufmann, 1993.

Related concepts: [[ACID]], [[Isolation|isolation]], [[Coordination|coordination]], [[Consensus|consensus]], [[Consensus Protocols|consensus protocols]], [[Orchestration and Choreography|orchestration and choreography]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Concurrency Control|concurrency control]], [[Persistence|persistence]], [[Durability|durability]], [[Recovery|recovery]], [[Durable Execution|durable execution]], [[Business Transactions|business transactions]], [[Cohesive System Model/Operational Concerns/Weak Isolation Patterns|weak isolation patterns]].
