---
realm: Principles
kind: principle
created: 2026-06-28
updated: 2026-06-29
---

# CALM Theorem

The CALM theorem, "Consistency as Logical Monotonicity", states that a program has a consistent, coordination-free distributed implementation if and only if it can be expressed in monotonic logic.

Monotonicity means that adding new input facts cannot invalidate conclusions already produced. If a computation only accumulates information, then replicas can process messages in different orders, at different times, and with partial local knowledge while still converging without synchronous [[Coordination|coordination]].

Non-monotonic computation depends on absence, exclusion, negation, exact completeness, or globally current knowledge. Those decisions usually require coordination, a narrower ownership boundary, a reservation or escrow scheme, a pending state, or a weaker domain promise.

In Cohesive terms, CALM gives a test for coordination avoidance:

- Monotone transitions, projections, and merge rules can often be implemented with asynchronous delivery and eventual convergence.
- Non-monotone invariants require some mechanism that establishes enough completeness or exclusion before the decision is exposed.
- [[CRDTs]] are one realization family for monotone replicated state, but CALM applies at the program and observation level, not only at the data type level.
- [[Weak Isolation Patterns]] often work by making non-monotonicity explicit through versions, reservations, pending states, compensation, reconciliation, or scoped coordination.

CALM is therefore not a replacement for [[Consistency Models|consistency models]]. It explains when a useful consistency guarantee can be obtained without coordination, and when coordination or model redesign is required.

Like the [[Asynchronous Computability Theorem|asynchronous computability theorem]], CALM is a computability-oriented constraint on distributed design. CALM uses logical monotonicity to characterize when coordination can be avoided; ACT uses topology to characterize when wait-free tasks can be solved.

## External References

- Joseph M. Hellerstein and Peter Alvaro, [Keeping CALM: When Distributed Consistency Is Easy](https://arxiv.org/abs/1901.01930), arXiv, 2019; Communications of the ACM, 63(9):72-81, 2020. [DOI](https://doi.org/10.1145/3369736)
- Peter Alvaro, Neil Conway, Joseph M. Hellerstein, and William R. Marczak, [Consistency Analysis in Bloom: a CALM and Collected Approach](https://people.ucsc.edu/~palvaro/cidr11.pdf), CIDR 2011.

Related concepts: [[Coordination|coordination]], [[Consistency Models|consistency models]], [[Safety and Liveness|safety and liveness]], [[Asynchronous Computability Theorem|asynchronous computability theorem]], [[Ordering|ordering]], [[Delivery Semantics|delivery semantics]], [[Weak Isolation Patterns|weak isolation patterns]], [[CRDTs]], [[Invariant|invariants]], [[Projection Models|projection models]], [[Observation|observation]], [[Compositionality|compositionality]], [[Universal Constructions|universal constructions]].
