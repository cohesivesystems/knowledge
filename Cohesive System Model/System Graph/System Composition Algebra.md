---
realm: System Graph
kind: reference
created: 2026-08-14
updated: 2026-08-17
status: draft
aliases:
  - Cohesive Composition Algebra
  - Composition Algebra Overview
  - System Composition Algebra Plain-English Summary
---

# System Composition Algebra

This note is a draft, plain-language overview of how Cohesive describes the composition of systems. It summarizes vocabulary under active development; precise operators, typing judgements, equivalences, and proof rules require further refinement before they should be treated as normative.

A system is a recursively composable semantic unit with a selected boundary. It may contain semantic constructs and other systems, have arbitrary internal structure, and expose selected externally relevant semantics through typed [[Surfaces|surfaces]].

A system might model a bounded application, database, payment provider, message broker, actor runtime, workflow engine, deployment unit, organization, or another semantic unit with a selected boundary. These names describe roles or derived configurations rather than primitive system kinds. Large systems can contain and connect smaller systems, so the same approach applies at many scales.

## Systems and Domain Concepts Are Different

Not every concept in a software design is itself a system.

An order, for example, is primarily a business concept with identity, state, rules, and allowed changes. An order-processing application can be modeled as a system because it establishes an operationally relevant boundary: it receives requests, stores state, produces events, and makes claims to its users.

A system may contain semantic concepts such as orders, payments, and shipments without treating each concept as an independently running service. This keeps business meaning separate from infrastructure while allowing the two to be related through [[Realization|realization]].

## Systems Present Surfaces

A system presents its externally relevant boundary semantics through a typed [[Surfaces|surface]] at a declared [[Boundaries|boundary]]. A surface may describe:

- commands, queries, events, observations, or streams;
- required and provided capabilities;
- interaction protocols and compatibility rules;
- expected ordering, delivery, timing, availability, and consistency;
- failure meanings, security, and authority requirements;
- semantic [[Effect|effects]], resource constraints, and assumptions; and
- evidence supporting the system's claims.

An [[Interfaces|interface]] is a reusable intentional interaction type projected on a surface. A [[Ports and Adapters|port]] is a particular occurrence of that interface on a system boundary, provided or required under boundary-specific ownership, policy, scope, and evidence. An [[Interaction Protocols|interaction protocol]] describes how interaction through those roles may unfold, including direction, sequencing, branching, retries, failures, and terminal outcomes.

A surface is broader than an interface and is not identical to its boundary. The boundary establishes the cut between scopes; the surface organizes what the system intentionally exposes, requires, and claims at that cut; interfaces supply reusable interaction types; and ports instantiate those types for the bounded system.

## Systems Connect through Compatible Contracts

A surface can declare what the system provides, what it requires from its environment, which effects it may produce, which guarantees it claims, which assumptions limit those claims, and which evidence supports them.

A connection relates a required port on one system to a provided port on another. [[Interaction Bindings|Interaction bindings]] attach the exact interface and protocol roles to channel directions and endpoints.

[[Compatibility and Evolution|Compatibility]] is directional and is not based only on names or data shapes. Under a declared policy, the provided role must discharge the required role's obligations: protocol actions, sequencing, cardinality, ordering, failure meanings, authority, assumptions, and guarantees must compose in the required direction. When two roles do not match directly, an explicit adapter must state what it translates, preserves, weakens, or assumes.

Terms such as client and server describe roles within a particular connection. They are not permanent kinds of system. The same system may act as a client in one interaction and a server in another.

## Composition Creates Larger Systems

Systems can be connected sequentially or placed side by side. When a connection discharges a required port, the connected ports may become internal to the resulting composite. The composite exposes its remaining outer surface while retaining the internal graph and evidence needed to explain it.

For example, an order system may require storage and event publication. Connecting it to PostgreSQL and Kafka can discharge those requirements when their interfaces, protocols, operational properties, and realization evidence are compatible. The resulting order platform might expose only an orders interface while retaining its internal dependencies, assumptions, and evidence chain.

The intended composition discipline includes familiar structural expectations:

- regrouping the same well-typed connections should not change their externally observable meaning;
- every typed system should admit an identity composition that leaves its exposed surface unchanged;
- independent systems can be placed in parallel; and
- feedback is structurally possible, although its protocols and realization must still establish causality and safe runtime behavior.

These are design commitments for the emerging algebra. Their exact equality, equivalence, typing, and proof conditions remain to be formalized.

## Wiring Alone Does Not Create Guarantees

Connecting systems establishes that declared boundary roles fit together under the stated compatibility rules. It does not automatically prove that the composite is reliable, atomic, secure, durable, or highly available.

If a guarantee depends on a quorum, transaction coordinator, consensus algorithm, replication protocol, cache policy, retry mechanism, or another realization choice, that mechanism and the relevant boundary must be represented explicitly. This keeps the realization mechanism and the scope of its guarantee visible in the model.

Guarantees may initially be declarations supported by assumptions, provider attestations, checks, tests, observations, proofs, or other evidence. More capable compilers and validators may later establish that selected guarantees are earned through composition.

## Internal Details Can Be Hidden without Being Discarded

A composite system can present a simplified external surface while retaining its internal structure, assumptions, and evidence. The outside world sees what it may rely on; the model preserves why those claims are believed, which realizations support them, and which obligations remain unresolved.

Different practical views may intentionally omit information. Each abstraction should declare what it preserves, hides, weakens, or forgets instead of treating a simplified projection as the complete truth.

## Specifications Can Have Many Realizations

A semantic or structural requirement does not prescribe one technology. Durable, exclusively mutated order state might, for example, be realized by a PostgreSQL transaction, an actor runtime, an event-sourced aggregate, or another mechanism that satisfies the declared requirements.

Likewise, one technology can realize several different specifications. Realization is therefore a many-to-many, evidence-bearing relationship between semantic and system-graph specifications and concrete mechanisms. Neither side is reducible to the other.

## Familiar Infrastructure Terms Are Derived Concepts

Service, database, broker, actor, client, and server are useful names, but they are not all fundamental building blocks of the composition model. They are recognizable configurations of more basic concepts such as systems, surfaces, boundaries, interfaces, ports, protocols, capabilities, contracts, connections, state, processes, guarantees, assumptions, and evidence.

This allows Cohesive to describe both familiar infrastructure and new arrangements without continually adding unrelated primitive types.

## Questions the Algebra Should Answer

The composition algebra is intended to give Cohesive a machine-checkable way to answer:

1. What does this system mean at the declared boundary?
2. What does it require and provide through its surfaces?
3. Which other systems may connect to it?
4. What becomes internal when systems are composed?
5. Which obligations and assumptions remain unresolved?
6. What may users of the composite safely rely on?
7. Which realization and evidence justify those claims?

Related concepts: [[System Language and Realization|system language and realization]], [[System Graph|system graph]], [[Surfaces|surfaces]], [[Boundaries|boundaries]], [[Interfaces|interfaces]], [[Ports and Adapters|ports and adapters]], [[Interaction Protocols|interaction protocols]], [[Interaction Bindings|interaction bindings]], [[Service Models|service models]], [[Compatibility and Evolution|compatibility and evolution]], [[Compositionality|compositionality]], [[Trace and Feedback|trace and feedback]], [[Observability and Provenance|observability and provenance]], [[Realization|realization]].

## Formal relations

- `documents`: [[System Graph]] — Provides an accessible overview of how system-graph boundaries, surfaces, interfaces, bindings, and composites participate in system composition.
- `documents`: [[Surfaces]] — Explains the role of surfaces as boundary-relative external contracts in the emerging composition algebra.
- `documents`: [[Compositionality]] — Applies the general principle of meaning-preserving composition to Cohesive systems and their realizations.
- `documents`: [[Realization]] — Explains why composed specifications require explicit, evidence-bearing mappings to concrete mechanisms.
