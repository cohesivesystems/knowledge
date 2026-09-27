---
realm: Principles
kind: principle
created: 2026-09-27
updated: 2026-09-27
status: draft
aliases:
  - Requirement and Capability
  - Demands and Offers
  - Requirement Demand
  - Capability Offer
---

# Requirements and Capabilities

Requirements and capabilities are distinct roles played by properties in a system description. A requirement states a property that a context or realization must establish. A capability states a property that a participant, facility, or composition claims it can provide under explicit conditions.

The roles should refer to one canonical vocabulary of properties rather than separate application and provider taxonomies. [[Idempotency]], [[Ordering]], [[Durability]], [[Consistency Models|consistency]], [[Isolation]], [[Recovery]], and [[Service Levels|service levels]] retain the same meanings when demanded by an application or offered by a facility. The role, subject, scope, assumptions, limits, and evidence differ.

## Parameterized Properties

A useful requirement or capability is more precise than a feature name. It identifies:

- the subject, operation, effect, binding, resource, or history being qualified;
- the identity or partition over which the property is scoped;
- the relevant [[Boundaries|boundary]] and participants;
- the failure, timing, workload, locality, and configuration assumptions;
- the interval or revision for which the claim is intended; and
- the [[Assurance and Evidence|evidence]] required or available.

“Supports transactions,” “uses actors,” or “has duplicate detection” does not by itself establish an application property. Likewise, an application requirement should state observable intent rather than prescribe a provider product or mechanism unless that dependency is intentionally part of the model.

## Discharge Is a Derivation

Application requirements and facility capabilities are generally many-to-many. One requirement may need several facilities, an auxiliary protocol, and an application obligation. One coherent facility configuration may jointly discharge several requirements.

A realization strategy therefore establishes a derivation of the form:

```text
offered properties
+ configuration and boundary facts
+ application or protocol obligations
+ stated assumptions
=> required property
```

The derivation may use:

- **Implication**, where a stronger property entails a weaker requirement within the same scope.
- **Composition**, where several supplied properties jointly establish a requirement.
- **Decomposition**, where one higher-level requirement induces several lower-level requirements.
- **Restriction**, where a property holds only for a partition, region, transaction, session, workload, or failure boundary.
- **Qualification**, where configuration, version, limits, or an operating envelope condition the offer.
- **Conflict analysis**, where individually available capabilities cannot coexist in one coherent realization.
- **Residual obligation**, where the facility supplies part of the construction and the application, operator, or another participant must supply the remainder.
- **Explicit weakening**, where an authorized policy accepts a weaker property without claiming that the original requirement was proved.

Capability-name equality is not such a derivation.

## Coherent Offers

Evidence must describe one coherent configured subject. A planner may not combine ordering evidence from one configuration, availability evidence from another, and duplicate-detection evidence from a third as though they described one deployable facility.

Capabilities can also be relational. Atomicity between state and publication, fencing between a lease and an authoritative store, authorization between a workload and resource, or ordering between producer and consumer belongs to a binding or multi-party construction rather than to one isolated node.

## Claims and Reality

A provider capability is a scoped claim, not an axiom about reality. Documentation, configuration analysis, certification, conformance testing, deployment attestation, and runtime observation provide different evidence for that claim. A formal theorem can establish what follows if the claim and its assumptions hold; it cannot by itself prove that a deployed provider behaves as claimed.

## Modeling Checks

- Is the statement a requirement, a capability offer, or a derived guarantee?
- Do the requirement and offer refer to the same canonical property definition?
- Are their subjects, scopes, parameters, boundaries, and failure models aligned?
- Which realization strategy justifies the implication or composition?
- Does the evidence describe one coherent configured subject?
- Which obligations remain with application code, operators, or other facilities?
- Is an accepted weakening clearly distinguished from satisfaction?

## Formal relations

- `constrains`: [[Contract Models]] — Requires demanded and provided roles to reference shared property meanings while retaining their different subjects, scopes, assumptions, and evidence.
- `constrains`: [[Realization]] — Requires requirement discharge to use an explicit implication, composition, restriction, or authorized weakening rather than name-based capability matching.
- `refines`: [[Judgement]] — Specializes context-indexed judgement to the relation between demanded properties, supplied properties, construction rules, assumptions, and evidence.
