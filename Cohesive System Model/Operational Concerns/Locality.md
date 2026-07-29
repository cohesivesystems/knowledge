---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-29
updated: 2026-07-29
status: draft
aliases:
  - Data Locality
  - Locality of Reference
  - Placement Locality
---

# Locality

Locality is the operational relationship between work and the information, authority, resources, or participants it repeatedly uses, such that their relative placement or recent availability materially changes access cost, latency, capacity, or progress.

Locality is boundary-relative and time-dependent. Two operations may be local within one process but remote across memory domains, storage devices, zones, or authority boundaries. State that is local now may become remote after scheduling, migration, failover, eviction, rebalancing, or a change of owner.

Locality is not semantic identity or authority. Co-locating a request handler with cached entity data does not authorize it to commit an entity transition. Session affinity can improve reuse without guaranteeing exclusive ownership, serialization, durability, or correctness.

## Forms of Locality

- **Temporal locality** means recently used information or resources are likely to be used again within a relevant interval.
- **Spatial locality** means nearby addresses, records, keys, or resources are likely to be used together.
- **Execution locality** keeps related activations near a core, memory domain, process, runtime, accelerator, or warm worker.
- **Data locality** places computation near authoritative or frequently accessed data, caches, logs, indexes, or storage partitions.
- **Interaction locality** places communicating participants or consecutive processing stages near one another in the network or topology.
- **Authority locality** routes work toward the participant that currently owns the relevant entity, partition, lease, or commit boundary.

These forms can conflict. Moving computation toward data may move it away from another dependency. Replicating data can improve read locality while increasing write coordination, consistency, and invalidation work. Concentrating related work can improve cache reuse while creating a hot partition or larger failure impact.

Fault locality is related but distinct. A failure domain describes which components may fail together; access locality describes which interactions are near or reusable. Co-location can improve performance while increasing correlated failure, and geographic separation can improve failure independence while increasing interaction cost.

## Working Sets and Thrashing

A working set is the information and resource population actively needed by a workload over a declared interval. Useful working-set measures may cover memory pages, cache entries, indexes, partition state, connections, code, models, tenant data, workflow material, or routing and membership state.

When active working sets fit their local capacity, reuse can reduce remote access and repeated reconstruction. When too many working sets compete for that capacity, eviction, paging, cache misses, connection turnover, migration, or repeated state loading can make effective service demand grow. Adding concurrency can then reduce useful throughput through thrashing.

The interval and workload class matter. One aggregate working-set estimate can hide per-tenant, per-key, per-partition, or per-stage locality. A cache can have a high global hit rate while the latency-critical path repeatedly misses.

## Local and Distributed Locality

Local mechanisms include processor caches, NUMA placement, memory and allocator arenas, thread or task affinity, runtime queues, connection pools, local disks, and process caches. Distributed mechanisms include partition placement, replica selection, data-aware scheduling, zone or region affinity, edge caches, ownership routing, colocated service stages, and movement of computation toward retained data.

The same pattern recurs across layers: a near access is usually cheaper, but preserving nearness requires placement information, capacity, and sometimes coordination. A scheduler can preserve one kind of locality while weakening [[Fairness|fairness]], packing efficiency, fault isolation, or another workload's locality.

[[Routing Models|Routing]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], and [[Consumer Coordination|consumer coordination]] determine how work reaches locality-bearing units. Affinity keys, partition keys, leases, and ownership epochs must remain aligned; stale routing can direct work toward a former owner or cold replica even when the logical key is correct.

## Locality and Scaling

[[Scaling Mechanisms|Scaling]] changes locality as well as resource quantity. Scale-out may introduce cold caches, new connections, state transfer, partition reassignment, and remote coordination before it supplies effective capacity. Scale-in can evict warm state, concentrate working sets, or move work away from data. Autoscaling that ignores these costs can create churn and oscillation.

Locality can improve [[Scalability|scalability]] by reducing service demand per useful completion. It can also limit scalability when affinity creates hot units, singular ownership prevents distribution, or replicated locality requires global invalidation. A local improvement does not necessarily compose into an end-to-end improvement; see [[Compositionality|compositionality]].

Capacity and recovery plans should account for locality loss. Failover capacity that is nominally sufficient may still be ineffective while caches are cold, state is transferring, routes are converging, or remote dependencies carry the displaced work.

## Modeling and Measurement Checks

- Which work and information are expected to be near or recently available?
- At which memory, process, host, partition, zone, region, or authority boundary is locality claimed?
- What is the working set, over which interval, and for which workload class?
- Which placement, routing, ownership, or caching mechanism realizes the locality?
- What happens on cache miss, migration, rebalance, failover, or ownership change?
- Does locality improve useful completion cost or only move work to another boundary?
- Which hotspots, skew, coordination, consistency, fairness, or failure tradeoffs result?
- How are local access, remote access, hit rate, reuse distance, state movement, and cold-start duration observed?
- Is affinity merely an optimization, or does correctness depend on a separately established authority mechanism?

## External References

- Peter J. Denning, [The Working Set Model for Program Behavior](https://doi.org/10.1145/357980.357997), *Communications of the ACM* 26(1):43-48, 1983 reprint of the foundational working-set model.
- Liang Yuan, Chen Ding, Peter Denning, and Yunquan Zhang, [A Measurement Theory of Locality](https://arxiv.org/abs/1802.01254), 2018.
- Jeffrey Dean and Sanjay Ghemawat, [MapReduce: Simplified Data Processing on Large Clusters](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/), *OSDI '04*, 2004.

Related concepts: [[Scalability|scalability]], [[Scaling Mechanisms|scaling mechanisms]], [[Stuff Structure Property|stuff structure property]], [[Compositionality|compositionality]], [[Boundaries|boundaries]], [[Identity|identity]], [[Authority|authority]], [[Entity|entity]], [[Interaction|interaction]], [[Routing Models|routing models]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Consumer Coordination|consumer coordination]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Coordination|coordination]], [[Consistency Models|consistency models]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Observability and Provenance|observability and provenance]], [[Compute|compute]], [[Runtimes|runtimes]], [[Application Hosts|application hosts]], [[Network|network]], [[Storage Systems|storage systems]], [[Infrastructure Graph|infrastructure graph]], [[Capacity Planning|capacity planning]].
