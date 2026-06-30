---
realm: Operational Semantics
kind: operational-semantics
---

# Recovery

Recovery defines how a system returns to coherent operation after failure, interruption, conflict, timeout, overload, or partial progress.

Recovery depends on the durable material provided by [[Persistence|persistence]] and the method used for [[Reconstitution|reconstitution]].

Retry is one recovery mechanism, but recovery is broader than retry. Some failures are recovered by re-driving incomplete work, while others require replay, reconstitution, compensation, rebuilding, or operator intervention.

Recovery may include:

- Replaying event history.
- Loading snapshots and subsequent events.
- Resuming workflow history.
- Rebuilding projections.
- Restoring CRDT replica state and causal metadata.
- Re-driving [[Outbox|outbox]] records.
- Rechecking [[Transactional Inbox|inbox]] or deduplication records before repeating local effects.
- Retrying incomplete work.
- Resuming durable execution state or replaying durable execution history.
- Compensating completed work.
- Activating an actor by identity.

Recovery must preserve the meaning of entity versions, committed events, idempotency records, CRDT causal metadata, and observer boundaries. Otherwise, the system may recover operationally while changing its semantic history or breaking convergence.

Database recovery systems such as ARIES make this explicit through [[Write-Ahead Logging|write-ahead logging]], transaction identifiers, log sequence numbers, checkpoints, redo, undo, and Compensation Log Records. The durable log is not merely an audit artifact; it is the material that lets the system reconstruct a coherent committed state after crash, partial rollback, or restart.

In [[Safety and Liveness|safety and liveness]] terms, recovery is a liveness mechanism constrained by safety. It should restore progress without inventing histories, duplicating non-idempotent effects, losing committed facts, or weakening the boundary's consistency claim.

## External References

- C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, and Peter Schwarz, [ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging](https://web.stanford.edu/class/cs345d-01/rl/aries.pdf), ACM Transactions on Database Systems, 17(1):94-162, March 1992. [IBM Research](https://research.ibm.com/publications/aries-a-transaction-recovery-method-supporting-fine-granularity-locking-and-partial-rollbacks-using-write-ahead-logging)

Related concepts: [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[ACID]], [[Write-Ahead Logging|write-ahead logging]], [[Durable Execution|durable execution]], [[Retry|retry]], [[Idempotency|idempotency]], [[Safety and Liveness|safety and liveness]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Coordination|coordination]], [[Dual-Write Problem|dual-write problem]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Event Sourcing|event sourcing]], [[CRDTs]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Actor Systems|actor systems]].
