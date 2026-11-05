---
realm: Domain Semantics
kind: semantic-construct
created: 2026-07-05
updated: 2026-11-05
aliases:
  - Relations
---

# Relation

A relation is a typed correspondence between [[Shape|shapes]]. It specifies which values stand together; a source value can correspond to zero, one, or many target values, and conversely. A span of the form `source ← witnesses → target` expresses this without making either direction the privileged way to evaluate it.

A [[Relationship|relationship]] associates identified subjects. A [[Mapping|mapping]] computes corresponding values from a source observation; a [[Query|query]] derives named results from input collections and parameters. Forward lookup, inverse lookup, and membership testing are distinct capabilities: knowing which pairs belong does not promise an implementation for every mode.

In this graph, a *formal relation* is an authored predicate between concept notes, such as `arranges`. That is graph vocabulary. A hosting link or causal dependency does not become a domain relation merely because it connects two nodes.
