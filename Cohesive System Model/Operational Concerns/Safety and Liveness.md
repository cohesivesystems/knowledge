---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-28
updated: 2026-07-01
---

# Safety and Liveness

Safety and Liveness separate two kinds of operational property of a distributed system.

**Safety** says that nothing bad happens. A safety violation is witnessed by a finite history prefix: an invalid transition commits, two replicas decide different values, an invariant is broken, a duplicate non-idempotent effect occurs, or an observer sees a history the model forbids.

**Liveness** says that something good eventually happens. A liveness property is about progress: a request eventually returns, a command is eventually accepted or rejected, a message is eventually delivered, a replica eventually catches up, a process eventually recovers, or a consensus instance eventually decides.

These properties are complementary but can be in tension. A system can preserve safety by refusing to act. A system can claim liveness by postponing correctness to an unbounded future. Useful operational concerns must therefore say both what is forbidden and what progress is promised under which failure, timing, retry, recovery, and fairness assumptions.

## Distributed Tension

In distributed systems, uncertainty makes the safety/liveness split unavoidable. A slow participant may be crashed, partitioned, overloaded, paused, or merely delayed. If the system proceeds without enough information, it may violate safety. If it waits for information that may never arrive, it may violate liveness.

[[Coordination]] is often the mechanism used to preserve safety under uncertainty. [[Recovery]], retry, failure detection, leader election, quorum availability, and partial synchrony assumptions are often the mechanisms used to regain liveness.

[[Consistency Models]] are primarily safety properties over histories: they constrain which observations and results are allowed. Availability, termination, delivery, recovery, and eventual convergence are liveness or progress properties. A complete operational claim usually needs both.

[[Progress Conditions]] refine liveness claims by saying who is guaranteed to complete: every participant, some participant, or only a participant that eventually runs without interference. This distinction matters when a system uses locks, retries, actors, quorum protocols, consensus, or coordination avoidance.

## Consensus

[[Consensus]] exposes the split directly:

- Agreement, validity, and integrity are safety properties.
- Termination is a liveness property.

The FLP result shows that deterministic consensus cannot guarantee termination in a fully asynchronous system with even one crash failure. Consensus protocols therefore preserve safety under broad uncertainty, while their liveness depends on additional assumptions such as partial synchrony, quorums of live participants, randomized progress, reliable storage, or eventually accurate failure detection.

The [[Asynchronous Computability Theorem|asynchronous computability theorem]] gives a complementary wait-free account in the read/write model. It represents configurations topologically and shows that, for consensus, the required progress condition would demand a structure-preserving map that does not exist.

This is the perspective behind indulgent consensus. The **Alpha** abstraction captures the safety part of a family of consensus algorithms, while **Omega**-style eventual leadership or failure-detection assumptions supply the progress side once the environment becomes sufficiently well behaved.

## CAP

The [[CAP Theorem|CAP theorem]] is a safety/liveness tradeoff under network partition. In the CAP formulation, consistency is a safety property for a shared object, availability is a liveness property for requests to non-failing nodes, and partition tolerance is the failure condition under which the tradeoff is forced.

This is why the slogan "choose two" is misleading. In the presence of a partition, preserving linearizable consistency may require refusing or delaying operations, weakening availability. Preserving availability may require serving responses that cannot be guaranteed linearizable. The theorem is about behavior under failure, not a general taxonomy of databases.

## External References

- Bowen Alpern and Fred B. Schneider, [Defining Liveness](https://www.cs.cornell.edu/fbs/publications/DefLiveness.pdf), Information Processing Letters, 21(4):181-185, October 1985.
- Michael J. Fischer, Nancy A. Lynch, and Michael S. Paterson, [Impossibility of Distributed Consensus with One Faulty Process](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf), Journal of the ACM, 32(2):374-382, April 1985.
- Maurice Herlihy and Nir Shavit, [The Topological Structure of Asynchronous Computability](https://cs.brown.edu/people/mph/HerlihyS99/p858-herlihy.pdf), Journal of the ACM, 46(6):858-923, November 1999.
- Rachid Guerraoui and Michel Raynal, [The Alpha of Indulgent Consensus](https://doi.org/10.1093/comjnl/bxl046), The Computer Journal, 50(1):53-67, January 2007.
- Leo Gorodinski, [The Asynchronous Computability Theorem](https://www.gorodinski.com/The-Asynchronous-Computability-Theorem-3188cf7881f980d9b170dfbb0780a971), 2019.

Related concepts: [[Coordination|coordination]], [[Consensus|consensus]], [[Consensus Protocols|consensus protocols]], [[Progress Conditions|progress conditions]], [[Asynchronous Computability Theorem|asynchronous computability theorem]], [[CAP Theorem|CAP theorem]], [[Consistency Models|consistency models]], [[Ordering|ordering]], [[Recovery|recovery]], [[Retry|retry]], [[Delivery Semantics|delivery semantics]], [[Network|network]], [[Invariant|invariants]], [[Cohesive System Model/Operational Concerns/Weak Isolation Patterns|weak isolation patterns]], [[CRDTs]].
