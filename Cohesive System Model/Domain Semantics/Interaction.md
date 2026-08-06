---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-08-06
---

# Interaction

Interaction names boundary-relative participation among subjects: how [[Observer|observers]], [[Process|processes]], [[Entity|entities]], or other participants affect, observe, request, notify, answer, share state with, wait for, or synchronize with one another.

Interaction is a cross-realm concept. Its semantic description identifies participant roles, meanings, occurrences, continuations, and obligations. The [[System Graph|system graph]] makes interactions explicit as compositional structure through observer models, process graphs, flow views, messages, channels, routes, and boundaries. Operational concerns specify the boundary-relative properties interactions require or exhibit. [[Realization|Realization]] relates that structure and those property demands to substrate mechanisms and capability evidence.

This note is located in Domain Semantics as the definitional entry point for interaction, not as a claim that the semantic perspective is intrinsically prior to its structural, operational, or realization descriptions.

Under the [[Stuff Structure Property|stuff structure property]] lens, an interaction may be structure when it relates participants and occurrences, stuff when it is reified as a modeled object, or the subject of properties that constrain valid interaction. Which aspect is foregrounded depends on the model boundary and purpose.

Every interaction description is relative to participant boundaries. A claim about a successful interaction must say which boundary observed success: sender-local acceptance, receiver-local admission, handler processing, durable persistence, responsibility transfer, or domain commitment.

A designed interaction surface is an [[Interfaces|interface]]. The boundary establishes scope; the interface declares the roles and contracts by which selected interactions may cross it; the interaction is the actual or possible participation through that surface. An [[Interaction Channels|interaction channel]] supplies logical exchanges and directions among [[Endpoints|endpoints]], while an [[Interaction Protocols|interaction protocol]] constrains how occurrences may unfold over time. An [[Interaction Bindings|interaction binding]] associates exact interface and protocol roles with those endpoints and channel directions.

Interaction is boundary-relative. It can occur over a [[Network|network]], between processes on one host, between threads in one process, between tasks in a runtime, between actors and mailboxes, between CPU cores through cache coherence, or between a program and memory/register state.

Network distribution is the common case when discussing distributed systems, but it is not the only case. A system is distributed whenever interaction crosses a boundary where observation, ordering, visibility, failure, authority, or commitment is nontrivial.

For the network-specific realization ladder from physical signaling through link, network, transport, and application protocols, see [[Network|network]]. For the detailed cross-realm correspondence between application or messaging channels and transport-layer channels, see [[Network Channels|network channels]].

## Cross-Realm Descriptions

From a semantic perspective, interaction is boundary-crossing participation: one [[Observer|observer]], [[Process|process]], or subject affects, observes, requests, notifies, answers, or synchronizes with another. Semantic properties can constrain authority, admissibility, causality, response obligations, continuation, completion, and valid composition without selecting a transport or runtime.

From the system-graph perspective, an interaction description arranges participants, interfaces, ports, endpoints, bindings, local occurrences, directions, carried roles, protocols, channels, topology, and composition. Operational properties refine semantic constraints and structural requirements into scoped claims about addressing, timing, delivery, ordering, acknowledgment, progress, settlement, durability, failure, commitment, and recovery. Realization selects or composes mechanisms capable of satisfying those claims and states the evidence and boundaries under which they hold.

Cohesive keeps these descriptions related without collapsing them. A semantic [[Command|command]], [[Query|query]], [[Event|event]], or [[Observation|observation]] may be carried by many system-graph interaction shapes and substrate mechanisms. Neither an interaction edge nor its realization determines the semantic role of what crosses it.

## Property Correspondence

Semantic and operational properties are related but not identical. Semantic properties state what must remain true for an interaction to preserve its modeled meaning. Operational properties refine those requirements into claims that can be attached to explicit graph and substrate boundaries. A system graph can carry these refinements as guarantee demands before a realization is selected; capability evidence from the selected mechanisms then supports or rejects the realization [[Judgement|judgement]].

| Semantic property | Possible operational refinements |
| --- | --- |
| A reply discharges one admitted request obligation. | Stable correlation, duplicate detection, idempotent discharge, concurrency control, and terminal-result retention. |
| A participant's continuation depends on a terminal result or declared terminal failure. | Durable pending state, explicit timeout meaning, delivery, retry, reconstitution, and recovery. |
| An emitted event represents an established fact. | Commit and publication ordering, durable responsibility, acknowledgment meaning, and recovery from partial failure. |
| Only an authorized participant may invoke or observe a role. | Address resolution, authentication, authorization, admission control, and auditable provenance at the relevant boundary. |
| One occurrence must causally precede another. | Scoped ordering, synchronization, acknowledgment, causal metadata, or a shared commit boundary. |
| Every accepted obligation eventually reaches a declared disposition. | Durability, retention, delivery, progress assumptions, retry, recovery, expiration, and quarantine. |
| An observation must correspond to an admissible state or version. | Consistency, isolation, version checks, freshness constraints, and visibility boundaries. |

The correspondence is generally many-to-many. Exactly one semantic discharge, for example, need not require physically exactly-once delivery. It may instead be preserved by at-least-once delivery together with stable identity, deduplication, serialized commitment, and durable result recovery. A realization must preserve the semantic property, not merely select a mechanism with a similar guarantee name.

## Minimal Edge

At a low level for software modeling, interaction can be modeled as asynchronous send and receive. A send operation usually means the local boundary accepted data for transmission, publication, storage, or delivery. A receive operation observes data already admitted by the receiver's local substrate. Stronger meanings, such as remote receipt, application processing, durable persistence, visibility to another participant, or domain commitment, require additional protocol structure.

Higher layers add addressing, atomicity, ordering, reliability, [[Flow Control|flow control]], framing, [[Multiplexing and Demultiplexing|multiplexing]], persistence, cursoring, acknowledgment, correlation, and semantic interpretation.

[[Synchrony and Asynchrony]] gives the governing distinction: asynchrony leaves sends, receives, observations, and effects as independently progressing occurrences; synchronization coordinates selected occurrences into one boundary-relative unit such as a call/return, rendezvous, transaction, barrier, actor turn, or commit point.

[[Actor Systems|Actor systems]] are an important realization family that deliberately takes asynchronous message passing as the primitive interaction form. Actor tell is one-way send to an addressable observer boundary. Actor ask adds a reply path and correlation. Mailboxes, placement, supervision, timers, persistence, and delivery guarantees enrich that primitive without making the actor address identical to the semantic entity or process being modeled.

## Constructive View

The common structure across interaction modes is not a transport type. It is a relation among local occurrences at boundaries.

An interaction description should say:

- Which participants or mediating loci are involved.
- What local occurrences happen: emit, admit, observe, read, write, wait, notify, commit, abort, or complete.
- How those occurrences are named: address, channel, topic, mailbox, location, lock, session, correlation identifier, cursor, or offset.
- Which participant actively drives each push, fetch, poll, callback, or delivery operation and in which direction the carried value moves.
- Which occurrences remain independent and which are joined by synchronization, acknowledgment, commit, reply, or rendezvous.
- What guarantees enrich the edge: ordering, durability, isolation, delivery, retention, idempotency, retry, [[Flow Control|flow control]], or recovery.
- Which semantic role the carried value has when interpreted: [[Command|command]], [[Query|query]], [[Event|event]], [[Observation|observation]], policy decision, acknowledgment, or signal.

These are reusable interaction shapes rather than disjoint categories. [[Interaction Protocols|Protocols]] refine them with legal traces and meanings, while [[Interaction Channels|channels]] can demand the coarse exchange morphology from a realization without owning the complete protocol.

## Addressing and Identity

Interaction requires some way to name a target, channel, location, or mediating locus. The address space may be logical, physical, stable, ephemeral, opaque, or structured: actor address, URL, topic name, queue name, partition key, socket address, memory location, lock name, cursor, or session identifier.

Addressing should not be collapsed into [[Identity|identity]]. An address names a delivery path or interaction locus; an identity names the modeled subject or observer. They may align, as when an actor address realizes one entity observer, but they may also be separated by load balancers, service discovery, virtual actors, shard routers, partitioned topics, replicated services, NAT, aliases, or temporary reply channels.

## Derived Modes

Interaction modes are edge configurations at a chosen abstraction layer. One mode may be realized in terms of another at a lower layer.

- **One-way send**: emit plus an address, channel, or location, with no modeled continuation. Examples include actor tell, asynchronous channel send, notification, fire-and-forget message send, and some event publication.
- **Request/reply**: one send plus a modeled continuation that expects a later response. The reply path may be direct, correlated, synchronous, asynchronous, multiplexed, carried through another channel, or observed through shared state. RPC, HTTP request/response, actor ask, memory read, and queue-based request/reply are examples.
- **Publish/consume**: one or more sends into a mediating channel from which consumers observe or consume. Queues, logs, topics, pub/sub buses, stream subscriptions, and multicast are configurations of publish/consume with different topology, retention, cursor ownership, and delivery semantics.
- **Stream/session**: a session identity relating many sends and receives over time. TCP realizes a full-duplex connection with an ordered byte stream in each direction. Higher layers can frame request/reply, publish/consume, or multiplexed protocols over a stream.
- **Shared-state interaction**: observers interact through a mediating state cell, register, memory location, table, log, lock, or object rather than by explicit point-to-point message. Examples include read, write, compare-and-swap, lock, wait, notify, memory barriers, cache coherence, and transactional memory.
- **Synchronization/rendezvous**: independent occurrences are joined so that progress, visibility, or commitment is coordinated. Examples include blocking handoff, CSP-style channel rendezvous, barrier, latch, semaphore acquire/release, join, await, and select/choice.

## Data Flow and Interaction Control Flow

[[Interaction Control Flow|Interaction control flow]] identifies which participant actively initiates an operation at each port. It is orthogonal to data flow. A sender actively pushes data to a passive sink, so the directions align. A fetcher actively polls or requests data from a passive source, so the data and driving directions oppose one another.

This per-interaction notion is not the branching or token progression of a process graph, logical waiting in [[Synchrony and Asynchrony|control-flow synchrony]], orchestration authority, or backpressure policy. It exposes who owns cadence and where queues, drivers, polling, batching, buffering, and scheduling enter a realization.

## Interaction Duality

Many interaction roles appear as duals or complements: send/receive, publish/consume, request/reply, write/read, lock/unlock, wait/notify, subscribe/publish, poll/offer, acquire/release. [[Duality and Symmetry|Duality and symmetry]] helps identify the paired structure without assuming both sides are equivalent.

Interaction duals are often asymmetric in authority, timing, visibility, and cardinality. A publisher may not know its consumers. A queue may accept many producers but expose one effective consumer per message. A request gives the receiver authority to accept, reject, reinterpret, or ignore the input. A lock acquire depends on a prior or future release, but the two operations may be performed by different observers under a shared protocol.

## Local Boundaries

Local interactions use the same structure. A function call, memory read, register write, lock acquire, actor mailbox enqueue, event-loop callback, task wakeup, or cache-coherence exchange can all be interaction at the boundary where it affects observation, ordering, ownership, or progress.

At the instruction-set boundary, a `mov` instruction may be treated as one synchronous effect or observation. At a lower microarchitectural boundary, the same instruction may be realized through cache lookups, buffers, bus transactions, speculative execution, invalidations, or other independently progressing activity. The model should therefore name the boundary whose guarantees are being claimed instead of treating "local" as automatically synchronous or trivial.

## Semantic Interpretation

Modes describe the edge shape. They do not determine the semantic role of the value crossing the edge.

A request may be interpreted as a [[Command|command]] when the receiver treats it as intent to cause a state transition. It may be interpreted as a [[Query|query]] when the receiver treats it as a request to observe or compute a value with no semantic state transition requested. It may also be a subscription request, negotiation, acknowledgment, policy decision, observation, or event notification.

At the emitting boundary, initiating such an interaction may be modeled as a request [[Effect|effect]]: the emitter establishes a typed terminal-response or terminal-failure obligation and a continuation that consumes it. The request is a distinct emission role rather than an event subtype. At the receiving boundary, message ingress is an exogenous event. Its carried value and contract supply evidence for interpretation as a command, query, negotiation, subscription, or another semantic role. The response is a later reply or terminal result at another boundary; it need not be synchronous or travel over the same channel.

A request differs from one-way publication by response obligation and continuation rather than necessarily by publication mechanics. Both may use an outbox, queue, broker, log, mailbox, or network call. A delivery acknowledgment is not automatically the requested response: it may establish only admission, persistence, publication, or responsibility transfer.

### Implicit Request Protocols

An **implicit request protocol** occurs when a publication is presented as an event even though the emitter's continuation depends on a responsible receiver eventually producing a correlated terminal result. The transport may be asynchronous, but the emission has the semantic role of a request [[Effect|effect]], not a domain-event emission.

This case is stronger than merely expecting some receiver to act. An event-styled one-way action obligation is a command or signal disguised as event publication. When the emitter requires a correlated terminal response or terminal failure in order to continue, the interaction is asynchronous request/reply and should declare its request identity, reply path or result-observation rule, correlation, timeout, and failure meanings explicitly.

Martin Fowler describes the broader modeling failure as using an event as a "passive-aggressive command." Cohesive uses **implicit request protocol** for the narrower case with a response obligation and treats the informal label only as external provenance.

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

Backpressure is capacity feedback over an interaction edge. [[Flow Control|Flow control]] is the operational protocol that turns capacity state or feedback into changed admission, demand, buffering, scheduling, batching, throttling, blocking, or shedding behavior.

Flow control should not be confused with [[Interaction Control Flow|interaction control flow]]. Flow control regulates how much work may progress in response to capacity; interaction control flow identifies which participant actively drives an operation. The interaction-control role constrains where a flow-control policy can act without defining that policy. The canonical [[Flow Control|flow-control]] concern defines push, pull, and mediated mechanisms together with their bounds, failure modes, and modeling requirements.

## Failure and Partial Failure

Non-trivial interaction boundaries admit partial failure. A send may succeed locally while the receiver never observes it. A receiver may process input but fail before replying or acknowledging. A reply may be lost after a transition commits. A broker may persist a message while a consumer crashes after processing but before advancing its offset or claim.

The structural ambiguity is that absence of response does not distinguish slow, lost, rejected, crashed, partitioned, duplicated, or already-committed work. Interaction designs therefore need explicit timeout, retry, acknowledgment, idempotency, dead-letter, circuit-breaking, and recovery meanings. Those meanings connect interaction to [[Retry|retry]], [[Idempotency|idempotency]], [[Acknowledgments|acknowledgments]], [[Delivery Semantics|delivery semantics]], [[Commit Boundaries|commit boundaries]], and [[Recovery|recovery]].

## Interaction Graphs

An interaction graph is one projection of the broader system graph. Its edges mean that one participant operationally affects, observes, invokes, signals, publishes to, consumes from, reads, writes, waits for, or synchronizes with another participant or channel through a declared or inferred interface.

Interaction edges can also induce causal or happens-before structure when a protocol relates one local occurrence to another. In Lamport-style causal ordering, a send happens before the corresponding receive. Request/reply, publish/consume, shared-state updates, acknowledgments, and synchronization points similarly create possible-causality edges when the model records those relations. The force of that ordering remains boundary- and mechanism-relative; see [[Ordering|ordering]].

Other graph projections use different edge meanings:

| Graph | Typical nodes | Edge meaning |
| --- | --- | --- |
| Interaction graph | observers, channels, brokers, services, actors, shared-state cells | send, receive, request, reply, publish, consume, read, write, wait, notify, synchronize |
| Entity relationship graph | entities, identities, aggregates, resources | semantic relation, reference, ownership, dependency, association |
| Process or flow graph | activities, steps, observers, states, events | process progression, causal flow, sequencing, handoff, compensation |
| State transition graph | states, versions, transition labels | possible state change under command, event, policy, or guard interpretation |
| Projection graph | sources, projections, read models, indexes | derivation, materialization, reconstitution dependency |
| Realization graph | runtimes, hosts, storage systems, brokers, networks | realizes, hosts, deploys, persists, routes, schedules |

The same system element can appear in several graphs. An entity relationship does not imply direct interaction. An interaction edge does not imply a semantic entity relationship. A process-flow edge may be realized by several interaction edges. A broker, channel, mailbox, lock, or shared memory cell may be modeled as an edge at one abstraction layer and as a node at another.

Interaction graphs are especially useful for reasoning about coordination, delivery, ordering, backpressure, failure, acknowledgment, progress, settlement, durability, and commit boundaries. An interaction edge should therefore be annotated with its provided and required interfaces, governing protocol, endpoints, interaction binding, channel and directions, boundary where guarantees hold, mode, topology, carried semantic roles, and realizing substrate layer.

## Dimensions

An interaction edge can be classified by:

- Abstraction level.
- Addressing space.
- Operation role: send, receive, request, reply, publish, consume, read, write, lock, wait, subscribe, poll.
- Interaction-control role and direction: active sender or fetcher, passive sink or source, and pusher, puller, queue, or driver at composed stages.
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

## External References

- Gregor Hohpe and Bobby Woolf, [Message Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/MessageChannel.html), [Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Message.html), and [Point-to-Point Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html), *Enterprise Integration Patterns*, 2003.
- Gregor Hohpe and Bobby Woolf, [Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html), *Enterprise Integration Patterns*, 2003.
- Gregor Hohpe and Bobby Woolf, [Return Address](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ReturnAddress.html) and [Correlation Identifier](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CorrelationIdentifier.html), *Enterprise Integration Patterns*, 2003.
- AsyncAPI Initiative, [Adding Reply Info](https://www.asyncapi.com/docs/concepts/asyncapi-document/reply-info).
- Martin Fowler, [What do you mean by "Event-Driven"?](https://martinfowler.com/articles/201701-event-driven.html), 2017.
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Interfaces|interfaces]], [[Interaction Protocols|interaction protocols]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Observer|observer]], [[Command|command]], [[Query|query]], [[Event|event]], [[Effect|effect]], [[Messages and Envelopes|messages and envelopes]], [[Interaction Channels|interaction channels]], [[Interaction Control Flow|interaction control flow]], [[Flow Control|flow control]], [[Routing Models|routing models]], [[Correlation and Conversations|correlation and conversations]], [[Consumer Coordination|consumer coordination]], [[Relation Models|relation models]], [[Flow Views|flow views]], [[Projection Models|projection models]], [[Delivery Semantics|delivery semantics]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Coordination|coordination]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Network Channels|network channels]], [[Network|network]], [[Brokers|brokers]], [[Actor Systems|actor systems]], [[Trace and Feedback|trace and feedback]], [[Duality and Symmetry|duality and symmetry]].
