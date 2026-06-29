---
realm: Architecture Practices
kind: reference
---

# Architecture Practices

Architecture practices are named bundles of modeling choices, constraints, and implementation habits that address recurring system-engineering problems.

In the Cohesive System Model, these practices are not primitives. They are ways of arranging semantic dynamics, system structure, operational semantics, and realization substrate to solve particular problems.

Cohesive provides language for expressing the problem each practice addresses, and a compiler-like discipline for projecting that expression into structures, operations, and realizations while preserving meaning.

For each practice, ask:

- What system-engineering problem is it trying to solve?
- Which Cohesive concepts express that problem directly?
- Which boundaries, observers, entities, transitions, flows, and realizations does it introduce or constrain?
- Which guarantees does it require, and at which boundary?
- Which failure modes occur when the practice is treated as a slogan rather than a model?

Some well-known patterns & practices:

- [[Domain-Driven Design]]
- [[Ports and Adapters]]
- [[Clean Architecture]]
- [[Modular Monolith]]
- [[Microservices]]
- [[Event-Driven Architecture]]
- [[CQRS as Architecture Practice]]
- [[Event Sourcing as Architecture Practice]]
- [[Sagas and Process Managers]]
- [[Actor Model]]
- [[Anti-Corruption Layer]]
- [[Transactional Outbox]]
- [[Weak Isolation Patterns as Architecture Practice]]
- [[CRDTs as Architecture Practice]]
- [[Data Mesh]]

Related concepts: [[Categorical Principles]], [[Stuff Structure Property]], [[Boundaries]], [[Observer]], [[Entity]], [[Transition]], [[Persistence]], [[Reconstitution]], [[Realization]].
