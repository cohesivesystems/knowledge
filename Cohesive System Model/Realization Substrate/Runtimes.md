---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-08-01
---

# Runtimes

Runtimes are execution environments that host code and provide operational behavior.

Examples include language runtimes, web runtimes, actor runtimes, workflow runtimes, [[Durable Execution Engines|durable execution engines]], serverless runtimes, job processors, stream processors, and application frameworks.

Different runtimes [[Realization|realize]] [[Observer|observers]] differently. An actor runtime may emphasize identity, placement, supervision, and serialized message handling. An HTTP host may emphasize request pipelines, routing, middleware, and short-lived handlers.

Some runtimes associate an observer with an OS thread and call stack. Green-thread, fiber, coroutine, task, or async runtimes relax that association: the observer follows the logical execution context governed by a scheduler, even when execution resumes on different OS threads.

Runtimes realize [[Scheduling|scheduling]] through mechanisms such as thread schedulers, event loops, work-stealing pools, actor dispatchers, continuation queues, timer services, and workflow activation queues. These mechanisms select execution opportunity; they do not automatically supply domain [[Authority|authority]], message-delivery guarantees, consistency, or one shared fairness property across layers.

Runtimes also realize [[Interaction Control Flow|interaction-control roles]] through polling loops, callbacks, subscription dispatchers, queue readers, source drivers, push handlers, batching loops, and demand protocols. A runtime can implement a public push boundary using an internal poller or implement a public pull boundary over lower-level calls. The public role, internal activity, and scheduler that owns cadence should therefore be modeled at their respective boundaries.

A broker poll, delivery dispatch, callback invocation, callback result, and later process transition can therefore be distinct occurrences connected by different relations. Polling or dispatch determines interaction activation; the runtime scheduler determines execution opportunity; an authorized observer interprets the result and determines whether semantic [[Control Flow|process control flow]] advances. Runtime registration and callback return alone do not supply that process authority.

A runtime scheduler may be preemptive or cooperative. Both forms can realize the same logical observer and process structure when they preserve the declared observations, decisions, effects, and ordering constraints, even though their possible execution interleavings and interruption points differ. A runtime with one OS thread may multiplex several green threads, fibers, or tasks preemptively if it supplies a user-level interruption and context-switch mechanism; otherwise switching among those units is cooperative at their yield or suspension points.

Temporal multiplexing can present observational [[Parallelism|parallelism]] to a higher boundary by hiding scheduler events and context switches. It remains distinct from physical parallelism at the runtime-resource boundary because only one logical unit executes on the shared resource at an instant. A runtime obtains physical parallelism by mapping compatible work onto distinct execution resources. Either realization may preserve the same [[Concurrency|concurrent]] process structure when the higher contract does not depend on physical overlap.

A runtime fairness claim should identify the schedulable unit and failure assumptions. Fair CPU scheduling does not imply fair actor activation, fair mailbox admission, eventual network delivery, or fair workflow retry. [[Arbitration]] at queues, locks, and asynchronous boundaries can introduce additional ordering and progress constraints.

This is where [[Synchrony and Asynchrony|blocking and non-blocking]] must be separated carefully. A logical operation may wait for an asynchronous result while the runtime does not block the physical thread. Callback-, continuation-, task-, fiber-, or actor-based runtimes can suspend the logical continuation and resume it later, preserving the semantic wait without tying up the underlying thread.

The same semantic model can be preserved across runtimes when observer, entity, event, command, state, and boundary meanings are kept explicit.

A runtime may host an [[Execution Kernel|execution-kernel]] interpreter for canonical transition or process definitions. Conforming interpretation requires the runtime to declare supported definition and schema versions, intrinsic operations, capabilities, constraints, guarantees, and operating boundaries. Runtime registration, dependency injection, callbacks, or generated handlers do not become semantic authority.

Each transition evaluation and process activation executes finite semantic work. A runtime may suspend and later resume a logical process through explicit continuation, waits, timers, signals, and durable cuts, but it must not hide ambient clock reads, randomness, external I/O, service lookup, waits, or unrestricted callbacks inside deterministic semantic computation.

When a runtime cannot realize a required atomicity, durability, ordering, compatibility, response, or recovery guarantee, it must report the unsupported requirement rather than silently choose a weaker path. Conformance compares stable semantic decisions and traces, not thread identity, worker placement, or wall-clock scheduling accidents.

Related concepts: [[Execution Kernel|execution kernel]], [[Realization|realization]], [[Transition Models|transition models]], [[Process Graphs|process graphs]], [[Fork and Join|fork and join]], [[Control Flow|control flow]], [[Concurrency|concurrency]], [[Parallelism|parallelism]], [[Observer|observer]], [[Effect|effect]], [[Interaction Control Flow|interaction control flow]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Authority|authority]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Progress Conditions|progress conditions]], [[Application Hosts|application hosts]], [[Actor Systems|actor systems]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Network|network]], [[Compute|compute]].

## Formal relations

- `may_realize`: [[Concurrency]] — Multiplexes or distributes logical tasks while preserving their declared dependency and observation structure.
- `may_realize`: [[Parallelism]] — Maps compatible work onto distinct execution resources or presents observationally equivalent progress through a declared higher boundary.
