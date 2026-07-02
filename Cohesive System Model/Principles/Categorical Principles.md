---
realm: Principles
kind: reference
---

# Categorical Principles

Categorical principles provide modeling discipline for the Cohesive System Model. They are not the entry point for ordinary readers, but they help keep distinctions precise when relating domain semantics, system structure, operational semantics, and realization substrate.

These principles are used to ask:

- What structure is preserved when one domain is related to another?
- Which concepts are dual, symmetric, or adjoint rather than identical?
- When can a model refer to "the" thing determined by a diagram of related things?
- Where does a construction lose, forget, quotient, aggregate, or create structure?
- When do local observations agree enough to glue into a coherent global view?
- Which relationships must commute for a realization, projection, reconstitution, or transition to be coherent?

Core principles:

- [[Equivalence vs Equality]]: sameness must be scoped to the equality or equivalence relation relevant within a boundary.
- [[Functoriality]]: mappings between domains should preserve the relationships and changes that matter.
- [[Stuff Structure Property]]: distinguish what the model contains, how it is organized, and what constraints it satisfies.
- [[Compositionality]]: composite meanings should be built from parts and their composition rules.
- [[Duality and Symmetry]]: paired concepts should be studied together without collapsing them into one thing or separating them too far.
- [[Naturality]]: avoid accidental dependence on implementation detail.
- [[Sheaves and Gluing]]: local observations must agree on overlaps before they can be glued into a coherent global view of system [[State|state]].
- [[Universal Constructions]]: define canonical objects through their relationships to other objects.

Additional recurring principles:

- [[Monads Monoids and Duals]]: sequencing, accumulation, context, observation, and dual structure.
- [[Algebras and Coalgebras]]: folding structure into values and unfolding values into behavior.
- [[State Machines|State machines]]: transition-based models of behavior that relate inputs, state, outputs, and runs.
- [[Yoneda Lemma]]: objects are understood by their relationships, observations, and interactions.
- [[Adjunctions]]: paired translations that are structured but not inverse.
- [[Fibrations and Indexed Structure]]: context-dependent families over identities, boundaries, subjects, or semantic roles.
- [[Systems Sheaf Semantics]]: local-to-global consistency for observer-relative sections of observations, states, versions, histories, and explanations.
- [[Database Sheaf Semantics]]: local-to-global consistency for relational schemas, database instances, views, joins, and mappings.
- [[Fixed Points and Recursion]]: recursive definitions, loops, stabilization, and repeated behavior.
- [[Enrichment and Order]]: relationships enriched with ordering, time, cost, authority, confidence, or guarantees.
- [[Optics and Lenses]]: focused observation, partial state, and view/update structure.
- [[Trace and Feedback]]: outputs feeding later inputs through modeled loops.

The point is not to force every concept into formal notation. The point is to use categorical language as a precision check: if a mapping does not preserve the required relations, if a duality is mistaken for identity, or if "the" object is named without its defining diagram, the model is probably hiding an assumption.

Related concepts: [[Realization|realization]], [[Event-State Duality|event-state duality]], [[Behavior|behavior]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Concurrency Control|concurrency control]], [[Boundaries|boundaries]].
