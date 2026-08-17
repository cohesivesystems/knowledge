---
realm: System Graph
kind: structural-construct
created: 2026-08-14
updated: 2026-08-17
status: draft
aliases:
  - Surface
  - System Surface
  - Contract Surface
---

# Surfaces

A surface is a typed, boundary-relative abstraction of a modeled system's externally relevant semantics. It declares what the system provides, requires, may affect, claims under stated assumptions, and must substantiate with evidence without exposing the system's entire internal graph.

A surface is not the boundary itself. A boundary establishes a cut between scopes and determines which meanings, authorities, observations, failures, and guarantees are relative to that cut. A surface selects and organizes what the system intentionally makes externally relevant at the cut. A boundary may expose no surface, one surface, or several audience-relative surfaces.

## Surface Contents

A surface may declare:

- provided and required capabilities expressed through ports typed by [[Interfaces|interfaces]];
- governing [[Interaction Protocols|interaction protocols]] and compatibility rules;
- expected inputs, outputs, observations, state projections, and semantic [[Effect|effects]];
- semantic obligations, assumptions, failure meanings, and authority requirements;
- boundary-relative operational claims such as ordering, delivery, consistency, availability, timing, and resource limits; and
- evidence, provenance, attestations, checks, or observations supporting those claims.

These declarations do not all belong to the same realm. Interfaces and their arrangement belong to the system graph. Their semantic meanings originate in domain semantics. Operational concerns qualify the declared behavior. [[Realization|Realization]] relates the surface and its demands to mechanisms and capability evidence. A surface brings those references together as an external contract without collapsing their meanings.

## Surface, Boundary, Interface, and Protocol

| Term | Governing question |
| --- | --- |
| [[Boundaries\|boundary]] | Which scopes are separated, and relative to which cut do meaning, authority, visibility, failure, and guarantees apply? |
| surface | What does the system intentionally expose, require, claim, and support with evidence at that boundary? |
| [[Interfaces\|interface]] | Which reusable intentional interaction type is projected on the surface? |
| [[Ports and Adapters\|port]] | Which occurrence of an interface is provided or required at this system boundary? |
| [[Interaction Protocols\|interaction protocol]] | In which legal traces may participants use the interface roles? |
| [[Interaction Bindings\|interaction binding]] | How are exact interface and protocol roles attached to channel directions and endpoints? |
| realization | Which concrete mechanisms preserve the bound contract and its required properties? |

An interface is therefore a reusable interaction type projected on a surface, not a synonym for the whole surface. A port is the boundary occurrence through which a system provides or requires that interface. A surface may project several interfaces through several ports and may also expose non-interaction claims such as operating assumptions, resource limits, security posture, or evidence. Conversely, a boundary may exist only to separate ownership, trust, consistency, persistence, or failure scopes and expose no surface or port.

Unqualified *surface* in Cohesive means this typed contract abstraction. Compound phrases such as *observation surface*, *decision surface*, or *administration surface* name specialized projections only when they satisfy this definition; otherwise they should be described as views, scopes, or facilities rather than as surfaces.

## Audience-Relative Projections

The same system may present different surfaces to different participants or purposes. A consumer surface may expose supported operations and service levels, an operator surface may additionally expose control and diagnostic capabilities, and a realization-facing surface may describe substrate requirements. These are projections of one modeled system, not automatically complete or interchangeable descriptions.

A projection should state what it preserves, hides, weakens, or forgets. Hiding internal structure is legitimate encapsulation; silently dropping an externally relevant obligation or assumption changes the contract.

## Composition and Internalization

Systems compose when provided and required ports on their surfaces are connected through explicit [[Interaction Bindings|bindings]]. [[Compatibility and Evolution|Compatibility]] is directional: under a declared policy, the provided interface and protocol behavior must discharge the required role's obligations, and the provider's guarantees must satisfy the requirement under compatible assumptions. Names and value shapes are insufficient; sequencing, cardinality, authority, failure meanings, effects, and operational properties must also be checked. An adapter may reconcile a mismatch only by declaring what it translates, preserves, weakens, or assumes.

When a connection satisfies a dependency, the connected roles may become internal to the composite and disappear from its public surface. The composite retains the internal boundaries, bindings, obligations, assumptions, realization mappings, and evidence needed to explain its remaining external claims. Internalization changes visibility; it does not erase provenance.

The composite surface is not necessarily the simple union of the component surfaces. Some required roles are discharged, some claims remain local to an internal boundary, and new composite behavior or unresolved obligations may emerge. See [[System Composition Algebra|system composition algebra]] for the accessible overview of this composition model.

## Guarantees and Evidence

A surface can declare a guarantee only at an explicit boundary and under explicit assumptions. Wiring compatible interfaces together does not by itself establish reliability, atomicity, security, availability, or another operational property. The mechanism that earns such a claim must be represented through operational qualifications and [[Realization|realization]] evidence.

Evidence may include provider attestations, static checks, proofs, tests, observed traces, configuration facts, or monitored behavior. Different evidence supports different confidence and scope. See [[Observability and Provenance|observability and provenance]] for the distinction between a claim and the evidence used to support it.

Related concepts: [[System Graph|system graph]], [[System Composition Algebra|system composition algebra]], [[Boundaries|boundaries]], [[Interfaces|interfaces]], [[Ports and Adapters|ports and adapters]], [[Interaction Protocols|interaction protocols]], [[Interaction Bindings|interaction bindings]], [[Compatibility and Evolution|compatibility and evolution]], [[Service Models|service models]], [[Service Levels|service levels]], [[Effect|effect]], [[Effect Models|effect models]], [[Observability and Provenance|observability and provenance]], [[Compositionality|compositionality]], [[Realization|realization]].

## Formal relations

- `arranges`: [[Interfaces]] — A surface projects reusable interface types through provided and required ports as part of the external contract at a declared boundary.
- `distinguished_from`: [[Boundaries]] — A boundary establishes the cut between scopes, whereas a surface organizes what a system intentionally exposes, requires, and claims at that cut.
- `distinguished_from`: [[Interfaces]] — A surface is the broader boundary-relative contract abstraction, whereas an interface is a reusable intentional interaction type projected on it.
