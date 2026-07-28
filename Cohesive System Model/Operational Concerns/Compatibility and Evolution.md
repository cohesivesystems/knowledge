---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-27
updated: 2026-07-27
aliases:
  - Schema Evolution
  - Contract Compatibility
  - Message Compatibility
---

# Compatibility and Evolution

Compatibility and evolution describe whether independently versioned producers, consumers, stored histories, schemas, definitions, and realizations can continue to correspond without changing the intended meaning.

Compatibility has several scopes:

- **Structural compatibility** asks whether a value remains readable under a declared [[Shape|shape]].
- **Semantic compatibility** asks whether names, units, defaults, authority, identity, and interpretation preserve meaning.
- **Protocol compatibility** asks whether interaction roles, reply obligations, errors, ordering, and lifecycle rules still compose.
- **Historical compatibility** asks whether retained material can still be interpreted, replayed, rebuilt, or migrated.
- **Execution compatibility** asks whether persisted definitions and continuations remain valid for a runtime or require explicit migration.

A format indicator or version field is evidence used to select an interpretation; it does not itself prove compatibility. Unknown variants, missing fields, changed defaults, expanded enumerations, and changed units require explicit rules.

## Translation and Canonical Forms

A message translator or [[Anti-Corruption Layer|anti-corruption layer]] maps between representations and semantic boundaries. A normalizer maps several source forms into a selected common form. These mappings must preserve the identities, relationships, authority, and distinctions required by the target; field correspondence alone is insufficient.

An Enterprise Integration Patterns **Canonical Data Model** is a shared integration representation intended to reduce pairwise translators. It is not automatically the canonical domain model or the canonical execution authority described by [[System Language and Realization|system language and realization]]. A shared representation may intentionally forget local domain distinctions and therefore requires explicit boundary and loss semantics.

## Evolution Obligations

Compatibility claims should name direction, versions, time horizon, stored history, participating consumers, and fallback or migration behavior. A consumer compatible with current live messages but unable to interpret retained history is not replay-compatible for that history. A long-lived process definition change must preserve or migrate continuation and effect identities, not only deserialize old checkpoints.

## External References

- Gregor Hohpe and Bobby Woolf, [Message Translator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html), [Normalizer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Normalizer.html), and [Canonical Data Model](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Shape|shape]], [[Version|version]], [[Value|value]], [[Boundaries|boundaries]], [[Anti-Corruption Layer|anti-corruption layer]], [[Ports and Adapters|ports and adapters]], [[Messages and Envelopes|messages and envelopes]], [[Interaction Channels|interaction channels]], [[System Language and Realization|system language and realization]], [[Execution Kernel|execution kernel]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]].
