---
realm: Realization Substrate
kind: pattern
created: 2026-06-28
updated: 2026-07-04
---

# Write-Ahead Logging

Write-Ahead Logging, or WAL, is a storage recovery pattern in which durable recovery records are written before the corresponding state changes are allowed to become unrecoverable.

The core rule is that the log record describing a change must reach stable storage before the changed data page or state image can be relied on after failure. A commit record must be durable before the system reports the transaction as committed. This lets recovery reconstruct a coherent state by replaying, undoing, or completing work according to the durable log.

WAL [[Realization|realizes]] [[Persistence|persistence]], [[Reconstitution|reconstitution]], and [[Recovery|recovery]] for a storage or transaction boundary. It supports [[ACID|ACID]] durability and atomicity by making the recovery history more authoritative than any one cached page, memory image, or interrupted write.

Common WAL structures include:

- Log sequence numbers.
- Transaction identifiers.
- Update records.
- Commit and abort records.
- Checkpoints.
- Dirty-page and transaction tables.
- Redo and undo information.
- Compensation Log Records.

ARIES is the canonical database recovery design built around WAL. It uses analysis, redo, and undo phases after restart. Its Compensation Log Records, or CLRs, record undo actions in the log so recovery can repeat history safely, resume interrupted rollback, and avoid undoing the same action twice.

WAL is not the same as [[Event Sourcing|event sourcing]]. WAL records are usually internal storage-engine recovery material. Event-sourced records are committed domain events that are addressable in the application model. Both make durable ordered history central, but they assign different meanings to the records.

WAL is also not the same as saga compensation. ARIES Compensation Log Records are storage-engine recovery records for undo. Saga compensation is a semantic forward action, command, or process step across boundaries.

## External References

- C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, and Peter Schwarz, [ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging](https://web.stanford.edu/class/cs345d-01/rl/aries.pdf), ACM Transactions on Database Systems, 17(1):94-162, March 1992. [IBM Research](https://research.ibm.com/publications/aries-a-transaction-recovery-method-supporting-fine-granularity-locking-and-partial-rollbacks-using-write-ahead-logging)
- Jim Gray and Andreas Reuter, [Transaction Processing: Concepts and Techniques](https://www.microsoft.com/en-us/research/publication/transaction-processing-concepts-and-techniques/), Morgan Kaufmann, 1993.

Related concepts: [[Storage Systems|storage systems]], [[ACID]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Concurrency Control|concurrency control]], [[Event Sourcing|event sourcing]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Durable Execution|durable execution]].
