---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-06-29
---

# Actor Systems

Actor Systems are runtimes that organize execution around addressable actor identities, message delivery, placement, isolation, and serialized handling per actor.

In the model, actor systems can realize [[Observer|observers]], [[Entity|entities]], [[Process|process]] participants, projections, or coordination components.

The distinctive contribution of an actor system is that it can make observers globally or system-wide addressable. An actor address gives other observers a delivery path to a receiving observer boundary:

```txt
actor address -> mailbox -> actor observer -> interpretation
```

The address names a reachable observer locus, not necessarily an entity identity and not direct access to entity state. In one design, an actor identity may align with an entity identity so the actor hosts that entity's transitions. In another, a router, shard, process manager, projection worker, or service actor may observe and coordinate many entities.

Actor-system concerns include:

- Actor identity and addressing.
- Placement and activation.
- Serialized message handling.
- Supervision and restart.
- State providers.
- Timers and reminders.
- Passivation and reactivation.
- Delivery and ordering guarantees.

Actor identity serialization can provide a concrete concurrency-control mechanism when the actor observer hosts the entity transition boundary. Routing all commands for an entity to the same logical actor and processing them one at a time aligns interpretation with commit for the duration of each operation.

If an actor only forwards, routes, caches, or partially observes an entity, actor serialization alone does not prove that the entity transition is correct. The semantic meaning of each message still depends on observer-relative command interpretation, and correctness may still require expected-version checks, durable persistence, idempotency, or coordination with another transition owner.

Related concepts: [[Realization|realization]], [[Identity|identity]], [[Observer|observer]], [[Entity|entity]], [[Process|process]], [[Concurrency Control|concurrency control]], [[Delivery Semantics|delivery semantics]], [[Persistence|persistence]], [[Reconstitution|reconstitution]].
