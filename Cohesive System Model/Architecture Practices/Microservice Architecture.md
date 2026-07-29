---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-07-29
aliases:
  - Microservices
  - Microservice
  - Microservices Architecture
---

# Microservice Architecture

Microservice architecture addresses the problem of independent ownership, deployment, scaling, and evolution across bounded capabilities. The prefix *micro* is relative to a coarser service, application, or deployment boundary; it does not prescribe a code size, endpoint count, process count, or team size.

## Cohesive Formulation

A microservice is an architecture-practice [[Realization|realization]] of an independently evolvable [[Service|service]] boundary within a [[Service Models|service model]]. It aligns selected semantic responsibilities and authority with provided and required [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], operational guarantees, code, ownership, deployment, and runtime infrastructure. It is not just a process or network endpoint.

The practice asks:

- What boundary does the service own?
- Which entities, processes, policies, and projections are inside it?
- Which provided and required interfaces admit events, commands, queries, and observations across the boundary?
- Which protocols and operational envelopes govern those interactions?
- What delivery, ordering, recovery, and consistency semantics apply?
- Which code modules and contracts realize the boundary?
- Which team owns semantic change, deployment, and operation?
- Which repositories, build artifacts, and deployment units are involved?
- How do schedulers place, replicate, restart, and scale its runtime work?

## Allocation across Structures

A microservice architecture selects correspondences across several structures; it does not make them identical.

| Structure | Allocation question |
| --- | --- |
| Semantic model | Which capabilities, entities, processes, policies, invariants, and [[Authority\|authority]] belong to the service boundary? |
| Code | Which modules implement those responsibilities and keep internal dependencies from bypassing the boundary? |
| Organization | Which team is accountable for the model, contracts, operation, and evolution? |
| Repository | Where do implementation, schemas, tests, deployment definitions, and ownership metadata live? |
| Build and deployment | Which versioned artifacts and deployment units can be released or rolled back independently? |
| Runtime topology | Which application hosts, workers, sidecars, stores, and interaction endpoints realize the service? |
| Scheduling | Which schedulers place instances, allocate execution opportunity, manage replicas, and participate in restart or scaling? |

Independence is a profile rather than one Boolean property. Semantic evolution, source changes, builds, contracts, deployment, scaling, failure, recovery, and team ownership may have different boundaries. One team may own several microservices; one repository may contain many of them; one microservice may contain many modules, produce several artifacts, and run as many scheduler-managed instances.

The resulting topology can make organizational structure visible—sometimes summarized as being able to “ship the org chart.” That is useful when team responsibility follows coherent semantic and operational ownership. It is harmful when arbitrary reporting lines are projected into runtime dependencies or when organizational autonomy is claimed without the platform, authority, and contract boundaries needed to sustain it.

Repository topology is orthogonal to service topology. A monorepo can preserve independently deployed microservices while enabling graph-wide refactoring, shared schema generation, static contract checking, affected builds, and atomic source changes. Separate repositories can strengthen access, dependency, or release boundaries, but require explicit contract publication, versioning, and compatibility automation. Compile-time agreement within one source revision does not prove compatibility among concurrently deployed versions: an atomic commit is not an atomic deployment.

A deployment architecture maps versioned artifacts into deployment units, runtime instances, networks, stores, and failure domains. A scheduler selects placement and execution opportunity within that architecture; it does not acquire domain authority merely by starting, stopping, or moving work. Stateful scaling additionally requires explicit partition identity, ownership, fencing, persistence, and recovery semantics.

## Platform Preconditions

Fine-grained services move composition work from host-language and build boundaries into a distributed operational environment. A manageable microservice architecture therefore depends on reusable platform mechanisms for:

- Interface binding, communication, discovery, identity, authentication, retries, timeouts, cancellation, and flow control.
- Schemas, interaction protocols, code generation, compatibility rules, contract publication, and version evolution.
- Repository conventions, dependency policy, builds, tests, artifact provenance, and ownership metadata.
- Packaging, configuration, secrets, health checks, deployment, rollout, and rollback.
- Placement, quotas, replication, autoscaling, disruption handling, and recovery.
- Logs, metrics, traces, service catalogs, operational control, and accountability.

The platform need not be one framework or repository, but these capabilities must be reusable and coherent. Otherwise each service team recreates distributed-systems infrastructure and turns formerly local composition errors into ad hoc runtime failures.

## In the Model

Microservice architecture projects selected semantic and structural boundaries into deployment and operational boundaries. That can increase autonomy, but it also turns local composition problems into distributed coordination, delivery, compatibility, and recovery problems. The projection is justified only when the independent change, scaling, failure, or ownership benefit exceeds that added cost.

## Pattern-Language Context

[[Microservice Pattern Language|The microservice pattern language]] expands this practice into decomposition, collaboration, data ownership, transactional messaging, communication, discovery, reliability, observability, security, testing, and deployment patterns. [[Pattern Languages and Correspondence|Realm correspondence]] keeps those decisions connected without making service, subdomain, bounded context, aggregate, database, team, and deployment unit synonyms.

## Failure Modes

The pattern fails when services are split by technical layer, table, team preference, or endpoint count rather than semantic ownership and operational boundary. It also fails when organization, repository, deployment, or scheduler boundaries are treated as proof of semantic independence; when supposedly independent services require coordinated releases; or when every team must rebuild the same communication, schema, deployment, scaling, and observability machinery. Distributed deployment does not create bounded-context clarity by itself.

## Formal relations

- `bundles`: [[Service]] — Adopts the boundary-relative service role as part of an alignment among semantic responsibility, ownership, deployment, and runtime realization.
- `constrains`: [[Service Models]] — Requires logical-service allocations to make independent evolution and the correspondences among semantic, organizational, deployment, and runtime boundaries explicit.

## External References

- Chris Richardson, [A Pattern Language for Microservices](https://microservices.io/patterns/).
- James Lewis and Martin Fowler, [Microservices](https://martinfowler.com/articles/microservices.html), 2014.
- Brad Hawkes and Chris Nokleberg, [Using Frameworks to Build Reliable Applications](https://research.google/pubs/using-frameworks-to-build-reliable-applications/), *ACM Queue*, 2020.
- Rachel Potvin and Josh Levenberg, [Why Google Stores Billions of Lines of Code in a Single Repository](https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/), *Communications of the ACM*, 2016.
- Ben Sigelman, [What We Got Wrong: Lessons from the Birth of Microservices](https://archive.qconlondon.com/london2019/presentation/what-we-got-wrong-lessons-birth-microservices), QCon London, 2019.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Service|service]], [[Service Models|service models]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Microservice Pattern Language|microservice pattern language]], [[Domain-Driven Design|domain-driven design]], [[Enterprise Integration Patterns|enterprise integration patterns]], [[Boundaries|boundaries]], [[Authority|authority]], [[Observer|observer]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Compatibility and Evolution|compatibility and evolution]], [[Coordination|coordination]], [[Scheduling|scheduling]], [[Recovery|recovery]], [[Infrastructure Graph|infrastructure graph]], [[Application Hosts|application hosts]], [[Brokers|brokers]], [[Network|network]], [[Realization|realization]], [[Modular Monolith|modular monolith]].
