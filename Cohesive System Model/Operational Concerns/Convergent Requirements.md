---
realm: Operational Concerns
kind: operational-concern
created: 2026-11-05
updated: 2026-11-05
---

# Convergent Requirements

A convergent requirement allows an intermediate state under an explicit contract. State the required outcome, the time bound and failure assumptions, which observers can see or act on intermediate states, and the required disposition if the outcome is missed.

For example, an accepted order must receive an assignment within thirty seconds under the stated delivery assumptions, or enter declared recovery. Dispatch may see the pending assignment; billing must not act as if assignment were complete. Compensation is another observable action, not erasure of an earlier one. An outbox or saga meets this contract only if the selected arrangement also satisfies its visibility, timing, and recovery conditions.

A **window-free invariant**, such as “allocated capacity never exceeds available capacity,” allows no violating interval. Repair after overcommitment is too late. A shared commit boundary or a reservation that makes the constraint local might preserve it; neither follows from eventual convergence.

## Formal relations

- `qualifies`: [[Arrangement Models]] — Determines whether the arrangement preserves the promised outcome, visibility, bound, and recovery under its failure assumptions.
- `distinguished_from`: [[Invariant]] — Eventual repair cannot establish an invariant that must hold throughout the intermediate interval.
