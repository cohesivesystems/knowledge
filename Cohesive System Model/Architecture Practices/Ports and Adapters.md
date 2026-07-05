---
realm: Architecture Practices
kind: pattern
created: 2026-06-24
updated: 2026-06-29
---

# Ports and Adapters

Ports and Adapters addresses the problem of keeping domain and application semantics independent from specific infrastructure, protocols, user interfaces, and external systems.

## Cohesive Formulation

Ports define interaction boundaries. Adapters are realization mechanisms that translate between substrate-specific messages and Cohesive concepts such as [[Command|commands]], [[Query|queries]], [[Observation|observations]], [[Event|events]], and [[Interaction|interactions]].

The practice asks:

- Which boundary is being crossed?
- What semantic object enters or leaves the boundary?
- Which observer interprets the input?
- What protocol, storage, UI, or external system realizes the edge?

## In the Model

An inbound adapter turns an external occurrence into an input event, command, or query relative to an [[Observer|observer]]. An outbound adapter turns an endogenous event, query, command, or observation into a protocol-specific effect.

## Failure Modes

The pattern fails when adapters leak substrate semantics into the domain, or when ports are treated as technical interfaces without stating the semantic boundary and authority they represent.

Related concepts: [[Boundaries|boundaries]], [[Observer|observer]], [[Command|command]], [[Query|query]], [[Observation|observation]], [[Event|event]], [[Interaction|interaction]], [[Network|network]], [[Application Hosts|application hosts]], [[Realization|realization]], [[Anti-Corruption Layer|anti-corruption layer]].
