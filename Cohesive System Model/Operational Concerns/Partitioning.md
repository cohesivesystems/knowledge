---
realm: Operational Concerns
kind: operational-concern
created: 2026-08-01
updated: 2026-08-01
status: draft
aliases:
  - Data Partitioning
  - Work Partitioning
  - Traffic Partitioning
---

# Partitioning

Partitioning governs how a population of subjects, data, or work is divided into assignment scopes at a declared boundary, and how the assignment behaves as the population, partition set, or rule changes.

The system-graph structure is recorded by [[Partition Models|partition models]]: partition identities, assignment rules and revisions, ownership and invariant boundaries, routes, and lifecycle. Partitioning is the operational concern that qualifies that structure with requirements for coverage, exclusivity or overlap, stability, skew, balance, movement, isolation, and recovery. Hashing, ranges, directories, tenant assignment, geography, time, and other mechanisms may realize an assignment rule without defining the concern itself.

## Assignment Shape

For a subject population `S` and partition population `P`, an assignment can be written abstractly as:

```txt
assign : Subject x Revision -> set of Partition
```

A strict partition covers the declared subject population and assigns each subject to exactly one disjoint partition for a given revision. System models may intentionally admit partial or overlapping assignment, but they should name the different shape: unassigned subjects require an admission or fallback rule, while assignment to several partitions may express replication, fanout, hedging, migration, or shared authority rather than strict partitioning.

The assigned unit may be an entity, key, record, relation, history, message, request, connection, task, tenant, time interval, geographic region, or unit of weighted demand. The partition scope may govern placement, ownership, authority, ordering, storage, execution, scheduling, retention, recovery, or failure isolation. These scopes can coincide without becoming identical.

## Traffic and Data

[[Load Balancing|Load balancing]] can be understood as partitioning and routing traffic. In the ordinary single-destination case, a selection policy assigns each request, connection, message, or task to a per-destination traffic partition, and [[Routing Models|routing]] carries it to the selected destination. The operational objective is usually expressed through service, capacity, locality, fairness, or failure behavior rather than through stable ownership of the traffic itself.

Data partitioning applies the same abstract shape to data. It assigns keys, records, entity subjects, relations, observations, or histories to placement, ownership, storage, ordering, or transaction scopes, then routes reads, writes, queries, and maintenance work to the relevant partitions. [[Partition Models|Partition models]] make those data partitions and their assignment revisions explicit in the system graph.

The distinction is the subject and the guarantees carried by its assignment. Traffic assignment may be transient and reconsidered for each interaction. Data assignment commonly persists across interactions and may determine authority, invariants, consistency, durability, locality, and recovery. Affinity can make traffic follow a data partition, but selecting a nearby or lightly loaded destination does not by itself transfer data authority or ownership.

## Distribution and Change

Partitioning creates a distribution; it does not guarantee a balanced one. Equal subject counts can conceal unequal sizes, costs, arrival rates, fanout, working sets, or coordination demand. Hot keys and correlated workloads can overload one partition while aggregate capacity remains available elsewhere.

Changing the assignment is repartitioning. It may require state movement, route convergence, forwarding, buffering, fencing, dual reads or writes, replay, and an explicit cutover condition. Old and new assignment revisions can coexist during change, so each observation and operation must be interpreted against a declared revision or compatibility rule.

Balancing and stability can conflict. Frequent reassignment may improve an instantaneous distribution while destroying [[Locality|locality]], moving state, invalidating caches, interrupting ordering, or amplifying recovery work. A partitioning policy should therefore account for both steady-state skew and the cost, rate, and correctness of movement.

## Distinctions

| Concept | Governing question |
| --- | --- |
| **partitioning** | What operational properties must the assignment into scopes preserve? |
| [[Partition Models\|partition models]] | Which partition identities, assignment rules, routes, boundaries, and revisions exist in the system graph? |
| [[Routing Models\|routing]] | How is a subject or operation directed to the partition or destination selected for it? |
| [[Load Balancing\|load balancing]] | How is traffic partitioned and routed across eligible capacity to meet operational objectives? |
| [[Replica Models\|replication]] | Which logical subject or partition is represented by several copies or authority roles? |
| network partition | Which required communications are unavailable because of a failure condition? |

## Modeling Checks

- What is the subject population and declared boundary?
- What identifies each partition and the active assignment revision?
- Is assignment complete, partial, disjoint, or overlapping?
- Which ownership, authority, invariant, ordering, transaction, storage, execution, and recovery scopes follow the assignment?
- How are subjects and operations routed under the current rule?
- Which measure defines skew or balance: count, bytes, cost, arrival rate, latency, working set, or useful completion demand?
- Which guarantees hold only per partition, and which compose across partitions?
- What movement, forwarding, fencing, cut, and completion rules govern repartitioning?
- How do replication, affinity, fanout, hedging, failover, and stale routes change the assignment shape?
- Does rebalancing improve the intended objective after accounting for locality loss, state movement, coordination, and recovery cost?

Related concepts: [[Stuff Structure Property|stuff structure property]], [[Compositionality|compositionality]], [[Partition Models|partition models]], [[Routing Models|routing models]], [[Load Balancing|load balancing]], [[Entity Models|entity models]], [[Relation Models|relation models]], [[Interaction Channels|interaction channels]], [[Policy Scopes|policy scopes]], [[Invariant Scopes|invariant scopes]], [[Boundaries|boundaries]], [[Identity|identity]], [[Authority|authority]], [[Ordering|ordering]], [[Consistency Models|consistency models]], [[Isolation|isolation]], [[Coordination|coordination]], [[Locality|locality]], [[Scalability|scalability]], [[Fairness|fairness]], [[Scheduling|scheduling]], [[Consumer Coordination|consumer coordination]], [[Recovery|recovery]], [[Failure Models|failure models]], [[Replica Models|replica models]], [[Scaling Mechanisms|scaling mechanisms]], [[Storage Systems|storage systems]].

## Formal relations

- `qualifies`: [[Partition Models]] — States the coverage, cardinality, stability, skew, movement, isolation, and recovery properties required of the system graph's partition identities and assignment relations.
