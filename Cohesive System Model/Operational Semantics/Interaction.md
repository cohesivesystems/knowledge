---
realm: Operational Semantics
---

# Interaction

Interaction answers: how do [[Observer|Observers]] address, observe, notify, or invoke one another?

Interaction defines the operational edges through which observers coordinate by exchange, observation, notification, invocation, shared state, or synchronization.

Interaction is boundary-relative. It can occur over a [[Network]], between processes on one host, between threads in one process, between tasks in a runtime, between actors and mailboxes, between CPU cores through cache coherence, or between a program and memory/register state.

Network distribution is the common case when discussing distributed systems, but it is not the only case. A system is distributed whenever interaction crosses a boundary where observation, ordering, visibility, failure, or commitment is not trivial.

## Minimal Edge

At a low level, interaction can be modeled as asynchronous send and receive. A send operation usually means the local boundary accepted data for transmission or delivery. A receive operation observes data already admitted by the receiver's local substrate. Stronger meanings, such as remote receipt, application processing, durable persistence, or domain commitment, require additional protocol structure.

Higher layers add addressing, atomicity, ordering, reliability, flow control, framing, multiplexing, persistence, cursoring, acknowledgment, and semantic interpretation.

## Modes

Interaction modes are edge configurations at a chosen abstraction layer. They are not disjoint leaves; one mode may be realized in terms of another at a lower layer.

- **One-way send**: one observer sends a value to another observer or channel with no modeled reply path. Examples include actor tell, asynchronous channel send, notification, fire-and-forget message send, and some event publication.
- **Request/reply**: a request has a reply path. The reply path may be direct, correlated, synchronous, asynchronous, multiplexed, or carried through another channel. RPC, HTTP request/response, actor ask, memory read, and queue-based request/reply are examples.
- **Publish/consume**: a producer publishes into a channel and consumers observe or consume from that channel. Queues, logs, topics, pub/sub buses, stream subscriptions, and multicast are configurations of publish/consume with different topology, retention, cursor ownership, and delivery semantics.
- **Stream/session**: an ongoing interaction edge over which many values flow. TCP realizes a full-duplex connection with an ordered byte stream in each direction. Higher layers can frame request/reply, publish/consume, or multiplexed protocols over a stream.
- **Shared-state interaction**: observers coordinate through common state rather than explicit messages. Examples include read, write, compare-and-swap, lock, wait, notify, memory barriers, cache coherence, and transactional memory.
- **Synchronization/rendezvous**: interaction whose primary purpose is coordinating progress. Examples include blocking handoff, CSP-style channel rendezvous, barrier, latch, semaphore acquire/release, join, await, and select/choice.

## Semantic Interpretation

Modes describe the edge shape. They do not determine the semantic role of the value crossing the edge.

A request may be interpreted as a [[Command]] when the receiver treats it as intent to cause a state transition. It may be interpreted as a [[Query]] when the receiver treats it as a request to observe or compute a value with no semantic state transition requested. It may also be a subscription request, negotiation, acknowledgment, policy decision, observation, or event notification.

Operational state can still change during a [[Query|query]]: caches may fill, metrics may record, cursors may advance, locks may be acquired, and acknowledgments may be emitted. The distinction is that the modeled semantic entity transition is not being requested.

Actor message send is the case where the addressed target is itself an observer locus. An actor address gives the sender a delivery path to a receiving observer boundary. Actor ask is request/reply over actor addressing; actor tell is one-way send. The receiver still decides how the message is interpreted.

## Layering

Interaction modes compose across layers:

- Request/reply can be framed over a stream, as with HTTP or RPC over TCP. RPC realizes application-level message-based request/reply by adding framing, correlation, multiplexing, dispatch, status, and metadata over a lower-level stream/session edge; see [[Network]].
- Request/reply can be realized over queues by carrying a reply address and correlation identifier.
- Publish/consume systems often expose lower-level request/reply operations to publish records, poll or fetch records, commit offsets, manage cursors, and create subscriptions.
- Shared memory can realize request/reply-like reads, one-way writes, publish/observe patterns, and synchronization through locking or waiting.
- UDP multicast and a broker topic are both one-to-many publication configurations at different abstraction layers, even though their delivery, durability, addressing, and retention semantics differ.

Systems build domain-level flows and [[Business Transactions]] by composing these edge configurations and then interpreting the values as commands, queries, events, observations, decisions, or acknowledgments.

## Interaction Graphs

An interaction graph is one projection of the broader system graph. Its edges mean that one participant operationally affects, observes, invokes, signals, publishes to, consumes from, reads, writes, waits for, or synchronizes with another participant or channel.

Other graph projections use different edge meanings:

| Graph | Typical nodes | Edge meaning |
| --- | --- | --- |
| Interaction graph | observers, channels, brokers, services, actors, shared-state cells | send, receive, request, reply, publish, consume, read, write, wait, notify, synchronize |
| Entity relationship graph | entities, identities, aggregates, resources | semantic relation, reference, ownership, dependency, association |
| Process or flow graph | activities, steps, observers, states, events | control flow, causal flow, sequencing, handoff, compensation |
| State transition graph | states, versions, transition labels | possible state change under command, event, policy, or guard interpretation |
| Projection graph | sources, projections, read models, indexes | derivation, materialization, reconstitution dependency |
| Realization graph | runtimes, hosts, storage systems, brokers, networks | realizes, hosts, deploys, persists, routes, schedules |

The same system element can appear in several graphs. An entity relationship does not imply direct interaction. An interaction edge does not imply a semantic entity relationship. A process-flow edge may be realized by several interaction edges. A broker, channel, mailbox, lock, or shared memory cell may be modeled as an edge at one abstraction layer and as a node at another.

Interaction graphs are especially useful for reasoning about coordination, delivery, ordering, backpressure, failure, acknowledgment, durability, and commit boundaries. An interaction edge should therefore be annotated with the boundary where its guarantees hold, the mode it uses, the topology it creates, the semantic roles it carries, and the substrate layer that realizes it.

## Dimensions

An interaction edge can be classified by:

- Abstraction level.
- Addressing space.
- Operation role: send, receive, request, reply, publish, consume, read, write, lock, wait, subscribe, poll.
- Topology: one-to-one, one-to-any, one-to-many, one-to-all, many-to-one, many-to-many.
- Channel form: socket stream, datagram, queue, log, topic, mailbox, shared memory cell, register, lock, condition variable.
- Unit of transfer: byte, frame, datagram, record, message, event, command, observation, transaction.
- Reply path: none, acknowledgment, correlated reply, streaming reply, shared-state observation.
- Time coupling: synchronous, asynchronous, deferred, replayable.
- Consumer position: ephemeral receive, durable cursor, offset, competing claim, retained subscription.
- Retention and durability.
- Delivery and ordering semantics.
- Acknowledgment and commit boundary.
- Failure boundary.
- Coordination role.
- Carried semantic roles: [[Command]], [[Query]], [[Event]], [[Observation]], acknowledgment, policy decision.
- Realization layer: memory, runtime, IPC, [[Network]], broker, database, workflow engine.

Interaction does not by itself define whether a domain transition committed. That depends on the receiver's observer-relative interpretation, validation, persistence, and delivery semantics.

Related concepts: [[Observer]], [[Command]], [[Query]], [[Event]], [[Relations]], [[Flows]], [[Projections]], [[Delivery Semantics]], [[Coordination]], [[Network]], [[Brokers]], [[Actor Systems]], [[Trace and Feedback]], [[Duality and Symmetry]].
