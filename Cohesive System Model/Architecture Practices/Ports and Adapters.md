---
realm: Architecture Practices
---

# Ports And Adapters

Realm: Architecture Practices

Ports and Adapters addresses the problem of keeping domain and application semantics independent from specific infrastructure, protocols, user interfaces, and external systems.

## Cohesive Formulation

Ports define interaction boundaries. Adapters are realization mechanisms that translate between substrate-specific messages and Cohesive concepts such as [[Command|commands]], [[Query|queries]], [[Observation|observations]], [[Event|events]], and [[Interaction|interactions]].

The practice asks:

- Which boundary is being crossed?
- What semantic object enters or leaves the boundary?
- Which observer interprets the input?
- What protocol, storage, UI, or external system realizes the edge?

## Practice Interpretation

An inbound adapter turns an external occurrence into an input event, command, or query relative to an [[Observer]]. An outbound adapter turns an endogenous event, query, command, or observation into a protocol-specific effect.

## Failure Modes

The pattern fails when adapters leak substrate semantics into the domain, or when ports are treated as technical interfaces without stating the semantic boundary and authority they represent.

Related concepts: [[Boundaries]], [[Observer]], [[Command]], [[Query]], [[Observation]], [[Event]], [[Interaction]], [[Network]], [[Application Hosts]], [[Realization]], [[Anti-Corruption Layer]].
