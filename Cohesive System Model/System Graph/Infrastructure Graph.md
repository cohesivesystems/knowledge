---
realm: System Graph
kind: structural-construct
created: 2026-07-05
updated: 2026-07-05
aliases:
  - Infrastructure Graphs
---

# Infrastructure Graph

An infrastructure graph is the system graph projection that relates modeled system structure to public realization substrate concepts.

It names how entity models, observer models, process graphs, relation models, projection models, boundaries, effects, policy scopes, invariant scopes, and business transactions depend on substrate roles such as [[Compute|compute]], [[Runtimes|runtimes]], [[Application Hosts|application hosts]], [[Network|network]], [[Storage Systems|storage systems]], [[Brokers|brokers]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Actor Systems|actor systems]], and [[Infrastructure|infrastructure]].

The infrastructure graph is not a private deployment inventory. Concrete hosts, credentials, customer environments, unpublished modules, private routing rules, and implementation-specific realization mappings belong outside this public repository unless explicitly published.

Use an infrastructure graph to ask:

- Which substrate roles host, persist, route, schedule, observe, or recover each system graph structure?
- Which operational guarantees are supplied by which substrate boundary?
- Where do failure, trust, deployment, persistence, and network boundaries shape the system graph?
- Which realization choices preserve the intended semantic relations, process graphs, effects, policy scopes, and invariant scopes?
- Which mappings are public conceptual commitments and which are private realization graph data?

An infrastructure graph therefore sits at the boundary between [[System Graph|system graph]] and [[Realization|realization]]. It is a public structural view when it names substrate roles and guarantee boundaries; it becomes a private realization graph when it maps those roles to concrete code, deployments, credentials, infrastructure instances, or customer-specific environments.

Related concepts: [[System Graph|system graph]], [[Realization|realization]], [[Infrastructure|infrastructure]], [[Entity Models|entity models]], [[Observer Models|observer models]], [[Process Graphs|process graphs]], [[Relation Models|relation models]], [[Projection Models|projection models]], [[Effects|effects]], [[Boundaries|boundaries]], [[Persistence|persistence]], [[Durability|durability]], [[Recovery|recovery]], [[Interaction|interaction]], [[Coordination|coordination]].
