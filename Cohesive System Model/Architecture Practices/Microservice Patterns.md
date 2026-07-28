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

The Microservice Architecture pattern language collects recurring decisions about application architecture, service boundaries, collaboration, data ownership, transactional messaging, communication, deployment, discovery, reliability, security, observability, testing, and migration.

## Cohesive Correspondence

| Pattern family | Cohesive correspondence |
| --- | --- |
| Monolith or microservice architecture | [[Modular Monolith|modular-monolith]] and [[Microservices|microservice]] practices over semantic, ownership, deployment, and failure boundaries |
| Decomposition by business capability or subdomain | [[Domain-Driven Design|DDD]], [[Boundaries|boundaries]], [[Entity Models|entity models]], [[Process Graphs|process graphs]], authority, and team ownership |
| Service collaboration | [[Interaction|interaction]], [[Business Transactions|business transactions]], [[Sagas|sagas]], [[CQRS as Architecture Practice|CQRS]], API composition, command-side replicas, and domain-event publication |
| Transactional messaging | [[Transactional Outbox|transactional outbox]], [[Transactional Inbox|transactional inbox]], log tailing, polling publication, idempotency, and commit boundaries |
| Communication and external API | [[Enterprise Integration Patterns|EIP]], request/reply, messaging, gateways, discovery, contracts, and [[Compatibility and Evolution|compatibility and evolution]] |
| Reliability and observability | Circuit breaking, retry, health checks, metrics, audit, tracing, and [[Observability and Provenance|provenance]] |
| Deployment and infrastructure | Hosts, containers, serverless platforms, service meshes, sidecars, configuration, and service registries as realization substrate |

Microservice patterns provide an important bridge between DDD and EIP, but their terms remain qualified. A service is not automatically one bounded context, subdomain, aggregate, entity, process, observer, team, or deployment instance. Database per Service establishes an access and ownership arrangement; it does not by itself establish semantic authority or correct service boundaries. A message labeled a domain event still requires the observer-relative event and boundary distinctions used throughout Cohesive.

## Overlapping Catalogs

Saga, CQRS, Event Sourcing, Transactional Outbox, Idempotent Consumer, Messaging, Shared Database, API Gateway, and Anti-Corruption Layer overlap DDD, EIP, enterprise application patterns, cloud patterns, and distributed-systems patterns. Cohesive preserves the source provenance while mapping them onto shared concepts rather than duplicating primitives.

## External References

- Chris Richardson, [A Pattern Language for Microservices](https://microservices.io/patterns/).
- Chris Richardson, [*Microservices Patterns*](https://microservices.io/book), Manning, 2018.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Microservices|microservices]], [[Modular Monolith|modular monolith]], [[Domain-Driven Design|domain-driven design]], [[Enterprise Integration Patterns|enterprise integration patterns]], [[Boundaries|boundaries]], [[Interaction|interaction]], [[Sagas|sagas]], [[CQRS as Architecture Practice|CQRS]], [[Transactional Outbox|transactional outbox]], [[Transactional Inbox|transactional inbox]], [[Compatibility and Evolution|compatibility and evolution]], [[Observability and Provenance|observability and provenance]], [[Realization|realization]].
