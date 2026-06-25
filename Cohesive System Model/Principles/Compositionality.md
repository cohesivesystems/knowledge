---
realm: Principles
---

# Compositionality

Compositionality is the principle that complex systems should be understood from parts and the rules by which those parts compose.

In the Cohesive System Model, compositionality asks whether semantic dynamics, system structure, operational semantics, and realization choices can be assembled without changing their intended meanings.

Compositionality helps ask:

- What are the parts?
- What interfaces, boundaries, or relations connect them?
- What meaning is preserved when parts are composed?
- What new behavior emerges only from the composition?
- Which guarantees compose, and which guarantees remain local to a boundary?

Examples:

- [[Business Transactions]] compose processes, flows, semantic roles, application protocols, operational guarantees, and realization substrate into domain-level work.
- [[Flows]] compose observers, events, commands, and delivery semantics into interaction paths.
- [[Processes]] compose multiple transitions and observers across time.
- [[Realization]] choices compose only when their guarantees preserve the intended semantic relations.
- [[Coordination]] is needed when local transitions must compose into coherent multi-participant work.

Compositionality fails when two parts are individually correct but their combination changes meaning. For example, an idempotent command handler and an at-least-once broker do not compose into exactly-once domain semantics unless the boundary, persistence, and concurrency rules also compose.

Related concepts: [[Business Transactions]], [[Flows]], [[Processes]], [[Relations]], [[Boundaries]], [[Coordination]], [[Realization]], [[Functoriality]].
