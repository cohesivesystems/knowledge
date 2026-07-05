---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-07-01
---

# Relations

Relations describe how semantic roles are connected in the system graph.

At the structure level, relations connect identities, states, observations, observers, entities, and events by dependency, reference, projection, observation, constraint, causation, or inclusion. This describes graph shape and semantic dependency, not a specific join mechanism, network link, storage relation, or runtime call.

Examples of relations include:

- Entity-to-entity references.
- Observer-to-entity hosting.
- Observer-to-observer interaction edges.
- Event-to-state causation.
- Projection derivation.
- Policy or invariant scope.
- Boundary inclusion.

Relations make the system graph navigable and explain how changes in one part of the model may be observed or interpreted elsewhere.

Related concepts: [[Entity|entity]], [[Observer|observer]], [[Identity|identity]], [[State|state]], [[Observation|observation]], [[Event|event]], [[Projections|projections]], [[Boundaries|boundaries]].
