---
realm: Architecture Practices
kind: architecture-practice
created: 2026-08-21
updated: 2026-08-21
status: draft
aliases:
  - Vertical Slices
  - Vertical Slice
  - VSA
---

# Vertical Slice Architecture

Vertical slice architecture organizes application code around distinct requests, use cases, or change units that cross the technical concerns needed to produce an outcome. The primary grouping question is not “is this code a controller, service, repository, or mapper?” but “which behavior changes for the same reason?”

The practice selects a request, use-case, or change axis for [[Cohesion and Coupling|cohesion and coupling]]. Code that interprets one request, validates it, invokes or implements the relevant behavior, accesses required data, produces a response, and tests that path can remain close to the slice. Dependencies between slices should be explicit and justified rather than emerging through shared technical-layer folders.

## Cohesive Formulation

A vertical slice is a code-organization and application-boundary choice, not a new domain-semantic primitive. A slice commonly begins at an admitted request or occurrence and ends at a declared result, commitment, or effect boundary. Depending on the use case, its input may be interpreted as a [[Command|command]] or [[Query|query]], and its output may be a response, [[Observation|observation]], event, or requested effect.

The practice asks:

- Which request, use case, or independently changing behavior gives the slice its identity?
- Which entry point, validation, application coordination, domain behavior, data access, mapping, and tests belong specifically to it?
- Which [[Boundaries|boundaries]] does the slice remain inside, and which does it cross through explicit [[Interfaces|interfaces]]?
- Which domain rules and shared mechanisms are genuinely common, rather than merely similar today?
- Which other slices must change when this slice changes, and what dependency or invariant explains that coupling?
- Which cross-cutting policies must be applied consistently without turning a shared utility layer into an unrestricted dependency surface?

The aim is change locality, not indiscriminate internal entanglement. Code within a slice still benefits from clear responsibilities and explicit contracts. Likewise, eliminating every shared abstraction is not the goal: shared domain authority, security policy, transaction behavior, observability, and substrate mechanisms should remain shared when their meaning and lifecycle are genuinely common.

## Package by Feature and Feature Folders

Package-by-feature and feature-folder layouts are related to vertical slices, but they are not synonyms.

A feature folder groups code under a product or domain label such as `Orders` or `Billing`. It may contain several use cases, and it may still reproduce technical layers internally through `Controllers`, `Services`, and `Repositories` subfolders. That layout improves navigation without necessarily making one end-to-end change path cohesive or isolating it from neighboring paths.

A vertical slice uses a request or use case as the stronger unit. A broad feature can contain many slices, such as placing, cancelling, and viewing an order. Conversely, one slice may use shared domain behavior or cross an application interface without turning every participating artifact into one feature folder. Folder placement is one realization of the slice boundary; dependency rules, ownership, tests, and change behavior determine whether the boundary is effective.

For example, one possible source layout is:

```text
src/
  Orders/
    PlaceOrder/
      Endpoint.cs
      Command.cs
      Validator.cs
      Handler.cs
      OrderWriter.cs
      Response.cs
      Tests.cs
    GetOrder/
      Endpoint.cs
      Query.cs
      Handler.cs
      Projection.cs
      Response.cs
      Tests.cs
  Shared/
    Authentication/
    Database/
    Observability/
```

The filenames are illustrative, not required roles. `PlaceOrder` may delegate complex rules to domain entities and policies, while `GetOrder` may read a purpose-built projection directly. Another language or framework may colocate these roles in fewer files, mirror tests in a separate tree, or express the entry point through a message handler, job, CLI command, or UI action. The architectural claim is about the use-case boundary and dependency graph, not a prescribed directory shape or mediator library.

## Relationship to Clean Architecture

Vertical slice architecture and [[Clean Architecture|clean architecture]] answer different questions.

Clean architecture constrains dependency direction so that domain and application meaning do not depend on volatile frameworks, delivery mechanisms, or storage choices. Vertical slice architecture selects which request-specific code should be grouped and allowed to evolve together. A system can therefore apply clean dependency rules within each slice, place several slices around a shared domain core, or use different internal patterns for slices with different complexity.

The two practices conflict only when one is applied as an inflexible global layout. Requiring every slice to pass through the same controller-service-repository chain can recreate technical-layer coupling. Conversely, colocating a slice does not justify letting framework or storage semantics define domain behavior.

## Relationship to Ports and Adapters

[[Ports and Adapters|Ports and adapters]] types and realizes crossings; it does not choose the slices. An inbound adapter can admit an HTTP request, message, scheduled trigger, or CLI invocation through a provided port and dispatch it to a slice. An outbound port can express a capability the slice requires, while a database, broker, or external-service adapter realizes that dependency.

Those ports preserve boundary and substitution choices regardless of folder layout. A slice-specific adapter may remain with its slice, while an adapter used by several slices may belong to a deliberately shared realization module. Neither placement makes the port, interface, endpoint, adapter, or slice synonymous.

## Domain, Module, and Service Boundaries

[[Domain-Driven Design|Domain-driven design]] can supply the language, entities, policies, invariants, and [[Bounded Context|bounded contexts]] that give slices semantic meaning. A use-case slice is usually narrower than a bounded context and should not duplicate a domain model merely to appear independent. Several slices may invoke the same authoritative domain behavior because they offer different ways to observe or change the same subject.

A [[Modular Monolith|modular monolith]] can use coarse modules to enforce semantic and code boundaries, then organize the application behavior inside each module as vertical slices. The module owns its exposed contracts and shared domain authority; its slices localize individual change paths.

Likewise, [[Microservice Architecture|microservice architecture]] may organize the implementation inside each independently evolvable service as vertical slices. Extracting every slice into a service is not implied. Service boundaries add independent deployment, compatibility, failure, recovery, and operational obligations that a source-code slice does not possess merely because it has its own folder or handler.

## Tradeoffs

Vertical slices can improve change locality, make request behavior easier to discover and test, reduce cross-layer ripple, and allow a simple use case to remain simple while a complex use case adopts richer domain patterns. They can also make the application’s offered behavior more visible than a top-level inventory of technical roles.

The practice can introduce duplication, uneven internal designs, repeated policy wiring, and a larger number of small artifacts. Discoverability can suffer when slice names do not match the [[Ubiquitous Language|ubiquitous language]] or when conventions differ arbitrarily. Cross-slice business processes, invariants, and shared domain behavior still require explicit models; copying them into each handler creates conflicting authority rather than independence.

The tradeoff should therefore be evaluated against observed change and dependency structure. A shared mechanism is useful when it preserves one stable contract for several slices. It is harmful when it becomes a generic service, repository, mapper, or utility through which otherwise independent slices can reach one another’s internals.

## Failure Modes

The practice fails when:

- files are moved into feature-shaped folders while behavior still depends on global controllers, services, repositories, or mutable shared state;
- a slice is chosen mechanically per table, endpoint, or CRUD operation rather than around a coherent request or use case;
- a handler accumulates domain decisions, persistence assumptions, mapping, retries, and external effects without preserving domain authority or commit boundaries;
- direct slice-to-slice dependencies and cycles make nominally independent changes propagate across the application;
- common security, transaction, compatibility, or observability rules diverge through copy and paste;
- a mediator, request-handler framework, or one-class-per-role convention is mistaken for the architecture;
- a feature folder is assumed to prove cohesion without examining dependencies and change history; or
- a code slice is mistaken for a bounded context, module, repository, deployable service, process, or failure boundary.

## Formal relations

- `bundles`: [[Cohesion and Coupling]] — Selects request, use-case, and change-axis relations as the primary criterion for keeping code together while requiring cross-slice dependencies to remain explicit.

## External References

- Jimmy Bogard, [Vertical Slice Architecture](https://www.jimmybogard.com/vertical-slice-architecture/), April 19, 2018.
- D. L. Parnas, [On the Criteria to Be Used in Decomposing Systems into Modules](https://doi.org/10.1145/361598.361623), *Communications of the ACM* 15(12):1053–1058, 1972.
