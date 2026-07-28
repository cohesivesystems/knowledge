---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-18
---

# Event

An event is a time-bearing occurrence carrying a [[Value|value]]. It marks, reports, or induces change depending on how it is interpreted by an [[Observer|observer]] relative to a [[Boundaries|boundary]].

Structurally, an event is a value with a notion of occurrence. Semantically, an event's role is observer and boundary relative. An event answers what occurred; it does not by itself determine what another observer should do or whether an emitter expects a response.

An incoming event becomes a [[Command|command]] only when an observer interprets it as an attempted [[Transition|transition]]. An outgoing event participates in a [[Effects|request effect]] only when its emitter establishes a modeled continuation that expects a later response. Command and request are therefore interpretation and interaction roles, not intrinsic event types.

## Common Uses of Event

The word event is used for several related but distinct concepts:

- **Domain events** are events relevant inside a domain boundary, such as `OrderPlaced`, `PaymentCaptured`, or `ShipmentDispatched`. They may be used as [[Event Sourcing|event-sourcing]] events, persisted in a [[Transactional Outbox|transactional outbox]], or published best-effort after a state change. In Cohesive terms, a domain event is endogenous relative to the domain boundary in which it occurs or is accepted.
- **Event-sourcing events** are domain events interpreted as state actions and committed as the authoritative history for an [[Entity|entity]]. They carry both the event-action aspect and the committed modality: they advance [[Version|version]] and can be folded or replayed into [[State|state]].
- **Telemetry or metric events** are system events about application behavior, runtime behavior, measurements, traces, or logs. They often have softer persistence guarantees and narrower retention windows. They may be exogenous to a domain model while endogenous to the observability system that records or aggregates them.
- **External events** are observations of a process outside the observer's boundary. They arrive as exogenous events and may be interpreted as [[Command|commands]], [[Query|queries]], or ignored inputs. A command interpretation may then lead to an accepted endogenous event, state change, or committed event record depending on the realization.
- **Request-bearing events** are output events emitted as part of a request effect. Their emitter expects a later response, but the response may be asynchronous, correlated through another channel, or observed indirectly through shared state. The receiver still determines whether to interpret the input as a command, query, negotiation, subscription, or another semantic role.
- **Machine events** are occurrences in a [[Runtimes|runtime]], host, operating system, orchestrator, or infrastructure boundary, such as restart, out-of-memory termination, timeout, placement change, or network partition. They are usually exogenous to an application or domain observer, while endogenous to the machine or infrastructure boundary that emits them.

These names are not mutually exclusive, and they are not intrinsic types of event. Endogenous, exogenous, input, and output are roles assigned relative to an [[Observer|observer]] and [[Boundaries|boundary]].

## Boundary Roles

Relative to an [[Observer|observer]]'s [[Boundaries|boundary]]:

- An **exogenous** event arrives from outside the observer [[Boundaries|boundary]].
- An **input event** is an exogenous event in the role of entering a system or observer.
- A [[Command|command]] is the interpretation of an input event as an attempted [[Transition|transition]] for a target subject.
- A [[Query|query]] is an input event interpreted as a request to observe, compute, or return information.
- An **endogenous** event occurs or is accepted within the observer's own semantic history.
- An **output event** is an endogenous event emitted across a [[Boundaries|boundary]].
- A **nil outcome** is the modeled absence of an accepted endogenous transition event after the observer interpreted the input. Nil is not itself an event.

The same carried occurrence may therefore be an output event for one observer, an exogenous input event for another, and a command or query only after interpretation by the receiving observer relative to its boundary, current state, policies, authority, and target subject. At a lower operational layer, emitting, persisting, publishing, admitting, receiving, acknowledging, and processing the carried event are distinct local occurrences.

## State Actions and Commitment

An accepted entity transition has a transition effect: entity state advances to a new [[Version|version]]. The occurrence of that state evolution is an endogenous event. In [[Event Sourcing|event-sourced]] semantics, this event becomes a state action when it is committed as authoritative entity history and interpreted through the entity's apply relation:

$$
\begin{align}
\mathrm{decide}&\colon\mathrm{state}_v\times\mathrm{Input}\times\mathrm{Context}\to\mathrm{Endogenous event}_v\lor\mathrm{nil}\lor\mathrm{Rejection}
\\
\mathrm{apply}&\colon\mathrm{state}_v\times\mathrm{Endogenous event}_v
\to\mathrm{state}_{v+1}
\end{align}
$$

Only committed endogenous transition events become part of the event-sourced state history. Attempted inputs, rejected commands, retries, telemetry, and nil outcomes may be recorded elsewhere, but they are not state actions for the target entity unless committed inside that entity boundary.

Commitment is a modality, not 'event-ness' itself. An event may be ephemeral, delivered through a broker, recorded in a log, retained as telemetry, persisted in an outbox, or committed as authoritative entity history. Each claim is scoped to a boundary and persistence mechanism.

Events participate in [[Event-State Duality|event-state duality]]:

- Events can be folded or integrated into current [[State|state]].
- State histories can be compared to derive deltas that an observer may interpret as events.
- Event streams can form [[Behavior|behavior]], and behavior can be sampled or detected as events.

Related concepts: [[Value|value]], [[Shape|shape]], [[Observation|observation]], [[State|state]], [[Event-State Duality|event-state duality]], [[Behavior|behavior]], [[Observer|observer]], [[Boundaries|boundaries]], [[Command|command]], [[Query|query]], [[Transition|transition]], [[Version|version]], [[Effects|effects]], [[Interaction|interaction]], [[Event Sourcing|event sourcing]].
