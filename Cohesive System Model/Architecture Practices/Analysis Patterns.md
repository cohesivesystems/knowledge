---
realm: Architecture Practices
kind: reference
created: 2026-07-28
updated: 2026-07-28
aliases:
  - Analysis Pattern Language
  - Reusable Object Models
---

# Analysis Patterns

Analysis Patterns, by Martin Fowler, collects reusable structures discovered while modeling domains such as health care, financial trading, accounting, and organizational relationships.

The catalog gravitates toward domain semantics and system-graph structure. It is complementary to DDD: analysis patterns provide candidate model structures, while DDD emphasizes the language, boundaries, collaboration, and continuous refinement through which a model becomes authoritative for a particular domain context.

## Cohesive Correspondence

- Party, role, organization, and accountability structures correspond to [[Entity|entities]], [[Relation|relations]], [[Authority|authority]], temporal qualifications, and [[Relation Models|relation models]].
- Observation and measurement structures correspond to [[Observable|observables]], contextual [[Observation|observations]], [[Value|values]], [[Shape|shapes]], [[Time|time]], provenance, and [[Uncertainty|uncertainty]].
- Accounting and transaction structures correspond to events, states, processes, quantities, claims, histories, balancing relations, and business transactions at declared boundaries.
- Planning and trading structures correspond to processes, proposals, agreements, obligations, policies, projections, and later fulfillment events.

## Boundary of Adoption

An analysis pattern is a candidate semantic structure, not a universal ontology. The same real-world subject may be modeled differently in different bounded contexts, and a reusable object-model diagram does not determine persistence, API shape, service boundary, workflow, or runtime realization.

The functorial question is whether a pattern imported into a context preserves the identities, relations, temporal qualifications, quantities, and changes that matter there. A convenient class correspondence is insufficient when it loses authority, provenance, units, uncertainty, or domain distinctions.

## External References

- Martin Fowler, [*Analysis Patterns: Reusable Object Models*](https://martinfowler.com/books/ap.html), Addison-Wesley, 1996.

Related concepts: [[Pattern Languages and Correspondence|pattern languages and correspondence]], [[Domain-Driven Design|domain-driven design]], [[Patterns of Enterprise Application Architecture|enterprise application patterns]], [[Entity|entity]], [[Relation|relation]], [[Relation Models|relation models]], [[Observable|observable]], [[Observation|observation]], [[Value|value]], [[Shape|shape]], [[Time|time]], [[Authority|authority]], [[Uncertainty|uncertainty]], [[Business Transactions|business transactions]], [[Boundaries|boundaries]], [[Functoriality|functoriality]].
