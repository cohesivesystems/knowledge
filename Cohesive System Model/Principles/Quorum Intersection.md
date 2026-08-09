---
realm: Principles
kind: principle
created: 2026-07-29
updated: 2026-08-08
status: draft
aliases:
  - Quorums
  - Quorum Systems
  - Read and Write Quorums
---

# Quorum Intersection

Quorum intersection is the principle that selected participant sets overlap so that later decisions or observations encounter evidence constraining earlier incompatible choices.

For a fixed membership of size $N$, two quorum families intersect when every admissible quorum from one family shares at least one participant with every admissible quorum from the other. A simple cardinality condition for two ordinary quorum sizes is:

$$
q_1 + q_2 > N.
$$

Majorities are one symmetric construction because any two majorities intersect. Flexible and weighted quorum systems can use different read, write, phase, or participant sets as long as the intersections required by the protocol are preserved.

## Intersection Is Not the Whole Protocol

Set intersection alone does not establish agreement, linearizability, freshness, or durability. The intersecting participant must preserve and reveal the evidence the protocol relies on, such as a ballot, accepted value, committed position, version, tombstone, or causal context. The protocol must also define how competing evidence is ordered, validated, propagated, and recovered.

The familiar read/write condition $R + W > N$ shows that read and write sets overlap for a fixed replica population. It does not by itself prove a linearizable register. Concurrent writes, stale versions, last-write-wins rules, partial write propagation, failed reads, clock ordering, sloppy quorums, and repair behavior determine which value the reader may return.

Likewise, a quorum acknowledgment is scoped evidence. It may establish that enough participants persisted a value, accepted a proposal, or observed a position under one configuration. It does not automatically mean that every replica applied the value, that a downstream projection is current, that the value is semantically valid, or that an external effect completed.

## Membership and Epochs

Intersection is relative to a membership or configuration. If participants independently use different memberships, each can assemble a quorum whose sets do not intersect in the required protocol state. Membership revision, joint configuration, epochs, terms, or other reconfiguration rules are therefore part of the safety argument.

A **sloppy quorum** may accept substitutes outside the intended replica set to improve availability. This changes the intersection claim. Hinted handoff or later repair may restore placement and convergence, but the temporary write set may not intersect a subsequent ordinary read set. The system must describe the weaker observation and conflict semantics rather than relying on the arithmetic of the intended replica count.

Durable quorum evidence must also survive the admitted [[Failure Models|failure model]]. If intersecting participants lose their accepted state on restart, or if a correlated failure removes every copy of the evidence, set intersection before the failure does not preserve the decision afterward.

## Quorums, Consensus, and Authority

[[Consensus]] protocols commonly use quorum intersection so two incompatible values cannot both be chosen for one log position or term. Quorum intersection is necessary to many such protocols but is not identical to consensus: consensus also defines proposal validity, state transitions, recovery, and liveness assumptions.

Quorum participation also does not create semantic [[Authority|authority]] by itself. The system model determines which protocol outcome counts as authoritative for a subject, while the quorum mechanism supplies evidence that the protocol's distributed acceptance rule was satisfied.

## Modeling Checks

- Which membership and revision define the participant universe?
- Which quorum families must intersect, and in which phases or read/write paths?
- What durable evidence does the intersecting participant preserve and reveal?
- How are concurrent, conflicting, stale, or incomparable values ordered or represented?
- Do substitute participants, failure domains, or topology changes weaken the intended intersection?
- How do membership changes preserve intersection between old and new configurations?
- What does a quorum acknowledgment prove, and what remains unapplied or externally incomplete?
- Which safety properties survive loss and recovery of quorum members?
- Which timing, fairness, and availability assumptions are required to assemble a quorum and make progress?

## Formal relations

- `constrains`: [[Consensus]] — Requires quorum-based agreement claims to preserve the participant overlap and durable evidence needed to prevent incompatible decisions.

## External References

- Leslie Lamport, [Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf), *ACM SIGACT News* 32(4):51-58, 2001.
- Martin Kleppmann, *Designing Data-Intensive Applications*, O'Reilly Media, 2017, chapters 5 and 9.

Related concepts: [[Consensus|consensus]], [[Consensus Protocols|consensus protocols]], [[Coordination|coordination]], [[Consistency Models|consistency models]], [[Authority|authority]], [[Replica Models|replica models]], [[Partition Models|partition models]], [[Version Histories|version histories]], [[Ordering|ordering]], [[Persistence|persistence]], [[Durability|durability]], [[Recovery|recovery]], [[Failure Models|failure models]], [[Safety and Liveness|safety and liveness]], [[Progress Conditions|progress conditions]], [[CAP Theorem|CAP theorem]].
