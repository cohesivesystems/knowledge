---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-08-08
aliases:
  - Projection
  - Projections
---

# Projection Models

Projection models describe how derived observations or derived state views are arranged in the system graph.

At the structure level, a projection model organizes how one semantic view is shaped from another. Projection models may support [[Query|queries]], read models, indexes, materialized views, UI models, analytics, routing views, or process state. This describes derivation and dependency structure, not the concrete database, cache, index, or compute substrate that realizes it.

Projection state is usually not the primary semantic history. It is a derived observation that must be related back to its source, update protocol, and recovery strategy.

In [[CQRS]], projection models commonly realize the query side: read-oriented observations derived from authoritative write-side persistence and selected by [[Query|queries]].

[[CRDTs]] may realize projection models or replicated read models when their update algebra can tolerate asynchronous, concurrent updates and converge without central serialization.

A projection model should be understood functorially where possible: it maps source structure into a derived view while preserving the identities, versions, dependencies, or ordering needed for the projection's purpose.

## Authority and Derivation

The source of a projection and the authority to answer from it should be stated separately. A projection may not be authoritative for accepting source transitions while still being authorized to answer selected [[Query|queries]] under a freshness and consistency contract. A cache, search index, routing table, analytics view, and process-status view can therefore carry useful query authority without becoming the primary semantic history.

A projection model should identify its derivation dependencies, not only its immediate input channel. If projection `C` is derived from `B`, and `B` from authoritative history `A`, then `C` depends transitively on the source positions, transformation revisions, compatibility rules, and recovery of both stages. A derivation graph makes this lineage and failure propagation explicit.

Useful projection identity may include:

- Projection definition and semantic revision.
- Source identities, partitions, versions, log positions, or [[Consistent Cuts|consistent cut]].
- Transformation, filter, join, and policy revisions.
- Output subject, shape, version, and authority scope.
- Provenance connecting an output observation to the source facts and decisions that produced it.

## Incremental Maintenance and Recomputation

Incremental maintenance applies admitted changes to existing projection state. Recomputation derives the projection again from an authoritative source, snapshot, or retained history. These paths should preserve the same declared meaning even when they use different scheduling, batching, or storage mechanisms.

Rebuildability is a bounded claim. It depends on retaining enough source history, schemas, transformation definitions, identity, provenance, and deduplication material for the claimed horizon. Replaying retained input is not sufficient if the old interpretation no longer exists or if processing the input repeats external effects that do not belong to projection construction.

A projection transformation should therefore separate derived-state updates from notifications, commands, payments, or other non-replayable [[Effect|effects]]. Backfill and replay require an explicit effect policy even when they reuse live transformation logic.

Incremental and recomputed results may diverge because of missed input, duplicate handling, nondeterministic logic, changed dependencies, corrupted state, or incompatible definitions. Validation and reconciliation should compare results at a declared source cut and shape rather than treating record counts alone as equivalence.

## Bootstrap, Backfill, and Cutover

A new or repaired projection commonly needs an initial finite build followed by live incremental maintenance. The cutover protocol should state:

- The authoritative source and cut or position used for the initial build.
- How changes after that cut are buffered, replayed, or consumed without a gap.
- How duplicates around the cut are detected or made harmless.
- How the candidate projection is validated for completeness and semantic equivalence.
- Which authority changes make queries use the new projection.
- How rollback or reconciliation works if the candidate is incomplete or incompatible.

Shadow projections and dual reads can provide comparison evidence, but they do not establish equality without a declared observation population, source cut, consistency tolerance, and treatment of late or missing input.

## Modeling Checks

A projection model should state:

- Source events or state.
- Source identity, position, version, or consistent cut.
- Definition and transformation revision.
- [[Shape]] and identity of the derived observation.
- Derivation dependencies and provenance.
- Update ordering, idempotency, and duplicate policy.
- Lag, freshness, consistency, and query-authority expectations.
- Retention, recomputation, rebuild, validation, and recovery behavior.
- Bootstrap, backfill, and cutover protocol.
- Effect policy during live processing and replay.

Related concepts: [[Functoriality|functoriality]], [[Observation|observation]], [[Observable|observable]], [[Shape|shape]], [[Query|query]], [[State|state]], [[Event|event]], [[Effect|effect]], [[Authority|authority]], [[Relation Models|relation models]], [[Replica Models|replica models]], [[Partition Models|partition models]], [[Flow Operators|flow operators]], [[Relational and Logic Programming|relational and logic programming]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Consistent Cuts|consistent cuts]], [[Compatibility and Evolution|compatibility and evolution]], [[Observability and Provenance|observability and provenance]], [[Temporal Completeness|temporal completeness]], [[Delivery Semantics|delivery semantics]], [[CRDTs]], [[CQRS]], [[Ordering|ordering]], [[Recovery|recovery]], [[Realization|realization]].

## Formal relations

- `arranges`: [[Observation]] — Places derived observations and state views into model-specific source, transformation, freshness, lineage, and query structures.
