---
realm: System Graph
kind: structural-construct
created: 2026-11-05
updated: 2026-11-05
---

# Arrangement Models

An arrangement model records how a system is divided into units: which unit owns a decision, which changes must commit together, what is serialized by key, what can fail independently, and which interactions cross unit boundaries. These are choices made during realization but described without choosing facilities. Assigning order acceptance to its own unit is an arrangement decision; selecting a database for that unit is a resource binding.

Two arrangements may contain the same domain constructs and expose different intermediate states or failure behavior. Moving an assignment decision across a unit boundary requires rechecking visibility, timing, recovery, and authority at the affected surfaces. An unchanged list of entities and transitions does not establish that the new arrangement preserves the contract.

## Formal relations

- `arranges`: [[Boundaries]] — Places ownership, commitment, interaction, and failure boundaries around selected units of the modeled system.
