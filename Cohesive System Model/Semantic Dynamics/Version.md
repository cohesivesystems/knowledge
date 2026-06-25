---
realm: Semantic Dynamics
---

# Version

Realm: Semantic Dynamics

A **Version** identifies a point in an [[Entity]] history at which a particular [[State]] became current.

Entity state can be addressed as [[Identity]] + version. In [[Event-State Duality]], for a sequential entity, state at version `V` is the result of applying the [[Event]] that produced version `V`.

Versions support:

- Current-state addressing.
- Historical state references.
- Expected-version or etag checks on [[Command|Commands]].
- Optimistic concurrency.
- Ordering of entity state observations over time.

If a command is rejected and no endogenous event is committed for the target entity, the entity version remains unchanged.

Related concepts: [[Identity]], [[State]], [[Entity]], [[Event]], [[Event-State Duality]], [[Command]], [[Concurrency Control]], [[Fibrations and Indexed Structure]], [[Enrichment and Order]].
