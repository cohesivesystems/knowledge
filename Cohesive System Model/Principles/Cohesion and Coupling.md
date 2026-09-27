---
realm: Principles
kind: principle
created: 2026-08-21
updated: 2026-09-07
status: draft
aliases:
  - High Cohesion and Low Coupling
  - Software Cohesion and Coupling
---

# Cohesion and Coupling

Cohesion and coupling are boundary-relative principles for evaluating how the elements of a system are allocated to modules. Cohesion asks how strongly the elements placed inside one module belong together under a chosen relationship. Coupling asks what dependencies, shared assumptions, or coordination obligations cross between modules and how strong those crossings are.

Neither property belongs intrinsically to a folder, class, service, or other container. A claim of high cohesion or low coupling must identify:

- The elements being allocated.
- The proposed module [[Boundaries|boundaries]].
- The relationship or evidence by which the elements belong together or depend on one another.
- The scale at which the allocation is being evaluated.
- The purpose, observer, workload, and time window for which the measure is relevant.

The familiar goal of *high cohesion within modules and low coupling between modules* is therefore a parameterized design objective, not a context-free score. A directory can make related source easy to find without enforcing encapsulation. A compiler-visible project can enforce some code dependencies without defining a semantic boundary. A separately deployed [[Service|service]] can isolate release and failure behavior while remaining tightly coupled through data, protocols, or coordinated change.

## Measure-Relative Meanings

Different relationships produce different cohesion and coupling measures over the same elements:

| Criterion | Evidence for cohesion within a module | Evidence for coupling across modules |
| --- | --- | --- |
| Semantic purpose | One capability, use case, policy, vocabulary, or invariant scope explains why the elements belong together. | A concept, rule, decision, or invariant must be understood or changed across several boundaries. |
| Change and evolution | Elements repeatedly change for the same reason and can be reviewed, tested, and released together. | One requirement or defect propagates changes across modules, repositories, or teams. |
| Static code structure | Calls, imports, type references, inheritance, and data access remain local behind an explicit interface. | Compiler-visible dependencies or access to another module's internals cross the boundary. |
| Runtime interaction | Work with strong locality, cadence, or data affinity executes together. | Calls, messages, shared state, traffic, latency, availability, or version assumptions cross runtime boundaries. |
| Authority and consistency | Rules and writes governed by one [[Authority\|authority]] and one invariant or [[Commit Boundaries\|commit boundary]] remain together. | Correctness requires cross-authority agreement, distributed commitment, reconciliation, or compensating action. |
| Ownership and operation | One accountable group can build, test, release, scale, observe, and recover the unit. | Work requires synchronized ownership, rollout, scaling, incident response, or recovery across units. |

These measures can disagree. Co-locating two chatty components may reduce runtime coupling while mixing separate authorities. Separating independently released capabilities may improve change cohesion while adding network and compatibility obligations. A deliberately narrow [[Interfaces|interface]] is still a coupling edge, but its direction, stability, semantic scope, and substitutability may make it preferable to implicit shared state or access to internals.

Low coupling does not mean no relationships. A useful system must compose, and [[Compositionality|composition]] requires connections. The design objective is to keep necessary relationships local where that preserves meaning and to make necessary boundary crossings explicit, appropriately weak, and governed by suitable contracts and guarantees.

## Classical Terminology

Structured design introduced a qualitative cohesion taxonomy. In the later conventional vocabulary, it is ordered from coincidental, logical, temporal, procedural, communicational, and sequential cohesion to functional cohesion. The categories characterize *why processing elements were placed in one module*; they are not equally spaced numerical levels and should not be transferred to every modern modular unit without qualification.

Two terms are especially easy to reverse:

- **Logical cohesion** groups several distinct operations because they belong to the same general category, often with one operation selected by a control parameter. A module that performs one of several kinds of input, or a source tree that groups all controllers merely because they are controllers, is the closer analogy. In the classical terminology, logical cohesion does not mean that every element implements one product feature.
- **Functional cohesion** means that every element is necessary for one well-defined task. A narrow end-to-end use case may exhibit functional cohesion when its input handling, policy, persistence interaction, and result production all contribute to that one task. A broad feature containing several independently changing use cases does not become functionally cohesive merely because it has one folder name.

*Feature cohesion* is a later and measure-specific term, not a synonym for logical cohesion. In feature-oriented software-product-line research, it measures how strongly the program elements assigned to a stakeholder-visible feature depend on elements of that same feature. In application architecture, *feature* may instead mean a request, use case, business capability, screen flow, or bounded area of a product. The intended meaning must be stated before feature cohesion can be evaluated.

The phrase *logical coupling* has also been used in software-evolution research for dependencies inferred from modules that repeatedly change together. This note calls that relation *co-change* or *evolutionary coupling* to keep it distinct from the classical logical-cohesion category.

## Scale and Realm

A scale is not a Cohesive realm. Scale identifies the granularity of the elements and candidate modules: expressions may be allocated to functions or methods, functions and methods to classes or types, classes to files or packages, packages to projects or compiler-visible solutions, code modules to services, and services to larger systems. A partition at one scale can induce a quotient graph whose modules become the elements considered at the next scale.

A realm identifies what kind of claim is being made:

- In Domain Semantics, cohesion can concern shared purpose, language, rules, identities, processes, invariants, and authority.
- In the [[System Graph|system graph]], it can concern how entities, processes, services, [[Interaction|interactions]], surfaces, interfaces, and boundaries are composed.
- In Operational Concerns, coupling can concern compatibility, coordination, consistency, latency, capacity, failure, recovery, and other required behavior at declared boundaries.
- In the [[Realization|realization substrate]], it can concern symbols, calls, imports, packages, build graphs, artifacts, stores, protocols, deployment units, processes, and networks.
- In Architecture Practices, it can guide how semantic responsibility, code, change, ownership, deployment, and operation are aligned without making those structures identical.

The concept belongs in Principles because it disciplines how boundaries and allocations in every other realm are evaluated; it is not itself one architecture practice or realization mechanism.

The correspondences among these partitions are not identities. One semantic capability may use several code modules; one code project may realize parts of several capabilities; one logical service may produce several artifacts and runtime roles; and one deployment may host several logical services. Feature implementations and cross-cutting concerns can also overlap rather than form a strict partition. A hierarchy of folders, projects, and services is therefore one possible projection of several related structures, not proof that their boundaries coincide.

Boundary cost changes with scale. A function call inside one process, a compiler dependency between projects, and a versioned request across a network may carry the same business value while having very different latency, failure, compatibility, observability, and recovery obligations. Moving a cut from a folder to a service can preserve the intended semantic partition while materially changing its operational coupling.

## Graph-Theoretic Formulation

At a chosen scale, cohesion and coupling can be represented through a typed, directed, weighted relation graph whose candidate modules form a partition. Internal relation weight, cross-boundary cuts, direction, module balance, and must-link or cannot-link constraints make the selected measure explicit.

That formulation does not discover meaning automatically. Static-call, co-change, runtime, and semantic-affinity graphs can support different partitions, while unconstrained cut objectives admit trivial solutions. [[Graph Partitioning and Software Modularization|Graph partitioning and software modularization]] surveys the relevant formulations, objectives, evidence limits, and search methods. Its outputs remain candidate boundaries for semantic and operational review.

## Correspondence with Architecture Practices

The same cohesion-and-coupling principle appears in several practices, but each emphasizes a different relation or constraint:

| Practice | Primary emphasis |
| --- | --- |
| Package by technical layer | Groups categorically similar mechanisms such as controllers or repositories. This resembles classical logical cohesion when category alone is the reason for grouping, though a well-defined layer can also enforce meaningful dependency constraints. |
| [[Vertical Slice Architecture\|vertical slice architecture]] | Groups the code needed for a request, use case, or feature and seeks to keep change and use-case dependencies within the slice. It optimizes an axis of purpose and change rather than removing every internal layer or shared abstraction. |
| [[Clean Architecture\|clean architecture]] | Constrains dependency direction so stable semantic policy does not depend on volatile mechanisms. Direction and stability can matter more than the number of crossing edges, and clean dependency rules can be applied inside feature-oriented modules. |
| [[Ports and Adapters\|ports and adapters]] | Gives selected boundary crossings purposeful ports and technology-specific adapters. It types, directs, and makes coupling substitutable; it does not choose the semantic partition or eliminate the crossing. |
| [[Modular Monolith\|modular monolith]] | Uses compiler-visible modules, interfaces, visibility, and dependency rules to enforce cohesive code boundaries while retaining a shared source and build graph. |
| [[Microservice Architecture\|microservice architecture]] | Projects selected semantic and code boundaries into independently evolving ownership, deployment, runtime, and failure profiles. That projection adds network, protocol, versioning, data, coordination, observability, and operational crossing costs. A code cluster is evidence for a candidate service, not proof of one. |

These practices can compose. A system can organize top-level modules by capability, use [[Vertical Slice Architecture|vertical slices]] within them, preserve inward dependency direction, expose ports at module boundaries, compile the modules in one solution, and deploy selected boundaries as microservices. The useful question is not which label wins, but which partitions and dependency constraints preserve the intended meaning and guarantees at each scale.

## Modeling Checks

- What exactly are the vertices, candidate modules, and boundary type?
- Which relationship makes two elements cohesive, and which crossing constitutes coupling?
- Is the graph directed, typed, weighted, temporal, overlapping, or multiway?
- What provenance and time window support each relation and weight?
- What prevents the all-in-one or one-element-per-module solution?
- Which constraints express meaning, authority, security, dependency direction, or operational necessity?
- Which objectives conflict, and who has authority to choose among the tradeoffs?
- Which boundary crossings are harmful, and which are explicit, stable, and necessary interfaces?
- Does the proposed code partition correspond to semantic, ownership, deployment, and runtime structures without identifying them?
- Which observed outcomes will validate or falsify the proposed improvement?

## Formal relations

- `constrains`: [[Boundaries]] — Requires a claim about modular boundary quality to identify the allocated elements, relationship measure, scale, crossing cost, and nontrivial partition conditions.

## External References

- Wayne P. Stevens, Glenford J. Myers, and Larry L. Constantine, [“Structured Design”](https://doi.org/10.1147/sj.132.0115), *IBM Systems Journal* 13(2), 115–139, 1974.
- Edward Yourdon and Larry L. Constantine, [*Structured Design: Fundamentals of a Discipline of Computer Program and Systems Design*](https://books.google.com/books?id=zMQmAAAAMAAJ), Prentice Hall, 1979.
- David L. Parnas, [“On the Criteria To Be Used in Decomposing Systems into Modules”](https://doi.org/10.1145/361598.361623), *Communications of the ACM* 15(12), 1053–1058, 1972.
- Sven Apel and Dirk Beyer, [“Feature Cohesion in Software Product Lines: An Exploratory Study”](https://doi.org/10.1145/1985793.1985851), *Proceedings of the 33rd International Conference on Software Engineering*, 421–430, 2011.
- Jimmy Bogard, [“Vertical Slice Architecture”](https://www.jimmybogard.com/vertical-slice-architecture/), 2018.
- Alistair Cockburn, [“Hexagonal Architecture: The Original 2005 Article”](https://alistair.cockburn.us/hexagonal-architecture/), HaT Technical Report 2005.02.
