---
realm: System Graph
kind: structural-construct
created: 2026-07-28
updated: 2026-08-01
status: draft
aliases:
  - Service Model
  - Service Topology
  - Service Graph
  - Logical Service
---

# Service Models

A service model is a system-graph view that bundles semantic responsibilities into logical [[Service|services]] and connects their provided and required [[Interfaces|interfaces]] through [[Interaction Channels|interaction channels]]. [[Interaction Protocols|Interaction protocols]] and operational envelopes qualify how those interactions may proceed. It mediates between the domain's entities, relations, queries, and processes and the concrete repositories, deployments, runtimes, and schedulers that realize them.

A logical service is not identical to a code module, repository, deployable, process, container, host, or runtime instance. Those are possible realization units, and their relationship to the logical service must be stated rather than assumed.

## Service as a Graph Node

Within a service model, a service is a node with:

- an encapsulated internal subgraph;
- provided interfaces expressing capabilities;
- required interfaces expressing dependencies;
- declared semantic and [[Service Levels|service-level]] guarantees; and
- ownership or accountability when those concerns are modeled.

Edges denote interface-mediated interactions, not undifferentiated dependency. Their [[Interaction Protocols|protocols]], [[Shape|shapes]], [[Interaction Channels|channels]], and operational envelopes qualify what the topology means.

## Semantic Correspondence

Service operations can correspond to different semantic structures:

| Operation role | Semantic correspondence |
| --- | --- |
| Entity command | Requests one or more valid entity transitions |
| Entity read | Returns entity state or an authorized view of it |
| Relational query | Evaluates a query across entities, relations, or projections |
| Process command | Starts, advances, pauses, cancels, or signals a semantic process |
| Process query | Exposes process state, history, obligations, or expected outcomes |
| Composite operation | Bundles several capabilities or coordinates several services |
| Technical operation | Provides a realization capability such as encoding, delivery, scheduling, or storage |
| External or opaque operation | Exposes observable behavior whose semantics belong to another domain or remain intentionally hidden |

The correspondence is many-to-many. A service can host several entity types; one entity's authoritative transitions and query projections can appear in different services; and a process can span many service boundaries. A domain relation also does not automatically imply a direct service dependency.

## Allocation and Realization

A service model makes several allocation relations explicit:

```text
semantic responsibility  -> logical service
logical service          -> code modules
code modules             -> repository and build graph
logical service          -> owning or operating team
logical service          -> deployable units
deployable units         -> runtime instances
runtime work             -> scheduler and resources
```

These relations need not be one-to-one. A monorepo can contain many independently deployed services, and one service can be built from modules stored in several repositories. Likewise, a deployment may contain multiple logical services, while one logical service may have many replicas or specialized runtime instances.

The mapping is acceptable only when the chosen substrate preserves the required semantic and operational properties. See [[System Language and Realization|system language and realization]] and [[Realization|realization]].

## Composition and Encapsulation

Some services own a semantic capability; others primarily compose, route, translate, or aggregate the capabilities of dependencies. These roles are independent of whether an operation executes locally or invokes another service.

Use [[Service|service]] for the general encapsulation principle and its capability/composition taxonomy. Use [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]] when a gateway or facade changes the visible topology by placing several logical flows behind one node.

## Projection Views

The same underlying system may be projected as:

- a semantic view of entities, relations, queries, and processes;
- a logical service topology;
- an interface and interaction view;
- a code, repository, and build graph;
- a team ownership graph;
- a deployment topology; or
- a runtime and scheduling graph.

These are related projections, not interchangeable descriptions. Conflating them is a common source of architectural ambiguity.

## Formal relations

- `arranges`: [[Service]] — Represents the boundary-relative service role as logical graph nodes with encapsulated responsibilities, provided and required interfaces, guarantees, and allocation relations.
- `realm_peer_of`: [[Service]] — Treats the same nominal service notion as a system-graph structure, while the peer entry owns the general boundary-relative provider role and its modeling discipline.

## Relationships

- Domain semantics supplies the semantic responsibilities allocated to services.
- [[Interfaces]] and [[Interaction Protocols]] define allowed service interactions.
- [[Service Levels|Service levels]] qualify provided capabilities with measurable objectives and accountable commitments.
- [[Microservice|Microservices]] are logical service nodes with an explicit independent-evolution profile; [[Microservice Architecture|microservice architecture]] owns the forces and cross-realm alignment practice that selects that profile.
- [[Infrastructure Graph]] records public realization mechanisms and evidence.
- Operational concerns qualify nodes, edges, and allocation mappings with runtime requirements.

## External References

- [Microsoft: Design patterns for microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/patterns)
- [Service Layer](https://martinfowler.com/eaaCatalog/serviceLayer.html)
