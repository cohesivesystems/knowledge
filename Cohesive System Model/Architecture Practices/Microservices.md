---
realm: Architecture Practices
---

# Microservices

Realm: Architecture Practices

Microservices address the problem of independent ownership, deployment, scaling, and evolution across bounded capabilities.

## Cohesive Formulation

A microservice is not just a process or network endpoint. It is a realization of a service boundary with its own observers, interaction edges, persistence choices, failure modes, and operational semantics.

The practice asks:

- What boundary does the service own?
- Which entities, processes, policies, and projections are inside it?
- Which events and commands cross the boundary?
- What delivery, ordering, recovery, and consistency semantics apply?

## Practice Interpretation

Microservices turn semantic and structural boundaries into deployment and operational boundaries. That can increase autonomy, but it also turns local composition problems into distributed coordination, delivery, and recovery problems.

## Failure Modes

The pattern fails when services are split by technical layer, table, team preference, or endpoint count rather than semantic ownership and operational boundary. Distributed deployment does not create bounded context clarity by itself.

Related concepts: [[Boundaries]], [[Observer]], [[Interaction]], [[Delivery Semantics]], [[Coordination]], [[Recovery]], [[Brokers]], [[Network]], [[Modular Monolith]].
