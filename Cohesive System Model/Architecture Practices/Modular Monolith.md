---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-07-29
---

# Modular Monolith

The modular monolith addresses the problem of maintaining strong internal boundaries and cohesive change units within one repository and one compiler-visible solution or build graph. The shared graph enables static contract checking, compiler-enforced dependency rules, coordinated refactoring, shared code, and common repository and delivery infrastructure across the modules.

In Cohesive, *monolith* in this term names the integrated source-and-build arrangement, not a requirement that every module share one deployment, process, data store, or runtime failure boundary. A modular monolith may produce one deployable application or module-selective artifacts and hosts. Separately deployed modules may form a [[Microservice Architecture|microservice architecture]] while retaining a modular-monolith source and build realization.

## Cohesive Formulation

A modular monolith aligns semantic and system-graph boundaries with enforceable code modules while keeping a cohesive source and build graph:

- Modules define [[Boundaries|boundaries]] and expose explicit provided and required [[Interfaces|interfaces]].
- Relation models, process graphs, and flow views across modules remain explicit rather than becoming unrestricted internal calls.
- One repository and one compiler-visible solution or build graph statically check contracts, support atomic cross-module refactoring, and reuse code without granting every module access to another module's internals.
- Dependency management, tests, schema generation, CI/CD, artifact provenance, and release automation may remain shared across the system.
- Persistence and transactions may be shared, but semantic [[Authority|authority]], write ownership, and commit meaning must still be scoped.
- Observer models may be realized through local calls, handlers, process participants, in-process dispatch, or declared interactions between separately hosted modules.

## Relationship to Microservice Architecture

A modular monolith and [[Microservice Architecture|microservice architecture]] answer different allocation questions. The modular-monolith classification is about repository and compiler-visible solution or build cohesion. The microservice classification is about independently versioned deployment, runtime, failure, and operational boundaries. A system can satisfy both classifications.

| Concern | Modular monolith | Microservice architecture |
| --- | --- | --- |
| Encapsulation and isolation | Module APIs, dependency rules, visibility, types, tests, and ownership isolate responsibilities inside a cohesive code system. Co-location does not provide process or host failure isolation. | Service contracts are reinforced by independently operating deployment and runtime boundaries, adding fault-containment opportunities as well as network and partial-failure modes. |
| Source and static checking | One repository and one compiler-visible solution or build graph support host-language type checking, shared code, compiler-enforced dependency rules, atomic refactoring, and whole-system analysis. | Services may use that same graph, separate solutions in one repository, or separate repositories. Separately deployed versions always require explicit compatibility because compile-time agreement does not cover runtime version skew. |
| Build and delivery workflow | Modules share a build graph and common infrastructure while allowing affected builds, module-specific pipelines, and separately versioned artifacts. | Pipelines produce and release independently versioned service artifacts; the source and build graph may still be shared. |
| Deployment | One application is possible but not required. A shared build may emit module-selective artifacts, or one artifact may start different module roles in separate [[Application Hosts\|application hosts]]. | Independent deployment is a first-class alignment between a service boundary and one or more versioned deployment units. |
| Scaling | The whole application can be replicated, or selected module roles can be routed and scaled separately when their work, state, and dependencies permit it. | Each service deployment can usually be replicated, partitioned, placed, and scaled independently, subject to the same state, routing, and dependency constraints. |
| Data and coordination | Shared storage and local transactions remain available, with module-owned schemas or write paths needed to preserve authority. | Service-local commit boundaries are emphasized; cross-service work introduces delivery, compatibility, and distributed-coordination obligations. |

## Repository, Solution, and Deployment Profiles

| Repository and build profile | Retained properties | Cohesive classification |
| --- | --- | --- |
| One repository, one compiler-visible solution or build graph, one deployable | Static type checking, compiler-enforced dependencies, atomic refactoring, shared code and infrastructure, coordinated deployment | Modular monolith in source, build, and deployment |
| One repository, one compiler-visible solution or build graph, independently deployable service artifacts | The same source and build benefits, plus independently versioned deployment and runtime boundaries | Modular monolith in source and build; microservice architecture in deployment and runtime |
| One repository, separate service solutions or build graphs | Code discovery, common infrastructure, coordinated CI, provenance, and atomic source changes, but not compiler-wide type checking or direct graph-wide refactoring | Monorepo microservice arrangement, not a full modular monolith |
| Separate repository and solution per service | Independent source, build, access, and release administration; cross-service changes require published contracts and coordination | Microservice architecture without a modular monolith |

Independent deployment and scaling are therefore not exclusive to one repository profile. A shared solution may emit a combined artifact, start role-selective hosts from one artifact, or produce service-specific artifacts. [[Scaling Mechanisms|Functional decomposition]] can route demand to and scale selected modules without requiring every interaction to become a network call.

The independence claim must be tested rather than inferred from artifact count. A module is independently deployable only when it can be released or rolled back without a coordinated application rollout and when concurrently deployed versions remain [[Compatibility and Evolution|compatible]]. It is independently scalable only when its demand can be routed to separately schedulable capacity and shared dependencies do not remain the limiting bottleneck. Once modules communicate across versioned runtime or network boundaries, their interactions acquire the same timeout, delivery, ordering, observability, and recovery obligations as other distributed components.

## In the Model

The monolith is a source-and-build realization choice. The modules are the important semantic and structural boundaries. A modular monolith can preserve bounded contexts, aggregate boundaries, service contracts, and ownership while projecting selected modules into one or several deployment and scaling units. That projection changes the operational profile and realization obligations, not automatically the semantic model or the repository-and-solution classification.

## Failure Modes

The pattern fails when shared source, solution, process, or database is mistaken for shared semantics; when shared libraries let dependencies bypass module interfaces; or when cyclic module dependencies make independent change impossible. It is also misclassified when co-location in one repository is called a modular monolith even though independent solutions or build graphs make modules opaque to compiler-wide checking. Separately deployed modules fail as microservices when they require coordinated releases or continue to assume same-version, in-process behavior. Without explicit and enforced module boundaries, the result is only a source monolith, not a modular one.

Related concepts: [[Boundaries|boundaries]], [[Service|service]], [[Service Models|service models]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Relation|relations]], [[Flow Views|flow views]], [[Process Graphs|process graphs]], [[Entity Models|entity models]], [[Application Hosts|application hosts]], [[Runtimes|runtimes]], [[Scaling Mechanisms|scaling mechanisms]], [[Persistence|persistence]], [[Commit Boundaries|commit boundaries]], [[Compatibility and Evolution|compatibility and evolution]], [[Delivery Semantics|delivery semantics]], [[Coordination|coordination]], [[Scheduling|scheduling]], [[Recovery|recovery]], [[Microservice Architecture|microservice architecture]].

## Formal relations

- `corresponds_to`: [[Microservice Architecture]] — Can preserve the same semantic and service boundaries while sharing one repository and compiler-visible build graph; the correspondence does not equate source, module, service, deployment, or runtime boundaries.
