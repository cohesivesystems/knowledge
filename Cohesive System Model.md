---
kind: overview
created: 2026-06-24
updated: 2026-08-17
---

# Cohesive System Model

## Vision

Cohesive has two linked goals:

- Establish a standard language for describing systems.
- Build a family of compiler-like realizations that lower that language into working infrastructure while preserving meaning.

The Markdown graph is the public source of truth for that language. It should make Cohesive building blocks traceable to well-defined concepts, and it should make important concepts precise enough to guide realization.

The model is inspired by [[Categorical Principles|categorical principles]], including the Lawvere tradition of using category theory to organize mathematical knowledge. The practical test, however, is executable systems: semantic descriptions should be reconcilable with actors, transactions, logs, brokers, workflows, storage systems, networks, runtimes, and other infrastructure through explicit [[Realization|realization]] relations.

See [[System Language and Realization|system language and realization]] for the broader vision and [[Process Theories|process theories]] for the first guiding principle under active refinement.

## Core Thesis

Domains can be described as cohesive system graphs composed from semantic constructs and arranged as:

- [[Entity Models|Entity models]] with stable [[Identity|identities]] and [[Transition Models|transition models]]
- [[Relation Models|Relation models]] over semantic [[Relation|relations]]
- [[State|States]], [[Value|values]], [[Transition|transitions]], and [[Event|events]]
- [[Observer Models|Observer models]] for active participants
- [[Command|Commands]] and [[Query|queries]] as observer-relative interpretations
- [[Process Graphs|Process graphs]] that compose processes, participants, decisions, and [[Effect|effects]] over time

Cohesive arranges interactions among these primitives through its system graph and qualifies that structure with operational concerns, including [[Delivery Semantics|delivery semantics]] and [[Commit Boundaries|commit boundaries]]. [[Realization|Realization]] maps the structure and its property demands to concrete [[Compute|compute]], [[Runtimes|runtimes]], [[Network Channels|network channels]], [[Storage Systems|storage systems]], and [[Infrastructure|infrastructure]] while preserving meaning across layers.

## Realms of Description

### 0. Principles

Describe modeling disciplines used across the system model.

- [[System Language and Realization]]
- [[Ubiquitous Language]]
- [[Execution Kernel]]
- [[Pattern Languages and Correspondence]]
- [[Categorical Principles]]
- [[Logic]], [[Judgement|judgement]], [[Law of Excluded Middle|law of excluded middle]], [[Type Theory|type theory]], [[Curry–Howard Correspondence|Curry–Howard correspondence]], [[Lambda Calculus|lambda calculus]], [[Substitution|substitution]], [[Linear Logic|linear logic]], [[Temporal Logic|temporal logic]]
- [[Programming Paradigms]], [[Functional Programming|functional programming]], [[Relational and Logic Programming|relational and logic programming]]
- [[Process Theories]], [[Process Calculi|process calculi]], [[Session Types|session types]]
- [[Service]]
- [[Control Flow]]
- [[Control Theory]]
- [[Queueing Theory]]
- [[Stuff Structure Property]]
- [[Compositionality]]
- [[Nondeterminism and Choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]]
- [[CALM Theorem]]
- [[Asynchronous Computability Theorem]]
- [[Glitch Principle]]
- [[Functoriality]]
- [[Naturality]]
- [[Duality and Symmetry]], [[Event-State Duality|event-state duality]], [[Synchrony and Asynchrony|synchrony and asynchrony]]
- [[Universal Constructions]]
- [[Equivalence vs Equality]]
- [[Concurrency]], [[Happened-Before|happened-before]]
- [[Quorum Intersection]]
- [[Monads Monoids and Duals]], [[Algebras and Coalgebras|algebras and coalgebras]], [[State Machines|state machines]], [[Yoneda Lemma|Yoneda lemma]], [[Adjunctions|adjunctions]]
- [[Fibrations and Indexed Structure]], [[Sheaves and Gluing|sheaves and gluing]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Database Sheaf Semantics|database sheaf semantics]], [[Recursion|recursion]], [[Fixed Points|fixed points]], [[Enrichment and Order|enrichment and order]], [[Optics and Lenses|optics and lenses]], [[Trace and Feedback|trace and feedback]]

### 1. Domain Semantics

Defines the meaning-bearing constructs used to describe domain state, events, effects,
values, observation, identity, behavior, processes, interactions, and transitions before
assigning operational guarantees or realization mechanisms.

- [[Domain]]
- [[Subdomain]]
- [[State]]  
- [[Value]]
- [[Shape]]
- [[Observable]]  
- [[Observation]]  
- [[Event]]  
- [[Effect]]
- [[Behavior]]  
- [[Process]]
- [[Interaction]]
- [[Observer]]
- [[Agent]]
- [[Entity]]  
- [[Relation]]
- [[Invariant]]
- [[Policy]]
- [[Command]]  
- [[Query]]
- [[Transition]]  
- [[Time]]  
- [[Identity]]  
- [[Version]]
- [[Authority]]
- [[Causality]]
- [[Uncertainty]]

### 2. Operational Concerns

Describes the properties required for domain semantics and system-graph structure to be made executable and reliable.

- [[Persistence]]  
- [[Durability]]
- [[Reconstitution]]  
- [[Delivery Semantics|Delivery semantics]]  
- [[Acknowledgments]]
- [[Commit Boundaries]]
- [[Coordination]]  
- [[Consensus]]
- [[Scheduling]], [[Parallelism|parallelism]], [[Fairness|fairness]], [[Arbitration|arbitration]]
- [[Scalability]], [[Locality|locality]], [[Partitioning|partitioning]]
- [[Safety and Liveness]], [[Progress Conditions|progress conditions]], [[Failure Models|failure models]], [[Fallacies of Distributed Computing|fallacies of distributed computing]], [[Deadlock and Livelock|deadlock and livelock]], [[CAP Theorem|CAP theorem]], [[Metastability|metastability]]
- [[Concurrency Control|Concurrency control]]
- [[Isolation]]
- [[ACID]], [[Two-Phase Commit|two-phase commit]]
- [[Distributed Failure Scenarios|Distributed failure scenarios]], [[Dual-Write Problem|dual-write problem]]
- [[Version Histories]]
- [[Consistency Models]]  
- [[Consistent Cuts]], [[Linearization Points|linearization points]]
- [[CRDTs]]
- [[Retry]], [[Rate Limiting|rate limiting]], [[Flow Control|flow control]], [[Load Balancing|load balancing]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Recovery|recovery]]
- [[Correlation and Conversations]], [[Consumer Coordination|consumer coordination]], [[Interaction Control Flow|interaction control flow]], [[Delivery Progress and Settlement|delivery progress and settlement]]
- [[Compatibility and Evolution]]
- [[Temporal Completeness]]
- [[Retention Expiration and Quarantine|Retention, expiration, and quarantine]]
- [[Service Levels]], [[Operational Control|operational control]], [[Observability and Provenance|observability and provenance]]

### 3. System Graph

Organizes domain semantics into a cohesive system graph. The system graph describes placement, composition, ownership, boundaries, dependencies, graph shape, and public substrate-facing projections; it is distinct from primitive semantic definitions, operational guarantees, and concrete realization substrate.

- [[System Graph]]
- [[System Composition Algebra]]
- [[Entity Models]]
- [[Transition Models]]
- [[Observer Models]]
- [[Control Models]]
- [[Relation Models]]
- [[Projection Models]]
- [[Replica Models]]
- [[Partition Models]]
- [[Process Graphs]], [[Fork and Join|fork and join]]
- [[Effect Models]]
- [[Flow Views]] as movement views within or between process graphs
- [[Service Models]], [[Surfaces|surfaces]], [[Interfaces|interfaces]], [[Interaction Modes|interaction modes]], [[Interaction Protocols|interaction protocols]]
- [[Interaction Bindings|Interaction bindings]], [[Endpoints|endpoints]]
- [[Messages and Envelopes]], [[Interaction Channels|interaction channels]]
- [[Routing Models]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Flow Operators|flow operators]]
- [[Business Transactions]]
- [[Policy Scopes]]
- [[Invariant Scopes]]
- [[Boundaries]]
- [[Bounded Context]]
- [[Infrastructure Graph]]

### 4. Realization Substrate

Provides concrete mechanisms.

- [[Realization]]
- [[Compute]]
- [[Scaling Mechanisms|Scaling mechanisms]]
- [[Additive Increase Multiplicative Decrease|AIMD]], [[PID Control|PID control]]
- [[Runtimes]]  
- [[Application Hosts|Application hosts]]  
- [[Network]], [[Network Channels|network channels]]
- [[Storage Systems|Storage systems]], [[Database Transactions|database transactions]]
- [[Write-Ahead Logging]]
- [[Consensus Protocols]]
- [[Event Sourcing]]
- [[Outbox]]
- [[CQRS]]
- [[Brokers]]  
- [[Workflow Engines|Workflow engines]]  
- [[Durable Execution Engines|Durable execution engines]]
- [[Actor Systems|Actor systems]]  
- [[TLA+]]
- [[Batch and File Exchange]]
- [[Infrastructure]]

### 5. Architecture Practices

Contextualizes named architecture practices as cross-realm bundles of problems, constraints, and realization choices.

- [[Architecture Practices]]
- [[Analysis Patterns]], [[Domain-Driven Design|domain-driven design]]
- [[Patterns of Enterprise Application Architecture]], [[Enterprise Integration Patterns|enterprise integration patterns]]
- [[Workflow Patterns]], [[Microservice Pattern Language|microservice pattern language]], [[Patterns of Distributed Systems|distributed-systems patterns]], [[Pattern-Oriented Software Architecture|POSA]], [[Reactive Manifesto|reactive manifesto]]
- [[Ports and Adapters]], [[Clean Architecture|clean architecture]], [[Modular Monolith|modular monolith]], [[Microservice Architecture|microservice architecture]], [[Event-Driven Architecture|event-driven architecture]], [[Asynchronous Interaction Design|asynchronous interaction design]], [[Capacity Planning|capacity planning]]
- [[CQRS as Architecture Practice]], [[Event Sourcing as Architecture Practice|event sourcing as architecture practice]]
- [[Orchestration and Choreography]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Durable Execution]], [[Actor Model|actor model]], [[Anti-Corruption Layer|anti-corruption layer]]
- [[Transactional Outbox]], [[Transactional Inbox|transactional inbox]], [[Weak Isolation Patterns|weak isolation patterns]], [[CRDTs as Architecture Practice|CRDTs as architecture practice]], [[Data Mesh|data mesh]]

## Domain Semantics

### State

A **[[State|state]]** is the condition or configuration of a subject within a model [[Boundaries|boundary]]. It represents what *is*, relative to a subject, boundary, [[Shape|shape]], and time or version.

State is not the same thing as the [[Value|value]] used to read, write, transmit, or compare it. State becomes usable through values and contextualized **[[Observation|observations]]** produced by [[Observable|observables]].

State does not inherently carry [[Identity|identity]], [[Version|version]], or lineage. For an [[Entity|entity]], entity state is state attributed to an [[Identity|identity]] at a [[Version|version]].

Entity business state, process coordination state, projection state, and execution material have different authorities even when stored together. A sparse observation must distinguish an unobserved path from absent, null, unknown, failed, and concrete values; a sparse patch becomes authoritative state only when committed.

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

An [[Event|event]] is a time-bearing occurrence carrying a [[Value|value]]. It marks, reports, or induces change depending on how it is interpreted by an [[Observer|observer]] relative to a [[Boundaries|boundary]].

Structurally, an event is a value with occurrence. Semantically, an event may be exogenous, input, command-bearing, query-bearing, endogenous, or output depending on the observer [[Boundaries|boundary]].

An event answers what occurred. A [[Command|command]] answers how a receiving observer interpreted an input event. An [[Effect|effect]] answers what modeled consequence or obligation a decision established. Domain events, requests, signals, and replies are distinct emission roles: a request creates an emitter-side response obligation, while an event does not.

Persistence events record reconstruction, audit, or storage mechanics. They are domain events only when the domain independently assigns them that meaning.

### Behavior

[[Behavior]] is a time-varying [[Value|value]]: a trajectory through state space. For an entity, behavior can be viewed as both an event schedule and a state history.

### Process

A [[Process|process]] is coherent work unfolding over time. It gives semantic unity to related observations, commands, queries, events, transitions, decisions, effects, artifacts, and participant activity.

A process is not defined by a workflow engine, scheduler, thread, transaction manager, application host, or broker. Those mechanisms may realize a process, execute one activation of it, or host one step of it. The semantic process is defined by its subject or correlation identity, participants, inputs, decisions, state or history, effects, completion meanings, and flows of movement between participants.

Processes compose when the outputs of one process become future inputs to another. Compositions may be pipelines, nested sub-processes, [[Concurrency|concurrent]] processes, or feedback loops.

An executable long-lived process advances through finite activations separated by quiescence or explicit durable cuts. It owns coordination state such as active tokens, waits, correlations, interaction results, compensation progress, and terminal outcome; it does not own a copied authoritative version of aggregate business state.

### Interaction

[[Interaction]] names boundary-relative participation among subjects: how observers, processes, entities, or other participants affect, observe, request, notify, answer, share state with, wait for, or synchronize with one another.

Interaction is cross-realm because no single realm fully describes it. Domain semantics identifies what the participation means; the system graph arranges participants and occurrences as compositional structure; operational concerns qualify that structure with boundary-relative property claims; and [[Realization|realization]] relates the structure and its property demands to substrate mechanisms and capability evidence. These descriptions must preserve meaning across lowering, but none substitutes for another.

Under the [[Stuff Structure Property|stuff structure property]] lens, an interaction may be structure when it relates participants and occurrences, stuff when reified as a modeled object, or the subject of properties constraining valid interaction. The aspect being described depends on the model boundary and purpose.

### Observer

An [[Observer|observer]] is a locus of interpretation: the participant, context, or execution locus relative to which values, observations, events, commands, queries, boundaries, and state acquire meaning. Every runtime participant is a potential observer, but an observer is realized only when a context supplies boundary, state view, authority, and interpretation rules.

An observer is characterized by:
- Its own **[[Identity|identity]]** (distinct from entity identities)
- Its own **[[Boundaries|boundary]]**  
- A realization context or logical execution context in which interpretation occurs
- The ability to observe observables, producing **observations** of state
- The ability to host, observe, route, or project **entities** and their **events** within its [[Boundaries|boundary]]
- The ability to receive events from other observers as **exogenous events**

Addressability is not intrinsic to the definition of an observer. A semantic [[Interaction|interaction]] can identify an intended participant or role; system-graph channels and routing models arrange the addressable path; operational concerns specify its delivery properties; and realization supplies concrete addresses and mechanisms. Some observers have globally addressable identities, such as actors. Others have transient or local identities, such as a request handler or logical execution context created for one operation.

An observer may be realized by an OS thread, logical thread, fiber, coroutine, task, actor mailbox turn, workflow activation, request handler, projection run, process step, or entity command handler. In green-thread, fiber, or async runtimes, the observer follows the logical execution context governed by a scheduler, not necessarily the OS thread.

Actor systems make observers addressable: an actor address gives other observers a delivery path to a receiving observer boundary. Entities and [[Process|processes]] can also be modeled as observers; in that model, inputs are interpreted relative to their own state, history, policies, and boundary.

Events, commands, and queries are **observer-relative interpretations**: an event that is endogenous to one observer may be exogenous to another, and the same incoming observation may be interpreted differently (or rejected) depending on the observer’s current view of entity state, [[Projection Models|projection models]], required observations, [[Invariant|invariants]], [[Policy|policies]], authority, and consistency expectations.

### Agent

An [[Agent|agent]] is an observer role whose modeled responsibility is to interpret observations and select or initiate actions in service of a purpose, objective, commitment, or obligation. Agency adds an attributable decision-and-action role governed by policies, available actions, authority, and capabilities.

Participant, observer, agent, and actor name different aspects. Participant is the broad relational role. Observer identifies where interpretation occurs. Agent identifies responsibility for selecting or initiating action. Actor identifies an addressable, message-driven execution role that may realize an observer or agent.

### Entity

An [[Entity|entity]] is an enduring, identifiable subject whose state evolves over time under controlled transitions.

An entity is defined by:
- A stable **identity** that persists across its lifetime
- A **family of entity-state observations** across time, indexed by version
- A **current state** at any point in time, attributed to identity + version
- **[[Transition|Transitions]]** that define how its state may change
- **[[Invariant|Invariants]]** and **[[Policy|policies]]** that constrain valid changes
- **[[Effect|Effects]]**, including transition effects, endogenous events, and publication, request, signal, or reply obligations established by accepted transitions

An entity is therefore state + identity + version history + transitions + invariants + policies + effects.

Entity state is a specialized observation: a shaped [[Value|value]] attributed to an entity identity at a version. It may be complete or partial only relative to a declared [[Shape|shape]], projection, transition, or [[Boundaries|boundary]]. Related entities, policies, projections, and environmental facts that affect a transition belong to the transition context, not automatically to the entity's own state.

An aggregate authority boundary may span several physical records, while independently authoritative entities require process coordination. Evaluating a transition produces a decision; only a successful commit establishes the transition effect and authoritative new state.

Identity is what allows a sequence of state observations to be understood as successive versions of *the same thing*.

An entity is not automatically an observer, but it may be modeled or realized as one when it interprets inputs relative to its own state and boundary. Correct entity transitions require the interpreting observer to remain aligned with the realization context that commits the transition: actor hosting can provide this through serialized message handling, while stateless request handlers usually require expected-version checks.

### Transition

A [[Transition|transition]] is a deterministic semantic decision relation over one subject or aggregate boundary. It consumes typed input and finite explicit observations and produces a typed outcome, sparse patch, emissions, movements, trace, and guarantee demands.

```txt
transition definition + input + observations
  -> transition decision
  -> capability-checked commit
  -> authoritative state effect and durable obligations
```

The decision does not commit state. Portable transition structure is finite and acyclic and contains no hidden I/O, waits, retries, service lookup, or arbitrary callbacks. [[Transition Models|Transition models]] arrange this structure in the system graph, and concrete interpreters and storage mechanisms realize it.

### Effect

An [[Effect|effect]] is a modeled consequence or obligation established by a semantic decision. Effect declaration, accepted responsibility, local commit, physical attempt, acknowledgment or result, and downstream interpretation are distinct boundaries.

A domain-event emission creates no response obligation. A request identifies an intended receiver and creates a typed terminal-response or terminal-failure obligation. A signal also identifies an intended receiver but creates no response obligation, and a reply discharges one admitted request. Effect handlers are impure realization adapters; they do not become semantic authority or mutate authoritative entity state directly.

### Command

A [[Command|command]] is the interpretation of an [[Event|event]] by a given [[Observer|observer]] as an attempted [[Transition|transition]] of a target subject.

Relative to the interpreting observer, the event is an exogenous input event. Relative to the emitter, the carried event is an endogenous output event. A message contract may express singular command intent toward an understood observer, making command interpretation expected and operationally unambiguous. The semantic command remains observer-relative because the receiver must admit and interpret the input in context.

```txt
Endogenous output event at an emitter boundary
  -> exogenous input event at an interpreting observer boundary
  -> attempted transition, relative to the observer and target subject
  -> validation against current entity state + required observations + invariants + policies + authority + expected version
  -> typed applied, no-change, alternate, conflict, or rejection outcome
```

Commands are not mere messages. They are interpretations made relative to:
- The specific observer
- The observer’s [[Boundaries|boundary]] and current view of state
- Authority, invariants, and policies  
- The intended transition  
- An optional expected version or ETag carried by the input event

The expected version ordinarily represents the emitter's observation of entity state when it formed its request. The receiving observer decides whether that claim is relevant and validates it before accepting the transition.

### Query

A [[Query|query]] is an observer-relative interpretation of an input event as a request to observe, compute, or return information without requesting a modeled semantic state transition.

```txt
Exogenous input event at an observer boundary
  -> query intent (relative to the observer and target subject or view)
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
- [[Projection Models|Projection]] state (derived observations)
- Derived observations

## Exogenous and Endogenous Events

Relative to an **observer’s [[Boundaries|boundary]]**:

- **Exogenous event**: An event arriving from outside the observer’s [[Boundaries|boundary]]. It may originate from another observer’s endogenous event, a runtime, a clock, a user, a sensor, or the external environment.
- **Input event**: An exogenous event in the role of entering the observer [[Boundaries|boundary]].
- **Command**: The receiving observer's interpretation of an input event as an attempted transition for a target subject.
- **Query**: The receiving observer's interpretation of an input event as a request to observe, compute, or return information without requesting a modeled semantic state transition.
- **Endogenous event**: An event that occurs or is accepted within the observer’s own semantic history.
- **Output event**: An endogenous event emitted across a [[Boundaries|boundary]].
- **Applied no-change outcome**: The input was admitted but the accepted decision changed no entity value. The outcome is not an event.

Some systems may still record audit, telemetry, or diagnostic events when interpretation yields no change or rejection. Those records are operational traces or events for another subject, not a committed domain transition for the target entity.

Interpretation flow:

```txt
Exogenous event
  -> input event
  -> command | query (observer-relative)
  -> validation or observation selection
  -> typed transition outcome | observation | value | nil query result
```

Examples of explicit no-change or alternate transition outcomes include duplicate input whose domain effect was already committed, a valid no-op against current state, and telemetry-only or correlation-only input. Failed validation and failed authority are rejections; an expected-version mismatch is a concurrency conflict.

One observer’s endogenous event may become another observer’s exogenous event.

## Commands (Expanded Flow with Versioning)

A command may carry an optional **expected version / ETag** based on the emitter's observation of entity state when it formed the request. The receiving observer interprets and validates that claim.

The entity transition interpreter, aligned with the interpreting observer, evaluates the definition against current entity state, required observations, invariants, policies, authority, and expected version. It produces a typed transition decision. A storage or runtime realization then validates the commit demands and either commits the patch and local obligations, reports a concurrency conflict, or reports another explicit failure.

## Operational Concerns

### Persistence

What is recorded as authoritative material?

- Current-state records (as entity-scoped observations)
- Event histories
- [[Outbox]] records
- [[Transactional Inbox|Inbox]] and deduplication records
- Actor state providers
- Workflow histories
- Process execution histories, checkpoints, timers, signals, and pending work
- Process state
- Projection state (derived observations)

### Durability

Which facts, histories, effects, decisions, or execution material survive which failures?

- Declare the failure boundary and fate-sharing assumptions
- Protect state, histories, decisions, timers, acknowledgments, and recovery material
- Preserve enough material for reconstitution, replay, retry, repair, or audit
- Distinguish local durability from end-to-end completion
- Bind the claim to explicit storage, replication, log, queue, acknowledgment, or commit boundaries

### Reconstitution

How is usable state recovered?

- Load latest record → produce an observation
- Replay events → fold into a current state sample
- Load snapshot + events
- Reconstitute process execution state, checkpoints, or workflow history
- Activate actor by identity
- Rebuild projection as a derived observation

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
- [[Durable Execution|Durable execution]] practice with resume
- Choreography through events  
- Process manager  
- Projection update protocol

### Control

What constrains execution?

- Optimistic concurrency (via expected version)  
- Pessimistic locking / fencing tokens  
- Actor identity serialization  
- Retries, [[Rate Limiting|rate limiting]], and [[Flow Control|flow control and backpressure]]
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

[[Realization]] is the relation by which domain semantics, system graph, operational concerns, and architecture practices are made concrete in a substrate. Realization is layered: a substrate at one layer can itself be modeled as semantic structure realized by lower-level substrate. [[Runtimes|Runtime]] is part of the realization substrate. An [[Actor Systems|actor system]], ASP.NET host, [[Workflow Engines|workflow engine]], [[Durable Execution Engines|durable execution engine]], [[Brokers|broker]], or database can realize operational concerns and architecture practices, but those concerns and practices should be described separately from any specific runtime.

Different runtimes realize observers differently (e.g., actor placement and supervision vs. HTTP request pipeline), while the semantic model (observer, entity, observation, event, command, query) remains consistent. In async, fiber, or green-thread runtimes, the observer follows the logical execution context rather than a fixed OS thread.

## Cohesive Role

Cohesive preserves correspondence across realms:

```txt  
Semantic description (State, Observation, Event, Observer, Entity, Process, Interaction, Relation, Command, Query, ...)
  -> System graph (Entity Models, Observer Models, Relation Models, Projection Models, Process Graphs, Flow Views, Interaction Channels, Boundaries, Infrastructure Graph, ...)
  -> Operational concerns (Persistence, Durability, Reconstitution, Delivery, Acknowledgment, Ordering, Coordination, Recovery, Control)
  -> Realization substrate (Realization, Compute, Runtimes, Network, Storage, Workflow engines, Durable execution engines, Actor systems, ...)
```

It lets a domain be modeled in terms of entities, observers, states, observations, events, commands, queries, relations, interactions, and processes, arranges them in a system graph, and realizes them as operational systems running on existing infrastructure while maintaining fidelity across layers and across different observers.

[[Architecture Practices]] contextualize named industry patterns and methodologies as cross-realm bundles of problems, constraints, and realization choices expressible in Cohesive terms.
