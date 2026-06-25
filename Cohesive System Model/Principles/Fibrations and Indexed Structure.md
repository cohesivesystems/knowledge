---
realm: Principles
---

# Fibrations And Indexed Structure

Realm: Principles

Fibrations and indexed structure describe situations where each object in a base domain has a category of things lying over it.

Informally:

```txt
base object -> fiber of things over that object
```

This is useful whenever meaning is context-dependent:

- Realizations over a semantic role.
- Observations over a subject.
- Versions over an identity.
- Policies over a boundary.
- Commands over an observer and target entity.
- Processes over a correlation identity.

The Grothendieck construction turns an indexed family of categories into one total category of pairs:

```txt
(base object, thing over it)
```

Examples:

- [[Realization]] can assign each semantic object a category of possible realizations.
- An entity identity can index the versions, observations, events, and state samples belonging to that entity.
- A boundary can index the observers, policies, guarantees, and meanings valid inside it.
- A workflow identity can index the durable history and activations belonging to that workflow.

Fibrational thinking prevents context from being erased. It keeps clear that an observation is not just a value, a version is not just a number, and a realization is not just an implementation artifact. Each is something over a subject, identity, boundary, or semantic role.

Related concepts: [[Realization]], [[Observation]], [[Identity]], [[Version]], [[Boundaries]], [[Observer]], [[Processes]].
