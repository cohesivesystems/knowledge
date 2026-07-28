---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-07-27
---

# Brokers

Brokers are concrete messaging substrates that mediate delivery between producers and consumers.

Examples include queues, topics, streams, pub/sub systems, event buses, and log-based messaging systems.

Brokers can realize interaction patterns such as:

- Queue delivery.
- Pub/sub.
- Stream subscription.
- Broadcast or fanout.
- Retained or replayable delivery.
- Dead-letter or retry paths.

A broker message is not intrinsically a domain event, request, signal, reply, command, or acknowledgment. Those are semantic or protocol roles established by the modeled [[Effect|effect]], emitter obligation, receiver interpretation, and boundary. One broker can carry several roles, and one role can be realized without a broker.

When a broker carries canonical emission envelopes, it should preserve or convey the required stable emission and contract identity, payload revision, correlation, causation, tenant or authority scope, idempotency basis, ordering key, response obligation, and provenance. Broker-assigned message, partition, offset, delivery, and acknowledgment identifiers remain substrate identities and do not replace the semantic ones.

Broker guarantees must be interpreted through the model's delivery semantics. Ordering, durability, deduplication, [[Acknowledgments|acknowledgment]], and replay are always scoped to the broker's own boundaries and keys.

Broker delivery does not by itself provide durable wait arbitration, exclusive signal consumption, entity concurrency control, request-result admission, external idempotency, or exactly-once logical consequences. Those guarantees may be composed with inbox, outbox, checkpoint, claim, fence, and operation-ledger mechanisms when the composition has explicit evidence.

Related concepts: [[Execution Kernel|execution kernel]], [[Realization|realization]], [[Effect|effect]], [[Effects]], [[Event|event]], [[Command|command]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Ordering|ordering]], [[Retry|retry]], [[Idempotency|idempotency]], [[Recovery|recovery]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Process Graphs|process graphs]], [[Flow Views|flow views]].
