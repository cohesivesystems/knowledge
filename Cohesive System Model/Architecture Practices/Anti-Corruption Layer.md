---
realm: Architecture Practices
kind: pattern
created: 2026-06-24
updated: 2026-07-27
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

Message translators, normalizers, and canonical integration models are possible translation structures. A canonical integration representation is not automatically canonical domain meaning: the anti-corruption layer must state which distinctions are preserved, transformed, approximated, or forgotten at each boundary.

## Failure Modes

The pattern fails when translation is only structural serialization. Matching fields is not the same as preserving semantics, authority, identity, version, causality, or invariant meaning.

## External References

- Gregor Hohpe and Bobby Woolf, [Message Translator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html), [Normalizer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Normalizer.html), and [Canonical Data Model](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Boundaries|boundaries]], [[Observer|observer]], [[Observation|observation]], [[Command|command]], [[Event|event]], [[Shape|shape]], [[Compatibility and Evolution|compatibility and evolution]], [[Functoriality|functoriality]], [[Naturality|naturality]], [[Equivalence vs Equality|equivalence vs equality]], [[Ports and Adapters|ports and adapters]].
