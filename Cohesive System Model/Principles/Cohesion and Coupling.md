---
realm: Principles
kind: principle
created: 2026-08-21
updated: 2026-08-21
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

At a chosen scale, let

$$
G = (V, \{E_r\}_{r \in R}, \{w_r\}_{r \in R})
$$

be a typed, directed, weighted graph. The vertices $V$ are the elements to allocate. Each edge layer $E_r \subseteq V \times V$ denotes one declared relationship $r \in R$, such as a static call, data access, use-case participation, semantic affinity, co-change, runtime traffic, shared transaction, or ownership dependency. Its nonnegative weight function $w_r : V \times V \to \mathbb{R}_{\ge 0}$ has support $E_r$ and records the observed strength, expected cost, or declared importance of that relationship. Distinct layers preserve relation types that a single untyped dependency graph would erase; repeated observations of one typed pair may be aggregated while retaining their provenance.

A candidate modularization is a partition map

$$
\pi : V \to \{1, \ldots, k\},
$$

with module $M_a = \{u \in V \mid \pi(u)=a\}$. For each relationship type, the partition induces a weighted quotient graph:

$$
W^r_{ab} = \sum_{u \in M_a}\sum_{v \in M_b} w_r(u,v).
$$

The diagonal $W^r_{aa}$ is relationship weight retained inside module $M_a$; an off-diagonal value $W^r_{ab}$ is directed coupling from module $M_a$ to module $M_b$. Two basic totals are

$$
I_r(\pi) = \sum_a W^r_{aa}
\qquad\text{and}\qquad
X_r(\pi) = \sum_{a \ne b} W^r_{ab},
$$

where $I_r$ is internal association and $X_r$ is the cut or external association. For an undirected graph, each edge should be counted once under a consistent convention.

This formulation makes the criterion explicit but does not make it correct automatically. A static-call graph, a co-change graph, and a semantic-affinity graph can propose different partitions. Their weights may come from declared models, source analysis, execution traces, repository history, or expert judgment, and that provenance remains part of the interpretation.

Some relationships are naturally multiway. A use case or commit can involve a set of vertices and may be modeled as a hyperedge rather than as unrelated pairs. Projecting a large hyperedge into every possible pair can overweight large use cases or commits. Likewise, an element that participates in several features may require overlapping membership, an explicit shared module, or several projections rather than forced assignment to exactly one block.

## Nontrivial Objectives and Constraints

For one fixed edge relation, internal and external weight exhaust the same total:

$$
I_r(\pi) + X_r(\pi) = \sum_{(u,v) \in E_r} w_r(u,v).
$$

Maximizing internal weight is then equivalent to minimizing cut weight. If the number and size of modules are unconstrained, placing every vertex in one module is the trivial optimum. A useful formulation must say what makes a nontrivial boundary valuable.

Common choices include:

- Fixing $k$, bounding module size or relationship volume, or requiring a minimum balance.
- Penalizing semantic dispersion, internal complexity, oversized modules, or excessive module count.
- Declaring must-link constraints for elements that share an indivisible responsibility and cannot-link constraints for authority, security, ownership, or isolation requirements.
- Constraining dependency direction, cycles, public surface area, allowed protocols, or compatibility obligations.
- Assigning different crossing costs to local calls, compiler boundaries, team boundaries, and network or deployment boundaries.

Several established objectives illustrate different assumptions:

### Constrained cut and normalized cut

A minimum cut minimizes $X_r$ subject to a fixed, nonempty partition or other constraints. A multiway normalized cut instead minimizes

$$
\operatorname{Ncut}(\pi)
=
\sum_a
\frac{\operatorname{cut}_r(M_a,V\setminus M_a)}
     {\operatorname{vol}_r(M_a)},
$$

where $\operatorname{vol}_r(M_a)$ is the relationship volume incident on $M_a$. Normalization discourages partitions that obtain a small raw cut merely by isolating a tiny weakly connected set. It still requires a declared affinity relation, a nontrivial partition, and suitable treatment of direction and zero-volume vertices.

### Modularity

For one selected undirected weighted relationship layer with total edge weight $m$ and weighted degrees $d_u$, standard modularity is

$$
Q(\pi)
=
\frac{1}{2m}
\sum_{u,v}
\left(
w_{uv} - \frac{d_ud_v}{2m}
\right)
[\pi(u)=\pi(v)].
$$

The score rewards more internal weight than expected under a degree-preserving null model. This avoids prescribing $k$ directly, but the answer depends on the null model; standard modularity can merge small, well-defined communities in a large graph. Directed and multilayer graphs require corresponding null models rather than silent symmetrization.

### Software modularization quality

The Bunch software-clustering work represents program entities and their source dependencies as a module-dependency graph and searches for partitions with high internal and low external connectivity. In a commonly used weighted modularization-quality form, let $\mu_a$ be the internal edge weight of module $M_a$ and $\epsilon_a$ the total weight of edges entering or leaving it. Its cluster factor is

$$
CF_a =
\begin{cases}
0, & \mu_a = 0,\\
\dfrac{2\mu_a}{2\mu_a+\epsilon_a}, & \mu_a > 0,
\end{cases}
\qquad
MQ(\pi)=\sum_a CF_a.
$$

This is an important software-specific precedent for search-based graph partitioning. It remains a score over the chosen dependency graph; it does not by itself recover domain purpose, authority, or the desired deployment boundary.

### Multiple objectives

Real modularization is usually better represented as a constrained multi-objective problem, for example:

```text
minimize (
  semantic dispersion,
  static dependency cut,
  co-change cut,
  runtime traffic,
  cross-boundary transaction and authority obligations,
  module count, size imbalance, and operational overhead
)
```

The result is a set of Pareto tradeoffs unless policy supplies defensible weights for a scalar objective. Search-based software modularization has accordingly been formulated as a multi-objective problem rather than only as one scalar score. Spectral relaxations, hierarchical clustering, local search, and evolutionary search can explore the large partition space, but their outputs are candidate boundaries for semantic and operational review rather than an architectural oracle.

## Evidence and Validation

A graph objective can optimize only the evidence encoded in its vertices, edges, weights, constraints, and null model.

- No observed edge can mean no relationship, an unexercised path, missing instrumentation, unsupported language analysis, or simply unknown evidence.
- Static analysis can miss reflection and runtime binding; runtime traces reflect selected workloads and time windows.
- Co-change can reveal hidden dependencies, but it can also reflect batch commits, current team ownership, or the existing directory structure rather than the desired semantic design.
- Using present directory membership both to derive and to validate clusters makes the evaluation circular.
- Abundant low-cost calls can swamp rare but decisive invariant, authority, security, or failure relationships unless relation layers are normalized and weighted deliberately.
- Utility, framework, generated, and platform vertices often behave as high-degree hubs and may need an explicit role instead of ordinary cluster assignment.

Weights should therefore retain source, time window, confidence, and interpretation through [[Observability and Provenance|observability and provenance]]. Sensitivity to plausible weights and modeling choices should be checked. A proposed partition should also be evaluated against outcomes outside the optimization score: change locality, comprehension, interface stability, build and test scope, independent release, runtime traffic, transaction and coordination cost, failure propagation, and recovery.

Most importantly, dependency evidence does not define semantic meaning. [[Domain-Driven Design|Domain-driven design]], domain experts, declared [[Bounded Context|bounded contexts]], invariant scopes, and authority assignments provide evidence that source and runtime graphs cannot infer on their own. An algorithm can expose tension between those declarations and observed structure; it cannot decide which domain distinctions ought to exist.

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
- Lionel C. Briand, John W. Daly, and Jürgen Wüst, [“A Unified Framework for Cohesion Measurement in Object-Oriented Systems”](https://doi.org/10.1023/A:1009783721306), *Empirical Software Engineering* 3(1), 65–117, 1998.
- Lionel C. Briand, John W. Daly, and Jürgen K. Wüst, [“A Unified Framework for Coupling Measurement in Object-Oriented Systems”](https://doi.org/10.1109/32.748920), *IEEE Transactions on Software Engineering* 25(1), 91–121, 1999.
- Harald C. Gall, Karin Hajek, and Mehdi Jazayeri, [“Detection of Logical Coupling Based on Product Release History”](https://doi.org/10.1109/ICSM.1998.738508), *Proceedings of the International Conference on Software Maintenance*, 190–198, 1998.
- Brian S. Mitchell and Spiros Mancoridis, [“On the Automatic Modularization of Software Systems Using the Bunch Tool”](https://doi.org/10.1109/TSE.2006.31), *IEEE Transactions on Software Engineering* 32(3), 193–208, 2006.
- K. Praditwong, M. Harman, and X. Yao, [“Software Module Clustering as a Multi-Objective Search Problem”](https://doi.org/10.1109/TSE.2010.26), *IEEE Transactions on Software Engineering* 37(2), 264–282, 2011.
- M. E. J. Newman and M. Girvan, [“Finding and Evaluating Community Structure in Networks”](https://doi.org/10.1103/PhysRevE.69.026113), *Physical Review E* 69, 026113, 2004.
- Jianbo Shi and Jitendra Malik, [“Normalized Cuts and Image Segmentation”](https://doi.org/10.1109/34.868688), *IEEE Transactions on Pattern Analysis and Machine Intelligence* 22(8), 888–905, 2000.
- Santo Fortunato and Marc Barthélemy, [“Resolution Limit in Community Detection”](https://doi.org/10.1073/pnas.0605965104), *Proceedings of the National Academy of Sciences* 104(1), 36–41, 2007.
- Sven Apel and Dirk Beyer, [“Feature Cohesion in Software Product Lines: An Exploratory Study”](https://doi.org/10.1145/1985793.1985851), *Proceedings of the 33rd International Conference on Software Engineering*, 421–430, 2011.
- Jimmy Bogard, [“Vertical Slice Architecture”](https://www.jimmybogard.com/vertical-slice-architecture/), 2018.
- Alistair Cockburn, [“Hexagonal Architecture: The Original 2005 Article”](https://alistair.cockburn.us/hexagonal-architecture/), HaT Technical Report 2005.02.
