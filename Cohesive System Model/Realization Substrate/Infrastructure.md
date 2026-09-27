---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-09-27
---

# Infrastructure

Infrastructure is the concrete operational environment that provides compute, networking, storage, deployment, security, observability, and platform services.

Infrastructure includes cloud platforms, clusters, networks, load balancers, service discovery, secrets, identity systems, deployment pipelines, monitoring, logging, tracing, backups, and disaster recovery.

An infrastructure **facility** is a configured mechanism or service considered as a possible provider of scoped capabilities. The same product can expose different capabilities under different versions, regions, consistency modes, partitions, quotas, identities, and lifecycle ownership. A facility claim should therefore name the configured subject, boundary, assumptions, limits, and supporting [[Assurance and Evidence|evidence]].

A facility is not the semantic or operational requirement it may satisfy. [[Requirements and Capabilities|Requirements and capabilities]] share property definitions while retaining different roles, and an [[Infrastructure Graph|infrastructure graph]] records the strategies and bindings that relate provider-neutral demands to coherent facility configurations.

Infrastructure shapes the boundaries within which the system runs:

- Failure boundaries.
- Trust boundaries.
- Network boundaries.
- Resource boundaries.
- Deployment boundaries.
- Persistence and recovery boundaries.

Infrastructure can support or undermine the model's operational concerns. Its concrete guarantees should be mapped back through [[Realization|realization]] and, when public structure is needed, through an [[Infrastructure Graph|infrastructure graph]] to interaction, delivery, coordination, concurrency, and recovery meanings.

Infrastructure also realizes [[Operational Control|operational control]] and [[Observability and Provenance|observability and provenance]] through [[Surfaces|administration surfaces]], policy distribution, metrics, logs, traces, diagnostic routes, and retained evidence. Those mechanisms do not define their own authority, semantic completion, or provenance meaning.

Infrastructure supplies [[Scaling Mechanisms|scaling mechanisms]] such as resource resizing, replication, placement, partition movement, routing changes, and autoscaling controllers. Their effectiveness is judged against a declared [[Scalability|scalability]] profile; a successful infrastructure operation does not prove that ready or useful capacity increased.

## Formal relations

- `may_realize`: [[Infrastructure Graph]] — Supplies configured facilities and lifecycle mechanisms for substrate-facing roles when their scoped capability claims and evidence satisfy the graph's requirements.
