---
realm: Domain Semantics
kind: semantic-construct
created: 2026-07-05
updated: 2026-07-05
aliases:
  - Relations
---

# Relation

A relation is a meaningful connection, dependency, association, correspondence, constraint, derivation, or causal link between semantic subjects.

Relations may connect [[Entity|entities]], [[Identity|identities]], [[State|state]], [[Observation|observations]], [[Event|events]], [[Observer|observers]], [[Process|processes]], [[Transition|transitions]], [[Invariant|invariants]], [[Policy|policies]], or [[Boundaries|boundaries]]. A relation says that one part of the model matters to another; it is not defined by a database join, foreign key, pointer, network call, or graph-storage edge.

Relations are interpreted relative to a model boundary. The same pair of subjects may be related differently under different purposes: ownership, reference, dependency, derivation, observation, causation, authorization, inclusion, or equivalence may all carry different meanings.

At the system graph layer, relations are arranged as [[Relation Models|relation models]]. A relation model may later be realized by foreign keys, indexes, graph edges, embedded documents, materialized projections, subscriptions, event streams, API links, shared state, or runtime routing, but those mechanisms do not exhaust the semantic relation.

Related concepts: [[Entity|entity]], [[Identity|identity]], [[State|state]], [[Observation|observation]], [[Event|event]], [[Observer|observer]], [[Process|process]], [[Transition|transition]], [[Boundaries|boundaries]], [[Relation Models|relation models]], [[Projection Models|projection models]], [[Relational and Logic Programming|relational and logic programming]], [[Realization|realization]].
