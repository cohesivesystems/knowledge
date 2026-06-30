---
realm: Architecture Practices
kind: pattern
aliases:
  - ACL
---

# Anti-Corruption Layer

An anti-corruption layer addresses the problem of integrating with another model without letting that model's semantics leak into the local boundary.

## Cohesive Formulation

The practice is a boundary translation discipline:

- Source observations, events, commands, and identities belong to one semantic domain.
- Target observations, events, commands, and identities belong to another.
- The ACL translates between them while preserving local meaning.

## In the Model

In categorical terms, an ACL should behave functorially where possible: it maps objects and changes from one domain into another while preserving the relationships that matter and explicitly forgetting what does not.

## Failure Modes

The pattern fails when translation is only structural serialization. Matching fields is not the same as preserving semantics, authority, identity, version, causality, or invariant meaning.

Related concepts: [[Boundaries|boundaries]], [[Observer|observer]], [[Observation|observation]], [[Command|command]], [[Event|event]], [[Functoriality|functoriality]], [[Naturality|naturality]], [[Equivalence vs Equality|equivalence vs equality]], [[Ports and Adapters|ports and adapters]].
