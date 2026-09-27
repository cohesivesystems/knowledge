---
realm: Principles
kind: reference
created: 2026-09-07
updated: 2026-09-07
status: draft
aliases:
  - Software Module Clustering
  - Software Modularization Metrics
---

# Graph Partitioning and Software Modularization

Graph partitioning and software modularization methods formulate candidate module boundaries as optimization problems over declared relation graphs. They provide evidence for [[Cohesion and Coupling|cohesion and coupling]], but they do not determine semantic meaning or architectural authority.

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

## Formal relations

- `documents`: [[Cohesion and Coupling]] — Surveys graph formulations and optimization methods that provide candidate modular boundaries while leaving semantic interpretation and architectural authority explicit.

## External References

- Lionel C. Briand, John W. Daly, and Jürgen Wüst, [“A Unified Framework for Cohesion Measurement in Object-Oriented Systems”](https://doi.org/10.1023/A:1009783721306), *Empirical Software Engineering* 3(1), 65–117, 1998.
- Lionel C. Briand, John W. Daly, and Jürgen K. Wüst, [“A Unified Framework for Coupling Measurement in Object-Oriented Systems”](https://doi.org/10.1109/32.748920), *IEEE Transactions on Software Engineering* 25(1), 91–121, 1999.
- Harald C. Gall, Karin Hajek, and Mehdi Jazayeri, [“Detection of Logical Coupling Based on Product Release History”](https://doi.org/10.1109/ICSM.1998.738508), *Proceedings of the International Conference on Software Maintenance*, 190–198, 1998.
- Brian S. Mitchell and Spiros Mancoridis, [“On the Automatic Modularization of Software Systems Using the Bunch Tool”](https://doi.org/10.1109/TSE.2006.31), *IEEE Transactions on Software Engineering* 32(3), 193–208, 2006.
- K. Praditwong, M. Harman, and X. Yao, [“Software Module Clustering as a Multi-Objective Search Problem”](https://doi.org/10.1109/TSE.2010.26), *IEEE Transactions on Software Engineering* 37(2), 264–282, 2011.
- M. E. J. Newman and M. Girvan, [“Finding and Evaluating Community Structure in Networks”](https://doi.org/10.1103/PhysRevE.69.026113), *Physical Review E* 69, 026113, 2004.
- Jianbo Shi and Jitendra Malik, [“Normalized Cuts and Image Segmentation”](https://doi.org/10.1109/34.868688), *IEEE Transactions on Pattern Analysis and Machine Intelligence* 22(8), 888–905, 2000.
- Santo Fortunato and Marc Barthélemy, [“Resolution Limit in Community Detection”](https://doi.org/10.1073/pnas.0605965104), *Proceedings of the National Academy of Sciences* 104(1), 36–41, 2007.
