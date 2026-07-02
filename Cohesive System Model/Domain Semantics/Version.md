---
realm: Domain Semantics
kind: semantic-construct
---

# Version

A **version** identifies a point in an [[Entity|entity]] history at which a particular [[State|state]] became current.

Entity state can be addressed as [[Identity|identity]] + version. In [[Event-State Duality|event-state duality]], for a sequential entity, state at version `V` is the result of applying the [[Event|event]] that produced version `V`.

Optimistic concurrency control is implemented with an expected-version or etag check: a [[Command|command]] carries the version of entity state the [[Observer|observer]] believed was current, and the transition may commit only if that expectation still matches the entity's current version at the commitment boundary.

Versions support:

- Current-state addressing.
- Historical state references.
- Optimistic concurrency through expected-version or etag checks on [[Command|commands]].
- Ordering of entity state observations over time.

A version need not be a single scalar counter. In distributed or replicated histories, version may be realized by logical timestamps, causal contexts, vector-clock-like metadata, branch heads, commit identifiers, or other [[Time|time]], [[Ordering|ordering]], and [[Version Histories|version-history]] mechanisms.

If a command is rejected and no accepted state change occurs for the target entity, the entity version remains unchanged.

Related concepts: [[Identity|identity]], [[State|state]], [[Entity|entity]], [[Event|event]], [[Event-State Duality|event-state duality]], [[Command|command]], [[Concurrency Control|concurrency control]], [[Version Histories|version histories]], [[Consistency Models|consistency models]], [[Time|time]], [[Ordering|ordering]], [[Fibrations and Indexed Structure|fibrations and indexed structure]], [[Enrichment and Order|enrichment and order]].
