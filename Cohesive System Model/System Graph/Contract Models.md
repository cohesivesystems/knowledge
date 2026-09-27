---
realm: System Graph
kind: structural-construct
created: 2026-09-27
updated: 2026-09-27
status: draft
aliases:
  - Contract Model
  - Semantic Contract
  - Semantic Contracts
  - Protocol Contract
  - Protocol Contracts
---

# Contract Models

A contract model arranges the semantically relevant relationship between a modeled construct and its context at an explicit [[Boundaries|boundary]]. It states what the context must supply, what the construct may cause, what it promises under stated assumptions, and what evidence is required to support those claims.

A contract model is system-graph structure, not a new source of domain meaning or a container that collapses the model realms. Its referenced [[Effect|effects]], [[Invariant|invariants]], [[Policy|policies]], interactions, and other semantic concepts retain their domain meanings. [[Cohesive System Model#2. Operational Concerns|Operational concerns]] define properties such as ordering, durability, consistency, recovery, and service levels. [[Realization|Realization]] relates those demands to mechanisms and evidence. The contract model makes their roles and boundary-relative relationships explicit.

## Contract Dimensions

A contract model may include:

- **Requirements** describing properties, context, resources, authority, or knowledge that must be supplied.
- **Provided properties** describing what the construct or participant offers under declared assumptions.
- **Effects** describing state changes, emissions, interactions, failures, and resource use that may follow.
- **Coeffects** describing context demanded by the construct, including authority, observations, consistency, clocks, topology, or coordination.
- **Guarantees** describing properties established for an explicit subject, scope, interval, and operating boundary.
- **Invariants and constraints** describing properties that must be preserved during interaction, composition, or realization.
- **Assumptions** describing the failure model, workload envelope, configuration, environmental conditions, and participant obligations under which a claim holds.
- **Evidence obligations** describing which proofs, checks, attestations, tests, observations, or other evidence an accepted claim requires.

These dimensions are roles within one attributable contract, not independently maintained copies of semantic facts. [[Requirements and Capabilities|Requirements and capabilities]] use one vocabulary of properties while distinguishing a demanded role from a supplied role.

## Subjects, Scope, and Boundaries

A contract property must identify its subject and scope. A statement such as “idempotent,” “ordered,” “durable,” or “available” is incomplete until it states which operation, effect, history, identity, population, failure model, interval, and boundary it qualifies.

Contracts may qualify transitions, processes, relations, projections, systems, bindings, resources, participants, or realization mappings. A property can hold at one boundary and fail at another. Serialized execution inside one actor turn, for example, does not by itself establish ordered admission, durable recovery, stale-owner exclusion, or idempotent external effects across the larger process boundary.

## Protocol Contracts

A protocol contract is the interaction-oriented specialization of a contract model. It combines the legal trace described by an [[Interaction Protocols|interaction protocol]] with the requirements, effects, guarantees, assumptions, authority, and evidence that qualify participation in that trace.

The protocol and its contract remain distinguishable. The protocol states how interaction may unfold; the contract states what participants and their context must supply and what claims may be made about that interaction. A reusable [[Interfaces|interface]] can participate in several protocols, and one protocol can be qualified by different boundary- or policy-specific contracts.

## Composition and Preservation

Contract composition is not merely the union of component declarations. Connecting systems can discharge requirements, hide internal roles, propagate effects and contextual demands, weaken or strengthen guarantees, introduce interference, and create new cross-boundary obligations.

Every composition rule used for certification should state:

- the contract dimensions it relates;
- the direction of propagation or implication;
- the assumptions and compatibility conditions it requires;
- the properties it preserves, strengthens, weakens, translates, or forgets; and
- the residual obligations retained when no sound rule is available.

This yields two related closure questions. **Contract closure** asks whether every requirement is discharged, deliberately exposed, or retained as a residual obligation. **Assurance closure** asks whether every accepted claim has evidence sufficient under the active [[Assurance and Evidence|assurance and evidence]] policy. Structural wiring alone establishes neither.

## Modeling Checks

- What is the contract subject, boundary, scope, and effective revision?
- Which properties are requirements, provisions, effects, guarantees, assumptions, or evidence obligations?
- Which semantic and operational definitions do those properties reference?
- Which dimensions compose lawfully, and in which direction?
- What does an adapter preserve, translate, weaken, or assume?
- Which obligations remain after composition or realization?
- Does the available evidence support the claim at the same subject, scope, boundary, and revision?

## Formal relations

- `arranges`: [[Surfaces]] — Organizes the requirements, provided properties, effects, guarantees, assumptions, and evidence obligations intentionally exposed at a system boundary.
- `arranges`: [[Interaction Protocols]] — Qualifies legal interaction traces with participant obligations, guarantees, authority, failure assumptions, and evidence requirements.
- `constrains`: [[Realization]] — Requires a selected mapping to preserve or explicitly transform every contract property on which its context depends.
- `distinguished_from`: [[Interfaces]] — A contract model qualifies a boundary relationship, whereas an interface is a reusable intentional interaction type that may participate in several contracts.
