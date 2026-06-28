---
realm: Architecture Practices
kind: architecture-practice
---

# Event Sourcing As Architecture Practice

Event sourcing is often described as an architecture practice. In the Cohesive System Model, the technical mechanics are captured by [[Event Sourcing]] as a realization substrate pattern.

## Problem

Event sourcing addresses the problem of preserving the committed history that explains current state, rather than persisting only a latest state record.

## Cohesive Formulation

The practice realizes [[Persistence]] as a durable sequence of committed endogenous [[Event|events]]. Reconstitution folds that committed event schedule into current state.

The important distinction is:

```txt
attempted input != committed endogenous event
```

Only committed events are state actions for the target entity. That is why event sourcing is also a consistency practice: the event history is the authoritative history of valid state transitions.

## Practice Interpretation

Event sourcing supports audit, replay, projection rebuild, temporal [[Query|queries]], and state reconstitution. It also raises operational concerns around schema evolution, idempotency, ordering, snapshots, retention, and event publication.

Related concepts: [[Event Sourcing]], [[Event]], [[Transition]], [[Query]], [[Persistence]], [[Reconstitution]], [[Version]], [[Event-State Duality]], [[CQRS as Architecture Practice]].
