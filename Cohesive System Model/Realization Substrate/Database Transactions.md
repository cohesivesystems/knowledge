---
realm: Realization Substrate
kind: realization-substrate
created: 2026-08-01
updated: 2026-08-01
status: draft
aliases:
  - Database Transaction
  - RDBMS Transaction
  - DB Transaction
---

# Database Transactions

Database Transactions are bounded units of database work whose covered operations commit or abort according to a transaction manager's contract.

A database transaction is a realization mechanism, not the semantic work itself. It may realize an atomic [[Commit Boundaries|commit boundary]], an [[ACID]] contract, and a selected [[Isolation|isolation]] level for reads and writes controlled by one database or a declared set of participating resource managers. Its guarantees do not extend to an HTTP reply, broker publication, workflow continuation, external API, human decision, or other effect merely because that effect was initiated while the transaction was open.

A [[Business Transactions|business transaction]] instead names domain work whose acceptance, rejection, compensation, or completion matters to the business. One business transaction may contain several database transactions and other commitments over a much longer period. The two boundaries coincide only when the whole business outcome and every effect required for that outcome are covered by the database transaction.

## Contract and Boundary

A database-transaction model should state:

- Which reads, writes, constraints, tables, partitions, databases, and resource managers are covered.
- What commit, abort, rollback, savepoint, and ambiguous-outcome states mean.
- Which concurrent histories the selected isolation level permits.
- Which [[Invariant|invariants]] are enforced by the database and which remain application obligations.
- Which failure modes committed state survives and how [[Write-Ahead Logging|write-ahead logging]], replication, redo, undo, or another [[Recovery|recovery]] mechanism provides that [[Durability|durability]].
- Which effects remain outside the transaction boundary and require an [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Two-Phase Commit|two-phase commit]], idempotency, compensation, or reconciliation.

The label “ACID transaction” is not a complete contract by itself. Isolation levels admit different histories, consistency depends on declared constraints and correct transaction logic, and durability is relative to a stated failure model. A nested transaction or savepoint may provide local rollback without providing an independently durable commit.

## An Equational Theory for Transactions

Andrew P. Black, Vincent Cremet, Rachid Guerraoui, and Martin Odersky's FSTTCS 2003 paper [*An Equational Theory for Transactions*](https://lampwww.epfl.ch/~cremet/publications/fsttcs03.pdf) separates three guarantees into nestable process operators:

- `⟨P⟩_A` is all-or-nothing: the covered process occurs completely or has no effect.
- `⟨P⟩_I` is isolated: concurrent executions have the effect of some serial execution.
- `⟨P⟩_D` is durable: after completion, later failures cannot undo the process.

Consistency is not a fourth operator. It is treated as an induction principle: actions that preserve consistency locally yield global consistency when the transaction guarantees preserve their boundaries. A conventional transaction is expressed by nesting the all-or-nothing action inside durability and then isolation, `⟨⟨⟨P⟩_A⟩_D⟩_I`. Because the operators do not generally commute, the calculus can distinguish mechanisms that offer different subsets or scopes of transaction guarantees.


Related concepts: [[Storage Systems|storage systems]], [[Business Transactions|business transactions]], [[ACID]], [[Commit Boundaries|commit boundaries]], [[Isolation|isolation]], [[Durability|durability]], [[Consistency Models|consistency models]], [[Invariant|invariants]], [[Concurrency Control|concurrency control]], [[Write-Ahead Logging|write-ahead logging]], [[Recovery|recovery]], [[Two-Phase Commit|two-phase commit]], [[Dual-Write Problem|dual-write problem]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Weak Isolation Patterns|weak isolation patterns]].

## Formal relations

- `may_realize`: [[Commit Boundaries]] — A database transaction can provide one atomic commit-or-abort boundary for operations controlled by its participating resource managers.
- `may_realize`: [[ACID]] — A database transaction can supply an ACID contract when its declared isolation, invariant, recovery, and failure assumptions satisfy that contract.
- `may_realize`: [[Business Transactions]] — A database transaction can realize a business transaction only when the entire domain outcome and its required effects fit within the same database-controlled boundary; otherwise it realizes only a local part.
