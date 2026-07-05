---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-07-05
---

# Event-Driven Architecture

Event-Driven Architecture addresses the problem of coordinating independent participants through event flow rather than direct synchronous control.

## Cohesive Formulation

The practice is about [[Flow Views|flow views]] between [[Observer|observers]] through [[Event|events]]. Its central Cohesive questions are:

- Which observer emitted the event?
- Is the event endogenous, output, exogenous, or input relative to each boundary?
- What does delivery guarantee?
- What state, projection model, process graph, or transition is affected by observing the event?

## In the Model

Events decouple producers and consumers only when boundaries and meanings are explicit. One observer's endogenous event may become another observer's exogenous event. A receiving observer still interprets the event relative to its state, policies, authority, and boundary.

## Failure Modes

The pattern fails when event schemas are treated as shared semantics, when broker delivery is mistaken for domain commitment, or when downstream consumers assume ordering, durability, or causality that the event flow does not guarantee.

Related concepts: [[Event|event]], [[Observer|observer]], [[Flow Views|flow views]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Brokers|brokers]], [[Trace and Feedback|trace and feedback]], [[Event-State Duality|event-state duality]].
