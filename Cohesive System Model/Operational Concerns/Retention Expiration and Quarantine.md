---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-27
updated: 2026-07-27
aliases:
  - Message Retention
  - Message Expiration
  - Quarantine
  - Dead Letter
  - Dead Letter Channel
---

# Retention, Expiration, and Quarantine

Retention, expiration, and quarantine describe how long interaction material remains available, when it ceases to be admissible for ordinary processing, and how exceptional material is isolated for inspection, repair, replay, reconciliation, or disposal.

[[Durability]] and retention are distinct. Durability states which failures recorded material survives. Retention states how long or under what policy it remains available. Expiration states when a message, request, claim, lease, reply obligation, or other item becomes stale for a declared purpose. An expired item may remain durably stored for audit while no longer being admissible for live processing.

## Quarantine

An invalid-message or dead-letter channel is a **quarantine path**, not a business completion state. It may contain malformed, incompatible, unauthorized, undeliverable, expired, poison, repeatedly failing, or operationally ambiguous material. Quarantine should record the attempted contract, failure boundary, reason, attempt history, prior acknowledgments or effects, and the policy that moved the item.

A viable quarantine path requires:

- Ownership and alerting.
- Access control, classification, and retention policy.
- Inspection, correction, replay, skip, reconciliation, or terminal-disposition procedures.
- Idempotency and effect checks before redrive.
- Ordering and gap rules for work removed from an ordered lane.
- Evidence that purge or expiry does not silently erase an outstanding semantic obligation.

## Subscription and Recovery Horizons

A durable subscriber requires subscription identity and retained material or another authoritative recovery source. Retention must cover the outage, detection, repair, and catch-up horizon, or the system must declare how snapshots, event histories, backfills, or reconciliation fill the gap.

Channel purging is an authorized operational action. It changes the available history and may invalidate pending work, test isolation, replay, or recovery claims. The target scope, cutoff, authority, audit record, and recoverability must be explicit.

## External References

- Gregor Hohpe and Bobby Woolf, [Invalid Message Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/InvalidMessageChannel.html), [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html), and [Message Expiration](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageExpiration.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Time|time]], [[Durability|durability]], [[Persistence|persistence]], [[Delivery Semantics|delivery semantics]], [[Interaction Channels|interaction channels]], [[Consumer Coordination|consumer coordination]], [[Acknowledgments|acknowledgments]], [[Retry|retry]], [[Recovery|recovery]], [[Idempotency|idempotency]], [[Ordering|ordering]], [[Operational Control|operational control]], [[Observability and Provenance|observability and provenance]], [[Asynchronous Interaction Design|asynchronous interaction design]].
