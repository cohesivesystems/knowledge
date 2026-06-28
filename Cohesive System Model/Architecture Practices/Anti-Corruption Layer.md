---
realm: Architecture Practices
---

# Anti-Corruption Layer

An Anti-Corruption Layer addresses the problem of integrating with another model without letting that model's semantics leak into the local boundary.

## Cohesive Formulation

The practice is a boundary translation discipline:

- Source observations, events, commands, and identities belong to one semantic domain.
- Target observations, events, commands, and identities belong to another.
- The ACL translates between them while preserving local meaning.

## Practice Interpretation

In categorical terms, an ACL should behave functorially where possible: it maps objects and changes from one domain into another while preserving the relationships that matter and explicitly forgetting what does not.

## Failure Modes

The pattern fails when translation is only structural serialization. Matching fields is not the same as preserving semantics, authority, identity, version, causality, or invariant meaning.

Related concepts: [[Boundaries]], [[Observer]], [[Observation]], [[Command]], [[Event]], [[Functoriality]], [[Naturality]], [[Equivalence vs Equality]], [[Ports and Adapters]].
