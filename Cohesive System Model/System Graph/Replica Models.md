---
realm: System Graph
kind: structural-construct
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - Replica Model
  - Replicated State Topology
  - Replication Topology
---

# Replica Models

Replica models describe how one logical subject, history, service role, or derived view is arranged across multiple replica observers in the system graph.

A replica is not merely another runtime instance. It has a replica [[Identity|identity]], an observation or state position, a relationship to the replicated subject, and a declared role in reading, proposing, accepting, applying, or repairing change. Several replicas may correspond to one logical [[Entity Models|entity model]], [[Projection Models|projection model]], interaction channel, service role, or storage boundary without having equal [[Authority|authority]] or equally current observations.

Replica models describe topology and role assignment. They do not by themselves guarantee [[Consistency Models|consistency]], [[Durability|durability]], convergence, availability, or failover. Those properties depend on the update protocol, ordering, coordination, delivery, persistence, recovery, and failure assumptions supplied at the relevant boundary.

## Replica Roles and Paths

A replica model should distinguish at least:

- The logical subject or history being replicated.
- Replica, member, region, and replica-set identities.
- Which replicas may accept commands, propose writes, serve queries, or only apply replicated change.
- The authoritative write path and any alternative path admitted during failure or reconfiguration.
- Read routing and the freshness, session, causal, or consistency claim of each read path.
- The propagation relation among committed positions, events, state snapshots, deltas, or operations.
- The ordering and conflict relation among concurrent or independently accepted updates.
- The membership, readiness, catch-up, promotion, demotion, and removal lifecycle.

Single-writer, leader-mediated, multi-writer, and merge-oriented arrangements are different replica-model families. Their names do not determine correctness. A single leader still needs fencing and durable authority transfer; a multi-writer arrangement needs conflict or commutativity semantics; a leaderless arrangement still needs rules for admission, version comparison, quorum participation, repair, and reconciliation.

Write topology and read topology should be modeled separately. A system may serialize writes through one authority while serving reads from asynchronous replicas, caches, or projections. The write path can therefore be linearizable while a query path provides bounded staleness, session consistency, causal consistency, or only eventual convergence.

## Replica Position and Semantic Version

A replica position is substrate or protocol evidence about how much replicated material a participant has applied. It is not automatically the semantic [[Version|version]] of every entity or observation carried by that material.

One log position may advance several subjects; one entity version may correspond to different storage or broker positions; a snapshot may cover a [[Consistent Cuts|consistent cut]] rather than one scalar position. Query and recovery contracts should state how replica positions correspond to the semantic versions and observations they expose.

## Divergence, Repair, and Reconfiguration

Replication can create temporarily or intentionally divergent histories. The model must say whether divergence is forbidden, hidden behind one authority, represented as concurrent versions, merged algebraically, resolved by policy, or repaired from an authoritative history. [[Consistency Models|Eventual consistency]] is not a repair algorithm and does not specify which intermediate observations or conflicts are admissible.

Repair mechanisms may compare versions, exchange missing events or deltas, transfer snapshots, rebuild a replica, perform read repair, or reconcile against authoritative material. Repair must preserve tombstones, causal metadata, semantic versions, retention assumptions, and other information needed to avoid resurrecting removed facts or accepting stale authority.

Failover is an authority transition, not merely a routing update. Promotion, election, lease transfer, or membership change must establish which replica may accept new transitions, fence former authorities, preserve committed history, and define what happens to writes that were acknowledged but not known to the new authority.

Reconfiguration may temporarily involve old and new memberships, routes, and replica positions. Its cutover rule must identify which configuration is authoritative, which quorums may decide, how state transfer becomes complete enough for service, and how stale members are prevented from committing after removal.

## Modeling Checks

- What logical subject, history, view, or service role is replicated?
- Which identities name the logical subject, replicas, membership, and configuration revision?
- Which replicas can accept writes, serve reads, vote, apply changes, or perform repair?
- What consistency and freshness does each read path expose?
- How do replica positions correspond to semantic versions and consistent cuts?
- Which concurrent histories are rejected, preserved, merged, or reconciled?
- What material survives replica loss, and which failures can remove all copies together?
- How are catch-up, repair, promotion, demotion, membership change, and failover completed?
- Which target boundary fences stale replicas or former leaders?
- Which guarantees belong to one partition or replica set rather than the whole system?

## Formal relations

- `arranges`: [[Observer Models]] — Places multiple replica observers around one logical subject or history while keeping their identities, observations, and authority roles explicit.
- `arranges`: [[Entity Models]] — Relates logical entity ownership and version history to replica roles without identifying an entity with any one physical copy.

## External References

- Martin Kleppmann, *Designing Data-Intensive Applications*, O'Reilly Media, 2017, chapters 5 and 9.

Related concepts: [[System Graph|system graph]], [[Observer Models|observer models]], [[Entity Models|entity models]], [[Projection Models|projection models]], [[Partition Models|partition models]], [[Identity|identity]], [[Authority|authority]], [[Version|version]], [[Version Histories|version histories]], [[Observation|observation]], [[Consistency Models|consistency models]], [[Consistent Cuts|consistent cuts]], [[Ordering|ordering]], [[Coordination|coordination]], [[Quorum Intersection|quorum intersection]], [[Consensus|consensus]], [[CRDTs]], [[Persistence|persistence]], [[Durability|durability]], [[Recovery|recovery]], [[Failure Models|failure models]], [[Routing Models|routing models]], [[Storage Systems|storage systems]], [[Consensus Protocols|consensus protocols]], [[Scaling Mechanisms|scaling mechanisms]].
