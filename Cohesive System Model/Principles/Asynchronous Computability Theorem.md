---
realm: Principles
kind: principle
created: 2026-06-28
updated: 2026-06-29
---

# Asynchronous Computability Theorem

The asynchronous computability theorem characterizes which distributed tasks can be solved wait-free in an asynchronous read/write system.

Where [[Progress Conditions|wait-free synchronization]] classifies the power of shared objects through consensus numbers, the asynchronous computability theorem gives a topological model of task solvability. It represents distributed configurations as simplicial complexes and solvability as the existence of an appropriate map between those complexes.

A distributed task is modeled by:

- An **input complex** describing possible initial configurations.
- An **output complex** describing possible final configurations.
- A **specification relation** `Delta` saying which outputs are legal for which inputs.

A configuration is represented by a simplex: vertices represent processes with local states, and the simplex records that those process states can coexist as one global configuration. Faces and shared vertices represent partial views and indistinguishability. This gives a notion of nearness between distributed configurations that is richer than ordinary graph adjacency.

Protocol executions subdivide the input complex into a protocol complex. A task is solvable when there is a color-preserving simplicial map from a subdivision of the input complex into the output complex, carried by the task specification. Intuitively, the protocol must continuously transform possible initial configurations into legal output configurations without tearing apart indistinguishable cases.

Consensus impossibility becomes geometric. Binary consensus requires decision regions for `0` and `1` that are disconnected in the output space, while the wait-free asynchronous protocol space preserves connectedness from the input space. There is no continuous, color-preserving map that both respects validity and separates the connected protocol space into the disjoint decision configurations consensus would require.

This is one way the theorem makes the impossibility visually satisfying: the obstruction can be seen as the absence of a suitable continuous map from possible executions to legal decisions.

The model does not require wall-clock time as a primitive. Time is displaced into protocol subdivisions and maps: execution appears as refinement of possible configurations, and computability is stated in terms of structure-preserving transformations.

## Relationship to Consensus

The theorem provides a formal account of why [[Consensus|consensus]] cannot be solved wait-free in the basic asynchronous read/write model for more than one process. This is adjacent to, but distinct from, FLP:

- FLP concerns deterministic message-passing consensus with crash failures and shows that termination cannot be guaranteed in a fully asynchronous system with one faulty process.
- The asynchronous computability theorem concerns wait-free task solvability and describes the topological obstruction in the read/write model.

Both results connect [[Safety and Liveness|safety and liveness]] to model structure. Consensus safety can be stated, but the progress condition cannot be satisfied under the stated assumptions.

## External References

- Maurice Herlihy and Nir Shavit, [The Asynchronous Computability Theorem for t-Resilient Tasks](https://groups.csail.mit.edu/tds/papers/Shavit/STOC93.pdf), STOC 1993.
- Maurice Herlihy and Nir Shavit, [The Topological Structure of Asynchronous Computability](https://cs.brown.edu/people/mph/HerlihyS99/p858-herlihy.pdf), Journal of the ACM, 46(6):858-923, November 1999.
- Leo Gorodinski, [The Asynchronous Computability Theorem](https://medium.com/@eulerfx/the-asynchronous-computability-theorem-171e9d7b9423), 2019.

Related concepts: [[Progress Conditions|progress conditions]], [[Consensus|consensus]], [[Safety and Liveness|safety and liveness]], [[Coordination|coordination]], [[CALM Theorem|CALM theorem]], [[Universal Constructions|universal constructions]], [[Compositionality|compositionality]], [[Enrichment and Order|enrichment and order]], [[State|state]], [[Observation|observation]], [[Process|process]].
