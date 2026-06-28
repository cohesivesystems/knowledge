---
realm: System Structure
---

# Invariants

Invariants describe where validity constraints are attached in the system graph.

At the structure level, an invariant constrains the evolution of an [[Entity]] by ruling out transitions that would produce invalid state or violate a domain rule. This describes the semantic constraint and its scope, not a specific validation mechanism or runtime enforcement substrate.

Under the [[Stuff Structure Property]] lens, an invariant is primarily property: a constraint or predicate that valid stuff and structure must satisfy. It may become structure when represented explicitly as a policy object, validation rule, or first-class model element.

Invariants may be checked against:

- Current state observations.
- Expected versions.
- Related entities or projections.
- Process state.
- Policy and authority context.
- External facts observed through an observer boundary.

When an invariant fails, the command is rejected for the target entity and no endogenous event is committed for that entity.

With [[CRDTs]], invariants must be checked for compatibility with monotonic merge or commutative updates. Non-monotonic invariants may still require coordination, escrow, reservations, or a different data model.

Related concepts: [[Entity]], [[State]], [[Observation]], [[Command]], [[Transition]], [[Version]], [[Stuff Structure Property]], [[Concurrency Control]], [[CRDTs]].
