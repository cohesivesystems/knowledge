---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-27
updated: 2026-07-29
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

## Compatibility Direction

Compatibility is directional and should name the reader, writer, stored material, and version relation involved:

- **Backward compatibility** commonly means that a newer reader can interpret material written by an older writer.
- **Forward compatibility** commonly means that an older reader can continue to interpret material written by a newer writer.
- **Full compatibility** requires both directions for the declared versions and operations.

The terms are sometimes used from the perspective of a schema rather than a reader, so the direction should still be stated explicitly as `reader revision R can interpret writer revision W`. Structural readability is only the first test. A reader that accepts a newly added field while assigning the wrong unit, default, authority, or lifecycle meaning is not semantically compatible.

Reader and writer schemas can differ. A decoder may project stored material into the reader's expected [[Shape|shape]], supply defaults, preserve unknown fields, reject unknown variants, or translate into a canonical form. Each choice can forget information and affect whether later re-encoding or forwarding remains compatible.

## Translation and Canonical Forms

A message translator or [[Anti-Corruption Layer|anti-corruption layer]] maps between representations and semantic boundaries. A normalizer maps several source forms into a selected common form. These mappings must preserve the identities, relationships, authority, and distinctions required by the target; field correspondence alone is insufficient.

An Enterprise Integration Patterns **Canonical Data Model** is a shared integration representation intended to reduce pairwise translators. It is not automatically the canonical domain model or the canonical execution authority described by [[System Language and Realization|system language and realization]]. A shared representation may intentionally forget local domain distinctions and therefore requires explicit boundary and loss semantics.

## Coexistence and Historical Horizons

Rolling deployment creates an interval in which old and new writers, readers, definitions, routes, and persisted continuations coexist. Compatibility must hold for the actual interaction directions during that interval, including rollback to an older executable after newer material has already been written.

Stored data often outlives the code that wrote it. Live compatibility, replay compatibility, migration compatibility, and rollback compatibility can therefore have different horizons. A change may be safe for current traffic but make an old snapshot, retained event, quarantine record, workflow continuation, or projection rebuild uninterpretable.

Unknown-field preservation can help an intermediary forward information it does not understand, but it does not prove that the intermediary preserves semantic meaning or validation. Likewise, schema-on-read defers interpretation until observation time; it moves the compatibility obligation rather than removing it.

Migration should declare whether material is rewritten in place, interpreted through versioned readers, translated on access, shadow-written, or rebuilt into a new projection. Cutover requires an authority rule for which representation is current and a recovery rule for partially migrated material.

## Evolution Obligations

Compatibility claims should name direction, versions, time horizon, stored history, participating consumers, and fallback or migration behavior. A consumer compatible with current live messages but unable to interpret retained history is not replay-compatible for that history. A long-lived process definition change must preserve or migrate continuation and effect identities, not only deserialize old checkpoints.

Useful compatibility checks include:

- Which reader and writer revisions are being related, in which direction?
- Which structural information may be absent, added, defaulted, ignored, or preserved opaquely?
- Which names, units, identities, authorities, invariants, and protocol obligations must retain meaning?
- Which old and new components coexist during rollout and rollback?
- Which retained histories, snapshots, continuations, and quarantine records remain interpretable?
- What migration, translation, fallback, or rejection behavior applies when correspondence fails?

## External References

- Gregor Hohpe and Bobby Woolf, [Message Translator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageTranslator.html), [Normalizer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Normalizer.html), and [Canonical Data Model](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CanonicalDataModel.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Shape|shape]], [[Version|version]], [[Value|value]], [[Boundaries|boundaries]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Anti-Corruption Layer|anti-corruption layer]], [[Ports and Adapters|ports and adapters]], [[Messages and Envelopes|messages and envelopes]], [[Interaction Channels|interaction channels]], [[Projection Models|projection models]], [[Delivery Semantics|delivery semantics]], [[Temporal Completeness|temporal completeness]], [[System Language and Realization|system language and realization]], [[Execution Kernel|execution kernel]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]].
