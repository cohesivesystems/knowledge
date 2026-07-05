---
realm: Principles
kind: principle
created: 2026-06-28
updated: 2026-06-30
---

# Synchrony and Asynchrony

Synchrony and Asynchrony describe whether events, observations, transitions, or participants are coupled into one boundary-relative unit.

**Asynchrony** is the semantics of independent occurrence. Events, observations, transitions, messages, or effects may occur, be observed, be delivered, be persisted, or complete independently unless a model supplies a stronger shared boundary. An operation is asynchronous when the begin and end events are separate events.

**Synchrony** is the semantics of coordinated co-occurrence. A boundary couples several otherwise separate events, observations, or transitions so they are treated as one unit for some purpose: one call/return interaction, one actor turn, one critical section, one transaction, one barrier, one commit point, one consensus decision, one logical round, or one atomic observation.

In this sense, asynchrony is the primitive absence of coordinated joining. Synchronization is the operation that turns asynchronous multiplicity into synchronous unity. Desynchronization exposes a formerly synchronous unit as separate events, phases, messages, observations, or effects.

## Duality

Asynchrony preserves multiplicity: many local events, observations, and timelines remain distinct.

Synchrony imposes unity: selected events, observations, or transitions are coordinated into one observation, step, or commitment boundary.

The duality can be summarized as:

| Asynchrony                                       | Synchrony                            |
| ------------------------------------------------ | ------------------------------------ |
| Separation                                       | Joining                              |
| Independence                                     | Coupling                             |
| Partial order                                    | Shared step or totalized moment      |
| Local observation                                | Common observation                   |
| Interleaving                                     | Atomicity                            |
| Eventual relation                                | Simultaneous boundary                |
| Coordination absent, deferred, or explicit later | coordination present at the boundary |

A synchronous event can therefore be modeled as a coordinated join of multiple events into one boundary-relative occurrence. The join may be logical rather than physical: the events need not happen at the same wall-clock instant, but the model treats them as one unit for observation, ordering, commitment, or progress.

In [[Systems Sheaf Semantics|systems sheaf semantics]], this coordinated join can be read as descent: compatible local sections over independently advanced contexts glue into a larger section at a synchronization boundary.

## Senses of Synchrony

Several meanings are often conflated:

- **Control-flow synchrony**: one operation waits for another result before continuing. A local function call, blocking RPC, or `await` point can have this shape.
- **Commit or observation synchrony**: several effects become visible or committed as one unit. Examples include database transactions, actor turns, lock-protected critical sections, atomic compare-and-swap operations, and consensus-decided log entries.
- **Timing-model synchrony**: the system assumes bounded message delay, bounded processing delay, clocks, or rounds. Distributed algorithms use this sense when contrasting synchronous, partially synchronous, and asynchronous models.

These senses can vary independently. A request may be control-flow synchronous without providing atomic commit. A transaction may provide commit synchrony while being invoked through asynchronous control flow. A distributed algorithm may assume partial synchrony even when implemented with non-blocking runtime APIs.

## Blocking and Non-Blocking

Blocking and non-blocking are realization and [[Progress Conditions|progress-condition]] notions, not definitions of synchrony and asynchrony.

Blocking may mean that a physical thread is parked, a lock owner prevents other workers from progressing, or a logical operation is waiting for a result. These should not be collapsed. Often the logical process should wait while the physical thread should not.

Async programming models reconcile this distinction. A logical operation can remain pending until an asynchronous operation completes, while the runtime releases the physical thread to run other work. In continuation or callback-shaped models, such as an F# async computation, the computation can be understood as arranging what continuation should run when the operation completes rather than occupying a thread for the whole wait.

This gives two different questions:

- Is the logical operation synchronized with a result, commit, or observation before it continues?
- Does the realization block a physical thread or prevent unrelated participants from making progress?

The first question belongs to interaction, observation, and commitment semantics. The second belongs to runtime scheduling, locks, waits, callbacks, promises, fibers, tasks, actors, event loops, and progress conditions.

## Local and Distributed Systems

In local programming, synchrony may be realized by a call stack, lock, monitor, condition variable, event-loop turn, memory barrier, transaction, or scheduler step. Asynchrony may be realized by callbacks, tasks, channels, futures, promises, fibers, actors, interrupts, or queues.

In distributed systems, synchrony may be realized by quorum protocols, consensus, two-phase commit, barriers, leases, logical rounds, clocks, or bounded-delay assumptions. Asynchrony is the default condition in which messages, clocks, failures, observations, and commits proceed independently unless a protocol coordinates them.

The same definitions apply in both settings when stated boundary-relatively: asynchrony means independent occurrence relative to the boundary; synchrony means coordinated co-occurrence relative to the boundary.

Related concepts: [[Duality and Symmetry|duality and symmetry]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Interaction|interaction]], [[Coordination|coordination]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Time|time]], [[Consensus|consensus]], [[Progress Conditions|progress conditions]], [[Safety and Liveness|safety and liveness]], [[Runtimes|runtimes]], [[Actor Systems|actor systems]], [[Workflow Engines|workflow engines]], [[Event|event]], [[Observation|observation]], [[Transition|transition]].
