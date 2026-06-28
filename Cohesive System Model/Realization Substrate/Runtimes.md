---
realm: Realization Substrate
---

# Runtimes

Runtimes are execution environments that host code and provide operational behavior.

Examples include language runtimes, web runtimes, actor runtimes, workflow runtimes, [[Durable Execution Engines|durable execution engines]], serverless runtimes, job processors, stream processors, and application frameworks.

Different runtimes [[Realization|realize]] [[Observer|Observers]] differently. An actor runtime may emphasize identity, placement, supervision, and serialized message handling. An HTTP host may emphasize request pipelines, routing, middleware, and short-lived handlers.

Some runtimes associate an observer with an OS thread and call stack. Green-thread, fiber, coroutine, task, or async runtimes relax that association: the observer follows the logical execution context governed by a scheduler, even when execution resumes on different OS threads.

The same semantic model can be preserved across runtimes when observer, entity, event, command, state, and boundary meanings are kept explicit.

Related concepts: [[Realization]], [[Observer]], [[Application Hosts]], [[Actor Systems]], [[Workflow Engines]], [[Durable Execution Engines]], [[Network]], [[Compute]].
