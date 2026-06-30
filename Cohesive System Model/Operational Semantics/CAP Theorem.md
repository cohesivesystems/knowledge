---
realm: Operational Semantics
kind: operational-semantics
---

# CAP Theorem

The CAP theorem describes an impossibility for distributed shared data under network partition: a system cannot simultaneously guarantee linearizable consistency, availability, and partition tolerance for all executions.

In the Gilbert-Lynch formulation:

- **Consistency** means atomic, or linearizable behavior for a shared object.
- **Availability** means every request to a non-failing node eventually receives a response.
- **Partition tolerance** means the system continues to operate in executions where messages between partitions may be lost or delayed indefinitely.

Partition is a failure condition. When a partition occurs, the system must decide whether to preserve the safety property of linearizable consistency by refusing or delaying some operations, or preserve the liveness property of availability by responding without enough information to guarantee one linearized history.

CAP therefore relates [[Safety and Liveness|safety and liveness]], [[Consistency Models|consistency models]], [[Coordination|coordination]], [[Consensus|consensus]], and [[Network|network]] behavior. It says that failure is part of the model: a consistency claim made only when the network is healthy is different from a consistency claim made through partitions.

CAP also uses narrower meanings than many architecture discussions:

- CAP consistency is not ACID consistency in the database acronym; it is closer to [[Consistency Models|linearizability]].
- CAP availability is not uptime, SLO compliance, or "the service usually works"; it is a progress property for requests to non-failing nodes.
- Partition tolerance is not a feature to opt into for any networked system; it is the failure scenario in which the tradeoff becomes observable.

Many practical systems choose finer-grained behavior than a global CAP label: preserve consistency for one key range while refusing writes, allow stale reads from followers, accept local writes and reconcile later, require quorum for some commands, or expose pending states until coordination or recovery completes. The boundary of the claim matters.

## External References

- Seth Gilbert and Nancy Lynch, [Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services](https://www.cs.princeton.edu/courses/archive/spr22/cos418/papers/cap.pdf), ACM SIGACT News, 33(2):51-59, June 2002.
- Eric Brewer, [CAP Twelve Years Later: How the "Rules" Have Changed](https://sites.cs.ucsb.edu/~rich/class/cs293b-cloud/papers/brewer-cap.pdf), Computer, 45(2):23-29, February 2012.

Related concepts: [[Safety and Liveness|safety and liveness]], [[Consistency Models|consistency models]], [[Consensus|consensus]], [[Consensus Protocols|consensus protocols]], [[Coordination|coordination]], [[Network|network]], [[Recovery|recovery]], [[Weak Isolation Patterns|weak isolation patterns]], [[CRDTs]], [[Boundaries|boundaries]].
