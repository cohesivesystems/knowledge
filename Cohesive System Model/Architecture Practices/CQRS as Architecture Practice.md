---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-07-30
aliases:
  - Command Query Responsibility Segregation as Architecture Practice
---

# CQRS as Architecture Practice

CQRS, command query responsibility segregation, is an architecture-practice bundle that deliberately gives command interpretation and query observation different models, responsibilities, and operational paths when their forces differ materially.

It spans several realms. The technical topology is captured separately by [[CQRS]] as a realization-substrate pattern, while [[Pattern Languages and Correspondence|pattern languages and correspondence]] supplies the reusable realm profile and visualization.

## Problem

[[Command|Command]] handling and [[Query|query]] answering often have different semantic, authority, consistency, shape, security, and performance requirements. A single model can force transition rules into read concerns, constrain query shapes to write structures, or make one storage representation the accidental source of domain meaning.

CQRS is useful when the benefits of separating those responsibilities exceed the costs of duplicated representations, asynchronous propagation, compatibility management, additional failure modes, and operational complexity.

## Realm Correspondence Profile

| Realm | CQRS correspondence |
| --- | --- |
| Domain Semantics | Commands are observer-relative requests for interpreted change. Queries request observations. Entities, transitions, invariants, policies, and authority determine what can change and what can be observed. |
| System Graph | [[Transition Models\|Transition models]] own command-side decisions; [[Projection Models\|projection models]] derive read-oriented observations; effects, source relations, and boundaries connect them. |
| Operational Concerns | Commit meaning, consistency, source position, projection lag, ordering, idempotency, read-your-writes, monotonic reads, compatibility, access control, and rebuild recovery are explicit. |
| Realization Substrate | Current-state stores, event histories, brokers, logs, projection workers, indexes, caches, search engines, and read stores are replaceable realization families. |
| Architecture Practices | CQRS names the deliberate separation, its forces, and the obligations introduced by composing the other realms. |

The central semantic correspondence is not merely `write database -> read database`. It is:

```txt
command interpretation -> authoritative transition and commit
authoritative source    -> derived projection observation
query interpretation   -> boundary-relative observation
```

## Preservation Conditions

The pattern remains coherent when:

- A command-side identity and committed version correspond to identifiable authoritative persistence.
- Projection input preserves source identity, position, ordering scope, and schema or contract revision.
- Projection progress and query results expose the freshness or consistency evidence required by their boundary.
- Read-model identity remains related to, but does not silently replace, semantic entity or process identity.
- Command success names the command-side commit boundary rather than universal projection visibility.
- Rebuild, replay, duplicate delivery, late input, and incompatible projection code have declared recovery behavior.
- Access-control projections do not disclose information merely because it exists in authoritative write state.

CQRS does not require event sourcing, asynchronous messaging, separate deployable services, or separate physical databases. Those are possible realizations. Conversely, two stores do not constitute CQRS when they merely duplicate the same undifferentiated model.

## Catalog Correspondence

CQRS appears in Fowler's architecture writing, Greg Young's CQRS material, cloud pattern catalogs, and the [[Microservice Pattern Language|microservice pattern language]]. Cohesive treats these as overlapping source descriptions of one architecture-practice family and preserves their provenance without creating separate semantic primitives.

In a microservice context, CQRS may provide query views across service-owned data, but the service topology does not define entity identity or domain authority. With [[Event Sourcing as Architecture Practice|event sourcing]], an event history can supply authoritative projection input, but CQRS still owns the command/query responsibility split and its consistency obligations.

## Failure Modes

The practice fails when read and write models are separated without distinct forces, when eventual consistency is hidden, when projection state is treated as authoritative entity state, when operational messages are mislabeled as domain events, or when rebuilding a view can repeat external effects.

## Formal relations

- `realm_peer_of`: [[CQRS]] — Treats the same named CQRS pattern as an architecture-practice bundle, while the peer entry owns the realization-substrate topology and its operational consequences.

## External References

- Martin Fowler, [CQRS](https://martinfowler.com/bliki/CQRS.html), 2011.
- Greg Young, [CQRS Documents](https://cqrs.files.wordpress.com/2010/11/cqrs_documents.pdf), 2010.
- Chris Richardson, [CQRS pattern](https://microservices.io/patterns/data/cqrs.html), Microservice Architecture pattern language.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[CQRS]], [[Microservice Pattern Language|microservice pattern language]], [[Command|command]], [[Query|query]], [[Entity|entity]], [[Transition|transition]], [[Transition Models|transition models]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Projection Models|projection models]], [[Observation|observation]], [[Consistency Models|consistency models]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Compatibility and Evolution|compatibility and evolution]], [[Recovery|recovery]], [[Asynchronous Interaction Design|asynchronous interaction design]], [[Event Sourcing as Architecture Practice|event sourcing as architecture practice]].
