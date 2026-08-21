---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-08-20
---

# Actor Systems

Actor Systems are runtimes that organize execution around addressable actor identities, message delivery, placement, isolation, and serialized handling per actor.

In the model, actor systems can realize [[Observer|observers]], [[Agent|agents]], [[Entity|entities]], [[Process|process]] participants, projections, or coordination components.

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

## Addressing, Placement, and Location Transparency

An actor address can remain stable while the actor is inactive, migrates, is rebalanced, fails over, or is reached through a router. This location transparency is an addressing and placement indirection: senders need not embed the actor's current process, host, or network coordinates.

It is not a guarantee that local and remote sends are operationally interchangeable. An in-process mailbox enqueue, cross-process serialization, cross-host network send, cross-region route, and activation through a remote state provider have different latency, capacity, ordering, delivery, security, cost, and partial-failure boundaries. A uniform `tell` or `ask` surface must not erase those differences from the [[Infrastructure Graph|infrastructure graph]], [[Failure Models|failure model]], [[Service Levels|service levels]], or operational policy.

Location transparency is not always desirable. A model may require co-location with authoritative state, affinity to a partition or region, separation across failure domains, data-sovereignty constraints, or a prohibition on remote interaction. [[Locality|Locality]] and placement policy should express those requirements even when application code uses one logical address form.

The [[Fallacies of Distributed Computing|fallacies of distributed computing]] are a useful check on actor abstractions: stable addressing does not make the network reliable, latency-free, unlimited, secure, static, singly administered, costless, or homogeneous. Actor systems can hide coordinates where they are irrelevant while still exposing operational consequences, placement evidence, and failure boundaries where they matter.

## Reception-Order Indeterminacy

Concurrent message transmissions need not determine one global next state or one universal arrival order. Transport, runtime [[Arbitration|arbitration]], and [[Scheduling|scheduling]] establish a local reception and execution order at each actor boundary. Different orders can lead to different future behavior; [[Nondeterminism and Choice|nondeterminism and choice]] names this actor-specific source **reception-order indeterminacy**.

An actor runtime may provide a FIFO relation for selected sender-receiver pairs, one mailbox, priority queues, work stealing, or another admission discipline. None of those guarantees follows from addressability or actor identity alone. Delivery, reception, scheduling, processing, persistence, and commitment orders must be stated at their actual boundaries.

[[Fairness]] can constrain whether a persistently eligible activation or deliverable message is eventually serviced, but fairness does not imply bounded latency or reliable delivery across crash and partition. Physical or runtime arbiters can also have unbounded decision latency; see the [[Glitch Principle|glitch principle]].

Reception-order indeterminacy becomes observationally harmless when handlers commute, are quasi-commutative, or form [[Reduction, Evaluation, and Confluence|confluent]] paths for the relevant observer. Otherwise, actor serialization chooses one semantically visible order, and correctness may require versions, durable history, explicit conflicts, or coordination.

Actor identity serialization can provide a concrete concurrency-control mechanism when the actor observer hosts the entity transition boundary. Routing all commands for an entity to the same logical actor and processing them one at a time aligns interpretation with commit for the duration of each operation.

If an actor only forwards, routes, caches, or partially observes an entity, actor serialization alone does not prove that the entity transition is correct. The semantic meaning of each message still depends on observer-relative command interpretation, and correctness may still require expected-version checks, durable persistence, idempotency, or coordination with another transition owner.

An actor system may interpret canonical [[Transition Models|transition models]] or advance finite activations of [[Process Graphs|process graphs]]. The actor definition, mailbox handler, state provider, timer callback, or runtime registration is not semantic authority unless it is the declared canonical definition itself. Actor-specific code and storage remain derived interpretations whose supported versions and capability boundaries must be explicit.

Actor serialization can be evidence for local transition exclusion, but it does not by itself prove atomic persistence of state and emissions, durable wait registration, logical exactly-once effects, multi-actor atomicity, or process recovery. Timers, reminders, persisted state, and mailboxes can realize process requirements only when stable identities, deduplication, definition compatibility, token state, acknowledgment, and crash boundaries are preserved.

An effect adapter hosted by an actor must not mutate authoritative entity state outside the entity's transition boundary. External results and signals return through explicit admission, observer, continuation, and transition semantics.

## Formal relations

- `may_realize`: [[Observer]] — Hosts addressable interpretation loci when actor identity, boundary, authority, state view, and activation semantics preserve the observer role.
- `may_realize`: [[Agent]] — Hosts addressable decision-and-action roles when an actor activation preserves the agent's observer context, purpose, policies, action repertoire, attribution, and authority boundary.
- `may_realize`: [[Entity]] — Hosts entity identity and transition authority when serialization, persistence, versioning, and commit requirements are satisfied.
- `may_realize`: [[Interaction Modes]] — Implements explicit message-passing profiles through actor addresses, mailboxes, placement, dispatch, and correlated continuations while preserving declared boundaries.

## External References

- Carl Hewitt, [Actor Model of Computation: Scalable Robust Information Systems](https://arxiv.org/abs/1008.1459), 2010.
