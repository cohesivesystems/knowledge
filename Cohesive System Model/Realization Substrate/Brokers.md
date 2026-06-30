---
realm: Realization Substrate
kind: realization-substrate
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

Broker guarantees must be interpreted through the model's delivery semantics. Ordering, durability, deduplication, [[Acknowledgments|acknowledgment]], and replay are always scoped to the broker's own boundaries and keys.

Related concepts: [[Realization|realization]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Ordering|ordering]], [[Retry|retry]], [[Idempotency|idempotency]], [[Recovery|recovery]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Flows|flows]].
