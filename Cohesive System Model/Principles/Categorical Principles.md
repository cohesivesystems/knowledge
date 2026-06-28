---
realm: Principles
kind: reference
---

# Categorical Principles

Categorical principles provide modeling discipline for the Cohesive System Model. They are not the entry point for ordinary readers, but they help keep distinctions precise when relating semantic dynamics, system structure, operational semantics, and realization substrate.

These principles are used to ask:

- What structure is preserved when one domain is related to another?
- Which concepts are dual, symmetric, or adjoint rather than identical?
- When can a model refer to "the" thing determined by a diagram of related things?
- Where does a construction lose, forget, quotient, aggregate, or create structure?
- Which relationships must commute for a realization, projection, reconstitution, or transition to be coherent?

Core principles:

- [[Stuff Structure Property]]: distinguish what the model contains, how it is organized, and what constraints it satisfies.
- [[Compositionality]]: complex meanings should be built from parts and their composition rules.
- [[Functoriality]]: mappings between domains should preserve the relationships and changes that matter.
- [[Naturality]]: transformations should commute with representation changes and avoid accidental dependence on implementation detail.
- [[Duality and Symmetry]]: paired concepts should be studied together without collapsing them into one thing or separating them too far.
- [[Universal Constructions]]: limits, colimits, and related universal properties let the model refer to canonical objects determined by their relationships.
- [[Equivalence vs Equality]]: sameness must be scoped to the equality or equivalence relation relevant to a boundary.

Additional recurring principles:

- [[Monads Monoids and Duals]]: sequencing, accumulation, context, observation, and dual structure.
- [[Algebras and Coalgebras]]: folding structure into values and unfolding values into behavior.
- [[Yoneda Lemma]]: objects are understood by their relationships, observations, and interactions.
- [[Adjunctions]]: paired translations that are structured but not inverse.
- [[Fibrations and Indexed Structure]]: context-dependent families over identities, boundaries, subjects, or semantic roles.
- [[Fixed Points and Recursion]]: recursive definitions, loops, stabilization, and repeated behavior.
- [[Enrichment and Order]]: relationships enriched with ordering, time, cost, authority, confidence, or guarantees.
- [[Optics and Lenses]]: focused observation, partial state, and view/update structure.
- [[Trace and Feedback]]: outputs feeding later inputs through modeled loops.

The point is not to force every concept into formal notation. The point is to use categorical language as a precision check: if a mapping does not preserve the required relations, if a duality is mistaken for identity, or if "the" object is named without its defining diagram, the model is probably hiding an assumption.

Related concepts: [[Realization]], [[Event-State Duality]], [[Behavior]], [[Persistence]], [[Reconstitution]], [[Concurrency Control]], [[Boundaries]].
