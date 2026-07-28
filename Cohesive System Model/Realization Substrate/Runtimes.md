---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-07-27
---

# Runtimes

Runtimes are execution environments that host code and provide operational behavior.

Examples include language runtimes, web runtimes, actor runtimes, workflow runtimes, [[Durable Execution Engines|durable execution engines]], serverless runtimes, job processors, stream processors, and application frameworks.

Different runtimes [[Realization|realize]] [[Observer|observers]] differently. An actor runtime may emphasize identity, placement, supervision, and serialized message handling. An HTTP host may emphasize request pipelines, routing, middleware, and short-lived handlers.

Some runtimes associate an observer with an OS thread and call stack. Green-thread, fiber, coroutine, task, or async runtimes relax that association: the observer follows the logical execution context governed by a scheduler, even when execution resumes on different OS threads.

Runtimes realize [[Scheduling|scheduling]] through mechanisms such as thread schedulers, event loops, work-stealing pools, actor dispatchers, continuation queues, timer services, and workflow activation queues. These mechanisms select execution opportunity; they do not automatically supply domain [[Authority|authority]], message-delivery guarantees, consistency, or one shared fairness property across layers.

A runtime fairness claim should identify the schedulable unit and failure assumptions. Fair CPU scheduling does not imply fair actor activation, fair mailbox admission, eventual network delivery, or fair workflow retry. [[Arbitration]] at queues, locks, and asynchronous boundaries can introduce additional ordering and progress constraints.

This is where [[Synchrony and Asynchrony|blocking and non-blocking]] must be separated carefully. A logical operation may wait for an asynchronous result while the runtime does not block the physical thread. Callback-, continuation-, task-, fiber-, or actor-based runtimes can suspend the logical continuation and resume it later, preserving the semantic wait without tying up the underlying thread.

The same semantic model can be preserved across runtimes when observer, entity, event, command, state, and boundary meanings are kept explicit.

A runtime may host an [[Execution Kernel|execution-kernel]] interpreter for canonical transition or process definitions. Conforming interpretation requires the runtime to declare supported definition and schema versions, intrinsic operations, capabilities, constraints, guarantees, and operating boundaries. Runtime registration, dependency injection, callbacks, or generated handlers do not become semantic authority.

Each transition evaluation and process activation executes finite semantic work. A runtime may suspend and later resume a logical process through explicit continuation, waits, timers, signals, and durable cuts, but it must not hide ambient clock reads, randomness, external I/O, service lookup, waits, or unrestricted callbacks inside deterministic semantic computation.

When a runtime cannot realize a required atomicity, durability, ordering, compatibility, response, or recovery guarantee, it must report the unsupported requirement rather than silently choose a weaker path. Conformance compares stable semantic decisions and traces, not thread identity, worker placement, or wall-clock scheduling accidents.

Related concepts: [[Execution Kernel|execution kernel]], [[Realization|realization]], [[Transition Models|transition models]], [[Process Graphs|process graphs]], [[Observer|observer]], [[Effect|effect]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Authority|authority]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Progress Conditions|progress conditions]], [[Application Hosts|application hosts]], [[Actor Systems|actor systems]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Network|network]], [[Compute|compute]].
