---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-07-04
---

# Realization

Realization is the relation by which semantic roles, system graph, operational concerns, and architecture practices are made concrete in a substrate.

A realization does not make the semantic concept identical to the substrate mechanism. It says that a concrete mechanism hosts, carries, preserves, or implements the relevant meaning under an explicit [[Boundaries|boundary]] and operational context.

[[System Language and Realization|System language and realization]] frames this as the practical half of the Cohesive vision: the system language should be precise enough to support compiler-like lowering into working infrastructure while preserving the semantic relationships that matter.

In [[Stuff Structure Property|stuff structure property]] terms, realization maps semantic stuff, structure, and properties into substrate stuff, structure, and properties. Correct realization requires preserving the distinctions that matter, not merely finding similarly named implementation artifacts.

Realization answers:

- Which substrate mechanism realizes a semantic, structural, or operational role?
- Which meanings and guarantees are preserved by that mechanism?
- Which guarantees belong only to the substrate boundary?
- Which semantic roles have multiple possible realizations?
- Which semantic roles are partial, virtual, deferred, or unrealized?
- Which realization layers are being treated as primitive within the current model boundary?
- How realization choices compose across a whole system model?

Examples include:

- An [[Observer|observer]] realized by an OS thread, logical task, fiber, actor mailbox turn, workflow activation, request handler, projection run, process step, or entity command handler.
- An [[Entity|entity]] realized by an actor-hosted aggregate, database record plus optimistic concurrency, event stream plus reconstitution, workflow subject, or storage document.
- A [[Transition|transition]] realized by a serialized actor turn, database transaction with expected-version check, compare-and-swap operation, workflow decision, or command handler plus durable commit.
- A [[Boundaries|boundary]] realized by a transaction, actor identity, process, broker partition, service API, deployment unit, or persistence scope.
- [[Persistence]] realized by records, logs, event streams, snapshots, workflow histories, [[Outbox|outbox]] records, [[Transactional Inbox|inbox]] records, or projection state.
- [[Durability]] realized by storage durability, write-ahead logging, replication, broker retention, workflow histories, stable timers, durable queues, backups, or consensus-backed logs.
- [[Behavior]] realized by an event schedule plus fold and interpolation, a workflow history, sampled state history, or live stream processor.
- [[Durable Execution]] realized by a durable execution engine, workflow engine, durable task runtime, database-backed process manager, or actor runtime with persisted state and reminders.

## Multiplicity

A semantic role may have several valid realizations. For example, an entity can be actor-hosted in one system, stored as a database row with optimistic concurrency in another, and represented by an event stream with reconstitution in a third.

A semantic role may also have no current realization. This can describe a conceptual model that has not been implemented, an optional capability, a deferred migration target, or a role that exists only as a projected or derived view.

The absence of a realization does not make the semantic concept invalid. It only means no substrate mechanism has been selected or deployed for that role within the current model boundary.

## Layered Realization

Realization is usually layered. A semantic construct may be realized in terms of the system graph and infrastructure, while that infrastructure can itself be modeled as realized by lower-level constructs.

For example:

```txt
semantic observer
-> actor observer
-> runtime task or mailbox turn
-> OS thread or scheduler continuation
-> process and kernel scheduling
-> CPU, memory, network, storage devices
-> physical processes
```

Each layer may be treated as substrate from the perspective above it and as semantic structure from the perspective below it. A runtime is substrate for an application observer, but it can also be modeled in terms of schedulers, queues, continuations, memory, system calls, and hardware behavior.

The model boundary determines where analysis stops. Cohesive usually treats infrastructure as the lower realization substrate for domain and application semantics, but the same modeling discipline can continue downward through platform, operating system, hardware, and physical realization layers when that distinction matters.

Layered realization explains why substrate guarantees must be scoped. A broker guarantee may depend on filesystem durability, replication protocol behavior, kernel scheduling, network partitions, disk flush semantics, and hardware failure modes. The application model does not need to expose every lower layer, but it should avoid treating a higher-level guarantee as stronger than its lower-layer realizations allow.

## Coherence

Realization choices must be coherent across relationships. It is not enough to choose a substrate mechanism for each role independently.

For example, if an actor realizes an entity observer, then routing, ordering, persistence, recovery, and concurrency control must preserve the fact that the actor hosts the entity transition boundary. If a request handler realizes only a temporary observer, then transition correctness must be preserved by another mechanism, such as expected-version checks.

A coherent architecture selects realizations that preserve the intended correspondence between domain semantics, system graph, operational concerns, and substrate behavior.

## Categorical Discipline

When one coherent implementation has been selected, realization can be viewed through [[Functoriality|functoriality]]: a functor from a semantic or system model category into a substrate model category. This is useful as a discipline because realization should preserve the relationships that matter, not merely map names to implementation artifacts.

That view is too strict for design work because a semantic role may have many possible realizations, or none. A more flexible formulation assigns each semantic object `s` a category `Real(s)` of possible realizations. Objects of `Real(s)` are possible concrete realizations, and morphisms describe refinements, substitutions, migrations, compatibility relations, or implementation-preserving transformations.

Layered realization can be understood as composition: a realization selected at one layer may itself become the semantic object for a lower realization layer. In categorical terms, realization functors or fibrations can be composed or iterated across layers, with each projection forgetting one layer of concrete structure.

The Grothendieck construction then gives a total category of realized objects whose objects are pairs:

```txt
(semantic object, realization)
```

The projection back to the semantic model forgets the concrete realization while preserving which semantic object is being realized. Empty fibers represent semantic objects with no current realization. Multiple objects in a fiber represent multiple possible realizations of the same semantic object. A deployed architecture can be understood as a section, or partial section, that selects compatible realizations across the semantic model.

This categorical language is not required for ordinary modeling, but it keeps the distinction precise: realization is not a collapse of meaning into implementation. It is a structured relationship between semantic objects and possible concrete mechanisms.

Related concepts: [[System Language and Realization|system language and realization]], [[Stuff Structure Property|stuff structure property]], [[Functoriality|functoriality]], [[Naturality|naturality]], [[Universal Constructions|universal constructions]], [[Fibrations and Indexed Structure|fibrations and indexed structure]], [[Equivalence vs Equality|equivalence vs equality]], [[Observer|observer]], [[Entity|entity]], [[Transition|transition]], [[Boundaries|boundaries]], [[Effects|effects]], [[Commit Boundaries|commit boundaries]], [[Persistence|persistence]], [[Durability|durability]], [[Reconstitution|reconstitution]], [[Durable Execution|durable execution]], [[Concurrency Control|concurrency control]], [[CRDTs]], [[Event Sourcing|event sourcing]], [[Outbox|outbox]], [[CQRS]], [[Runtimes|runtimes]], [[Actor Systems|actor systems]], [[Application Hosts|application hosts]], [[Storage Systems|storage systems]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Infrastructure|infrastructure]].
