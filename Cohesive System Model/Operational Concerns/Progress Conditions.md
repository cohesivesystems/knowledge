---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-28
updated: 2026-07-01
---

# Progress Conditions

Progress Conditions classify liveness guarantees for concurrent or distributed operations.

A progress condition says who is guaranteed to make progress, under what interference, scheduling, failure, retry, and timing assumptions. It refines [[Safety and Liveness|liveness]] by distinguishing system-wide progress from per-participant progress, and weak eventual progress from bounded completion.

Progress conditions are model-relative. A guarantee stated for shared-memory algorithms does not automatically transfer to message-passing systems, databases, actors, brokers, or distributed services. The model must say what can pause, crash, partition, retry, or interfere.

## Common Conditions

- **Blocking**: progress may depend on another participant releasing a lock, completing a critical section, or recovering. If that participant stalls or crashes, others may be unable to proceed.
- **Deadlock-free**: the system as a whole does not get permanently stuck, but an individual participant may still starve.
- **Starvation-free** or **lockout-free**: every eligible participant eventually completes under the stated fairness assumptions.
- **Obstruction-free**: an operation completes if it eventually runs in isolation for long enough.
- **Lock-free**: the system as a whole makes progress; some operation completes in a finite number of steps, though individual operations may starve.
- **Wait-free**: every operation completes in a finite number of its own steps regardless of the speed or failure of other participants, under the model's assumptions.
- **Bounded wait-free**: wait-freedom with an explicit finite step bound.
- **Population-oblivious wait-free**: bounded wait-freedom where the bound does not depend on the number of participating processes.

The usual non-blocking hierarchy is:

```txt
wait-free => lock-free => obstruction-free
```

The implication is one-way. A lock-free algorithm may starve one participant forever while some other participant keeps completing operations. An obstruction-free algorithm may require a contention manager, backoff, or scheduler behavior to avoid livelock under interference.

## Coordination

Progress conditions matter for [[Coordination|coordination]] because stronger progress guarantees reduce dependence on other participants. A wait-free operation does not need another participant to release a lock or complete a protocol step before it can finish. A blocking operation may be simpler and faster in the uncontended case, but it couples progress to the participant currently holding the resource.

[[Synchrony and Asynchrony]] should not be reduced to blocking and non-blocking. A logical operation may synchronously wait for a result while the runtime implements that wait non-blockingly by suspending the continuation and freeing the physical thread. Conversely, a non-blocking API can still coordinate a later synchronous commit or observation boundary.

In distributed systems, this distinction becomes sharper. Waiting for a coordinator, quorum, leader, lock owner, or remote dependency may preserve [[Safety and Liveness|safety]], but it weakens liveness under crash, partition, pause, or delay. Coordination-avoidance techniques such as [[CRDTs]], monotone updates, escrow, reservations, local acceptance with reconciliation, or idempotent retry often improve local progress by narrowing or postponing the coordination point.

Progress is not free. A stronger progress condition may require more metadata, helping, retry loops, contention management, constrained update algebra, weaker consistency, or a different domain protocol.

## Consensus

[[Consensus]] connects progress conditions to computability. In Herlihy's wait-free synchronization model, consensus is used to classify shared objects by their ability to solve wait-free consensus for a given number of processes. This is the basis of consensus numbers and the universality result for wait-free synchronization.

In asynchronous message-passing systems with crash failures, the FLP result shows that deterministic consensus cannot guarantee termination in all executions. Consensus protocols therefore separate safety from progress: they preserve agreement, validity, and integrity while liveness depends on additional assumptions such as partial synchrony, randomized progress, quorum availability, stable storage, or eventual leadership.

## Consensus Numbers

A **consensus number** classifies a shared object type by the largest number of processes for which that object can solve wait-free consensus, assuming read/write registers are also available.

Consensus numbers form a hierarchy of synchronization power:

- Read/write registers have consensus number 1.
- Test-and-set and fetch-and-add have consensus number 2.
- Compare-and-swap has infinite consensus number.
- A consensus object has infinite consensus number by definition.

The number is not a throughput or availability metric. It is a computability boundary: it says which wait-free distributed objects can be constructed from a given primitive. If an object type has consensus number `n`, it cannot be used to build a wait-free consensus protocol for `n + 1` processes.

This is why consensus is universal in Herlihy's model. A primitive with infinite consensus number can implement any object with a sequential specification in a wait-free manner, by deciding the next operation and applying the sequential transition rule.

In Cohesive terms, consensus numbers help separate two questions:

- What semantic object or transition rule is being implemented?
- Which substrate primitive is strong enough to provide the required progress condition without adding stronger coordination elsewhere?

The [[Asynchronous Computability Theorem|asynchronous computability theorem]] picks up the wait-free question from a different angle. Instead of classifying object types by consensus number, it models tasks topologically and asks whether a wait-free protocol complex can be mapped continuously into the legal output complex.

## Operational Use

When a system claims liveness, the model should ask:

- Is progress guaranteed for every operation, for some operation, or only when interference stops?
- Does the guarantee require fairness, bounded delay, a live leader, a quorum, a lock owner, or a contention manager?
- Can one stalled participant prevent others from completing?
- Is completion bounded, eventual, best-effort, or conditional on recovery?
- Does avoiding coordination weaken the consistency model, expose tentative state, or require later reconciliation?

Progress conditions are therefore not only implementation details. They shape which [[Consistency Models|consistency]], availability-like, recovery, and coordination claims can honestly be made at a boundary.

## External References

- Maurice P. Herlihy, [Wait-Free Synchronization](https://cs.brown.edu/people/mph/Herlihy91/p124-herlihy.pdf), ACM Transactions on Programming Languages and Systems, 13(1):124-149, January 1991.
- Maurice Herlihy and Nir Shavit, [The Asynchronous Computability Theorem for t-Resilient Tasks](https://groups.csail.mit.edu/tds/papers/Shavit/STOC93.pdf), STOC 1993.
- Maurice Herlihy, Victor Luchangco, and Mark Moir, [Obstruction-Free Synchronization: Double-Ended Queues as an Example](https://cs.brown.edu/people/mph/HerlihyLM03/main.pdf), ICDCS 2003.
- Maurice Herlihy and Nir Shavit, [The Art of Multiprocessor Programming](https://books.google.com/books/about/The_Art_of_Multiprocessor_Programming.html?id=7MqcBAAAQBAJ), Morgan Kaufmann.

Related concepts: [[Safety and Liveness|safety and liveness]], [[Asynchronous Computability Theorem|asynchronous computability theorem]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Coordination|coordination]], [[Consensus|consensus]], [[Consensus Protocols|consensus protocols]], [[Concurrency Control|concurrency control]], [[Consistency Models|consistency models]], [[CAP Theorem|CAP theorem]], [[CALM Theorem|CALM theorem]], [[Ordering|ordering]], [[Retry|retry]], [[Recovery|recovery]], [[CRDTs]], [[Cohesive System Model/Operational Concerns/Weak Isolation Patterns|weak isolation patterns]], [[Actor Systems|actor systems]], [[Storage Systems|storage systems]].
