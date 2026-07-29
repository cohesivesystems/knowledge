---
realm: Architecture Practices
kind: reference
created: 2026-06-24
updated: 2026-07-29
---

# Architecture Practices

Architecture practices are named bundles of modeling choices, constraints, and implementation habits that address recurring system-engineering problems.

In the Cohesive System Model, these practices are not primitives. They are ways of arranging domain semantics, system graph, operational concerns, and realization substrate to solve particular problems.

Cohesive provides language for expressing the problem each practice addresses, and a compiler-like discipline for projecting that expression into structures, operations, and realizations while preserving meaning. See [[System Language and Realization|system language and realization]] for the broader vision.

[[Pattern Languages and Correspondence|Pattern languages and correspondence]] provides a reusable realm profile for reconciling external catalogs with these practices and with the semantic, structural, operational, and realization concepts they bundle.

For each practice, ask:

- What system-engineering problem is it trying to solve?
- Which Cohesive concepts express that problem directly?
- Which boundaries, observers, entities, transitions, flows, and realizations does it introduce or constrain?
- Which guarantees does it require, and at which boundary?
- Which failure modes occur when the practice is treated as a slogan rather than a model?

Some well-known patterns & practices:

- [[Analysis Patterns]]
- [[Patterns of Enterprise Application Architecture]]
- [[Enterprise Integration Patterns]]
- [[Workflow Patterns]]
- [[Microservice Pattern Language]]
- [[Patterns of Distributed Systems]]
- [[Pattern-Oriented Software Architecture]]
- [[Domain-Driven Design]]
- [[Ports and Adapters]]
- [[Clean Architecture]]
- [[Modular Monolith]]
- [[Microservice Architecture]]
- [[Event-Driven Architecture]]
- [[Asynchronous Interaction Design]]
- [[Capacity Planning]]
- [[CQRS as Architecture Practice]]
- [[Event Sourcing as Architecture Practice]]
- [[Orchestration and Choreography]]
- [[Process Managers]]
- [[Sagas]]
- [[Durable Execution]]
- [[Actor Model]]
- [[Anti-Corruption Layer]]
- [[Transactional Outbox]]
- [[Transactional Inbox]]
- [[Weak Isolation Patterns]]
- [[CRDTs as Architecture Practice]]
- [[Data Mesh]]

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Analysis Patterns|analysis patterns]], [[Patterns of Enterprise Application Architecture|enterprise application patterns]], [[Enterprise Integration Patterns|enterprise integration patterns]], [[Workflow Patterns|workflow patterns]], [[Microservice Pattern Language|microservice pattern language]], [[Patterns of Distributed Systems|distributed-systems patterns]], [[Pattern-Oriented Software Architecture|POSA]], [[Capacity Planning|capacity planning]], [[System Language and Realization|system language and realization]], [[Categorical Principles|categorical principles]], [[Process Theories|process theories]], [[Stuff Structure Property|stuff structure property]], [[Boundaries|boundaries]], [[Observer|observer]], [[Entity|entity]], [[Transition|transition]], [[Persistence|persistence]], [[Durability|durability]], [[Reconstitution|reconstitution]], [[Effects|effects]], [[Commit Boundaries|commit boundaries]], [[Realization|realization]].
