---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-07-01
---

# Clean Architecture

Clean Architecture addresses the problem of dependency direction: keeping high-value semantic rules from depending on volatile delivery, persistence, framework, and infrastructure choices.

## Cohesive Formulation

Clean Architecture can be expressed as a separation between domain semantics, system graph, operational concerns, and realization substrate.

The domain core defines entities, values, transitions, invariants, policies, and events. Outer layers realize interaction, persistence, reconstitution, protocols, and application hosting.

## In the Model

The dependency rule says that substrate choices should realize semantic roles without defining them. A database, web framework, broker, or UI can realize an observer or interaction edge, but it should not determine the meaning of entity state, command interpretation, or invariant scope.

## Failure Modes

The pattern fails when layer names replace boundary definitions, when DTOs become the domain model, or when framework lifecycle and storage shape determine semantic behavior.

Related concepts: [[Realization|realization]], [[Application Hosts|application hosts]], [[Storage Systems|storage systems]], [[Network|network]], [[Functoriality|functoriality]], [[Ports and Adapters|ports and adapters]].
