

## Core Thesis

Domains can be described as semantic system graphs composed of:

- [[Entity Models|Entity models]] with stable [[Identity|identities]]
- [[Relations]] between identities, states, observations, and observers 
- [[State|States]], [[Value|values]], [[Transition|transitions]], [[Event|events]] and [[Observation|observations]]  
- [[Observers]] as active participants 
- [[Command|Commands]] and [[Query|queries]] as observer-relative interpretations
- [[Process|Processes]] over time, including the flows by which work moves between participants

Cohesive operationalizes these primitives by assigning [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Interaction|interaction]], [[Delivery Semantics|delivery]], [[Coordination|coordination]], and control semantics, then realizes them through concrete [[Compute|compute]], [[Runtimes|runtimes]], [[Network|network]], [[Storage Systems|storage]], and [[Infrastructure|infrastructure]] components while preserving coherence across layers.

## Realms of Description

### 0. Principles

Describe modeling disciplines used across the system model.

- [[Categorical Principles]]
- [[Stuff Structure Property]]
- [[Compositionality]]
- [[CALM Theorem]]
- [[Functoriality]]
- [[Naturality]]
- [[Duality and Symmetry]], [[Event-State Duality]]
- [[Universal Constructions]]
- [[Equivalence vs Equality]]
- [[Monads Monoids and Duals]], [[Algebras and Coalgebras]], [[Yoneda Lemma]], [[Adjunctions]]
- [[Fibrations and Indexed Structure]], [[Fixed Points and Recursion]], [[Enrichment and Order]], [[Optics and Lenses]], [[Trace and Feedback]]

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
- [[Coordination]]  
- [[Consensus]]
- [[Safety and Liveness]], [[CAP Theorem]]
- [[Durable Execution]]
- [[Concurrency Control|Concurrency control]]
- [[Isolation]]
- [[ACID]], [[Two-Phase Commit]], [[Weak Isolation Patterns]]
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
- [[Consensus Protocols]]
- [[Event Sourcing]]
- [[CQRS]]
- [[Brokers]]  
- [[Workflow Engines|Workflow engines]]  
- [[Durable Execution Engines|Durable execution engines]]
- [[Actor Systems|Actor systems]]  
- [[Infrastructure]]

### 5. Architecture Practices

Contextualizes named architecture practices as cross-realm bundles of problems, constraints, and realization choices.

- [[Architecture Practices]]
- [[Domain-Driven Design]], [[Ports and Adapters]], [[Clean Architecture]]
- [[Modular Monolith]], [[Microservices]], [[Event-Driven Architecture]]
- [[CQRS as Architecture Practice]], [[Event Sourcing as Architecture Practice]]
- [[Sagas and Process Managers]], [[Actor Model]], [[Anti-Corruption Layer]]
- [[Transactional Outbox]], [[Weak Isolation Patterns as Architecture Practice]], [[CRDTs as Architecture Practice]], [[Data Mesh]]

## Semantic Dynamics

### State

A **[[State]]** is the condition or configuration of a subject within a model [[Boundaries|boundary]]. It represents what *is*, relative to a subject, boundary, [[Shape|shape]], and time or version.

State is not the same thing as the [[Value|value]] used to read, write, transmit, or compare it. State becomes usable through values and contextualized **[[Observation|Observations]]** produced by [[Observable|observables]].

State does not inherently carry [[Identity]], [[Version]], or lineage. For an [[Entity]], entity state is state attributed to an [[Identity]] at a [[Version]].

In [[Event-State Duality]]:
- [[Event|Events]] carry time and change information.  
- States carry information and become current at a specific version/time.

For a sequential entity, State at Version *V* is the result of applying the Event that produced version *V*. [[Event-State Duality]] does not imply isomorphism: event histories and state histories are dual views of [[Behavior]], not interchangeable representations.

### Value

A **[[Value]]** is pure structured data. It is the concrete information used to read, write, transmit, compare, validate, transform, or carry state.

Values are identity-free, version-free, lineage-free, and timeless. A Value may be empty, scalar, or composite. It may be understood through a [[Shape|shape]] and represented as a record, map, array, vector, bytes, dictionary-backed object, ordinal layout, sparse buffer, packed presence bits, columnar storage, or struct-of-arrays storage.

Representation is not semantic identity. Two values with the same logical content are the same value even if their physical representations differ.

### Shape

A [[Shape]] is the logical structure expected of a [[Value]], [[Observation]], state view, event payload, command input, query result, or projection result within a model [[Boundaries|boundary]].

Shape is distinct from both value and representation. A value is the concrete structured data. A representation is the physical or substrate form. Shape is the declared structure under which the value can be interpreted, validated, compared, transformed, observed, or transmitted.

### Observable

An [[Observable]] is a probe, projection, measurement, or accessor that produces an Observation from State.

Observables define how State becomes visible to an [[Observer]]. Different Observables may produce different Observations from the same underlying State.

### Observation

An **[[Observation]]** is a contextualized [[Value|value]] produced by an observable acting on State. It is the form in which state becomes usable by an [[Observer]] relative to a [[Boundaries|boundary]].

An Observation has:
- A **[[Value|value]]** (scalar, array, vector, map, record, bytes, null, or another composite)
- A **[[Shape|shape]] or representation** (schema, projection, record layout, or optimized internal buffer)
- A **subject, source, or address** indicating what state the value was read from or derived from
- Optional **context** such as version, observer, source, and field-level lineage

The value inside an Observation is identity-free, version-free, lineage-free, and timeless. Observation metadata supplies attribution and provenance when correctness requires it. Observations do not carry intrinsic occurrence time; time and occurrence belong to Events.

When an Entity is [[Reconstitution|reconstituted]], its current State is delivered as an entity-scoped Observation. [[Command|Commands]] are validated against observations of current entity state, related state, policy state, and environmental state. [[Query|Queries]] request observations or values from state, projections, read models, or computations.

Entity state is a specialized Observation whose subject is an Entity.

### Event

An [[Event]] is a time-bearing occurrence with a [[Value|value]]. It marks, reports, or induces change depending on how it is interpreted by an [[Observer]] relative to a [[Boundaries|boundary]].

Structurally, an event is a value with occurrence. Semantically, an event may be exogenous, input, command-bearing, query-bearing, endogenous, or output depending on the observer [[Boundaries|boundary]].

### Behavior

[[Behavior]] is a time-varying [[Value|value]]: a trajectory through state space. For an Entity, behavior can be viewed as both an event schedule and a state history.

### Process

A [[Process]] is coherent work unfolding over time. It gives semantic unity to related observations, commands, queries, events, transitions, decisions, effects, artifacts, and participant activity.

A Process is not defined by a workflow engine, scheduler, thread, transaction manager, application host, or broker. Those mechanisms may realize a Process, execute one activation of it, or host one step of it. The semantic Process is defined by its subject or correlation identity, participants, inputs, decisions, state or history, effects, completion meanings, and flows of movement between participants.

Processes compose when the outputs of one process become future inputs to another. Compositions may be pipelines, nested sub-processes, concurrent processes, or feedback loops.

### Observer

An [[Observer]] is a locus of interpretation: the participant, context, or execution locus relative to which values, observations, events, commands, queries, boundaries, and state acquire meaning. Every runtime participant is a potential Observer, but an Observer is realized only when a context supplies boundary, state view, authority, and interpretation rules.

An Observer is characterized by:  
- Its own **[[Identity]]** (distinct from Entity identities)  
- Its own **[[Boundaries|boundary]]**  
- A realization context or logical execution context in which interpretation occurs
- The ability to observe observables, producing **Observations** of State  
- The ability to host, observe, route, or project **Entities** and their **Events** within its [[Boundaries|boundary]]
- The ability to receive events from other Observers as **exogenous events**

Addressability of an Observer is an operational concern (part of [[Interaction]] and [[Delivery Semantics]]), not intrinsic to the definition. Some Observers have globally addressable identities, such as actors. Others have transient or local identities, such as a request handler or logical execution context created for one operation.

An Observer may be realized by an OS thread, logical thread, fiber, coroutine, task, actor mailbox turn, workflow activation, request handler, projection run, process step, or entity command handler. In green-thread, fiber, or async runtimes, the Observer follows the logical execution context governed by a scheduler, not necessarily the OS thread.

Actor systems make Observers addressable: an actor address gives other Observers a delivery path to a receiving Observer boundary. Entities and [[Process|processes]] can also be modeled as Observers when they interpret inputs relative to their own state, history, policies, and boundary.

An endogenous event emitted inside one Observer’s [[Boundaries|boundary]] can be observed as an exogenous event by another Observer.

Commands and queries are **observer-relative interpretations**: the same incoming [[Value|value]] or event may be interpreted differently (or rejected) depending on the Observer’s current view of Entity state, projections, required observations, [[Invariants|invariants]], [[Policies|policies]], authority, and consistency expectations.

### Entity

An [[Entity]] is an enduring, identifiable subject whose state evolves over time under controlled transitions.

An Entity is defined by:
- A stable **Identity** that persists across its lifetime
- A **family of entity-state Observations** across time, indexed by Version
- A **current State** at any point in time, attributed to Identity + Version
- **[[Transition|Transitions]]** that define how its state may change
- **[[Invariants]]** and **[[Policies]]** that constrain valid changes
- **Effects**, primarily the endogenous Events it produces when transitions are committed

An Entity is therefore State + Identity + Version history + transitions + invariants + policies + effects.

Entity state is a specialized observation: a shaped [[Value|value]] attributed to an entity identity at a version. It may be complete or partial only relative to a declared [[Shape|shape]], projection, transition, or [[Boundaries|boundary]]. Related entities, policies, projections, and environmental facts that affect a transition belong to the transition context, not automatically to the entity's own state.

Identity is what allows a sequence of state Observations to be understood as successive versions of *the same thing*.

An Entity is not automatically an Observer, but it may be modeled or realized as one when it interprets inputs relative to its own state and boundary. Correct entity transitions require the interpreting Observer to remain aligned with the realization context that commits the transition: actor hosting can provide this through serialized message handling, while stateless request handlers usually require expected-version checks.

### Command

A [[Command]] is an observer-relative interpretation of an input event or incoming [[Value|value]] as an attempted transition.

```txt
Exogenous event
  -> input event at an Observer [[Boundaries|boundary]]
  -> command intent (relative to the Observer and target subject)
  -> validation against current Entity state + required observations + invariants + policies + authority + expected version
  -> endogenous event | nil
```

Commands are not mere messages. They are interpretations made relative to:  
- The specific Observer  
- The Observer’s [[Boundaries|boundary]] and current view of state
- Authority, invariants, and policies  
- The intended transition  
- An optional expected version / etag (the version of Entity state the Observer believed was current when formulating the command)

### Query

A [[Query]] is an observer-relative interpretation of an input event, request, or incoming [[Value|value]] as a request to observe, compute, or return information without requesting a modeled semantic state transition.

```txt
Exogenous event or incoming value
  -> input at an Observer [[Boundaries|boundary]]
  -> query intent (relative to the Observer and target subject or view)
  -> selection of observable + projection + read model + authority + consistency expectation
  -> observation | value | stream | nil | rejection
```

Queries are not mere messages. They are interpretations made relative to:
- The specific Observer
- The Observer's [[Boundaries|boundary]] and current view of state
- The requested [[Observable]], projection, read model, or computation
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
- [[Projections|Projection]] state (derived Observations)
- Derived observations

## Exogenous and Endogenous Events

Relative to an **Observer’s [[Boundaries|boundary]]**:

- **Exogenous event**: An event arriving from outside the Observer’s [[Boundaries|boundary]]. It may originate from another Observer’s endogenous event, a runtime, a clock, a user, a sensor, or the external environment.
- **Input event**: An exogenous event in the role of entering the Observer [[Boundaries|boundary]].
- **Command**: An input event interpreted as an attempted transition for a target subject.
- **Query**: An input event or incoming value interpreted as a request to observe, compute, or return information without requesting a modeled semantic state transition.
- **Endogenous event**: An event committed within the Observer’s own semantic history (emitted by an Entity it hosts).
- **Output event**: An endogenous event emitted across a [[Boundaries|boundary]].
- **Nil endogenous event**: The Observer observed the input but no domain transition event was committed for the target Entity (version unchanged).

Some systems may still record rejection, audit, telemetry, or diagnostic events when interpretation yields `nil`. Those records are operational traces or events for another subject, not a committed domain transition for the target Entity.

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

One Observer’s endogenous event may become another Observer’s exogenous event.

## Commands (Expanded Flow with Versioning)

A Command carries an optional **expected version / etag** — the version of Entity state the Observer believed was current when it decided to issue the command.

The entity transition runtime, aligned with the interpreting Observer, performs:
- Validation against current entity state + required observations + invariants + policies
- [[Concurrency Control|Expected version check]] (if provided)
- Decision: commit endogenous Event → new State Version, or reject → `nil` (version unchanged)

## Operational Semantics

### Persistence

What is made durable and authoritative?

- Current-state records (as entity-scoped observations)
- Event histories
- Outbox records
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

How do Observers address, observe, notify, or invoke one another?

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

### Coordination

How is multi-step or multi-participant work made coherent across Observers?

- Local transaction  
- Distributed transaction / transactional outbox  
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
- Bind the guarantee to an explicit execution boundary

### Control

What constrains execution?

- Optimistic concurrency (via expected version)  
- Pessimistic locking / fencing tokens  
- Actor identity serialization  
- Retries, rate limiting, backpressure  
- Idempotency

## Protocol Layering and Space

Guarantees are always relative to a semantic space and an Observer’s [[Boundaries|boundary]].

- **Addressing space**: What kind of thing is addressed? (Entity, Observer, actor, etc.)  
- **Message space**: What unit is delivered or interpreted? (Observation, Event, Command, Query)
- **Acknowledgment space**: What has actually been accepted, persisted, processed, or committed?  
- **[[Ordering|Ordering space]]**: Ordered relative to which key, stream, partition, actor, or transaction?  
- **Failure space**: What [[Boundaries|boundary]] can fail independently?

None of these automatically mean “the business transition committed” unless the Observer’s application semantics define that [[Boundaries|boundary]].

## Runtime

[[Realization]] is the relation by which semantic dynamics, system structure, and operational semantics are made concrete in a substrate. Realization is layered: a substrate at one layer can itself be modeled as semantic structure realized by lower-level substrate. [[Runtimes|Runtime]] is part of the realization substrate. An [[Actor Systems|actor system]], ASP.NET host, [[Workflow Engines|workflow engine]], [[Durable Execution Engines|durable execution engine]], [[Brokers|broker]], or database can realize operational semantics, but the semantics should be described separately from any specific runtime.

Different runtimes realize Observers differently (e.g., actor placement and supervision vs. HTTP request pipeline), while the semantic model (Observer, Entity, Observation, Event, Command, Query) remains consistent. In async, fiber, or green-thread runtimes, the Observer follows the logical execution context rather than a fixed OS thread.

## Cohesive Role

Cohesive preserves correspondence across realms:

```txt  
Semantic dynamics (State, Observation, Event, Observer, Entity, Command, Query, ...)
  -> System structure (Entity Models, Observers, Relations, Projections, Flows, Boundaries, ...)
  -> Operational semantics (Persistence, Reconstitution, Interaction, Delivery, Coordination, Durable Execution, Control)  
  -> Realization substrate (Realization, Compute, Runtimes, Network, Storage, Workflow engines, Durable execution engines, Actor systems, ...)
```

It lets a domain be modeled in terms of entities, observers, states, observations, events, commands, queries, relations, and flows, then projects those primitives into operational systems running on existing infrastructure while maintaining semantic fidelity across layers and across different Observers.

[[Architecture Practices]] contextualize named industry patterns and methodologies as cross-realm bundles of problems, constraints, and realization choices expressible in Cohesive terms.
