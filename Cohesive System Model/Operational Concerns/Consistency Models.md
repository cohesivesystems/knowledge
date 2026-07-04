---
realm: Operational Concerns
kind: operational-concern
---

# Consistency Models

Consistency Models constrain which observations are valid for a set of events, transitions, versions, sessions, replicas, and ordering relations.

A consistency model is a predicate over histories. It says which operation results, reads, observations, or replica states are allowed relative to a chosen [[Boundaries|boundary]], [[Ordering|ordering]] space, [[Version Histories|version history]], and subject.

Consistency models are not global by default. A system may provide one model for an entity transition boundary, another for a read model, another for a cache, another for a workflow history, and another for a broker or storage substrate.

Most consistency models are [[Safety and Liveness|safety]] properties: they forbid histories that violate the model. They do not by themselves promise that an operation will eventually complete, that a replica will eventually catch up, or that a partitioned system will remain available.

[[Isolation]] is adjacent but distinct. Isolation describes what concurrent operations may observe while they execute. Consistency models describe which histories and observations are valid at the boundary being claimed.

## Linearizability

Linearizability requires each operation to appear as if it took effect at a single point between invocation and response. The resulting history must be equivalent to a legal sequential history and must preserve real-time order for non-overlapping operations.

Linearizability is a strong model for shared objects and entity boundaries because it lets observers reason as if each operation happened atomically at some point during its execution. It is usually expensive across distributed boundaries because preserving real-time order requires coordination.

[[Consensus]] is a common way to construct a linearizable replicated object: participants agree on a sequence of operations, then each replica applies the same deterministic sequential specification in that order. The resulting consistency guarantee belongs to the governed object or boundary, not automatically to every cache, projection, read replica, or downstream observer.

## Registers and Linearization Points

A SQL table row can realize a linearizable read/write register when all reads and writes go through one authoritative transaction boundary and reads observe the latest committed value for that boundary.

The **linearization point** is the point at which each operation takes effect in the abstract history. For a row update, this is usually the successful atomic update or transaction commit. For a read, it is the point at which the database returns the committed row version being observed.

For example, an expected-version update can realize an atomic compare-and-set operation:

```sql
UPDATE register
SET value = ?, version = version + 1
WHERE id = ? AND version = ?;
```

This claim is configuration- and boundary-dependent. A database may be evaluated for linearizability as a system property, while a deployed application may not actually get linearizable reads or writes if it uses asynchronous replicas, stale snapshots, caches outside the consistency protocol, weak isolation, multi-primary conflict resolution, or read routing that does not preserve freshness.

The model should therefore state the register boundary explicitly: primary row, transaction, replica set, cache, session, read model, or API endpoint. Linearizability belongs to that declared boundary, not to the word "database" in general.

## Serializability and Linearizability

Serializable [[Isolation|isolation]] does not by itself imply linearizability.

**Serializability** requires that transactions be equivalent to some legal serial order. That serial order need not preserve real-time order between non-overlapping transactions.

**Linearizability** additionally requires real-time order: if operation `A` completes before operation `B` begins, then `A` must appear before `B` in the legal history.

For transactions, the stronger property is usually called **strict serializability** or **external consistency**: serializability plus real-time ordering of committed transactions. This is the transaction-level analogue of linearizability.

## Sequential Consistency

Sequential consistency requires that the result be explainable by some legal total order of operations that preserves each participant's program order. It does not require that the total order preserve real-time order between operations from different participants.

Sequential consistency is therefore weaker than linearizability. It can preserve each observer's local order while allowing a global explanation that may differ from wall-clock order.

## Causal Consistency

Causal consistency preserves the order of causally related operations while allowing concurrent or unrelated operations to be observed in different orders.

This model is naturally related to [[Time|logical time]], happened-before, vector clocks, and causal metadata. It is useful when the model needs to preserve potential causation without imposing one global total order on independent work.

## Consistent Cut

A **[[Glossary#consistent cut|consistent cut]]** is a selected set of events, versions, or observations that is closed under causality: if the cut includes an event, it must also include the causal prerequisites of that event.

In a distributed system, a consistent cut represents a coherent global snapshot relative to a partial order. It may include concurrent events in different combinations, but it must not include an effect while omitting a cause that happened before it.

Consistent cuts matter for snapshots, checkpoints, debugging, projection rebuilds, workflow recovery, replicated reads, and cross-entity observations. A read that spans multiple entities, partitions, replicas, or projections may need to declare whether it observes a consistent cut, a stale cut, a session-relative cut, or merely independent local observations.

[[Systems Sheaf Semantics]] treats consistent cuts as contexts over which state, observations, versions, or knowledge can be restricted, compared on overlaps, and sometimes glued into a coherent larger explanation.

## Session Consistency

Session consistency is a family of guarantees scoped to one observer, client, process, or session. Common session guarantees include:

- Read-your-writes.
- Monotonic reads.
- Monotonic writes.
- Writes-follow-reads.

Session guarantees make weak or replicated systems easier to use because they preserve a coherent experience for one observer even when different observers may see different replica states.

## Eventual Consistency

Eventual consistency says that replicas converge if updates stop and delivery, reconciliation, or merge eventually completes.

Eventual consistency alone does not say what intermediate observations are allowed, how conflicts are represented, whether causality is preserved, whether reads observe a consistent cut, or what merge semantics are valid. Those details must be supplied by [[Version Histories|version histories]], [[Ordering|ordering]], [[Delivery Semantics|delivery semantics]], [[CRDTs]], conflict resolution, or application-specific invariants.

## Relationship to History Shape

Consistency models choose how much history shape must be preserved.

Linearizability and sequential consistency require a legal total order, though they differ on real-time constraints. Causal consistency preserves a partial order. Session consistency preserves an observer-relative slice of history. Eventual consistency focuses on convergence and may tolerate temporary divergence, stale observations, or concurrent incomparable versions.

Consensus-based replication is one way to manufacture a total order from a distributed history. Coordination-avoidance designs instead preserve less order, use merge semantics, or expose eventuality as part of the domain protocol.

The [[CALM Theorem|CALM theorem]] relates consistency to program shape rather than only storage behavior: monotone programs can preserve consistent results without coordination because additional facts do not retract prior conclusions. Non-monotone programs need coordination or an explicit weaker protocol before exposing decisions that depend on completeness, absence, or exclusion.

The [[CAP Theorem|CAP theorem]] is a specific safety/liveness impossibility: under network partition, a system cannot guarantee both linearizable consistency and request availability for all non-failing nodes.

The design question is not simply "strong" or "weak" consistency. It is which observations must be coherent for which observer, boundary, invariant, and history shape.

## External References

- Maurice P. Herlihy and Jeannette M. Wing, [Linearizability: A Correctness Condition for Concurrent Objects](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf), ACM Transactions on Programming Languages and Systems, 12(3):463-492, July 1990.
- Leslie Lamport, [How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs](https://www.microsoft.com/en-us/research/publication/make-multiprocessor-computer-correctly-executes-multiprocess-programs/), IEEE Transactions on Computers, C-28(9):690-691, September 1979.
- Douglas B. Terry, Alan J. Demers, Karin Petersen, Mike Spreitzer, Marvin Theimer, and Brent Welch, [Session Guarantees for Weakly Consistent Replicated Data](https://www.cs.cornell.edu/courses/cs734/2000FA/cached%20papers/SessionGuaranteesPDIS_1.html), PDIS 1994.
- Werner Vogels, [Eventually Consistent](https://queue.acm.org/detail.cfm?id=1466448), ACM Queue, 2008.

Related concepts: [[Glossary|glossary]], [[Ordering|ordering]], [[Consensus|consensus]], [[Consensus Protocols|consensus protocols]], [[Safety and Liveness|safety and liveness]], [[CAP Theorem|CAP theorem]], [[CALM Theorem|CALM theorem]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Version Histories|version histories]], [[Version|version]], [[Time|time]], [[Observation|observation]], [[Observer|observer]], [[Boundaries|boundaries]], [[Isolation|isolation]], [[ACID]], [[Two-Phase Commit|two-phase commit]], [[Weak Isolation Patterns|weak isolation patterns]], [[Concurrency Control|concurrency control]], [[Coordination|coordination]], [[Delivery Semantics|delivery semantics]], [[CRDTs]], [[CQRS]], [[Persistence|persistence]], [[Reconstitution|reconstitution]].
