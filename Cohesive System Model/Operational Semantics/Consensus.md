---
realm: Operational Semantics
kind: operational-semantics
---

# Consensus

Consensus answers: how do multiple [[Observer|observers]] agree on one decision, value, or ordered position despite concurrency, delay, partial failure, or independent local views?

Consensus is a form of [[Coordination|coordination]] used to achieve a desired [[Consistency Models|consistency model]] at a declared boundary. It converts competing proposals into one agreed outcome, which can then be interpreted as a committed operation, log entry, leader term, membership change, or version position.

A consensus object is usually characterized by:

- **Agreement**: correct participants decide the same value.
- **Validity**: the decided value comes from the proposed values.
- **Termination**: correct participants eventually decide under the system assumptions.
- **Integrity**: participants do not decide more than once for the same consensus instance.

These properties split across [[Safety and Liveness|safety and liveness]]. Agreement, validity, and integrity are safety properties: they forbid bad decisions. Termination is a liveness property: it requires progress. The FLP result concerns this liveness side, showing that deterministic consensus cannot guarantee termination in a fully asynchronous system with even one crash failure.

[[Progress Conditions]] make the liveness side more precise. In the wait-free synchronization model, every operation must complete despite the speed or failure of other participants. In asynchronous message-passing consensus, termination depends on different assumptions, such as partial synchrony, randomized progress, or eventual leadership.

The [[Asynchronous Computability Theorem|asynchronous computability theorem]] gives a topological account of this impossibility in the asynchronous read/write model: consensus would require a map from possible protocol configurations into disjoint decision configurations, but the required continuous, color-preserving map does not exist.

Consensus is powerful because it supplies an agreed order or decision where the distributed system otherwise has only partial, observer-relative knowledge. Once operations are agreed in a common sequence, replicas can apply the same deterministic sequential specification and produce equivalent state. This is the basis of state-machine replication and of the **universality of consensus**: consensus can be used to construct a distributed, linearizable implementation of an object from its sequential specification.

In Cohesive terms, consensus often decides which input [[Command|command]], [[Event|event]], or transition proposal becomes the next endogenous [[Event|event]] or [[Version|version]] at a boundary. The decided value is not automatically domain-valid; it must still be interpreted by the boundary's [[Transition|transition]], [[Invariants|invariants]], and [[Policies|policies]].

Consensus should not be treated as "consistency" in general. It is one coordination primitive for constructing certain consistency guarantees. It requires assumptions about failures, quorum intersection, network timing, persistence, membership, and recovery. Under stronger timing assumptions or randomized protocols, termination can be obtained in practical settings; in a fully asynchronous system with even one crash failure, deterministic consensus cannot guarantee termination.

Consensus is a synchronizing construction in the sense of [[Synchrony and Asynchrony|synchrony and asynchrony]]: multiple proposals, observations, or participant states are joined into one decided value or log position. The join is logical, not wall-clock simultaneous.

## Universality

Consensus gives a universal construction for distributed objects: decide the next operation, apply it to the local state machine, return the operation's result, and repeat. The distributed implementation inherits the sequential object's meaning by making all correct replicas apply operations in the same agreed order.

This connects [[Universal Constructions|universal constructions]] to operational semantics. A sequential specification supplies the transition rule; consensus supplies the ordered choice of which operation is next; [[Consistency Models|linearizability]] supplies the correctness condition that lets observers reason as if the distributed object were atomic.

## External References

- Leo Gorodinski, [Universality of Consensus](https://medium.com/@eulerfx/universality-of-consensus-feceead50641), 2017.
- Maurice P. Herlihy, [Wait-Free Synchronization](https://cs.brown.edu/people/mph/Herlihy91/p124-herlihy.pdf), ACM Transactions on Programming Languages and Systems, 13(1):124-149, January 1991.
- Maurice Herlihy and Nir Shavit, [The Topological Structure of Asynchronous Computability](https://cs.brown.edu/people/mph/HerlihyS99/p858-herlihy.pdf), Journal of the ACM, 46(6):858-923, November 1999.
- Michael J. Fischer, Nancy A. Lynch, and Michael S. Paterson, [Impossibility of Distributed Consensus with One Faulty Process](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf), Journal of the ACM, 32(2):374-382, April 1985.
- Rachid Guerraoui and Michel Raynal, [The Alpha of Indulgent Consensus](https://doi.org/10.1093/comjnl/bxl046), The Computer Journal, 50(1):53-67, January 2007.

Related concepts: [[Coordination|coordination]], [[Consensus Protocols|consensus protocols]], [[Safety and Liveness|safety and liveness]], [[Progress Conditions|progress conditions]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Asynchronous Computability Theorem|asynchronous computability theorem]], [[CAP Theorem|CAP theorem]], [[Consistency Models|consistency models]], [[Ordering|ordering]], [[Version Histories|version histories]], [[Time|time]], [[Version|version]], [[State|state]], [[Event|event]], [[Command|command]], [[Transition|transition]], [[Invariants|invariants]], [[Policies|policies]], [[Universal Constructions|universal constructions]].
