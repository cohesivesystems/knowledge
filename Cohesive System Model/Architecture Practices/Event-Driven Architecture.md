---
realm: Architecture Practices
---

# Event-Driven Architecture

Realm: Architecture Practices

Event-Driven Architecture addresses the problem of coordinating independent participants through event flow rather than direct synchronous control.

## Cohesive Formulation

The practice is about [[Flows]] between [[Observer|observers]] through [[Event|events]]. Its central Cohesive questions are:

- Which observer emitted the event?
- Is the event endogenous, output, exogenous, or input relative to each boundary?
- What does delivery guarantee?
- What state, projection, process, or transition is affected by observing the event?

## Practice Interpretation

Events decouple producers and consumers only when boundaries and meanings are explicit. One observer's endogenous event may become another observer's exogenous event. A receiving observer still interprets the event relative to its state, policies, authority, and boundary.

## Failure Modes

The pattern fails when event schemas are treated as shared semantics, when broker delivery is mistaken for domain commitment, or when downstream consumers assume ordering, durability, or causality that the event flow does not guarantee.

Related concepts: [[Event]], [[Observer]], [[Flows]], [[Interaction]], [[Delivery Semantics]], [[Ordering]], [[Brokers]], [[Trace and Feedback]], [[Event-State Duality]].
