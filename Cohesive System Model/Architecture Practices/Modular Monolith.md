---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-07-05
---

# Modular Monolith

The modular monolith addresses the problem of maintaining strong internal boundaries and cohesive change units without paying the operational cost of distributed deployment.

## Cohesive Formulation

A modular monolith is primarily a system-structure practice:

- Modules define [[Boundaries|boundaries]] inside one deployment.
- Relation models and flow views across modules are explicit.
- Persistence and transactions may be shared, but semantic ownership must still be scoped.
- Observer models may be local calls, handlers, process participants, or in-process message dispatch.

## In the Model

The monolith is a realization choice. The modules are the important semantic and structural boundaries. A modular monolith can preserve bounded contexts, aggregate boundaries, interaction contracts, and ownership without forcing network boundaries.

## Failure Modes

The pattern fails when shared process and shared database are mistaken for shared semantics. Without explicit module boundaries, the result is only a monolith, not a modular one.

Related concepts: [[Boundaries|boundaries]], [[Relation|relations]], [[Flow Views|flow views]], [[Process Graphs|process graphs]], [[Entity Models|entity models]], [[Application Hosts|application hosts]], [[Persistence|persistence]], [[Coordination|coordination]], [[Microservices|microservices]].
