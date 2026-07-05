---
realm: Realization Substrate
kind: pattern
created: 2026-06-24
updated: 2026-07-04
---

# Event Sourcing

Event sourcing is a realization pattern in which an entity's durable history is represented by committed [[Event|events]] rather than only by current-state records.

In the Cohesive System Model, event-sourced events are not merely time-bearing values. They are committed endogenous events: events accepted within an [[Observer|observer]] boundary as the result of a valid [[Transition|transition]]. Once committed, they can be treated as state actions:

```txt
event : State -> State
```

Reconstitution then folds the committed event schedule from an initial state or snapshot to recover current entity state:

```txt
initial state + committed endogenous events -> current state
```

The word committed is essential. Event sourcing is interested in committed events because they maintain consistency:

- Only committed events advance the entity [[Version|version]].
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

## Relationship to Outbox

Event sourcing can also act as a coordination substrate when the committed event history is the source from which projections, [[Process Managers|process managers]], subscribers, and outbound publications are driven.

This gives an atomic unification of persistence and orchestration:

```txt
committed endogenous event history
  -> reconstitute entity state
  -> drive projections and follow-up processes
  -> publish output events
```

The event append is the local commit that makes both state history and follow-up responsibility observable. Publication and downstream processing still have their own [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], retry, and idempotency requirements, but the trigger for that work is durably tied to the authoritative transition.

If an event-sourced system appends the event and separately writes an unrelated broker message with no recovery link, it reintroduces the [[Dual-Write Problem|dual-write problem]]. A separate [[Outbox|outbox]] may still be useful, but it must either be committed atomically with the event append or derived reliably from the committed event history.

ARIES is relevant by analogy and contrast. In a database, the transaction log is often an internal [[Write-Ahead Logging|write-ahead]] recovery structure used for redo, undo, checkpoints, and crash recovery. In event-sourced systems, the event log is usually an addressable, first-class primitive of the application model: committed events define entity history, version succession, reconstitution, projection, audit, and sometimes publication.

The logs therefore have different semantics. ARIES log records are recovery records for a storage engine. Event-sourced records are committed domain events for an entity boundary. Both make durable ordered history central to [[Persistence|persistence]], [[Reconstitution|reconstitution]], and [[Recovery|recovery]].

## External References

- Martin Fowler, [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html), 2005.
- Greg Young, [CQRS Documents](https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf), 2010.
- Microsoft Azure Architecture Center, [Event Sourcing pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing).
- C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, and Peter Schwarz, [ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging](https://web.stanford.edu/class/cs345d-01/rl/aries.pdf), ACM Transactions on Database Systems, 17(1):94-162, March 1992.

Related concepts: [[Event|event]], [[State|state]], [[Transition|transition]], [[Entity|entity]], [[Version|version]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Write-Ahead Logging|write-ahead logging]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Concurrency Control|concurrency control]], [[Event-State Duality|event-state duality]], [[Behavior|behavior]], [[Outbox|outbox]], [[Transactional Outbox|transactional outbox]], [[Dual-Write Problem|dual-write problem]], [[Process Managers|process managers]], [[CQRS]], [[Storage Systems|storage systems]], [[Realization|realization]].
