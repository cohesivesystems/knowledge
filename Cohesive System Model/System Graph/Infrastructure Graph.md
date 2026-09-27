---
realm: System Graph
kind: structural-construct
created: 2026-07-05
updated: 2026-09-27
aliases:
  - Infrastructure Graphs
---

# Infrastructure Graph

An infrastructure graph is the system graph projection that relates modeled system structure and guarantee demands to public realization substrate concepts and capability evidence.

It names how entity models, transition models, observer models, process graphs, relation models, projection models, boundaries, effects, policy scopes, invariant scopes, and business transactions depend on substrate roles such as [[Compute|compute]], [[Runtimes|runtimes]], [[Application Hosts|application hosts]], [[Network|network]], [[Storage Systems|storage systems]], [[Brokers|brokers]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Actor Systems|actor systems]], and [[Infrastructure|infrastructure]].

The mapping is not only from a semantic role to a similarly named mechanism. Transition models, process graphs, effect scopes, and business transactions produce structural requirements for observations, writes, waits, emissions, replies, atomicity, visibility, durability, idempotency, ordering, recovery, compensation, compatibility, ownership, and fencing. Candidate substrates supply evidence about which requirements they can realize and within which operating boundaries.

Operational concerns are properties and requirements of this projection. They may qualify a source node, a target node, a system-graph edge, or the mapping between realms. Replica placement, for example, introduces scheduling, routing, identity, consistency, isolation, and recovery obligations on the relation between one logical role and its many runtime instances.

## Requirement and Realization Views

An infrastructure graph preserves stable correspondence among several views without treating them as one graph or source of authority:

1. The **requirement view** contains provider-neutral resource roles, bindings, environment intent, operating envelopes, and requirements derived from semantic and system-graph structure.
2. The **candidate-strategy view** relates those requirements to possible constructions, their premises, residual obligations, and rejected alternatives.
3. The **physical-realization view** contains selected facilities, exact configurations, physical paths, lifecycle ownership, and the evidence used to discharge requirements.
4. The **lifecycle and observation view** records attestations, plans, receipts, observed configuration and behavior, drift, and time-indexed [[Assurance and Evidence|assurance assessments]].

The views may share stable identities and provenance while retaining different authority. A requirement does not become a provider resource, a selected resource does not become the semantic requirement it realizes, and an observed estate does not silently rewrite either definition.

## Strategies, Facilities, and Construction Witnesses

[[Requirements and Capabilities|Requirements and capabilities]] usually meet through a realization strategy rather than a one-to-one name match. A strategy states how supplied properties, configuration facts, application or protocol obligations, and assumptions jointly establish a demanded property. The result is a construction witness with provenance to the exact requirements, rules, facilities, and evidence used.

For example, a demand for fenced exclusive mutation of one entity identity may be realized through a lease, a monotonic epoch, and authoritative rejection of stale epochs. A keyed actor can provide serialized turns but does not by itself establish durable admission, FIFO delivery, stale-owner exclusion, or idempotent external effects. Those properties remain separate requirements unless the selected construction establishes them.

One configured facility may discharge several requirements, and one requirement may need several facilities. Capabilities may also belong to a binding or multi-party protocol rather than one resource. The graph must therefore retain parameter and scope alignment, implication and composition rules, interference checks, and residual obligations.

Evidence must describe one coherent configuration. The compiler may not combine mutually incompatible provider modes or cherry-pick claims from several configurations as though they described one deployable resource.

See [[Fenced Exclusive Mutation Example|fenced exclusive mutation example]] for one bounded requirement traced through lease- and actor-based strategies, a rejected unfenced candidate, conformance obligations, and runtime evidence.

The infrastructure graph is not a private deployment inventory. Concrete hosts, credentials, customer environments, unpublished modules, private routing rules, and implementation-specific realization mappings belong outside this public repository unless explicitly published.

Use an infrastructure graph to ask:

- Which substrate roles host, persist, route, schedule, observe, or recover each system graph structure?
- Which code, repository, team, deployment, and runtime projections correspond to each [[Service Models|logical service]]?
- Which operational guarantees are supplied by which substrate boundary?
- Which requirements are realized natively, through composition, only under constraints, by an explicit authorized override, or not at all?
- Which claimed capabilities remain unknown or lack sufficient evidence?
- Where do failure, trust, deployment, persistence, and network boundaries shape the system graph?
- Which realization choices preserve the intended semantic relations, process graphs, effects, policy scopes, and invariant scopes?
- Which realization strategy derives each demanded property from which coherent facility capabilities and application obligations?
- Which provider claims are merely declared, which configurations are attested, and which deployed behaviors are observed?
- Which assurance assessments are established, conditional, refuted, unknown, or explicitly overridden?
- Which mappings are public conceptual commitments and which are private realization graph data?

An infrastructure graph therefore sits at the boundary between [[System Graph|system graph]] and [[Realization|realization]]. It is a public structural view when it names substrate roles and guarantee boundaries; it becomes a private realization graph when it maps those roles to concrete code, deployments, credentials, infrastructure instances, or customer-specific environments.

A realization compiler may select a stronger semantically equivalent mechanism, but it must not silently select a weaker one. Unavailable or unproven requirements remain explicit diagnostics or unrealized graph edges rather than hidden fallbacks. For example, unavailable multi-entity atomicity does not authorize automatic replacement with a saga; compensation and reconciliation must exist in the authored process graph.

## Formal relations

- `arranges`: [[Contract Models]] — Projects boundary-relative requirements, guarantees, assumptions, and evidence obligations into substrate-facing roles without redefining their meanings.
- `arranges`: [[Realization]] — Relates provider-neutral requirement structure to candidate strategies, selected facilities, physical paths, and retained provenance.
- `constrains`: [[Infrastructure]] — Requires concrete infrastructure claims to identify the exact configured subject, scope, limits, evidence, and residual obligations they support.
