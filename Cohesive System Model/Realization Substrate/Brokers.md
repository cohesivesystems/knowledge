---
realm: Realization Substrate
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

Broker guarantees must be interpreted through the model's delivery semantics. Ordering, durability, deduplication, acknowledgment, and replay are always scoped to the broker's own boundaries and keys.

Related concepts: [[Realization]], [[Interaction]], [[Delivery Semantics]], [[Ordering]], [[Retry]], [[Idempotency]], [[Recovery]], [[Flows]].
