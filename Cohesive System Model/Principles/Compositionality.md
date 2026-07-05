---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-07-05
---

# Compositionality

Compositionality is the principle that complex systems should be understood from parts and the rules by which those parts compose.

In the Cohesive System Model, compositionality asks whether domain semantics, system graph, operational concerns, and realization choices can be assembled without changing their intended meanings.

Compositionality helps ask:

- What are the parts?
- What interfaces, boundaries, or relations connect them?
- What meaning is preserved when parts are composed?
- What new behavior emerges only from the composition?
- Which guarantees compose, and which guarantees remain local to a boundary?

Examples:

- [[Business Transactions]] compose process graphs, flow views, semantic roles, application protocols, operational guarantees, and realization substrate into domain-level work.
- [[Process Graphs]] compose multiple transitions, observer models, decisions, effects, and flow views across time.
- [[Flow Views]] compose observers, events, commands, and delivery semantics into movement paths within or between process graphs.
- [[Realization]] choices compose only when their guarantees preserve the intended semantic relations.
- [[Coordination]] is needed when local transitions must compose into coherent multi-participant work.

Compositionality fails when two parts are individually correct but their combination changes meaning. For example, an idempotent command handler and an at-least-once broker do not compose into exactly-once domain semantics unless the boundary, persistence, and concurrency rules also compose.

Related concepts: [[Business Transactions|business transactions]], [[Process|process]], [[Process Graphs|process graphs]], [[Flow Views|flow views]], [[Relation Models|relation models]], [[Relation|relations]], [[Boundaries|boundaries]], [[Coordination|coordination]], [[Realization|realization]], [[Functoriality|functoriality]].
