---
realm: Architecture Practices
kind: reference
created: 2026-07-28
updated: 2026-07-28
aliases:
  - PoEAA
  - Enterprise Application Patterns
  - Enterprise Application Architecture Patterns
---

# Patterns of Enterprise Application Architecture

Patterns of Enterprise Application Architecture, or PoEAA, catalogs recurring structures for domain logic, application boundaries, relational persistence, web presentation, distribution, offline concurrency, session state, and foundational mapping or gateway roles.

## Cohesive Correspondence

| PoEAA family | Representative patterns | Cohesive correspondence |
| --- | --- | --- |
| Domain logic | Transaction Script, Domain Model, Table Module, Service Layer | semantic transitions and processes, application observer boundaries, architecture practices, and host-language realization |
| Data source architecture | Table Data Gateway, Row Data Gateway, Active Record, Data Mapper | persistence and reconstitution correspondences, ports, storage systems, and separation or collapse of domain and storage shapes |
| Object-relational behavior | Unit of Work, Identity Map, Lazy Load | commit boundaries, identity correspondence, observation, caching, concurrency, and reconstitution |
| Object-relational structure | Identity Field, association and inheritance mappings, Embedded Value, Serialized LOB | entity and value correspondence to storage schemas, shapes, relations, and compatibility |
| Presentation | Model-View-Controller, Page Controller, Front Controller, Template View, Application Controller | observer models, projection models, interaction, application hosts, and UI realization |
| Distribution | Remote Facade, Data Transfer Object | interaction boundaries, shapes, batching or coarsening, network realization, and information loss |
| Offline concurrency | Optimistic, Pessimistic, Coarse-Grained, and Implicit Lock | concurrency control, isolation, versioning, authority, and commit boundaries |
| Base patterns | Gateway, Mapper, Repository, Separated Interface, Registry, Value Object | architecture-practice and realization roles that require semantic qualification |

## Reconciliation with DDD

PoEAA often begins closer to application structure and persistence mechanics than DDD. Its Domain Model pattern can host DDD semantics, but an object graph does not become a domain model merely by containing behavior. Repository can present collection-like access to domain objects, but storage identity, freshness, query semantics, and commit behavior remain explicit. Value Object corresponds to identity-free domain [[Value|value]] only when equality, shape, units, and boundary meaning agree.

Patterns such as Active Record deliberately combine concerns that Data Mapper separates. Cohesive records that structural choice without declaring one universally correct: the preservation question is whether the selected arrangement maintains domain identity, transition authority, invariants, observations, and commit meaning.

## External References

- Martin Fowler, with David Rice, Matthew Foemmel, Edward Hieatt, Robert Mee, and Randy Stafford, [*Patterns of Enterprise Application Architecture*](https://martinfowler.com/books/eaa.html), Addison-Wesley Professional, 2002.
- Martin Fowler, [Catalog of Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/).

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Domain-Driven Design|domain-driven design]], [[Analysis Patterns|analysis patterns]], [[Entity|entity]], [[Value|value]], [[Transition|transition]], [[Observer Models|observer models]], [[Projection Models|projection models]], [[Interaction|interaction]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Commit Boundaries|commit boundaries]], [[Concurrency Control|concurrency control]], [[Ports and Adapters|ports and adapters]], [[Storage Systems|storage systems]], [[Application Hosts|application hosts]].
