---
realm: Semantic Dynamics
kind: semantic-construct
---

# Event

An Event is a time-bearing occurrence with a [[Value|value]]. It marks, reports, or induces change depending on how it is interpreted by an [[Observer]] relative to a [[Boundaries|boundary]].

Structurally, an event is a [[Value|value]] with a notion of occurrence. Semantically, an event's role is observer and boundary relative.

## Common Uses of Event

The word event is used for several related but distinct concepts:

- **Domain events** are events relevant inside a domain boundary, such as `OrderPlaced`, `PaymentCaptured`, or `ShipmentDispatched`. They may be used as [[Event Sourcing|event-sourcing]] events, persisted in a [[Transactional Outbox|transactional outbox]], or published best-effort after a state change. In Cohesive terms, a domain event is endogenous relative to the domain boundary in which it is committed.
- **Event-sourcing events** are domain events interpreted as state actions and committed as the authoritative history for an [[Entity]]. They carry both the event-action aspect and the committed modality: they advance [[Version|version]] and can be folded or replayed into [[State]].
- **Telemetry or metric events** are system events about application behavior, runtime behavior, measurements, traces, or logs. They often have softer persistence guarantees and narrower retention windows. They may be exogenous to a domain model while endogenous to the observability system that records or aggregates them.
- **External events** are observations of a process outside the observer's boundary. They arrive as exogenous events and may be interpreted as [[Command|commands]], [[Query|queries]], or ignored inputs. A command interpretation may then lead to a committed endogenous event.
- **Machine events** are occurrences in a [[Runtimes|runtime]], host, operating system, orchestrator, or infrastructure boundary, such as restart, out-of-memory termination, timeout, placement change, or network partition. They are usually exogenous to an application or domain observer, while endogenous to the machine or infrastructure boundary that emits them.

These names are not mutually exclusive, and they are not intrinsic types of event. Endogenous, exogenous, input, and output are roles assigned relative to an [[Observer]] and [[Boundaries|boundary]].

## Boundary Roles

Relative to an [[Observer]]'s [[Boundaries|boundary]]:

- An **exogenous** event arrives from outside the observer [[Boundaries|boundary]].
- An **input event** is an exogenous event in the role of entering a system or observer.
- A [[Command|command]] is an input event interpreted as an attempted [[Transition]] for a target subject.
- A [[Query|query]] is an input event or incoming value interpreted as a request to observe, compute, or return information.
- An **endogenous** event is committed within the observer's own semantic history.
- An **output event** is an endogenous event emitted across a [[Boundaries|boundary]].
- A **nil** endogenous event is the modeled absence of a committed domain transition after the observer interpreted the input.

The same occurrence may therefore be an output event for one system, an exogenous input event for another, and a command or query only after interpretation by an observer relative to that system's boundary, current state, policies, authority, and target subject.

## State Actions and Commitment

An event becomes a state action only when an observer interprets it through a transition or apply relation for a subject. In [[Event Sourcing|event-sourced]] semantics, the relevant events are committed endogenous events:

$$
\begin{align}
\mathrm{decide}&\colon\mathrm{State}_v\times\mathrm{Input}\times\mathrm{Context}\to\mathrm{Endogenous Event}_v\lor\mathrm{nil}\lor\mathrm{Rejection}
\\
\mathrm{apply}&\colon\mathrm{State}_v\times\mathrm{Endogenous Event}_v
\to\mathrm{State}_{v+1}
\end{align}
$$

Only committed endogenous events advance entity version and become part of the event-sourced state history. Attempted inputs, rejected commands, retries, telemetry, and nil outcomes may be recorded elsewhere, but they are not state actions for the target entity unless committed inside that entity boundary.

Commitment is a modality, not 'event-ness' itself. An event may be ephemeral, delivered through a broker, recorded in a log, retained as telemetry, persisted in an outbox, or committed as authoritative entity history. Each claim is scoped to a boundary and persistence mechanism.

Events participate in [[Event-State Duality]]:

- Events can be folded or integrated into current [[State]].
- State histories can be compared to derive deltas that an observer may interpret as events.
- Event streams can form [[Behavior]], and behavior can be sampled or detected as events.

Related concepts: [[Value]], [[Shape]], [[Observation]], [[State]], [[Event-State Duality]], [[Behavior]], [[Observer]], [[Boundaries]], [[Command]], [[Query]], [[Transition]], [[Version]], [[Event Sourcing]].
