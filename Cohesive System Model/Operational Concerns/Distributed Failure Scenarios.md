---
realm: Operational Concerns
kind: reference
created: 2026-07-04
updated: 2026-07-04
status: draft
aliases:
  - Distributed Failure Modes
  - Distributed Hazards
  - Isolation Leak
  - Stale Cache
---

# Distributed Failure Scenarios

Distributed failure scenarios are recurring hazard shapes that appear when [[Effects|effects]], [[Observation|observations]], [[Commit Boundaries|commit boundaries]], [[Durability|durability]], [[Isolation|isolation]], [[Coordination|coordination]], and [[Recovery|recovery]] cross independently governed boundaries.

They are diagnostic names, not solution names. Each scenario should identify the missing guarantee, the boundary where the hazard appears, and the [[Weak Isolation Patterns|weak isolation patterns]] or stronger coordination mechanism that replaces the missing guarantee.

Useful scenario descriptions usually name:

- The subject, observer, and affected boundary.
- The observations used for a decision, including versions or freshness expectations.
- The effects that may commit, abort, retry, duplicate, or remain ambiguous.
- The acknowledgment that transfers responsibility.
- The durable material, if any, that survives the relevant failure boundary.
- The recovery rule when progress is partial or uncertain.

## Dual write

A [[Dual-Write Problem|dual write]] occurs when one operation tries to commit two or more effects across independent commit boundaries without one atomic commit protocol or durable recovery protocol connecting them.

The hazard is partial commitment: one effect commits while another fails, remains ambiguous, or is retried without a shared recovery record.

Typical resolutions include [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Event Sourcing|event sourcing]], [[Durable Execution|durable execution]], [[Sagas|sagas]] or [[Process Managers|process managers]], or [[Two-Phase Commit|two-phase commit]] when the participants and costs justify it.

See [[Dual-Write Problem|dual-write problem]].

## Non-idempotent effect race

A non-idempotent effect race occurs when concurrent, retried, replayed, or resumed execution can attempt the same external effect more than once, while the external boundary cannot naturally collapse duplicates into one semantic result.

This is a better name than "distributed lock scenario" when the lock is only one possible resolution. The hazard is duplicate or competing authority over a non-idempotent effect.

Common examples include charging a payment, creating a shipment, issuing a refund, sending a one-time credential, or invoking an external command whose result must be known by the caller.

Typical resolutions include [[Idempotency|idempotency]] keys accepted by the external boundary, receiver-side deduplication, expected-version checks, actor serialization at the entity boundary, fencing tokens, durable process state, or a [[Process Managers|process manager]] that records the external attempt and its observed result.

## Ambiguous external outcome

An ambiguous external outcome occurs when a caller times out, crashes, or loses the response after invoking an external operation and cannot tell whether the external effect committed.

Retry may duplicate the effect. Abandoning the attempt may lose a committed effect. Treating the timeout as failure invents a history the external boundary may not agree with.

Typical resolutions include external idempotency keys, result lookup by operation id, durable execution checkpoints around the call, reconciliation, or a process state such as `PaymentPending` that waits for later observation before claiming completion.

## Tentative observation leak

A tentative observation leak occurs when a decision, observation, or effect escapes from work whose facts are not yet committed as final at the boundary that later consumers rely on.

This is a broader and more specific name for the initial phrase "isolation leak." It keeps several subtypes distinct:

- **Dirty read**: an observer reads uncommitted data from another operation.
- **Rollback leak**: a decision or effect depends on data that later aborts or is reverted.
- **Precommit effect leak**: an outbound message, call, cache update, or publication happens before the local transition commits.
- **Tentative-state misclassification**: a pending, provisional, reserved, or compensating state is exposed or interpreted as final.

Typical resolutions include stronger [[Isolation|isolation]], delaying external effects until commit, [[Outbox|outbox]] records, explicit pending states, versioned observations, compensation, or reconciliation.

## Stale observation

A stale observation occurs when an observer makes a decision from an observation that is older than the decision requires.

This is a better umbrella than "stale cache" because caches are only one source of stale observations. Subtypes include:

- **Stale cache read**: a cache returns an expired or invalidated value.
- **Stale replica read**: a follower, replica, or region has not observed the latest committed write.
- **Stale projection read**: a read model or materialized view lags behind the authoritative transition history.
- **Stale policy observation**: an authorization rule, pricing rule, limit, feature flag, or fraud signal has changed but the decision uses an older value.
- **Stale absence**: a cached or projected "not found" or "none exists" observation is used after a matching fact has been created.
- **Session freshness gap**: a caller writes successfully but its later read is routed to a boundary that has not observed its write.

Typical resolutions include freshness contracts, dependency tokens, read-your-writes routing, monotonic-read guarantees, expected-version checks, related-version checks, cache invalidation, bounded staleness, explicit pending states, or rejection and retry when the required observation is too old.

## Fractured read

A fractured read occurs when one decision uses several observations that do not belong to one coherent [[Consistent Cuts|consistent cut]].

Each observation may be individually valid, but their combination may never have been true together. This matters for cross-entity validation, policy decisions, reports, projections, and workflows that join independently updated facts.

Typical resolutions include transactional reads, snapshot reads, causal metadata, consistent-prefix reads, dependency tokens, process-level checkpoints, or weaker semantics that explicitly tolerate independent local observations.

## Stale dependency decision

A stale dependency decision occurs when an operation validates the target entity but relies on a related observation whose version, policy, capacity, ownership, or authority has changed before commit.

This is the cross-boundary version of a stale read. Expected-version checks on the target entity alone are not enough when the invariant depends on related facts.

Typical resolutions include related-version checks, reservations, escrow, semantic locks, policy-version checks, compensating transitions, or coordination at the invariant boundary.

## Lost update

A lost update occurs when two observers read the same current state and both attempt successor transitions, but one accepted update overwrites or hides the other without recognizing the conflict.

Typical resolutions include expected-version checks, compare-and-set writes, actor serialization, stronger transaction isolation, or merge semantics when the state history is intentionally non-sequential.

## Write skew

Write skew occurs when concurrent operations each preserve an invariant relative to their own observation, but the combination of accepted effects violates the invariant.

The hazard often appears when the invariant is not owned by one entity, row, stream, actor, partition, or transaction boundary.

Typical resolutions include serializable isolation, uniqueness sentinels, invariant-owner entities, reservations, escrow, semantic locks, or redesigning the invariant as a monotone or commutative process when possible.

## Stale ownership

Stale ownership occurs when a worker, lease holder, lock holder, actor activation, leader, or claimed process step continues acting after its authority has expired, moved, or been superseded.

The failure is not merely concurrent execution. It is the target boundary accepting work from an authority that is no longer current.

Typical resolutions include fencing tokens, monotonically increasing ownership epochs, compare-and-set claims, lease-expiry assumptions made explicit, idempotent receivers, and target-side rejection of stale tokens.

## Split authority

Split authority occurs when two or more observers can each accept transitions for the same subject, invariant, or ownership boundary while believing they are authoritative.

Typical causes include network partitions, misrouted requests, multi-primary replication, actor placement races, lock service failures, or unclear ownership in the system graph.

Typical resolutions include consensus, leader election with fencing, single-writer boundaries, conflict records, CRDT-compatible semantics, or explicit reconciliation when simultaneous authority is intentionally tolerated.

## Duplicate delivery

Duplicate delivery occurs when a broker, retry loop, workflow replay, outbox relay, or recovery process delivers the same semantic input more than once.

At-least-once delivery is often the correct availability choice, but it moves correctness to the receiver boundary.

Typical resolutions include [[Idempotency|idempotency]] keys, [[Transactional Inbox|transactional inbox]] records, deduplication windows, expected-version checks, and nil transitions for duplicate semantic inputs.

## Acknowledgment gap

An acknowledgment gap occurs when the work and the acknowledgment for that work commit at different boundaries.

For example, a receiver may commit local effects and crash before acknowledging the sender. The sender may then retry an input that already committed. The inverse gap can also occur when an acknowledgment or offset is committed before local effects are durable.

Typical resolutions include transactional inbox records, idempotent receipt, durable acknowledgments, offset management tied to local commit, or recovery that replays from the last durable responsibility transfer.

## Queue handoff without completion protocol

A queue handoff without completion protocol occurs when a synchronous caller moves work into asynchronous processing but still needs a determinate result, completion meaning, or failure reason.

The queue serializes or buffers work, but it does not by itself provide an awaitable semantic result. Without a completion protocol, callers may poll stale observations, retry unsafely, or treat enqueue acknowledgment as business completion.

Typical resolutions include process identity, durable process state, result observations, workflow queries, callbacks, signals, pending states, timeouts, cancellation, and explicit completion events.

Related concepts: [[Weak Isolation Patterns|weak isolation patterns]], [[Dual-Write Problem|dual-write problem]], [[Isolation|isolation]], [[Consistency Models|consistency models]], [[Concurrency Control|concurrency control]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Acknowledgments|acknowledgments]], [[Delivery Semantics|delivery semantics]], [[Durability|durability]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], [[Coordination|coordination]], [[Orchestration and Choreography|orchestration and choreography]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Durable Execution|durable execution]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Actor Systems|actor systems]], [[Business Transactions|business transactions]], [[Invariant|invariants]].
