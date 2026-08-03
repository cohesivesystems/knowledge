---
realm: System Graph
kind: structural-construct
created: 2026-07-05
updated: 2026-07-28
aliases:
  - Infrastructure Graphs
---

# Infrastructure Graph

An infrastructure graph is the system graph projection that relates modeled system structure and guarantee demands to public realization substrate concepts and capability evidence.

It names how entity models, transition models, observer models, process graphs, relation models, projection models, boundaries, effects, policy scopes, invariant scopes, and business transactions depend on substrate roles such as [[Compute|compute]], [[Runtimes|runtimes]], [[Application Hosts|application hosts]], [[Network|network]], [[Storage Systems|storage systems]], [[Brokers|brokers]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Actor Systems|actor systems]], and [[Infrastructure|infrastructure]].

The mapping is not only from a semantic role to a similarly named mechanism. Transition models, process graphs, effect scopes, and business transactions produce structural requirements for observations, writes, waits, emissions, replies, atomicity, visibility, durability, idempotency, ordering, recovery, compensation, compatibility, ownership, and fencing. Candidate substrates supply evidence about which requirements they can realize and within which operating boundaries.

Operational concerns are properties and requirements of this projection. They may qualify a source node, a target node, a system-graph edge, or the mapping between realms. Replica placement, for example, introduces scheduling, routing, identity, consistency, isolation, and recovery obligations on the relation between one logical role and its many runtime instances.

The infrastructure graph is not a private deployment inventory. Concrete hosts, credentials, customer environments, unpublished modules, private routing rules, and implementation-specific realization mappings belong outside this public repository unless explicitly published.

Use an infrastructure graph to ask:

- Which substrate roles host, persist, route, schedule, observe, or recover each system graph structure?
- Which code, repository, team, deployment, and runtime projections correspond to each [[Service Models|logical service]]?
- Which operational guarantees are supplied by which substrate boundary?
- Which requirements are realized natively, through composition, only under constraints, by an explicit authorized override, or not at all?
- Which claimed capabilities remain unknown or lack sufficient evidence?
- Where do failure, trust, deployment, persistence, and network boundaries shape the system graph?
- Which realization choices preserve the intended semantic relations, process graphs, effects, policy scopes, and invariant scopes?
- Which mappings are public conceptual commitments and which are private realization graph data?

An infrastructure graph therefore sits at the boundary between [[System Graph|system graph]] and [[Realization|realization]]. It is a public structural view when it names substrate roles and guarantee boundaries; it becomes a private realization graph when it maps those roles to concrete code, deployments, credentials, infrastructure instances, or customer-specific environments.

A realization compiler may select a stronger semantically equivalent mechanism, but it must not silently select a weaker one. Unavailable or unproven requirements remain explicit diagnostics or unrealized graph edges rather than hidden fallbacks. For example, unavailable multi-entity atomicity does not authorize automatic replacement with a saga; compensation and reconciliation must exist in the authored process graph.

Related concepts: [[System Graph|system graph]], [[Execution Kernel|execution kernel]], [[Realization|realization]], [[Infrastructure|infrastructure]], [[Service Models|service models]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Entity Models|entity models]], [[Transition Models|transition models]], [[Observer Models|observer models]], [[Process Graphs|process graphs]], [[Relation Models|relation models]], [[Projection Models|projection models]], [[Effect|effect]], [[Effect Models|effect models]], [[Boundaries|boundaries]], [[Commit Boundaries|commit boundaries]], [[Persistence|persistence]], [[Durability|durability]], [[Recovery|recovery]], [[Interaction|interaction]], [[Coordination|coordination]].
