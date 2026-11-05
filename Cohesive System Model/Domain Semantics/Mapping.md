---
realm: Domain Semantics
kind: semantic-construct
created: 2026-11-05
updated: 2026-11-05
---

# Mapping

A mapping is a derivation rooted in a source [[Observation|observation]]. For example, a mapping from a shipment notice to shipment lines computes zero or more target values per notice. It can discard source distinctions, such as the spelling of a unit. A [[Query|query]] instead takes input collections and parameters and defines named results.

An inverse lookup may find several notices compatible with a line. That is different from reconstructing the original notice. A bidirectional transformation must declare its inverse and the laws it satisfies; [[Codecs|codecs]] make those promises explicit at representation boundaries.

## Formal relations

- `refines`: [[Relation]] — Computes the corresponding target values from each source observation.
