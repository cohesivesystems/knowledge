---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-28
updated: 2026-07-04
---

# Consensus Protocols

Consensus Protocols are concrete protocol families that [[Realization|realize]] [[Consensus|consensus]] under specified network, failure, timing, persistence, and membership assumptions.

Protocols such as Paxos, Multi-Paxos, Raft, Zab, and Viewstamped Replication use quorum intersection, terms or epochs, durable metadata, and recovery rules to make distributed participants agree on values or log positions. In practice they are most often used to build replicated logs, replicated state machines, leader election, membership changes, configuration stores, and strongly consistent storage partitions.

A consensus protocol usually provides:

- A proposal or command value to decide.
- A ballot, term, epoch, or view that orders competing leadership attempts.
- A quorum rule that prevents two incompatible decisions from both committing.
- A replicated log or sequence of consensus instances.
- A commit rule that determines when a value is durable enough to expose.
- Recovery behavior that preserves decided values across crashes, restarts, and leader changes.

Consensus protocols are a realization choice, not typically a domain concept. They can support [[Consistency Models|linearizability]], strict serializability, and coherent replicated state, but only at the boundary they actually govern. Read routing, follower reads, caches, projections, asynchronous replication, membership changes, and clock or lease assumptions can weaken the guarantee exposed to observers.

The cost is coordination. Consensus protocols preserve a chosen [[Ordering|order]] by requiring communication, durable metadata, quorum participation, and failure detection or timing assumptions. This can increase latency, reduce availability during partitions, and create operational coupling, but it lets systems construct distributed behavior that can be reasoned about using a sequential specification.

Operationally, consensus protocols tend to preserve [[Safety and Liveness|safety]] even when progress is temporarily impossible. Their liveness depends on the behavior of participants, storage, and network, and on timing assumptions.

In terms of [[Orchestration and Choreography|orchestration and choreography]], Paxos is closer to choreography than to an index rebuild coordinated by one process manager. It has a shared global protocol and a singular replicated-state-machine goal, and a leader or proposer may coordinate a round. But the leader is a dynamic protocol role constrained by quorum rules, acceptor state, ballots, and recovery behavior. No single node monitors and controls the whole execution in the way an index rebuild coordinator assigns work, records progress, retries workers, and decides completion.

## External References

- Leslie Lamport, [Paxos Made Simple](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf), ACM SIGACT News, 32(4):51-58, December 2001.
- Diego Ongaro and John Ousterhout, [In Search of an Understandable Consensus Algorithm](https://raft.github.io/raft.pdf), USENIX ATC, 2014.
- Barbara Liskov and James Cowling, [Viewstamped Replication Revisited](https://www.cs.princeton.edu/courses/archive/fall19/cos418/papers/vr-revisited.pdf), MIT CSAIL, 2012.

Related concepts: [[Consensus|consensus]], [[Orchestration and Choreography|orchestration and choreography]], [[Safety and Liveness|safety and liveness]], [[CAP Theorem|CAP theorem]], [[Coordination|coordination]], [[Consistency Models|consistency models]], [[Ordering|ordering]], [[Time|time]], [[Version|version]], [[Persistence|persistence]], [[Recovery|recovery]], [[Storage Systems|storage systems]], [[Infrastructure|infrastructure]], [[Network|network]], [[Brokers|brokers]], [[Actor Systems|actor systems]].
