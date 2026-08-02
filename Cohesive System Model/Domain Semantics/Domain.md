---
realm: Domain Semantics
kind: semantic-construct
created: 2026-08-01
updated: 2026-08-01
status: draft
aliases:
  - Problem domain
  - Domain of discourse
---

# Domain

A domain is a sphere of knowledge, activity, or concern selected as subject matter for understanding, modeling, or action.

A domain establishes what is being discussed: its relevant subjects, phenomena, distinctions, vocabulary, rules, goals, and open questions. Its scope is relative to an inquiry or endeavor. “Commerce,” “insurance,” “claims handling,” and “payment settlement” can each be treated as a domain at a different scale when the chosen scope is explicit.

A domain is not identical to a domain model. The domain is the subject matter; a domain model is a selected system of abstractions used to describe and reason about aspects of that subject matter for a purpose. Several models may give different, simultaneously useful accounts of the same domain.

A domain is also not identical to the Domain Semantics realm. Domain Semantics supplies general meaning-bearing constructs such as [[Entity|entity]], [[Value|value]], [[Relation|relation]], [[Event|event]], [[Process|process]], [[Invariant|invariant]], and [[Policy|policy]] with which particular domains can be described. A domain supplies the particular subject matter and distinctions expressed through those constructs.

## Decomposition

A [[Subdomain|subdomain]] identifies a coherent region of a larger domain. The decomposition criterion should be explicit: knowledge, activity, capability, purpose, policy, strategic value, or another semantic distinction. Different criteria can yield different decompositions, so a subdomain boundary is not discovered solely from code, organization charts, or deployment topology.

Domains and subdomains belong primarily to problem-space description. A [[Bounded Context|bounded context]] belongs primarily to the [[System Graph|system graph]]: it scopes the applicability and ownership of a particular model and its [[Ubiquitous Language|ubiquitous language]]. The correspondence may be one-to-one, but it need not be.

## Distinctions

- A domain is not a service, application, product, team, repository, database, or deployment boundary.
- A domain does not require one canonical model. Multiple purposes and observers may require several models and languages.
- A domain boundary does not by itself assign [[Authority|authority]], operational guarantees, or realization mechanisms. Those choices must be made in the system graph and its realization.
- A domain name does not guarantee shared meaning. Its terms remain relative to an explicit model and context.

## External References

- Eric Evans, [*Domain-Driven Design Reference: Definitions and Pattern Summaries*](https://www.domainlanguage.com/ddd/reference/), definition of “domain.”
- Eric Evans, [*Domain-Driven Design: Tackling Complexity in the Heart of Software*](https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217), Addison-Wesley Professional, 2003.

Related concepts: [[Subdomain|subdomain]], [[Bounded Context|bounded context]], [[Ubiquitous Language|ubiquitous language]], [[Domain-Driven Design|domain-driven design]], [[System Graph|system graph]], [[Entity|entity]], [[Relation|relation]], [[Value|value]], [[Event|event]], [[Process|process]], [[Invariant|invariant]], [[Policy|policy]], [[Observer|observer]], [[Authority|authority]], and [[Boundaries|boundaries]].
