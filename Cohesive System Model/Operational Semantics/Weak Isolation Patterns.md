---
realm: Operational Semantics
kind: operational-semantics
---

# Weak Isolation Patterns

Weak Isolation Patterns are design techniques used when one [[ACID]] transaction or [[Two-Phase Commit|two-phase commit]] boundary is unavailable, too expensive, or not aligned with the business process.

As an architecture practice, these patterns are discussed in [[Weak Isolation Patterns as Architecture Practice]].

They do not make weak isolation disappear. They replace implicit transactional guarantees with explicit rules about [[Ordering]], [[Idempotency]], [[Retry]], [[Recovery]], compensation, reconciliation, and invariant preservation.

## Common Patterns

- **Optimistic concurrency**: use expected-version or etag checks to reject stale transitions.
- **Related-version checks**: include versions, etags, read-model positions, policy versions, or causal metadata for related observations used during validation.
- **Idempotency records**: remember processed inputs or operation identifiers so retries do not duplicate effects.
- **Transactional outbox**: commit local state and publication responsibility in one local transaction, then publish asynchronously.
- **Sagas and process managers**: decompose long-running work into steps with explicit recovery, compensation, or forward progress.
- **Compensation**: perform semantic follow-up actions when prior accepted work must be counteracted.
- **Reservations and escrow**: allocate scarce capacity or rights in advance so later concurrent work cannot overdraw an invariant.
- **Reconciliation**: detect divergence after the fact and repair, merge, compensate, or escalate.
- **Commutative or monotone updates**: design updates so concurrent application can commute, merge, or converge, as in compatible [[CRDTs]].
- **Durable workflows**: persist process progress and decisions so partial work can resume coherently after failure.

## Design Requirement

Each pattern must name the guarantee it replaces.

For example, an outbox replaces atomic commit between a database and broker with local atomicity plus asynchronous publication responsibility. A saga replaces one atomic transaction with a process whose partial progress, compensation, and recovery semantics are explicit. A reservation replaces global serializable allocation with a bounded right to consume capacity later.

Weak isolation patterns must be checked against [[Invariants]]. If the invariant is non-monotonic or requires a globally current view, avoiding coordination may be impossible without changing the model, accepting weaker semantics, or introducing escrow, reservation, or coordination at a narrower boundary.

## External References

- Pat Helland, [Life beyond Distributed Transactions: an Apostate's Opinion](https://www.ics.uci.edu/~cs223/papers/cidr07p15.pdf), CIDR 2007.
- Hector Garcia-Molina and Kenneth Salem, [Sagas](https://www.cs.princeton.edu/techreports/1987/070.pdf), Princeton CS-TR-070-87, 1987.
- Peter Bailis, Alan Fekete, Ali Ghodsi, Joseph M. Hellerstein, and Ion Stoica, [Coordination Avoidance in Database Systems](https://www.vldb.org/pvldb/vol8/p185-bailis.pdf), PVLDB 8(3):185-196, 2014.

Related concepts: [[Weak Isolation Patterns as Architecture Practice]], [[ACID]], [[Two-Phase Commit]], [[Isolation]], [[Coordination]], [[Concurrency Control]], [[Consistency Models]], [[Ordering]], [[Idempotency]], [[Retry]], [[Recovery]], [[Durable Execution]], [[Transactional Outbox]], [[CRDTs]], [[Invariants]], [[Business Transactions]].
