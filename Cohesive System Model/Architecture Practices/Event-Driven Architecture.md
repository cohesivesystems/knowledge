---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-08-23
---

# Event-Driven Architecture

Event-Driven Architecture addresses the problem of coordinating independent participants through event flow rather than direct synchronous control.

## Cohesive Formulation

The practice is about [[Flow Views|flow views]] between [[Observer|observers]] through [[Event|events]]. Its central Cohesive questions are:

- Which observer emitted the event?
- Is the event endogenous, output, exogenous, or input relative to each boundary?
- Where is the reported fact authoritative?
- Is the publication authoritative history, a state transfer or delta, or a notification hint?
- What does delivery guarantee?
- What observer dependency is being satisfied, and what postcondition proves [[Semantic Propagation|semantic propagation]]?
- How can an observer recover after missing a publication?
- What state, projection model, process graph, or transition is affected by observing the event?

## In the Model

Events decouple producers and consumers only when boundaries and meanings are explicit. One observer's endogenous event may become another observer's exogenous event. A receiving observer still interprets the event relative to its state, policies, authority, and boundary.

Event occurrence, notification emission, message delivery, receiver processing, and semantic propagation are separate claims. A durable event stream may be the authoritative history an observer must follow. In another design, authoritative state exists elsewhere and publication only prompts the observer to resynchronize. The architecture should declare which relationship applies rather than making the notification channel part of the domain fact by accident.

Adopting event flow also creates the capacity, failure, retention, replay, topology, evolution, and observability obligations described by [[Asynchronous Interaction Design|asynchronous interaction design]]. Those obligations apply to the operational edge even when its broker reports no errors.

## Failure Modes

The pattern fails when event schemas are treated as shared semantics, when broker delivery is mistaken for domain commitment, when successful publication or delivery is presented as proof that semantic consequences propagated, or when downstream consumers assume ordering, durability, causality, authority, or recoverability that the event flow does not guarantee.

Related concepts: [[Event|event]], [[Observer|observer]], [[Observer Models|observer models]], [[Flow Views|flow views]], [[Interaction|interaction]], [[Asynchronous Interaction Design|asynchronous interaction design]], [[Delivery Semantics|delivery semantics]], [[Semantic Propagation|semantic propagation]], [[Ordering|ordering]], [[Brokers|brokers]], [[Trace and Feedback|trace and feedback]], [[Event-State Duality|event-state duality]].
