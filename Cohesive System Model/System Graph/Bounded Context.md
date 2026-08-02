---
realm: System Graph
kind: structural-construct
created: 2026-08-01
updated: 2026-08-01
status: draft
aliases:
  - Bounded contexts
  - DDD bounded context
---

# Bounded Context

A bounded context is a [[Boundaries|system-graph boundary]] within which a particular domain model is defined and applicable and its [[Ubiquitous Language|ubiquitous language]] has consistent meaning and ownership.

The boundary makes model expressions interpretable. Inside it, participants can use a term, relation, rule, or scenario according to one model without silently mixing incompatible interpretations. Outside it, the same expression may be absent, differently named, or governed by a different model. “Consistent” here means that the model and language are kept conceptually coherent; it does not by itself promise transactional, replicated-data, or temporal [[Consistency Models|consistency]].

A bounded context belongs primarily to the solution or model space. It gives selected [[Domain|domain]] subject matter structural scope in a modeled system. A [[Subdomain|subdomain]], by contrast, identifies a coherent region of problem-space subject matter.

## Boundary Dimensions

A bounded context should make explicit:

- the model whose expressions are valid within the boundary;
- the ubiquitous language used to discuss, test, document, and implement that model;
- the participants responsible for the model and authorized to evolve it;
- the code, interfaces, data, and other artifacts that express or realize the model;
- the admitted crossings and the source and target meanings at each crossing; and
- the relationships to other bounded contexts.

Team organization, application usage, codebases, schemas, services, and deployments can make a context boundary concrete and enforceable. They are manifestations or realization choices, not individually sufficient definitions. A boundary that exists only as a box in a diagram, with no control over language, model evolution, or crossings, is not being preserved in practice.

## Correspondence with Subdomains

Bounded contexts and subdomains need not correspond one-to-one:

| Correspondence | Interpretation |
| --- | --- |
| One subdomain, one bounded context | The model boundary aligns with one coherent region of subject matter. |
| Several subdomains, one bounded context | One model and language select subject matter from several subdomains. |
| One subdomain, several bounded contexts | Several models serve different purposes or participants within the same subject-matter region. |
| Several subdomains, several bounded contexts | A context map records the model boundaries, coverage, dependencies, and translations. |

The mapping should be stated rather than inferred from names. A context models portions of subdomains; it does not structurally contain problem-space regions. A subdomain represented in several contexts does not acquire several meanings in the abstract; each context supplies a particular model and interpretation of that subject matter.

## Context Maps and Crossings

A context map is a system-graph view of bounded contexts and their relationships. It records where translation, influence, dependency, collaboration, shared model material, or deliberate separation occurs.

Cross-context interaction should identify the source and target models, the translation owner, and what the mapping preserves, introduces, or forgets. An [[Anti-Corruption Layer|anti-corruption layer]], published language, open-host service, shared kernel, or explicit [[Interaction Protocols|interaction protocol]] may govern the crossing. These arrangements connect contexts without creating one global model.

## Non-Identities

A bounded context is not automatically one:

- domain or subdomain;
- aggregate or entity model;
- [[Service|service]] or [[Microservice|microservice]];
- application, module, code package, or repository;
- team or organizational unit;
- database, schema, transaction, or data-ownership boundary; or
- deployment unit, runtime process, container, or failure boundary.

Any of these may align with a bounded context when that alignment helps preserve the model and language. The correspondence must remain explicit because one element on either side may map to several on the other.

## Formal relations

- `arranges`: [[Ubiquitous Language]] — Gives one model-grounded language a structural scope of applicability, consistency, ownership, and evolution.
- `corresponds_to`: [[Subdomain]] — Relates model-space boundaries to problem-space subject matter through a mapping that may be one-to-one, one-to-many, many-to-one, or many-to-many.

## External References

- Eric Evans, [*Domain-Driven Design Reference: Definitions and Pattern Summaries*](https://www.domainlanguage.com/ddd/reference/), especially “Bounded Context,” “Ubiquitous Language,” and “Context Map.”
- Martin Fowler, [“Bounded Context”](https://martinfowler.com/bliki/BoundedContext.html), 2014.
- Vaughn Vernon, [*Implementing Domain-Driven Design*](https://www.informit.com/store/domain-driven-design-9780321834577), Addison-Wesley Professional, 2013.

Related concepts: [[Domain|domain]], [[Subdomain|subdomain]], [[Ubiquitous Language|ubiquitous language]], [[Domain-Driven Design|domain-driven design]], [[System Graph|system graph]], [[Boundaries|boundaries]], [[Anti-Corruption Layer|anti-corruption layer]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Service Models|service models]], [[Entity Models|entity models]], [[Authority|authority]], [[Compatibility and Evolution|compatibility and evolution]], [[Functoriality|functoriality]], and [[Realization|realization]].
