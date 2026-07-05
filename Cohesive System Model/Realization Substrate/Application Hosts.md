---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-06-29
---

# Application Hosts

Application Hosts are runtime containers for application code, request handling, background work, dependency management, and operational concerns.

An application host may expose HTTP endpoints, subscribe to queues, run workers, schedule jobs, host actors, execute workflow activities, or maintain projections.

Application hosts commonly provide:

- Lifecycle management.
- Dependency injection or component composition.
- Configuration.
- Request or message pipelines.
- Logging and telemetry.
- Health checks.
- Graceful shutdown and restart behavior.

In the model, an application host is a concrete [[Realization|realization]] mechanism for one or more [[Observer|observers]] and their interaction edges.

In stateless web hosts, a request handler often realizes a short-lived observer for one operation. It may load an entity state observation, interpret an input as a command, and attempt a transition, but it usually does not own the entity's transition boundary across requests. Correctness therefore depends on explicit [[Concurrency Control|concurrency control]], such as expected-version checks, rather than on the request observer itself.

Session affinity can preserve locality for cached state or repeated interactions, but it does not by itself provide exclusive transition ownership unless the host also guarantees serialized access to the entity boundary.

Related concepts: [[Realization|realization]], [[Runtimes|runtimes]], [[Observer|observer]], [[Entity|entity]], [[Interaction|interaction]], [[Network|network]], [[Compute|compute]], [[Infrastructure|infrastructure]], [[Concurrency Control|concurrency control]].
