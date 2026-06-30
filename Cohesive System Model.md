

## Core Thesis

Domains can be described as semantic system graphs composed of:

- [[Entity Models|Entity models]] with stable [[Identity|identities]]
- [[Relations]] between identities, states, observations, and observers 
- [[State|States]], [[Value|values]], [[Transition|transitions]], [[Event|events]] and [[Observation|observations]]  
- [[Observers]] as active participants 
- [[Command|Commands]] and [[Query|queries]] as observer-relative interpretations
- [[Process|Processes]] over time, including the flows and [[Effects|effects]] by which work moves between participants

Cohesive operationalizes these primitives by assigning [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Interaction|interaction]], [[Delivery Semantics|delivery]], [[Acknowledgments|acknowledgment]], [[Commit Boundaries|commit]], [[Coordination|coordination]], and control semantics, then realizes them through concrete [[Compute|compute]], [[Runtimes|runtimes]], [[Network|network]], [[Storage Systems|storage]], and [[Infrastructure|infrastructure]] components while preserving coherence across layers.

## Realms of Description

### 0. Principles

Describe modeling disciplines used across the system model.

- [[Categorical Principles]]
- [[Stuff Structure Property]]
- [[Compositionality]]
- [[CALM Theorem]]
- [[Asynchronous Computability Theorem]]
- [[Functoriality]]
- [[Naturality]]
- [[Duality and Symmetry]], [[Event-State Duality|event-state duality]], [[Synchrony and Asynchrony|synchrony and asynchrony]]
- [[Universal Constructions]]
- [[Equivalence vs Equality]]
- [[Monads Monoids and Duals]], [[Algebras and Coalgebras|algebras and coalgebras]], [[State Machines|state machines]], [[Yoneda Lemma|Yoneda lemma]], [[Adjunctions|adjunctions]]
- [[Fibrations and Indexed Structure]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Database Sheaf Semantics|database sheaf semantics]], [[Fixed Points and Recursion|fixed points and recursion]], [[Enrichment and Order|enrichment and order]], [[Optics and Lenses|optics and lenses]], [[Trace and Feedback|trace and feedback]]

### 1. Semantic Dynamics

Describes change, time, observation, and participation.

- [[State]]  
- [[Value]]
- [[Shape]]
- [[Observable]]  
- [[Observation]]  
- [[Event]]  
- [[Behavior]]  
- [[Process]]
- [[Observer]]  
- [[Entity]]  
- [[Command]]  
- [[Query]]
- [[Transition]]  
- [[Time]]  
- [[Identity]]  
- [[Version]]

### 2. Operational Semantics

Describes how semantic dynamics are made executable and reliable.

- [[Persistence]]  
- [[Reconstitution]]  
- [[Interaction]]  
- [[Delivery Semantics|Delivery semantics]]  
- [[Acknowledgments]]
- [[Commit Boundaries]]
- [[Coordination]]  
- [[Consensus]]
- [[Safety and Liveness]], [[Progress Conditions|progress conditions]], [[CAP Theorem|CAP theorem]]
- [[Durable Execution]]
- [[Concurrency Control|Concurrency control]]
- [[Isolation]]
- [[ACID]], [[Two-Phase Commit|two-phase commit]], [[Weak Isolation Patterns|weak isolation patterns]]
- [[Dual-Write Problem]]
- [[Version Histories]]
- [[Consistency Models]]  
- [[CRDTs]]
- [[Retry]], [[Rate Limiting|rate limiting]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Recovery|recovery]]

### 3. System Structure

Organizes semantic dynamics into a system graph. System Structure describes placement, composition, ownership, boundaries, dependencies, and graph shape; it is distinct from primitive semantic definitions and concrete realization substrate.

- [[Entity Models]]
- [[Observers]]  
- [[Relations]]  
- [[Projections]]  
- [[Processes]]  
- [[Effects]]
- [[Flows]] as movement views within or between processes
- [[Business Transactions]]
- [[Policies]]  
- [[Invariants]]  
- [[Boundaries]]

### 4. Realization Substrate

Provides concrete mechanisms.

- [[Realization]]
- [[Compute]]  
- [[Runtimes]]  
- [[Application Hosts|Application hosts]]  
- [[Network]]
- [[Storage Systems|Storage systems]]  
- [[Write-Ahead Logging]]
- [[Consensus Protocols]]
- [[Event Sourcing]]
- [[Outbox]]
- [[CQRS]]
- [[Brokers]]  
- [[Workflow Engines|Workflow engines]]  
- [[Durable Execution Engines|Durable execution engines]]
- [[Actor Systems|Actor systems]]  
- [[Infrastructure]]

### 5. Architecture Practices

Contextualizes named architecture practices as cross-realm bundles of problems, constraints, and realization choices.

- [[Architecture Practices]]
- [[Domain-Driven Design]], [[Ports and Adapters|ports and adapters]], [[Clean Architecture|clean architecture]]
- [[Modular Monolith]], [[Microservices|microservices]], [[Event-Driven Architecture|event-driven architecture]]
- [[CQRS as Architecture Practice]], [[Event Sourcing as Architecture Practice|event sourcing as architecture practice]]
- [[Sagas and Process Managers]], [[Actor Model|actor model]], [[Anti-Corruption Layer|anti-corruption layer]]
- [[Transactional Outbox]], [[Transactional Inbox|transactional inbox]], [[Weak Isolation Patterns as Architecture Practice|weak isolation patterns as architecture practice]], [[CRDTs as Architecture Practice|CRDTs as architecture practice]], [[Data Mesh|data mesh]]

## Semantic Dynamics

### State

A **[[State|state]]** is the condition or configuration of a subject within a model [[Boundaries|boundary]]. It represents what *is*, relative to a subject, boundary, [[Shape|shape]], and time or version.

State is not the same thing as the [[Value|value]] used to read, write, transmit, or compare it. State becomes usable through values and contextualized **[[Observation|observations]]** produced by [[Observable|observables]].

State does not inherently carry [[Identity|identity]], [[Version|version]], or lineage. For an [[Entity|entity]], entity state is state attributed to an [[Identity|identity]] at a [[Version|version]].

In [[Event-State Duality|event-state duality]]:
- [[Event|Events]] carry time and change information.  
- States carry information and become current at a specific version/time.

For a sequential entity, state at version *V* is the result of applying the event that produced version *V*. [[Event-State Duality]] does not imply isomorphism: event histories and state histories are dual views of [[Behavior|behavior]], not interchangeable representations.

### Value

A **[[Value|value]]** is pure structured data. It is the concrete information used to read, write, transmit, compare, validate, transform, or carry state.

Values are identity-free, version-free, lineage-free, and timeless. A value may be empty, scalar, or composite. It may be understood through a [[Shape|shape]] and represented as a record, map, array, vector, bytes, dictionary-backed object, ordinal layout, sparse buffer, packed presence bits, columnar storage, or struct-of-arrays storage.

Representation is not semantic identity. Two values with the same logical content are the same value even if their physical representations differ.

### Shape

A [[Shape|shape]] is the logical structure expected of a [[Value|value]], [[Observation|observation]], state view, event payload, command input, query result, or projection result within a model [[Boundaries|boundary]].

Shape is distinct from both value and representation. A value is the concrete structured data. A representation is the physical or substrate form. Shape is the declared structure under which the value can be interpreted, validated, compared, transformed, observed, or transmitted.

### Observable

An [[Observable|observable]] is a probe, projection, measurement, or accessor that produces an observation from state.

Observables define how state becomes visible to an [[Observer|observer]]. Different observables may produce different observations from the same underlying state.

The current state of an [[Entity|entity]] is not itself an observable; it is state. The accessor, [[Reconstitution|reconstitution]] procedure, projection, cache read, or subscription that exposes that current state is a current-state observable, producing an entity-scoped observation at a declared boundary, version, and consistency expectation.

Observables include field accessors, read models, metrics, sensors, UI views, policy-shaped views, derived computations, and stream subscriptions. Reactive-programming observables are one operational realization when they emit observations of state; physics offers a useful informal analogy in which an observable names what can be measured rather than the state itself.

### Observation

An **[[Observation|observation]]** is a contextualized [[Value|value]] produced by an observable acting on state. It is the form in which state becomes usable by an [[Observer|observer]] relative to a [[Boundaries|boundary]].

An observation has:
- A **[[Value|value]]** (scalar, array, vector, map, record, bytes, null, or another composite)
- A **[[Shape|shape]] or representation** (schema, projection, record layout, or optimized internal buffer)
- A **subject, source, or address** indicating what state the value was read from or derived from
- Optional **context** such as version, observer, source, and field-level lineage

The value inside an observation is identity-free, version-free, lineage-free, and timeless. Observation metadata supplies attribution and provenance when correctness requires it. Observations do not carry intrinsic occurrence time; time and occurrence belong to events.

When an entity is [[Reconstitution|reconstituted]], its current state is delivered as an entity-scoped observation. [[Command|Commands]] are validated against observations of current entity state, related state, policy state, and environmental state. [[Query|Queries]] request observations or values from state, projections, read models, or computations.

Entity state is a specialized observation whose subject is an entity.

### Event

An [[Event|event]] is a time-bearing occurrence with a [[Value|value]]. It marks, reports, or induces change depending on how it is interpreted by an [[Observer|observer]] relative to a [[Boundaries|boundary]].

Structurally, an event is a value with occurrence. Semantically, an event may be exogenous, input, command-bearing, query-bearing, endogenous, or output depending on the observer [[Boundaries|boundary]].

### Behavior

[[Behavior]] is a time-varying [[Value|value]]: a trajectory through state space. For an entity, behavior can be viewed as both an event schedule and a state history.

### Process

A [[Process|process]] is coherent work unfolding over time. It gives semantic unity to related observations, commands, queries, events, transitions, decisions, effects, artifacts, and participant activity.

A process is not defined by a workflow engine, scheduler, thread, transaction manager, application host, or broker. Those mechanisms may realize a process, execute one activation of it, or host one step of it. The semantic process is defined by its subject or correlation identity, participants, inputs, decisions, state or history, effects, completion meanings, and flows of movement between participants.

Processes compose when the outputs of one process become future inputs to another. Compositions may be pipelines, nested sub-processes, concurrent processes, or feedback loops.

### Observer

An [[Observer|observer]] is a locus of interpretation: the participant, context, or execution locus relative to which values, observations, events, commands, queries, boundaries, and state acquire meaning. Every runtime participant is a potential observer, but an observer is realized only when a context supplies boundary, state view, authority, and interpretation rules.

An observer is characterized by:
- Its own **[[Identity|identity]]** (distinct from entity identities)
- Its own **[[Boundaries|boundary]]**  
- A realization context or logical execution context in which interpretation occurs
- The ability to observe observables, producing **observations** of state
- The ability to host, observe, route, or project **entities** and their **events** within its [[Boundaries|boundary]]
- The ability to receive events from other observers as **exogenous events**

Addressability of an observer is an operational concern (part of [[Interaction|interaction]] and [[Delivery Semantics|delivery semantics]]), not intrinsic to the definition. Some observers have globally addressable identities, such as actors. Others have transient or local identities, such as a request handler or logical execution context created for one operation.

An observer may be realized by an OS thread, logical thread, fiber, coroutine, task, actor mailbox turn, workflow activation, request handler, projection run, process step, or entity command handler. In green-thread, fiber, or async runtimes, the observer follows the logical execution context governed by a scheduler, not necessarily the OS thread.

Actor systems make observers addressable: an actor address gives other observers a delivery path to a receiving observer boundary. Entities and [[Process|processes]] can also be modeled as observers when they interpret inputs relative to their own state, history, policies, and boundary.

An endogenous event emitted inside one observer’s [[Boundaries|boundary]] can be observed as an exogenous event by another observer.

Commands and queries are **observer-relative interpretations**: the same incoming [[Value|value]] or event may be interpreted differently (or rejected) depending on the observer’s current view of entity state, projections, required observations, [[Invariants|invariants]], [[Policies|policies]], authority, and consistency expectations.

### Entity

An [[Entity|entity]] is an enduring, identifiable subject whose state evolves over time under controlled transitions.

An entity is defined by:
- A stable **identity** that persists across its lifetime
- A **family of entity-state observations** across time, indexed by version
- A **current state** at any point in time, attributed to identity + version
- **[[Transition|Transitions]]** that define how its state may change
- **[[Invariants]]** and **[[Policies|policies]]** that constrain valid changes
- **[[Effects]]**, primarily the endogenous events it produces when transitions are committed

An entity is therefore state + identity + version history + transitions + invariants + policies + effects.

Entity state is a specialized observation: a shaped [[Value|value]] attributed to an entity identity at a version. It may be complete or partial only relative to a declared [[Shape|shape]], projection, transition, or [[Boundaries|boundary]]. Related entities, policies, projections, and environmental facts that affect a transition belong to the transition context, not automatically to the entity's own state.

Identity is what allows a sequence of state observations to be understood as successive versions of *the same thing*.

An entity is not automatically an observer, but it may be modeled or realized as one when it interprets inputs relative to its own state and boundary. Correct entity transitions require the interpreting observer to remain aligned with the realization context that commits the transition: actor hosting can provide this through serialized message handling, while stateless request handlers usually require expected-version checks.

### Command

A [[Command|command]] is an observer-relative interpretation of an input event or incoming [[Value|value]] as an attempted transition.

```txt
Exogenous event
  -> input event at an Observer [[Boundaries|boundary]]
  -> command intent (relative to the Observer and target subject)
  -> validation against current Entity state + required observations + invariants + policies + authority + expected version
  -> endogenous event | nil
```

Commands are not mere messages. They are interpretations made relative to:
- The specific observer
- The observer’s [[Boundaries|boundary]] and current view of state
- Authority, invariants, and policies  
- The intended transition  
- An optional expected version / etag (the version of entity state the observer believed was current when formulating the command)

### Query

A [[Query|query]] is an observer-relative interpretation of an input event, request, or incoming [[Value|value]] as a request to observe, compute, or return information without requesting a modeled semantic state transition.

```txt
Exogenous event or incoming value
  -> input at an Observer [[Boundaries|boundary]]
  -> query intent (relative to the Observer and target subject or view)
  -> selection of observable + projection + read model + authority + consistency expectation
  -> observation | value | stream | nil | rejection
```

Queries are not mere messages. They are interpretations made relative to:
- The specific observer
- The observer's [[Boundaries|boundary]] and current view of state
- The requested [[Observable|observable]], projection, read model, or computation
- Authority, access policy, and disclosure rules
- Freshness, ordering, and consistency expectations

Operational state may still change while serving a query, but the modeled semantic entity transition is not being requested.

## Dualities

```txt
Events -> State
  Fold or integrate committed events to produce a state sample at a new version.

State -> Events
  Observe differences, transitions, or threshold crossings in state samples and emit new Events.

Events -> Behavior
  Fold, integrate, scan, switch, or transform event streams through an observer-defined accumulator to produce time-varying values.

Behavior -> Events
  Sample, detect changes, or detect crossings in Behavior and emit Events.
```

[[Persistence]] chooses which view is made durable:
- Current state records as observations
- Event history
- Behavior samples
- [[Workflow Engines|Workflow]] history
- [[Projections|Projection]] state (derived observations)
- Derived observations

## Exogenous and Endogenous Events

Relative to an **observer’s [[Boundaries|boundary]]**:

- **Exogenous event**: An event arriving from outside the observer’s [[Boundaries|boundary]]. It may originate from another observer’s endogenous event, a runtime, a clock, a user, a sensor, or the external environment.
- **Input event**: An exogenous event in the role of entering the observer [[Boundaries|boundary]].
- **Command**: An input event interpreted as an attempted transition for a target subject.
- **Query**: An input event or incoming value interpreted as a request to observe, compute, or return information without requesting a modeled semantic state transition.
- **Endogenous event**: An event committed within the observer’s own semantic history (emitted by an entity it hosts).
- **Output event**: An endogenous event emitted across a [[Boundaries|boundary]].
- **Nil endogenous event**: The observer observed the input but no domain transition event was committed for the target entity (version unchanged).

Some systems may still record rejection, audit, telemetry, or diagnostic events when interpretation yields `nil`. Those records are operational traces or events for another subject, not a committed domain transition for the target entity.

Interpretation flow:

```txt
Exogenous event
  -> input event
  -> Command | Query (observer-relative)
  -> validation or observation selection
  -> endogenous event | observation | value | nil
```

Examples of `nil`:  
- Duplicate input  
- Failed validation or precondition  
- Unauthorized request  
- Version conflict (expected version mismatch)  
- Telemetry-only or correlation-only signal

One observer’s endogenous event may become another observer’s exogenous event.

## Commands (Expanded Flow with Versioning)

A command carries an optional **expected version / etag** — the version of entity state the observer believed was current when it decided to issue the command.

The entity transition runtime, aligned with the interpreting observer, performs:
- Validation against current entity state + required observations + invariants + policies
- [[Concurrency Control|Expected version check]] (if provided)
- Decision: commit endogenous event → new state version, or reject → `nil` (version unchanged)

## Operational Semantics

### Persistence

What is made durable and authoritative?

- Current-state records (as entity-scoped observations)
- Event histories
- [[Outbox]] records
- [[Transactional Inbox|Inbox]] and deduplication records
- Actor state providers
- Workflow histories
- Durable execution histories, checkpoints, timers, signals, and pending work
- Process state
- Projection state (derived observations)

### Reconstitution

How is usable state recovered?

- Load latest record → produce an observation
- Replay events → fold into a current state sample
- Load snapshot + events
- Resume durable execution state, checkpoints, or workflow history
- Activate actor by identity
- Rebuild projection as a derived observation

### Interaction

How do observers address, observe, notify, or invoke one another?

- One-way send
- Request/reply
- Publish/consume
- Stream/session
- Shared-state interaction
- Synchronization/rendezvous

### Delivery Semantics

What guarantees does an interaction edge provide?

- At-most-once / at-least-once / effectively-once within a defined [[Boundaries|boundary]]
- Ordered per key  
- Durable / volatile delivery  
- Replayable / retained  
- Deduplicated  
- Requires idempotent receiver
- Explicit [[Acknowledgments|acknowledgment]] meaning

### Coordination

How is multi-step or multi-participant work made coherent across observers?

- Local transaction  
- Distributed transaction / [[Transactional Outbox|transactional outbox]]
- [[Transactional Inbox|Transactional inbox]] or idempotent receiver
- Saga with compensation  
- [[Durable Execution|Durable execution]] with resume  
- Choreography through events  
- Process manager  
- Projection update protocol

### Durable Execution

How does process execution remain coherent across failure, restart, suspension, timeout, or delayed external work?

- Persist execution state, history, checkpoints, timers, signals, or pending work
- Reconstitute usable process context after interruption
- Resume, replay, retry, compensate, or escalate without changing semantic history
- Preserve idempotency at effect boundaries
- Preserve [[Commit Boundaries|commit boundaries]] and acknowledgment meanings
- Bind the guarantee to an explicit execution boundary

### Control

What constrains execution?

- Optimistic concurrency (via expected version)  
- Pessimistic locking / fencing tokens  
- Actor identity serialization  
- Retries, rate limiting, backpressure  
- Idempotency

## Protocol Layering and Space

Guarantees are always relative to a semantic space and an observer’s [[Boundaries|boundary]].

- **Addressing space**: What kind of thing is addressed? (Entity, observer, actor, etc.)
- **Message space**: What unit is delivered or interpreted? (Observation, event, command, query)
- **[[Acknowledgments|Acknowledgment]] space**: What has actually been accepted, persisted, processed, or committed?
- **[[Ordering|Ordering space]]**: Ordered relative to which key, stream, partition, actor, or transaction?  
- **Failure space**: What [[Boundaries|boundary]] can fail independently?

None of these automatically mean “the business transition committed” unless the observer’s application semantics define that [[Boundaries|boundary]].

## Runtime

[[Realization]] is the relation by which semantic dynamics, system structure, and operational semantics are made concrete in a substrate. Realization is layered: a substrate at one layer can itself be modeled as semantic structure realized by lower-level substrate. [[Runtimes|Runtime]] is part of the realization substrate. An [[Actor Systems|actor system]], ASP.NET host, [[Workflow Engines|workflow engine]], [[Durable Execution Engines|durable execution engine]], [[Brokers|broker]], or database can realize operational semantics, but the semantics should be described separately from any specific runtime.

Different runtimes realize observers differently (e.g., actor placement and supervision vs. HTTP request pipeline), while the semantic model (observer, entity, observation, event, command, query) remains consistent. In async, fiber, or green-thread runtimes, the observer follows the logical execution context rather than a fixed OS thread.

## Cohesive Role

Cohesive preserves correspondence across realms:

```txt  
Semantic dynamics (State, Observation, Event, Observer, Entity, Command, Query, ...)
  -> System structure (Entity Models, Observers, Relations, Projections, Flows, Boundaries, ...)
  -> Operational semantics (Persistence, Reconstitution, Interaction, Delivery, Coordination, Durable Execution, Control)  
  -> Realization substrate (Realization, Compute, Runtimes, Network, Storage, Workflow engines, Durable execution engines, Actor systems, ...)
```

It lets a domain be modeled in terms of entities, observers, states, observations, events, commands, queries, relations, and flows, then projects those primitives into operational systems running on existing infrastructure while maintaining semantic fidelity across layers and across different observers.

[[Architecture Practices]] contextualize named industry patterns and methodologies as cross-realm bundles of problems, constraints, and realization choices expressible in Cohesive terms.
