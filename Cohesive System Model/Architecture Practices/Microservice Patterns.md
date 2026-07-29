---
realm: Architecture Practices
kind: reference
created: 2026-07-28
updated: 2026-07-28
aliases:
  - Microservices Patterns
  - Microservice Architecture Pattern Language
---

# Microservice Patterns

Microservice patterns are [[Architecture Practices|architecture-practice]] patterns that allocate semantic responsibility and [[Authority|authority]] to independently evolvable [[Service|services]], connect them in [[Service Models|service models]] through provided and required [[Interfaces|interfaces]], govern their conversations with [[Interaction Protocols|interaction protocols]], state their operational guarantees, and select [[Realization|realization]] mechanisms. Together, they form a pattern language for decomposition, collaboration, data ownership, transactional messaging, communication, deployment, discovery, reliability, security, observability, testing, and migration.

## Cohesive Correspondence

| Pattern family | Cohesive correspondence |
| --- | --- |
| Monolith or microservice architecture | [[Modular Monolith\|modular monolith]] and [[Microservices\|microservice]] practices over semantic, ownership, deployment, and failure boundaries |
| Decomposition by business capability or subdomain | [[Domain-Driven Design\|DDD]], [[Service Models\|service models]], [[Entity Models\|entity models]], [[Process Graphs\|process graphs]], authority, and team ownership |
| Service collaboration | [[Interfaces\|interfaces]], [[Interaction Protocols\|interaction protocols]], [[Interaction\|interaction]], [[Business Transactions\|business transactions]], [[Sagas\|sagas]], [[CQRS as Architecture Practice\|CQRS]], API composition, and domain-event publication |
| Transactional messaging | [[Transactional Outbox\|transactional outbox]], [[Transactional Inbox\|transactional inbox]], log tailing, polling publication, idempotency, and commit boundaries |
| Communication and external API | [[Enterprise Integration Patterns\|EIP]], request/reply, messaging, gateways, [[Multiplexing and Demultiplexing\|multiplexing and demultiplexing]], discovery, contracts, and [[Compatibility and Evolution\|compatibility and evolution]] |
| Reliability and observability | Circuit breaking, retry, health checks, metrics, audit, tracing, and [[Observability and Provenance\|provenance]] |
| Deployment and infrastructure | Hosts, containers, serverless platforms, service meshes, sidecars, configuration, and service registries as realization substrate |

Microservice patterns connect DDD's semantic boundary and ownership concerns with EIP's message, channel, routing, and endpoint structures, then add operational and realization concerns such as consistency, deployment, discovery, failure isolation, and observability. These correspondences are not equivalences: a [[Service|service]] is not automatically one bounded context, subdomain, aggregate, entity, process, observer, team, or deployment instance. Database per Service establishes an access and ownership arrangement; it does not by itself establish semantic authority or a sound service boundary. Likewise, a message labeled a domain event is not necessarily the domain occurrence itself; its meaning remains relative to the producing and consuming boundaries and their observers.

## Overlapping Catalogs

Saga, CQRS, Event Sourcing, Transactional Outbox, Idempotent Consumer, Messaging, Shared Database, API Gateway, and Anti-Corruption Layer overlap DDD, EIP, enterprise application patterns, cloud patterns, and distributed-systems patterns. Cohesive preserves the source provenance while mapping them onto shared concepts rather than duplicating primitives.

## External References

- Chris Richardson, [A Pattern Language for Microservices](https://microservices.io/patterns/).
- Chris Richardson, [*Microservices Patterns*](https://microservices.io/book), Manning, 2018.
- Microsoft, [Design patterns for microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/patterns), Azure Architecture Center.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Service|service]], [[Service Models|service models]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Microservices|microservices]], [[Modular Monolith|modular monolith]], [[Domain-Driven Design|domain-driven design]], [[Enterprise Integration Patterns|enterprise integration patterns]], [[Boundaries|boundaries]], [[Interaction|interaction]], [[Sagas|sagas]], [[CQRS as Architecture Practice|CQRS]], [[Transactional Outbox|transactional outbox]], [[Transactional Inbox|transactional inbox]], [[Compatibility and Evolution|compatibility and evolution]], [[Observability and Provenance|observability and provenance]], [[Realization|realization]].
