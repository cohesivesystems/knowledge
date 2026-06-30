---
realm: Architecture Practices
kind: architecture-practice
---

# Data Mesh

Data Mesh addresses the problem of scaling analytical and operational data ownership across organizational and domain boundaries.

## Cohesive Formulation

Data Mesh can be expressed as ownership and projection boundaries:

- Domain teams own data products as boundary-scoped observations or projections.
- Data products expose contracts for interpretation, freshness, lineage, access, and quality.
- Consumers observe data through explicit boundaries rather than shared implicit databases.
- Governance is policy over identities, access, lineage, retention, and quality.

## In the Model

A data product is not merely a dataset. It is a boundary-specific observation surface with declared semantics, source relationships, reconstitution rules, policies, and operational guarantees.

## Failure Modes

The practice fails when data products are just replicated tables without ownership, lineage, interpretation rules, freshness guarantees, or recovery semantics.

Related concepts: [[Boundaries|boundaries]], [[Observation|observation]], [[Projections|projections]], [[Policies|policies]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Realization|realization]], [[CQRS as Architecture Practice|CQRS as architecture practice]].
