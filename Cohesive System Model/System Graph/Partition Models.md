---
realm: System Graph
kind: structural-construct
created: 2026-07-29
updated: 2026-08-01
status: draft
aliases:
  - Partition Model
  - Partitioned Topology
  - Sharding Model
---

# Partition Models

Partition models describe how subjects, histories, relations, observations, or work are assigned to distinct ownership, ordering, storage, and execution scopes in the system graph.

A partition model consists of more than a partition key. It includes the partition identities, assignment rule, rule revision, authority and invariant boundaries, route from a subject to its current partition, and lifecycle by which assignments change. Hash, range, tenant, geography, time, function, and manually declared schemes are possible realizations of that structure.

[[Partitioning]] states the operational requirements on this structure, including assignment coverage and cardinality, skew, balance, stability, isolation, movement, and recovery. This note records the system-graph arrangement those requirements qualify.

Partitioning should be distinguished from a network partition. A partition model is an authored division of work or data. A network partition is a failure condition that prevents participants from exchanging information within required timing or delivery assumptions.

## Assignment and Scope

The assignment relation can be written abstractly as:

```txt
subject or work identity + partition-definition revision -> partition identity
```

The relation may be total or partial, stable or time-varying, and one-to-one or one-to-many. A replicated partition maps one logical partition to several [[Replica Models|replicas]]; replication and partitioning are independent structural dimensions.

A partition boundary may scope:

- Transition authority and entity ownership.
- Ordered histories, streams, or delivery lanes.
- Transaction and atomic-commit capability.
- Invariants and uniqueness constraints.
- Query locality, indexes, and materialized projections.
- Consumer assignment, scheduling, and recovery progress.
- Capacity, retention, durability, and failure isolation.

A guarantee stated per partition does not automatically compose into a global guarantee. Per-partition ordering does not create one total order. Per-partition serializability does not make a cross-partition transaction serializable. Independently fresh partitions do not necessarily form one [[Consistent Cuts|consistent cut]].

## Skew, Fanout, and Secondary Structures

Partitioning creates a distribution of work, not a promise of balance. Hot keys, large tenants, temporal bursts, uneven value sizes, and correlated access can overload one partition while aggregate capacity appears sufficient. Splitting or salting a hot subject may improve distribution while weakening locality, per-subject ordering, or single-partition invariants.

Queries and relations that do not align with the primary assignment may require scatter-gather, a global index, partition-local indexes followed by fanout, or a [[Projection Models|projection]] organized by a different key. Each secondary structure has its own update, lag, consistency, recovery, and cutover obligations.

Cross-partition transitions expose a modeling choice. The invariant may be moved behind one authority, coordinated across partitions, represented through reservations or escrow, made monotone or commutative, or protected procedurally by a [[Process Graphs|process graph]]. Partitioning does not remove the invariant; it changes the boundary at which preserving it is inexpensive.

## Repartitioning and Rebalancing

Repartitioning changes the assignment relation while work may still be arriving. During movement, old and new definitions, owners, routes, and copies can coexist. The rebalancing protocol must state:

- The source and destination partition identities and assignment revisions.
- The cut or position to which transferred state corresponds.
- How changes after that cut are copied, buffered, forwarded, or replayed.
- Which owner may accept transitions during each phase.
- How stale routes and former owners are fenced.
- How duplicates and gaps around cutover are detected or made harmless.
- When the new partition is complete enough to serve reads, accept writes, or participate in recovery.
- How rollback, cancellation, or partial movement is recovered.

Rebalancing is therefore a stateful process with identity, authority, persistence, and completion semantics, not an instantaneous redistribution command.

## Modeling Checks

- What semantic subjects or work units does the partition relation assign?
- Which identity and definition revision determine the assignment?
- Which authority, invariant, ordering, transaction, and recovery scopes coincide with the partition?
- Which relations and queries align with the key, and which require fanout or secondary projections?
- How are skew, hot subjects, large partitions, and correlated demand measured and handled?
- Which operations cross partitions, and what coordination or weaker protocol preserves their meaning?
- How do replication and partitioning compose for each logical partition?
- What state-transfer cut, forwarding rule, fence, and completion condition govern rebalancing?
- Which guarantees remain only per partition, and which are deliberately composed globally?

## Formal relations

- `arranges`: [[Entity Models]] — Assigns entity subjects and transition authority to explicit partition identities and assignment revisions.
- `arranges`: [[Interaction Channels]] — Divides carried histories or work into declared ordering, ownership, and consumption lanes.

## External References

- Martin Kleppmann, *Designing Data-Intensive Applications*, O'Reilly Media, 2017, chapter 6.

Related concepts: [[System Graph|system graph]], [[Partitioning|partitioning]], [[Entity Models|entity models]], [[Relation Models|relation models]], [[Projection Models|projection models]], [[Replica Models|replica models]], [[Interaction Channels|interaction channels]], [[Routing Models|routing models]], [[Consumer Coordination|consumer coordination]], [[Identity|identity]], [[Authority|authority]], [[Boundaries|boundaries]], [[Invariant Scopes|invariant scopes]], [[Ordering|ordering]], [[Consistent Cuts|consistent cuts]], [[Isolation|isolation]], [[Coordination|coordination]], [[Locality|locality]], [[Scalability|scalability]], [[Recovery|recovery]], [[Failure Models|failure models]], [[Scaling Mechanisms|scaling mechanisms]].
