---
realm: Realization Substrate
---

# Event Sourcing

Event sourcing is a realization pattern in which an entity's durable history is represented by committed [[Event|events]] rather than only by current-state records.

In the Cohesive System Model, event-sourced events are not merely time-bearing values. They are committed endogenous events: events accepted within an [[Observer|observer]] boundary as the result of a valid [[Transition]]. Once committed, they can be treated as state actions:

```txt
event : State -> State
```

Reconstitution then folds the committed event schedule from an initial state or snapshot to recover current entity state:

```txt
initial state + committed endogenous events -> current state
```

The word committed is essential. Event sourcing is interested in committed events because they maintain consistency:

- Only committed events advance the entity [[Version]].
- Rejected commands do not produce committed events for the target entity.
- Nil endogenous events record no domain transition for the target entity.
- Expected-version checks, transactions, actor serialization, or compare-and-swap operations ensure that only valid successors enter the history.
- Reconstitution, projections, audit, recovery, and downstream publication must be based on the committed history, not merely on attempted inputs.

Exogenous events, messages, commands, retries, telemetry, and rejection records may be persisted elsewhere, but they are not automatically part of the entity's event-sourced state history. They become part of that history only if interpreted and committed as endogenous events for the entity boundary.

Event sourcing therefore realizes several concepts together:

- [[Persistence]] as durable committed event history.
- [[Reconstitution]] as replay or snapshot-plus-replay.
- [[Concurrency Control]] as protection of the versioned event schedule.
- [[Event-State Duality]] as the relation between committed event history and state history.
- [[Behavior]] as the trajectory obtained by folding committed events and applying a hold or interpolation rule.

Event sourcing is often combined with [[CQRS]], but the patterns are distinct. Event sourcing chooses committed event history as authoritative persistence; CQRS separates command-side consistency from query-side reconstitution and projection.

## External References

- Martin Fowler, [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html), 2005.
- Greg Young, [CQRS Documents](https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf), 2010.
- Microsoft Azure Architecture Center, [Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing).

Related concepts: [[Event]], [[State]], [[Transition]], [[Entity]], [[Version]], [[Persistence]], [[Reconstitution]], [[Concurrency Control]], [[Event-State Duality]], [[Behavior]], [[CQRS]], [[Storage Systems]], [[Realization]].
