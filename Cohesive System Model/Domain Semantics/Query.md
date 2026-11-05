---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-11-05
---

# Query

A query is a parameterized derivation from input collections to named results with declared [[Shape|shapes]]. It defines which tuples or values follow from the inputs. An evaluation is one invocation with particular parameters and selected outputs.

For example, an open-orders query can select orders for a given account. The definition exists whether an observer invokes it through a [[Query Request|query request]], uses it to build a read model, or evaluates it locally. Two evaluations can return different observations because their inputs, read boundaries, or parameters differ. The definition alone promises neither access to the inputs nor freshness of the result.

## Formal relations

- `refines`: [[Relation]] — A query defines a computed correspondence from input collections and parameters to result values.
