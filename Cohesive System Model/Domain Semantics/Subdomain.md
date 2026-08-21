---
realm: Domain Semantics
kind: semantic-construct
created: 2026-08-01
updated: 2026-08-21
status: draft
aliases:
  - Sub-domain
  - Core subdomain
  - Supporting subdomain
  - Generic subdomain
---

# Subdomain

A subdomain is a coherent region of a larger [[Domain|domain]], distinguished by its subject matter, knowledge, activity, capability, purpose, policy, or strategic value.

A subdomain is a problem-space distinction. It identifies a portion of what must be understood or addressed, not the software boundary chosen to model or realize it. A useful subdomain has enough [[Cohesion and Coupling|semantic cohesion]] under a declared purpose that its concepts and relationships can be discussed together, and enough distinction that separating it clarifies the larger domain.

The decomposition is purpose-relative. The same domain may be partitioned by business capability for investment, by knowledge area for modeling, by regulatory responsibility for governance, or by another declared criterion. Subdomains can have relations or shared subject matter; calling something a subdomain does not by itself prove that it is independent or disjoint from every other subdomain.

## Strategic Classification

DDD commonly distinguishes subdomains by their strategic role:

- A **core subdomain** contains differentiating knowledge or capability central to the endeavor's advantage or purpose.
- A **supporting subdomain** is specific enough to require tailored understanding but is not itself the primary source of differentiation.
- A **generic subdomain** addresses a broadly shared problem for which a standard model, product, or external capability may be sufficient.

These roles are relative to an organization, product, and time. The same subject matter may be core for one organization and generic for another, and strategic changes may reclassify a subdomain without changing its basic vocabulary overnight. Classification guides attention and investment; it is not an intrinsic semantic type.

## Correspondence with Bounded Contexts

A [[Bounded Context|bounded context]] scopes one model and [[Ubiquitous Language|ubiquitous language]] in the solution or model space. It should not be used as a synonym for subdomain.

| Correspondence | Meaning |
| --- | --- |
| One subdomain, one bounded context | One model covers the relevant subject matter. This is a common alignment, not a rule. |
| Several subdomains, one bounded context | One coherent model draws on portions of several problem-space regions. |
| One subdomain, several bounded contexts | Different models select different purposes, users, histories, or aspects of the same subject matter. |
| Several subdomains, several bounded contexts | A context map records the general many-to-many relationship and the translations among models. |

A bounded context therefore models subject matter from one or more subdomains; it does not contain those subdomains as structural components. Conversely, when a subdomain “spans” contexts, the subject matter is represented by several boundary-scoped models rather than being structurally divided by definition.

## Failure Modes

- Deriving subdomains directly from the current service, team, repository, or database layout.
- Assuming every named business capability is automatically a semantically coherent subdomain.
- Treating core, supporting, and generic as permanent rankings rather than strategic classifications.
- Forcing a one-to-one bounded-context mapping and then distorting either the problem description or the model boundary to preserve it.

## External References

- Eric Evans, [*Domain-Driven Design Reference: Definitions and Pattern Summaries*](https://www.domainlanguage.com/ddd/reference/), especially “Core Domain,” “Generic Subdomains,” and “Domain Vision Statement.”
- Vaughn Vernon, [*Domain-Driven Design Distilled*](https://www.informit.com/store/domain-driven-design-distilled-9780134434988), Addison-Wesley Professional, 2016.

Related concepts: [[Domain|domain]], [[Bounded Context|bounded context]], [[Ubiquitous Language|ubiquitous language]], [[Domain-Driven Design|domain-driven design]], [[System Graph|system graph]], [[Boundaries|boundaries]], [[Authority|authority]], [[Policy|policy]], [[Invariant|invariant]], [[Entity|entity]], [[Process|process]], and [[Service|service]].
