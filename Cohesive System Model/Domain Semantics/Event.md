---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-27
---

# Event

An event is a time-bearing occurrence carrying a [[Value|value]]. It marks, reports, or induces change depending on how it is interpreted by an [[Observer|observer]] relative to a [[Boundaries|boundary]].

Structurally, an event is a value with a notion of occurrence. Semantically, an event's role is observer and boundary relative. An event answers what occurred; it does not by itself determine what another observer should do or whether an emitter expects a response.

Message ingress at a receiving boundary is an exogenous event carrying a value. Message egress is an endogenous event at the emitting boundary. A message contract may strongly indicate how its value is intended to be interpreted, but transport classification and semantic interpretation remain distinct.

An incoming event becomes a [[Command|command]] when an observer interprets it as an attempted [[Transition|transition]]. A request, signal, or reply is instead a distinct emission and interaction role. A request establishes an emitter-side response obligation; an event does not. These roles may use similar payloads or the same transport without becoming the same semantic construct.

A publication presented as an event is therefore not a domain-event emission when its emitter must receive a correlated terminal result before its own process can continue. It participates in an [[Interaction|implicit request protocol]], even when dispatch and response are asynchronous.

## Common Uses of Event

The word event is used for several related but distinct concepts:

- **Domain events** are events relevant inside a domain boundary, such as `OrderPlaced`, `PaymentCaptured`, or `ShipmentDispatched`. They may be used as [[Event Sourcing|event-sourcing]] events, persisted in a [[Transactional Outbox|transactional outbox]], or published best-effort after a state change. In Cohesive terms, a domain event is endogenous relative to the domain boundary in which it occurs or is accepted.
- **Event-sourcing events** are committed persistence events interpreted as state actions and used as authoritative history for an [[Entity|entity]]. They can be folded or replayed into [[State|state]]. An event-sourcing event is also a domain event only when its meaning records a domain-relevant fact rather than merely reconstruction, audit, or storage mechanics.
- **Telemetry or metric events** are system events about application behavior, runtime behavior, measurements, traces, or logs. They often have softer persistence guarantees and narrower retention windows. They may be exogenous to a domain model while endogenous to the observability system that records or aggregates them.
- **External events** are observations of a process outside the observer's boundary. They arrive as exogenous events and may be interpreted as [[Command|commands]], [[Query|queries]], or ignored inputs. A command interpretation may then lead to an accepted endogenous event, state change, or committed event record depending on the realization.
- **Persistence events** record state reconstruction, audit, or storage mechanics. They may be committed and occurrence-bearing without automatically being domain events or outbound publications.
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
- An **applied no-change outcome** records that the input was admitted but the accepted decision changed no entity value. The outcome is not itself an event.

The same carried occurrence may therefore be an output event for one observer, an exogenous input event for another, and a command or query only after interpretation by the receiving observer relative to its boundary, current state, policies, authority, and target subject. At a lower operational layer, emitting, persisting, publishing, admitting, receiving, acknowledging, and processing the carried event are distinct local occurrences.

## Decisions, State Actions, and Commitment

Evaluating an entity transition produces a decision; it does not commit state or establish that every declared emission has occurred. An accepted commit has a transition [[Effect|effect]]: entity state advances according to its versioning rule, and the occurrence of that state evolution is an endogenous event. The decision and commit boundaries can be summarized as:

$$
\begin{align}
\mathrm{decide}&\colon\mathrm{Definition}\times\mathrm{Input}\times\mathrm{Observation}\times\mathrm{Context}
\to\mathrm{Decision}
\\
\mathrm{commit}&\colon\mathrm{state}_v\times\mathrm{AcceptedDecision}
\to\mathrm{state}_{v'}\times\mathrm{CommittedEffects}
\end{align}
$$

In [[Event Sourcing|event-sourced]] semantics, committed persistence events become state actions when interpreted through the entity's apply relation. A transition decision may declare domain-event emissions as well as persistence actions, but an uncommitted declaration is not yet committed entity history or a successfully externalized event.

Only committed persistence events become part of the event-sourced state history. Attempted inputs, rejected commands, retries, telemetry, no-change outcomes, and uncommitted emissions may be recorded elsewhere, but they are not state actions for the target entity unless committed inside that entity boundary.

Commitment is a modality, not 'event-ness' itself. An event may be ephemeral, delivered through a broker, recorded in a log, retained as telemetry, persisted in an outbox, or committed as authoritative entity history. Each claim is scoped to a boundary and persistence mechanism.

Events participate in [[Event-State Duality|event-state duality]]:

- Events can be folded or integrated into current [[State|state]].
- State histories can be compared to derive deltas that an observer may interpret as events.
- Event streams can form [[Behavior|behavior]], and behavior can be sampled or detected as events.

## External References

- Cloud Native Computing Foundation, [CloudEvents Specification](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md) and [CloudEvents Primer](https://github.com/cloudevents/spec/blob/main/cloudevents/primer.md).
- Gregor Hohpe and Bobby Woolf, [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html), *Enterprise Integration Patterns*, 2003.
- Martin Fowler, [What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html), 2017.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Value|value]], [[Shape|shape]], [[Observation|observation]], [[State|state]], [[Event-State Duality|event-state duality]], [[Behavior|behavior]], [[Observer|observer]], [[Boundaries|boundaries]], [[Command|command]], [[Query|query]], [[Transition|transition]], [[Version|version]], [[Effect|effect]], [[Effects]], [[Messages and Envelopes|messages and envelopes]], [[Interaction|interaction]], [[Event Sourcing|event sourcing]].
