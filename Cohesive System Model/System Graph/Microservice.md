---
realm: System Graph
kind: structural-construct
created: 2026-08-01
updated: 2026-08-01
status: draft
aliases:
  - Microservices
  - Logical Microservice
---

# Microservice

A microservice is a logical [[Service|service]] node in a [[Service Models|service model]] with an explicit profile for independent semantic evolution, contract evolution, ownership, deployment, scaling, failure, recovery, and operation. The profile states which of those boundaries align and where independence remains partial rather than treating *micro* as a code-size or process-count rule.

This note owns the system-graph structure of a microservice. [[Microservice Architecture|Microservice architecture]] owns the recurring problem, forces, platform preconditions, costs, and cross-realm practice of selecting and sustaining that structure.

## Structural Profile

A microservice node declares:

- The semantic capabilities, entities, processes, policies, invariants, and [[Authority|authority]] allocated to its boundary.
- Its provided and required [[Interfaces|interfaces]] and the [[Interaction Protocols|interaction protocols]] that govern them.
- The operational guarantees exposed to consumers and dependencies.
- The code, ownership, deployment, runtime, storage, scheduling, and failure-boundary correspondences selected to realize the logical service.
- The dimensions expected to evolve independently and the compatibility or coordination obligations that remain shared.

These correspondences need not be one-to-one. One microservice may use several deployable units, runtime processes, stores, or workers, and one repository or team may contain or own several microservices. A microservice is not automatically one bounded context, subdomain, aggregate, database, repository, team, container, process, or endpoint.

Within one service model, microservices can coexist with logical services that use different deployment or ownership profiles. The distinction is justified by the independent change, scaling, failure-isolation, or accountability benefit, not by a fixed granularity threshold.

Related concepts: [[Service|service]], [[Service Models|service models]], [[Microservice Architecture|microservice architecture]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Boundaries|boundaries]], [[Authority|authority]], [[Compatibility and Evolution|compatibility and evolution]], [[Service Levels|service levels]], [[Scaling Mechanisms|scaling mechanisms]], [[Infrastructure Graph|infrastructure graph]], [[Application Hosts|application hosts]], [[Runtimes|runtimes]], [[Scheduling|scheduling]], [[Recovery|recovery]], [[Modular Monolith|modular monolith]], [[Realization|realization]].

## Formal relations

- `arranges`: [[Service]] — Places the boundary-relative service role into a logical node with an explicit independent-evolution and cross-structure allocation profile.
