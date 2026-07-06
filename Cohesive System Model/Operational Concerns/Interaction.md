---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-24
updated: 2026-07-06
---

# Interaction

Interaction answers: how do [[Observer|observers]] address, observe, notify, or invoke one another?

Interaction defines the operational edges through which observers affect, observe, notify, invoke, share state with, wait for, or synchronize with one another.

Every interaction edge is relative to observer boundaries. A successful interaction claim must say which boundary observed success: sender-local acceptance, receiver-local admission, handler processing, durable persistence, responsibility transfer, or domain commitment.

Interaction is boundary-relative. It can occur over a [[Network|network]], between processes on one host, between threads in one process, between tasks in a runtime, between actors and mailboxes, between CPU cores through cache coherence, or between a program and memory/register state.

Network distribution is the common case when discussing distributed systems, but it is not the only case. A system is distributed whenever interaction crosses a boundary where observation, ordering, visibility, failure, authority, or commitment is not trivial.

For the network-specific realization ladder from physical signaling through link, network, transport, and application protocols, see [[Network|network]].

## Semantic and Operational Senses

Interaction has both semantic and operational senses. Semantically, interaction is boundary-crossing participation: one [[Observer|observer]], [[Process|process]], or subject affects, observes, requests, notifies, or synchronizes with another. Operationally, interaction is the edge structure that realizes this participation with concrete addressing, channels, timing, delivery, ordering, acknowledgment, failure, and commitment guarantees.

Cohesive keeps these senses distinct. A semantic [[Command|command]], [[Query|query]], [[Event|event]], or [[Observation|observation]] may be carried by many operational interaction modes. An operational edge does not by itself determine the semantic role of what crosses it.

## Minimal Edge

At a low level for software modeling, interaction can be modeled as asynchronous send and receive. A send operation usually means the local boundary accepted data for transmission, publication, storage, or delivery. A receive operation observes data already admitted by the receiver's local substrate. Stronger meanings, such as remote receipt, application processing, durable persistence, visibility to another participant, or domain commitment, require additional protocol structure.

Higher layers add addressing, atomicity, ordering, reliability, flow control, framing, multiplexing, persistence, cursoring, acknowledgment, correlation, and semantic interpretation.

[[Synchrony and Asynchrony]] gives the governing distinction: asynchrony leaves sends, receives, observations, and effects as independently progressing occurrences; synchronization coordinates selected occurrences into one boundary-relative unit such as a call/return, rendezvous, transaction, barrier, actor turn, or commit point.

[[Actor Systems|Actor systems]] are an important realization family that deliberately takes asynchronous message passing as the primitive interaction form. Actor tell is one-way send to an addressable observer boundary. Actor ask adds a reply path and correlation. Mailboxes, placement, supervision, timers, persistence, and delivery guarantees enrich that primitive without making the actor address identical to the semantic entity or process being modeled.

## Constructive View

The common structure across interaction modes is not a transport type. It is a relation among local occurrences at boundaries.

An interaction description should say:

- Which participants or mediating loci are involved.
- What local occurrences happen: emit, admit, observe, read, write, wait, notify, commit, abort, or complete.
- How those occurrences are named: address, channel, topic, mailbox, location, lock, session, correlation identifier, cursor, or offset.
- Which occurrences remain independent and which are joined by synchronization, acknowledgment, commit, reply, or rendezvous.
- What guarantees enrich the edge: ordering, durability, isolation, delivery, retention, idempotency, retry, flow control, or recovery.
- Which semantic role the carried value has when interpreted: [[Command|command]], [[Query|query]], [[Event|event]], [[Observation|observation]], policy decision, acknowledgment, or signal.

This makes interaction modes derived protocol shapes rather than disjoint categories.

## Addressing and Identity

Interaction requires some way to name a target, channel, location, or mediating locus. The address space may be logical, physical, stable, ephemeral, opaque, or structured: actor address, URL, topic name, queue name, partition key, socket address, memory location, lock name, cursor, or session identifier.

Addressing should not be collapsed into [[Identity|identity]]. An address names a delivery path or interaction locus; an identity names the modeled subject or observer. They may align, as when an actor address realizes one entity observer, but they may also be separated by load balancers, service discovery, virtual actors, shard routers, partitioned topics, replicated services, NAT, aliases, or temporary reply channels.

## Derived Modes

Interaction modes are edge configurations at a chosen abstraction layer. One mode may be realized in terms of another at a lower layer.

- **One-way send**: emit plus an address, channel, or location, with no modeled continuation. Examples include actor tell, asynchronous channel send, notification, fire-and-forget message send, and some event publication.
- **Request/reply**: one send plus a modeled continuation path. The reply path may be direct, correlated, synchronous, asynchronous, multiplexed, or carried through another channel. RPC, HTTP request/response, actor ask, memory read, and queue-based request/reply are examples.
- **Publish/consume**: one or more sends into a mediating channel from which consumers observe or consume. Queues, logs, topics, pub/sub buses, stream subscriptions, and multicast are configurations of publish/consume with different topology, retention, cursor ownership, and delivery semantics.
- **Stream/session**: a session identity relating many sends and receives over time. TCP realizes a full-duplex connection with an ordered byte stream in each direction. Higher layers can frame request/reply, publish/consume, or multiplexed protocols over a stream.
- **Shared-state interaction**: observers interact through a mediating state cell, register, memory location, table, log, lock, or object rather than by explicit point-to-point message. Examples include read, write, compare-and-swap, lock, wait, notify, memory barriers, cache coherence, and transactional memory.
- **Synchronization/rendezvous**: independent occurrences are joined so that progress, visibility, or commitment is coordinated. Examples include blocking handoff, CSP-style channel rendezvous, barrier, latch, semaphore acquire/release, join, await, and select/choice.

## Interaction Duality

Many interaction roles appear as duals or complements: send/receive, publish/consume, request/reply, write/read, lock/unlock, wait/notify, subscribe/publish, poll/offer, acquire/release. [[Duality and Symmetry|Duality and symmetry]] helps identify the paired structure without assuming both sides are equivalent.

Interaction duals are often asymmetric in authority, timing, visibility, and cardinality. A publisher may not know its consumers. A queue may accept many producers but expose one effective consumer per message. A request gives the receiver authority to accept, reject, reinterpret, or ignore the input. A lock acquire depends on a prior or future release, but the two operations may be performed by different observers under a shared protocol.

## Local Boundaries

Local interactions use the same structure. A function call, memory read, register write, lock acquire, actor mailbox enqueue, event-loop callback, task wakeup, or cache-coherence exchange can all be interaction at the boundary where it affects observation, ordering, ownership, or progress.

At the instruction-set boundary, a `mov` instruction may be treated as one synchronous effect or observation. At a lower microarchitectural boundary, the same instruction may be realized through cache lookups, buffers, bus transactions, speculative execution, invalidations, or other independently progressing activity. The model should therefore name the boundary whose guarantees are being claimed instead of treating "local" as automatically synchronous or trivial.

## Semantic Interpretation

Modes describe the edge shape. They do not determine the semantic role of the value crossing the edge.

A request may be interpreted as a [[Command|command]] when the receiver treats it as intent to cause a state transition. It may be interpreted as a [[Query|query]] when the receiver treats it as a request to observe or compute a value with no semantic state transition requested. It may also be a subscription request, negotiation, acknowledgment, policy decision, observation, or event notification.

Operational state can still change during a [[Query|query]]: caches may fill, metrics may record, cursors may advance, locks may be acquired, and acknowledgments may be emitted. The distinction is that the modeled semantic entity transition is not being requested.

Actor message send is the case where the addressed target is itself an observer locus. An actor address gives the sender a delivery path to a receiving observer boundary. Actor ask is request/reply over actor addressing; actor tell is one-way send. The receiver still decides how the message is interpreted.

## Layering and Lowering

Interaction modes compose upward into richer protocols and lower into more primitive realization steps:

- Request/reply can be framed over a stream, as with HTTP or RPC over TCP. RPC realizes application-level message-based request/reply by adding framing, correlation, multiplexing, dispatch, status, and metadata over a lower-level stream/session edge; see [[Network|network]].
- Request/reply can be realized over queues by carrying a reply address and correlation identifier.
- Publish/consume systems often expose lower-level request/reply operations to publish records, poll or fetch records, commit offsets, manage cursors, and create subscriptions.
- Shared memory can realize request/reply-like reads, one-way writes, publish/observe patterns, and synchronization through locking or waiting.
- UDP multicast and a broker topic are both one-to-many publication configurations at different abstraction layers, even though their delivery, durability, addressing, and retention semantics differ.

Systems build domain-level flows and [[Business Transactions|business transactions]] by composing these edge configurations and then interpreting the values as commands, queries, events, observations, decisions, or acknowledgments.

Lowering asks the inverse question: what lower-layer interactions realize this edge? A synchronous-looking rendezvous may lower into runtime scheduling, kernel waits, futex operations, interrupts, socket writes, TCP segments, link-layer frames, media access, clock recovery, encoding, and physical signal transitions. Each layer has its own local occurrences and guarantee boundaries. A physical signal transition, link acknowledgment, kernel wakeup, broker acknowledgment, and domain command response are related by protocol structure, but they do not mean the same thing.

This section states the general principle. [[Network|Network]] develops the specific realization ladder for network-based interaction across physical, link, network, transport, and application protocol layers.

## Backpressure and Flow Control

Backpressure is feedback over an interaction edge: a receiver, channel, broker, runtime, or dependency signals that it cannot accept or process work at the offered rate. Flow control is the protocol structure that turns that signal into admission, buffering, scheduling, throttling, dropping, batching, or slowing behavior.

Backpressure can be push-based or pull-based. Push-based systems need bounded channels, credits, windows, refusal, shedding, or blocking points to avoid unbounded accumulation. Pull-based systems let consumers control demand through polling, fetch size, cursor advancement, subscription demand, or lease acquisition. Topology matters: fan-in creates bottleneck pressure, fan-out can amplify work, and partitioned consumer groups distribute pressure only within the partitioning and assignment rules.

Backpressure is related to [[Rate Limiting|rate limiting]], [[Trace and Feedback|trace and feedback]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], and [[Recovery|recovery]], but it is specifically about how capacity information travels through the interaction graph.

## Failure and Partial Failure

Non-trivial interaction boundaries admit partial failure. A send may succeed locally while the receiver never observes it. A receiver may process input but fail before replying or acknowledging. A reply may be lost after a transition commits. A broker may persist a message while a consumer crashes after processing but before advancing its offset or claim.

The structural ambiguity is that absence of response does not distinguish slow, lost, rejected, crashed, partitioned, duplicated, or already-committed work. Interaction designs therefore need explicit timeout, retry, acknowledgment, idempotency, dead-letter, circuit-breaking, and recovery meanings. Those meanings connect interaction to [[Retry|retry]], [[Idempotency|idempotency]], [[Acknowledgments|acknowledgments]], [[Delivery Semantics|delivery semantics]], [[Commit Boundaries|commit boundaries]], and [[Recovery|recovery]].

## Interaction Graphs

An interaction graph is one projection of the broader system graph. Its edges mean that one participant operationally affects, observes, invokes, signals, publishes to, consumes from, reads, writes, waits for, or synchronizes with another participant or channel.

Interaction edges can also induce causal or happens-before structure when a protocol relates one local occurrence to another. In Lamport-style causal ordering, a send happens before the corresponding receive. Request/reply, publish/consume, shared-state updates, acknowledgments, and synchronization points similarly create possible-causality edges when the model records those relations. The force of that ordering remains boundary- and mechanism-relative; see [[Ordering|ordering]].

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
- Carried semantic roles: [[Command|command]], [[Query|query]], [[Event|event]], [[Observation|observation]], acknowledgment, policy decision.
- Realization layer: memory, runtime, IPC, [[Network|network]], broker, database, workflow engine.

Interaction does not by itself define whether a domain transition committed. That depends on the receiver's observer-relative interpretation, validation, persistence, and delivery semantics.

Related concepts: [[Observer|observer]], [[Command|command]], [[Query|query]], [[Event|event]], [[Relation Models|relation models]], [[Flow Views|flow views]], [[Projection Models|projection models]], [[Delivery Semantics|delivery semantics]], [[Coordination|coordination]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Network|network]], [[Brokers|brokers]], [[Actor Systems|actor systems]], [[Trace and Feedback|trace and feedback]], [[Duality and Symmetry|duality and symmetry]].
