---
realm: Semantic Dynamics
kind: semantic-construct
---

# Version

A **Version** identifies a point in an [[Entity]] history at which a particular [[State]] became current.

Entity state can be addressed as [[Identity]] + version. In [[Event-State Duality]], for a sequential entity, state at version `V` is the result of applying the [[Event]] that produced version `V`.

Optimistic concurrency control is implemented with an expected-version or etag check: a [[Command]] carries the version of entity state the [[Observer]] believed was current, and the transition may commit only if that expectation still matches the entity's current version at the commitment boundary.

Versions support:

- Current-state addressing.
- Historical state references.
- Optimistic concurrency through expected-version or etag checks on [[Command|commands]].
- Ordering of entity state observations over time.

A version need not be a single scalar counter. In distributed or replicated histories, version may be realized by logical timestamps, causal contexts, vector-clock-like metadata, branch heads, commit identifiers, or other [[Time|time]], [[Ordering|ordering]], and [[Version Histories|version-history]] mechanisms.

If a command is rejected and no accepted state change occurs for the target entity, the entity version remains unchanged.

Related concepts: [[Identity]], [[State]], [[Entity]], [[Event]], [[Event-State Duality]], [[Command]], [[Concurrency Control]], [[Version Histories]], [[Consistency Models]], [[Time]], [[Ordering]], [[Fibrations and Indexed Structure]], [[Enrichment and Order]].
