---
realm: Domain Semantics
kind: semantic-construct
created: 2026-11-05
updated: 2026-11-05
---

# Relationship

A relationship associates subjects with declared [[Identity|identities]]. It names participant roles, cardinality, and optionality: an order may have one assigned carrier while a carrier may serve many orders. These roles do not promise that either lookup is available.

An asserted association records a fact. If referential integrity is required, its contract says what counts as a live or superseded subject, at which boundary the reference must resolve, and how a broken reference is handled. A derived association, such as eligibility computed from current qualifications, instead depends on its derivation and the freshness of its inputs. A foreign key, embedded reference, or junction table is a realization choice.

## Formal relations

- `refines`: [[Relation]] — Restricts the correspondence to identified participants in declared roles.
