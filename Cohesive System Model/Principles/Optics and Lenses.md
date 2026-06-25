---
realm: Principles
---

# Optics And Lenses

Optics are structured ways to focus on, observe, transform, or update part of a larger structure.

Lenses are the familiar case:

```txt
get : Whole -> Part
set : Whole x Part -> Whole
```

In modeling, optics are useful for understanding observations, projections, partial state, and boundary-specific views.

Examples:

- An [[Observable]] focuses on part of state and produces an [[Observation]].
- A [[Projections|projection]] derives a view from source state or events.
- A command may target a partial aspect of entity state while requiring broader context for validation.
- A boundary may expose a view of an entity without exposing its full internal state.

Lawful optics preserve round-trip expectations. For example, if a view is updated and then read back, the read should reflect the update where that update is meaningful. Not every projection is a lawful lens: many projections are lossy, derived, eventually consistent, or read-only.

Optics help keep partial observation distinct from full state and derived views distinct from canonical history.

Related concepts: [[Observable]], [[Observation]], [[State]], [[Projections]], [[Command]], [[Boundaries]], [[Equivalence vs Equality]].
