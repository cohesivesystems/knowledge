---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-07-29
---

# Modular Monolith

The modular monolith addresses the problem of maintaining strong internal boundaries and cohesive change units while retaining an integrated source, build, and delivery environment. Its conventional realization is one deployable application, but the module structure can also support module-selective hosts or artifacts when particular capabilities need independent deployment or scaling.

The defining claim is modularity, not that every concern shares one undifferentiated code, data, or runtime boundary. Conversely, producing several processes or deployment units does not by itself turn the modules into microservices.

## Cohesive Formulation

A modular monolith aligns semantic and system-graph boundaries with enforceable code modules while keeping a cohesive development graph:

- Modules define [[Boundaries|boundaries]] and expose explicit provided and required [[Interfaces|interfaces]].
- Relation models, process graphs, and flow views across modules remain explicit rather than becoming unrestricted internal calls.
- A shared language and build graph can statically check contracts, refactor across boundaries atomically, and reuse code without granting every module access to another module's internals.
- Repositories, dependency management, tests, schema generation, CI/CD, and release automation may remain shared across the application.
- Persistence and transactions may be shared, but semantic [[Authority|authority]], write ownership, and commit meaning must still be scoped.
- Observer models may be realized through local calls, handlers, process participants, in-process dispatch, or declared interactions between separately hosted modules.

## Relationship to Microservice Architecture

A modular monolith and [[Microservice Architecture|microservice architecture]] can realize similar semantic boundaries, encapsulation, ownership, interfaces, and functional decomposition. They differ primarily in how those structures are allocated to source, build, deployment, version, runtime, network, and failure boundaries.

| Concern | Modular monolith | Microservice architecture |
| --- | --- | --- |
| Encapsulation and isolation | Module APIs, dependency rules, visibility, types, tests, and ownership isolate responsibilities inside a cohesive code system. Co-location does not provide process or host failure isolation. | Service contracts are reinforced by independently operating deployment and runtime boundaries, adding fault-containment opportunities as well as network and partial-failure modes. |
| Source and static checking | A shared source and dependency graph supports host-language type checking, shared code, atomic refactoring, and whole-system analysis. | A monorepo can retain many of the same checks, but separately deployed versions still require explicit compatibility because compile-time agreement does not cover runtime version skew. |
| Build and delivery workflow | Modules can share build tooling, tests, CI/CD stages, artifact provenance, and coordinated release policy while using affected builds or module-specific pipelines. | Pipelines normally produce and release independently versioned service artifacts; shared tooling remains possible, but one service's release should not require a coordinated release of unrelated services. |
| Deployment | The conventional form produces one versioned deployment unit. A shared build may instead emit module-selective artifacts, or one artifact may start different module roles in separate [[Application Hosts\|application hosts]]. | Independent deployment is a first-class alignment between a service boundary and one or more versioned deployment units. |
| Scaling | The whole application can be replicated, or selected module roles can be routed and scaled separately when their work, state, and dependencies permit it. | Each service deployment can usually be replicated, partitioned, placed, and scaled independently, subject to the same state, routing, and dependency constraints. |
| Data and coordination | Shared storage and local transactions remain available, with module-owned schemas or write paths needed to preserve authority. | Service-local commit boundaries are emphasized; cross-service work introduces delivery, compatibility, and distributed-coordination obligations. |

## Deployment and Scaling

Independent deployment and scaling are not exclusive benefits of microservices. A modular codebase may use a combined artifact and host, start role-selective hosts from the same artifact, or produce module-specific artifacts from one shared source and build graph. [[Scaling Mechanisms|Functional decomposition]] can then route demand to and scale selected modules without requiring every interaction to become a network call.

The independence claim must be tested rather than inferred from artifact count. A module is independently deployable only when it can be released or rolled back without a coordinated application rollout and when concurrently deployed versions remain [[Compatibility and Evolution|compatible]]. It is independently scalable only when its demand can be routed to separately schedulable capacity and shared dependencies do not remain the limiting bottleneck. Once modules communicate across versioned runtime or network boundaries, their interactions acquire the same timeout, delivery, ordering, observability, and recovery obligations as other distributed components.

## In the Model

The monolith is a realization choice. The modules are the important semantic and structural boundaries. A modular monolith can preserve bounded contexts, aggregate boundaries, service contracts, and ownership without forcing network boundaries, and it can later project selected modules into separate deployment or scaling units without redefining their meaning. That projection changes the operational profile and realization obligations, not automatically the semantic model.

## Failure Modes

The pattern fails when shared process, source, or database is mistaken for shared semantics; when shared libraries let dependencies bypass module interfaces; or when cyclic module dependencies make independent change impossible. It also fails when module-specific artifacts are called independently deployable despite mandatory coordinated releases, or when separately hosted modules continue to assume same-version, in-process behavior. Without explicit and enforced module boundaries, the result is only a monolith, not a modular one.

Related concepts: [[Boundaries|boundaries]], [[Service|service]], [[Service Models|service models]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Relation|relations]], [[Flow Views|flow views]], [[Process Graphs|process graphs]], [[Entity Models|entity models]], [[Application Hosts|application hosts]], [[Runtimes|runtimes]], [[Scaling Mechanisms|scaling mechanisms]], [[Persistence|persistence]], [[Commit Boundaries|commit boundaries]], [[Compatibility and Evolution|compatibility and evolution]], [[Delivery Semantics|delivery semantics]], [[Coordination|coordination]], [[Scheduling|scheduling]], [[Recovery|recovery]], [[Microservice Architecture|microservice architecture]].

## Formal relations

- `corresponds_to`: [[Microservice Architecture]] — Can preserve similar semantic and service boundaries while choosing a more integrated source, build, and default deployment mapping; the correspondence does not equate module, service, deployment, or runtime boundaries.
