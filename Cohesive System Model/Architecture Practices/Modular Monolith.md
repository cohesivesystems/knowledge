---
realm: Architecture Practices
---

# Modular Monolith

Realm: Architecture Practices

The modular monolith addresses the problem of maintaining strong internal boundaries and cohesive change units without paying the operational cost of distributed deployment.

## Cohesive Formulation

A modular monolith is primarily a system-structure practice:

- Modules define [[Boundaries]] inside one deployment.
- Relations and flows across modules are explicit.
- Persistence and transactions may be shared, but semantic ownership must still be scoped.
- Observers may be local calls, handlers, processes, or in-process message dispatch.

## Practice Interpretation

The monolith is a realization choice. The modules are the important semantic and structural boundaries. A modular monolith can preserve bounded contexts, aggregate boundaries, interaction contracts, and ownership without forcing network boundaries.

## Failure Modes

The pattern fails when shared process and shared database are mistaken for shared semantics. Without explicit module boundaries, the result is only a monolith, not a modular one.

Related concepts: [[Boundaries]], [[Relations]], [[Flows]], [[Processes]], [[Entity Models]], [[Application Hosts]], [[Persistence]], [[Coordination]], [[Microservices]].
