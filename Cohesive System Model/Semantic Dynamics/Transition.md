---
realm: Semantic Dynamics
kind: semantic-construct
---

# Transition

A Transition is the semantic decision relation that determines whether an attempted change is accepted for a subject.

Under the [[Stuff Structure Property]] lens, a transition is structure: an operation or relation that organizes how entity state, command values, observations, authority, policies, and versions may produce an accepted endogenous event, nil outcome, or rejection.

For entities, a transition is evaluated from a transition context:

```txt
observer and boundary
+ target entity state
+ command/input value
+ required observations
+ invariants, policies, authority, and expected version
-> transition decision
```

The transition context should be treated as "the" context only relative to the diagram of required observations, policies, authority, boundary, and version constraints that determine it.

The transition decision may accept, reject, or produce nil. Acceptance is an endogenous [[Event]]: the entity's state changes within the entity boundary and advances to a new [[Version]]. Whether that event is explicitly captured, persisted, or committed as an event record depends on the [[Realization|realization]]. Rejection produces no accepted state change for the target entity. Nil means the input was interpreted but no domain state transition occurred.

Lower-level value changes are better described as value transforms. The before/after relation between two entity states is a state evolution or state change. The domain transition is the stronger concept because it includes observer-relative interpretation, authority, policy, invariants, concurrency checks, and realization-specific commitment.

Examples of rejected transitions include:

- Duplicate input.
- Failed validation or precondition.
- Unauthorized request.
- Expected-version conflict.
- Telemetry-only or correlation-only input.

Related concepts: [[Value]], [[Shape]], [[Command]], [[Observer]], [[Entity]], [[State]], [[Event]], [[Version]], [[Stuff Structure Property]], [[Universal Constructions]], [[Algebras and Coalgebras]], [[Monads Monoids and Duals]], [[Realization]], [[Concurrency Control]].
