---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-28
updated: 2026-07-17
aliases:
  - Consistency beyond Transaction Boundaries
  - Cross-Boundary Consistency Patterns
---

# Weak Isolation Patterns

Weak isolation patterns are architecture practices for preserving useful correctness when one [[ACID]] transaction or [[Two-Phase Commit|two-phase commit]] boundary is unavailable, too expensive, or misaligned with the domain process. This is mostly about deciding which weaker guarantees become explicit parts of the domain protocol, entity model, process state, and recovery behavior.

They do not make weak isolation disappear. They replace implicit transactional guarantees with explicit rules about [[Ordering|ordering]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], compensation, reconciliation, and invariant preservation.

Here, weak isolation does not mean choosing a weak database isolation level. It means that the larger business process is not enclosed by one isolation and commit boundary. **Consistency beyond transaction boundaries** is a more explicit name for this design problem and avoids making the note sound like a catalog of database isolation levels.

## Problem

Distributed work often crosses databases, brokers, APIs, workflow engines, and external systems. A single transaction manager rarely controls every read, write, effect, and observation involved in the business outcome.

Without an explicit weak-isolation design, systems often rely on accidental timing: a message arrives soon enough, a read model catches up, a retry is harmless, a downstream system is available, or a related fact has not changed. Those assumptions are not a correctness model.

[[Distributed Failure Scenarios|Distributed failure scenarios]] name common ways those assumptions break across independently governed boundaries.

This note is intentionally narrower than [[Asynchronous Interaction Design|asynchronous interaction design]]. It focuses on semantic correctness and invariant preservation after a shared transaction boundary is lost. Asynchronous interaction design also covers liveness and operating obligations such as capacity, backlog, lag, retention, replay, topology, observability, schema evolution, and consumer bootstrap.

## Cohesive Formulation

Weak isolation design makes the missing transaction guarantees explicit in the model:

- [[Version|Version]] and etag checks for target entities and related observations.
- [[Idempotency]] records for retryable operations.
- [[Transactional Outbox|Transactional outbox]] records for local commit plus asynchronous publication responsibility.
- [[Transactional Inbox|Transactional inbox]] records for consumer-side deduplication and idempotent receipt.
- [[Sagas|Sagas]] and [[Process Managers|process managers]] for long-running coordination.
- Reservations, escrow, leases, or holds for scarce capacity.
- Compensation and reconciliation when later facts invalidate earlier progress.
- [[CRDTs as Architecture Practice|CRDT-compatible]] or monotone updates when order can be safely forgotten.
- [[Durable Execution]] for resumable progress across failures.

Each choice says which stronger guarantee has been replaced and which invariant, ordering, recovery, or visibility rule now carries the correctness burden.

For example, an outbox replaces atomic commit between a database and broker with local atomicity plus asynchronous publication responsibility. An inbox complements it on the consumer side by making redelivery safe through local atomicity and deduplication. A saga replaces one atomic transaction with a process whose partial progress, compensation, and recovery semantics are explicit. A reservation replaces global serializable allocation with a bounded right to consume capacity later.

Weak isolation patterns must be checked against [[Invariant|invariants]]. If an invariant is non-monotonic or requires a globally current view, avoiding coordination may be impossible without changing the model, accepting weaker semantics, or introducing escrow, reservation, or coordination at a narrower boundary.

The [[CALM Theorem|CALM theorem]] is a useful filter for these choices: monotone parts of the process can often remain asynchronous and coordination-free, while non-monotone decisions need a coordination boundary or an explicit domain protocol for pending, reserved, compensating, or reconciled progress.

## Pattern Families

### Version and Dependency Patterns

- **Expected-version checks** reject stale updates to the target entity.
- **Related-version checks** carry versions, etags, read-model positions, policy versions, or causal metadata for related facts used during validation.
- **Causal or dependency tokens** carry dependency context across requests so later reads or writes can wait for, validate, or reject against missing prerequisites.
- **Read-your-writes routing** sends a session to a primary, sufficiently fresh replica, or dependency-aware read path after it has written.
- **Consistent-prefix reads** prevent an observer from seeing later effects without earlier prerequisite effects.
- **Compare-and-set or conditional writes** accept a write only if a declared value, version, or predicate still holds.

### Ownership and Claim Patterns

- **Fencing tokens** give each owner a monotonically ordered authority token so stale workers cannot commit after losing ownership.
- **Leases** grant time-bounded authority to act, with explicit clock and expiry assumptions.
- **Claims or work ownership** assign a task, row, partition, subject, or process step before processing.
- **Semantic locks** represent domain-level exclusion as state, such as `TransferInProgress`, `InventoryHeld`, or `AccountClosing`.
- **Uniqueness sentinels** serialize one invariant through a dedicated key, row, or document, such as a unique email or one booking per slot.

### Reservation and Escrow Patterns

- **Reservations** hold capacity, money, inventory, seats, or rights before final use.
- **Escrow** preallocates bounded rights to replicas or processes so local operations remain safe without global coordination.
- **Bounded counters** track remaining capacity in partitions or rights buckets.
- **Holds with expiry** make partial allocation visible and give abandoned work a cleanup path.

### Messaging Reliability Patterns

- **Transactional outbox** records local state change and publication responsibility in one local commit boundary.
- **Transactional inbox** records input receipt and local processing in one local commit boundary before acknowledging completion to the delivery boundary.
- **Inbox or deduplication records** make consumption idempotent by recording processed input identifiers.
- **Deduplication windows** remember recent operation ids for a bounded period when infinite retention is unnecessary.
- **Idempotent effect protocols** make repeated sends, retries, or handler executions converge to one semantic effect.
- **Process checkpoints** persist progress after each step so partial work can resume without redoing unsafe effects.

### Pending, Tentative, and Repair Patterns

- **Pending states** make incomplete progress part of the domain protocol.
- **Tentative writes** record provisional facts that must later be confirmed, expired, compensated, or reconciled.
- **Reconciliation jobs** detect and repair divergence between systems after the fact.
- **Anti-entropy or repair protocols** exchange state, events, or deltas until replicas converge.
- **Human review states** route ambiguous, conflicting, or high-risk cases into explicit manual resolution.
- **Compensating command protocols** model compensation as new commands and transitions, not inverse database updates.

## Pending State as Domain Protocol

A common weak-isolation practice is to adopt partiality, asynchrony, and eventuality as part of the domain language instead of hiding them behind synchronous-looking APIs.

An entity may enter a **pending** state when it has accepted local progress but is awaiting later observation, confirmation, publication, settlement, shipment, approval, reconciliation, or timeout. Pending is not an implementation leak when the business process itself is incomplete. It is a determinate domain state that says the entity is waiting for further progress.

Examples include:

- `PaymentPending` before authorization or settlement is observed.
- `ShipmentChangePending` while carrier confirmation is outstanding.
- `InventoryReserved` before final allocation or release.
- `InvitePending` before acceptance, expiration, or revocation.
- `ProjectionPending` or `PublicationPending` when downstream visibility is part of the promise.

Pending states should define their allowed inputs, timeout behavior, retry policy, cancellation, compensation, observation requirements, and completion meanings. Otherwise "pending" becomes an unbounded limbo rather than a protocol state.

## In the Model

Weak isolation patterns do not claim the system is secretly strongly isolated. They make incompleteness, delay, and uncertainty explicit.

This shifts design work into the semantic model:

- Which facts were observed, and at which versions?
- Which facts may become stale before completion?
- Which partial outcomes are visible to which observers?
- Which downstream effects are obligations rather than completed facts?
- Which acknowledgments transfer responsibility, and at which boundary?
- Which states are pending, final, compensating, expired, failed, or reconciled?
- Which invariants are protected synchronously, and which are protected procedurally over time?

## Failure Modes

The practice fails when pending states are not first-class, when asynchronous work is presented as complete, when retries lack idempotency, when compensation is treated as inverse transition, or when related facts are read without versioning, reservations, or reconciliation.

It also fails when eventual consistency is used as a slogan. Eventuality must say what will eventually happen, under which delivery and recovery assumptions, and what observers may see before convergence.

## External References

- Pat Helland, [Life beyond Distributed Transactions: an Apostate's Opinion](https://www.ics.uci.edu/~cs223/papers/cidr07p15.pdf), CIDR 2007.
- Hector Garcia-Molina and Kenneth Salem, [Sagas](https://www.cs.princeton.edu/techreports/1987/070.pdf), Princeton CS-TR-070-87, 1987.
- Peter Bailis, Alan Fekete, Ali Ghodsi, Joseph M. Hellerstein, and Ion Stoica, [Coordination Avoidance in Database Systems](https://www.vldb.org/pvldb/vol8/p185-bailis.pdf), PVLDB 8(3):185-196, 2014.

Related concepts: [[Asynchronous Interaction Design|asynchronous interaction design]], [[Distributed Failure Scenarios|distributed failure scenarios]], [[Isolation|isolation]], [[ACID]], [[Two-Phase Commit|two-phase commit]], [[Coordination|coordination]], [[Orchestration and Choreography|orchestration and choreography]], [[Process Managers|process managers]], [[Sagas|sagas]], [[CALM Theorem|CALM theorem]], [[Concurrency Control|concurrency control]], [[Consistency Models|consistency models]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Acknowledgments|acknowledgments]], [[Version|version]], [[Observation|observation]], [[Entity|entity]], [[Transition|transition]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], [[Durable Execution|durable execution]], [[Transactional Outbox|transactional outbox]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Dual-Write Problem|dual-write problem]], [[CRDTs]], [[CRDTs as Architecture Practice|CRDTs as architecture practice]], [[Invariant|invariants]], [[Business Transactions|business transactions]].
