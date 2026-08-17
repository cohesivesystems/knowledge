---
realm: Principles
kind: principle
created: 2026-07-28
updated: 2026-08-17
status: draft
aliases:
  - Services
  - Domain Service
  - Domain Services
  - Application Service
  - Application Services
  - Service Layer
  - Background Service
  - Background Services
  - Daemon
  - Daemons
---

# Service

A service is a boundary-relative role in which a provider makes a capability available to a consumer through a contract, including declared semantic and operational guarantees. The role says what can be requested, observed, or relied upon at that boundary; it does not by itself determine where the behavior is implemented, whether it runs in another process, how it is deployed, or which team owns it.

The unqualified word *service* is therefore incomplete in a system model. The capability, provider role, [[Observer|participant that interprets service interactions]], interaction contract, [[Service Levels|service-level commitments]], semantic [[Authority|authority]], code, deployment, runtime process, and organizational owner may have different identities and lifecycles.

## Qualified Meanings

| Term | Center of gravity | Cohesive correspondence | Does not imply |
| --- | --- | --- | --- |
| Domain service | domain semantics and [[Domain-Driven Design\|DDD]] | A domain operation, policy, transition, or process expressed in the domain language when responsibility does not naturally belong to one entity or value. Its interface and decisions belong to the domain model. | An application coordinator, network endpoint, daemon, or independently deployed service. |
| Application service or Service Layer | system graph and architecture practice | An application-boundary [[Observer Models\|observer role]] that admits commands or queries, coordinates domain work, transactions, and effects, and returns observations. | New domain meaning merely because it coordinates domain behavior. |
| Background service or daemon | realization substrate | A runtime-managed process, worker, or [[Application Hosts\|application host]] activated by boot, timers, queues, files, messages, or other triggers and governed by lifecycle and [[Scheduling\|scheduling]] mechanisms. | A domain service, application boundary, or microservice. |
| Microservice | system graph and architecture practice spanning several realms | An independently evolvable [[Microservice\|service boundary]] whose semantic responsibilities, interactions, guarantees, code, ownership, deployment, and runtime realization are deliberately aligned through [[Microservice Architecture\|microservice architecture]]. | A fixed code size, one module, one repository, one process, one team, or one bounded context. |
| Queueing service | analytical and operational language | Processing supplied by a service center, described by service time, service rate, capacity, and queue discipline. | Any of the software-architecture meanings above. |

## Relationships among the Meanings

One microservice may expose several application services, run several background workers, and use domain services inside its model. The same domain service can be realized inside a modular monolith, microservice, command handler, workflow activity, or background worker. An application service can be invoked locally or exposed through a remote endpoint. A daemon may host a microservice or perform supporting infrastructure work, but running out of process does not make it a microservice.

## Encapsulation and Bundling

The common role across these meanings is encapsulation. A service bundles some internal structure and presents a more stable, selective [[Surfaces|interaction surface]] to consumers:

```text
service = encapsulated internal subgraph
        + externally relevant surface
        + provided and required ports
        + reusable interface types
        + declared guarantees
        + accountable ownership
```

The internal subgraph may contain entities, policies, domain services, queries, processes, code modules, storage, workers, or calls to other services. Its [[Interfaces|interfaces]] expose capabilities without requiring consumers to know that internal arrangement. This is boundary-relative: a composite service may encapsulate several downstream services for one consumer while appearing as a dependency node to another.

Encapsulation can be semantic, structural, operational, organizational, or some combination. A model should say which internal changes consumers are protected from and which guarantees remain valid across the interface.

[[Service Levels|Service levels]] make selected operational outcomes measurable and, where an SLA applies, accountable between provider and consumer. They qualify the service boundary rather than the code or deployment alone: an SLI defines what is observed, an SLO defines the target, and an SLA makes selected objectives commitments with declared consequences.

### Facades, Gateways, and Services

The GoF Facade pattern has a close structural correspondence: it provides a unified, simplified interface to a subsystem. A service can act as a facade, but *service* is the broader role. A service interface may carry semantic authority, remote failure, compatibility, security, throughput, and operational commitments that an object-oriented facade does not imply.

| Role | Primary purpose |
| --- | --- |
| Facade | Simplifies access to an internal subsystem without implying a deployment or network boundary |
| Adapter | Translates one interface or representation into another |
| Gateway | Controls or translates passage across an external, trust, protocol, or topology boundary |
| Aggregator | Combines correlated results or values under an explicit completion rule |
| Service | Provides a capability while encapsulating how it is realized |

A single node can fulfill several of these roles, but naming each role separately exposes its obligations.

## Capability and Composition Roles

A service's semantic authority and realization role are independent dimensions: whether it owns domain meaning, and whether it primarily realizes behavior locally or composes dependencies.

| Semantic role | Realization role | Recommended description |
| --- | --- | --- |
| Owns a domain capability | Primarily local | Capability-owning service |
| Owns a domain capability | Substantially composes dependencies | Capability-owning composition service |
| Does not own domain semantics | Provides reusable technical behavior | Technical or utility service |
| Does not own domain semantics | Routes, translates, aggregates, or coordinates dependencies | Composition service, qualified as gateway, aggregator, facade, or orchestrator |

Composing dependencies is independent of whether a service owns domain semantics. A composition service owns domain semantics when it decides domain-valid sequencing, eligibility, policy, or outcomes; it is composition-only when it preserves the authority and meanings of downstream capabilities while changing their accessibility or presentation.

The same distinction applies at the operation level:

| Operation role | Meaning |
| --- | --- |
| Authoritative command | Decides or records a semantic transition under local authority |
| Local query | Reads locally governed state or a declared projection |
| Delegating operation | Preserves another capability's meaning while invoking its provider |
| Routing operation | Selects a destination without combining semantic results |
| Aggregate query | Combines several observations under an explicit completeness rule |
| Composite command | Coordinates several commands and owns the exposed outcome contract |
| Process operation | Starts, advances, signals, or observes a semantic process |
| Translating operation | Adapts shape, protocol, or vocabulary across boundaries |

[[Service Models|Service models]] use these roles to distinguish a service's visible node from the entities, relations, queries, processes, and dependencies it encapsulates.

The direction of realization is therefore:

```txt
domain capability or operation
  -> application-boundary coordination
  -> code modules and interaction contracts
  -> deployment units and runtime processes
  -> scheduler-managed executions
```

This is a possible correspondence, not an identity chain. A layer may be absent, combined with another layer, or realized in several ways.

## Modeling Discipline

When using *service*, state:

- Which capability is provided, to whom, and at which [[Boundaries|boundary]]?
- Which observer interprets the request, message, timer, or other input?
- Where do domain rules, transition authority, coordination, and effects belong?
- Which provided and required ports instantiate which [[Interfaces|interface types]] and semantic contracts?
- Which [[Interaction Protocols|interaction protocols]] govern ordering, concurrency, completion, cancellation, and failure?
- Which [[Interaction Channels|channels]] and network bindings realize those interfaces?
- Which operational guarantees apply to delivery, ordering, consistency, recovery, and compatibility?
- Which SLIs, SLOs, or SLAs qualify the service, and which evidence establishes whether they are met?
- Which code modules, repositories, build artifacts, deployment units, runtime instances, and schedulers realize the role?
- Which team owns semantic change, contract evolution, deployment, and operation?

Names such as `CustomerService`, a `/services` directory, a service-manager unit, or a network endpoint are realization evidence, not proof of any particular service meaning.

## External References

- Eric Evans, [*Domain-Driven Design Reference*](https://www.domainlanguage.com/ddd/reference/), especially the Service pattern.
- Randy Stafford, [Service Layer](https://martinfowler.com/eaaCatalog/serviceLayer.html), *Patterns of Enterprise Application Architecture*.
- Erich Gamma et al., *Design Patterns: Elements of Reusable Object-Oriented Software*, Facade, 1994.
- Refactoring.Guru, [Facade](https://refactoring.guru/design-patterns/facade).
- Linux man-pages project, [daemon(7)](https://man7.org/linux/man-pages/man7/daemon.7.html).
- James Lewis and Martin Fowler, [Microservices](https://martinfowler.com/articles/microservices.html), 2014.

Related concepts: [[System Language and Realization|system language and realization]], [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Service Models|service models]], [[Service Levels|service levels]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Domain-Driven Design|domain-driven design]], [[Patterns of Enterprise Application Architecture|enterprise application patterns]], [[Microservice|microservice]], [[Microservice Architecture|microservice architecture]], [[Modular Monolith|modular monolith]], [[Queueing Theory|queueing theory]], [[Observer|observer]], [[Observer Models|observer models]], [[Process|process]], [[Interaction|interaction]], [[Command|command]], [[Query|query]], [[Effect|effect]], [[Boundaries|boundaries]], [[Authority|authority]], [[Scheduling|scheduling]], [[Observability and Provenance|observability and provenance]], [[Capacity Planning|capacity planning]], [[Application Hosts|application hosts]], [[Runtimes|runtimes]], [[Realization|realization]].
