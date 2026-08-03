---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-08-02
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

A broker message is a transport record or carrier. Emission, broker admission, delivery, and receiving-boundary ingress are distinct occurrences; ingress is an exogenous event for the receiving observer. The message contract may explicitly express event, request, signal, reply, command, or acknowledgment intent and thereby make an interpretation expected. The corresponding semantic or protocol role is still established relative to the modeled [[Effect|effect]], emitter obligation, receiver interpretation, and boundary. One broker can carry several roles, and one role can be realized without a broker.

When a broker carries canonical emission envelopes, it should preserve or convey the required stable emission and contract identity, payload revision, correlation, causation, tenant or authority scope, idempotency basis, ordering key, response obligation, and provenance. Broker-assigned message, partition, offset, delivery, and acknowledgment identifiers remain substrate identities and do not replace the semantic ones.

Broker guarantees must be interpreted through the model's delivery semantics. Ordering, durability, deduplication, [[Acknowledgments|acknowledgment]], replay, [[Delivery Progress and Settlement|progress, and settlement]] are always scoped to the broker's own boundaries and keys. A replay cursor, provider delivery identity, current settlement authority, application checkpoint, and settlement receipt remain different evidence even when one SDK exposes them through adjacent operations.

A brokered messaging channel is normally realized by more than one [[Network Channels|network channel]]: producers interact with broker endpoints, broker state mediates the exchange, and consumers interact through later or concurrent sessions. Broker protocol acknowledgments and flow control compose with transport acknowledgments and receive windows but do not inherit their meanings. Conversely, one broker connection may multiplex many topics, subscriptions, partitions, and logical channel directions.

At its public ports, a broker queue commonly behaves as a passive sink for active producers and a passive source for active consumers. It therefore separates producer and consumer cadence and changes the [[Interaction Control Flow|interaction-control driver]] across the queue. Push subscriptions, event routers, and managed pipes may expose other roles, often by combining internal queues with active drivers. Public push or pull behavior, internal scheduling, buffering, batching, ordering, and backpressure should be modeled separately.

Broker delivery does not by itself provide durable wait arbitration, exclusive signal consumption, entity concurrency control, request-result admission, external idempotency, or exactly-once logical consequences. Those guarantees may be composed with inbox, outbox, checkpoint, claim, fence, and operation-ledger mechanisms when the composition has explicit evidence.

## External References

- Gregor Hohpe and Bobby Woolf, [Message Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html), [Point-to-Point Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html), [Publish-Subscribe Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html), and [Message Bus](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageBus.html), *Enterprise Integration Patterns*, 2003.
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Execution Kernel|execution kernel]], [[Realization|realization]], [[Effect|effect]], [[Effect Models]], [[Event|event]], [[Command|command]], [[Messages and Envelopes|messages and envelopes]], [[Interaction|interaction]], [[Interaction Control Flow|interaction control flow]], [[Interaction Channels|interaction channels]], [[Network Channels|network channels]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Routing Models|routing models]], [[Consumer Coordination|consumer coordination]], [[Delivery Semantics|delivery semantics]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Acknowledgments|acknowledgments]], [[Ordering|ordering]], [[Retry|retry]], [[Idempotency|idempotency]], [[Recovery|recovery]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Process Graphs|process graphs]], [[Flow Views|flow views]].
