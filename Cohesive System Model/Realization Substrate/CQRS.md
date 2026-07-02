---
realm: Realization Substrate
kind: pattern
---

# CQRS

CQRS, command query Responsibility Segregation, is a realization pattern that separates the write side that interprets [[Command|commands]] and persists authoritative change from the read side that answers [[Query|queries]] by reconstituting queryable observations.

In the Cohesive System Model, CQRS can be understood as a separation of [[Persistence|persistence]] and [[Reconstitution|reconstitution]]:

- The command side interprets input as [[Command|commands]] relative to an [[Observer|observer]], [[Boundaries|boundary]], current entity state, invariants, policies, authority, and expected version.
- Accepted transitions commit authoritative state changes, often as current-state records, [[Event Sourcing|event-sourced]] committed events, or transactional writes.
- The query side interprets input as [[Query|queries]] and reconstitutes read-oriented [[Observation|observations]] through projections, indexes, materialized views, caches, or derived state.

CQRS does not require event sourcing. Event sourcing is one possible write-side persistence strategy. CQRS can also use current-state records, relational tables, documents, actor state, workflow state, or other persistence mechanisms.

The separation is useful because command handling and query answering often have different shapes:

- Commands require interpretation, validation, authority, invariants, and concurrency control.
- [[Query|Queries]] require efficient observation, projection, filtering, indexing, aggregation, and access control.
- Write models usually protect semantic consistency.
- Read models usually optimize visibility and access patterns.

## Consistency under Asynchrony

CQRS often updates read models asynchronously from the write side. That creates operational concerns that must be explicit:

- Projection lag: a committed write may not be visible to a [[Query|query]] immediately.
- Read-your-writes: a caller may need a way to observe its own committed change.
- Monotonic reads: a caller may need to avoid seeing older projection versions after newer ones.
- Ordering scope: projection updates may be ordered per entity, stream, partition, tenant, or process, not globally.
- Idempotency: projection updates may be delivered more than once.
- Rebuild and recovery: read models must be rebuildable or otherwise recoverable from authoritative persistence.
- Acknowledgment meaning: command success means the write-side transition committed, not necessarily that every read model has caught up.

The consistency question is therefore boundary-relative. A command boundary may be strongly consistent while a query boundary is eventually consistent. A projection may be current for one entity and stale for another. A UI, API, process, or downstream observer must know which boundary its observation comes from and what freshness guarantee applies.

## Relationship to Event Sourcing

Event sourcing and CQRS are often combined but remain distinct.

```txt
command -> transition -> committed event history
                         -> projections/read models
                         -> queries
```

In this combined pattern, event sourcing supplies the committed event history, while CQRS separates command-side consistency from query-side reconstitution. The read side must still handle asynchronous projection, ordering, idempotency, and recovery.

## External References

- Martin Fowler, [CQRS](https://martinfowler.com/bliki/CQRS.html), 2011.
- Greg Young, [CQRS Documents](https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf), 2010. See also the [CQRS Documents page](https://cqrs.wordpress.com/documents/).
- Microsoft Azure Architecture Center, [CQRS pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs).

Related concepts: [[Command|command]], [[Query|query]], [[Transition|transition]], [[Observer|observer]], [[Entity|entity]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Projections|projections]], [[Observation|observation]], [[Event Sourcing|event sourcing]], [[Concurrency Control|concurrency control]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Recovery|recovery]], [[Delivery Semantics|delivery semantics]], [[Realization|realization]].
