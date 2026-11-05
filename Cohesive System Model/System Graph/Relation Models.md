---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-11-05
aliases:
  - Relation Graph
  - Relation Graphs
  - Relational Model
  - Relational Models
---

# Relation Models

Relation models arrange a domain [[Relation|relation]] by assigning source and target shapes, participant roles, constraints, and supported modes of evaluation. For an asserted [[Relationship|relationship]], the model can name who owns the association and where references must resolve. For a derived one, it can identify the [[Mapping|mapping]] or [[Query|query]] that supplies its contents and the freshness required of the inputs.

A [[Projection Models|projection model]] can arrange the maintenance and exposure of those derived results. Hosting, causal dependency, and boundary inclusion remain meaningful system graph links, but they describe different structures; they do not imply an association stored or queried by the domain.

## Formal relations

- `arranges`: [[Relation]] — Places a domain correspondence in a modeled system with explicit roles, evaluation modes, constraints, and ownership.
