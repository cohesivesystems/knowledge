---
realm: System Graph
kind: structural-construct
created: 2026-08-17
updated: 2026-08-17
status: draft
aliases:
  - Interaction Mode
  - Interaction Patterns
  - Communication Modes
  - Communication Patterns
---

# Interaction Modes

Interaction modes are boundary-relative profiles of how participants are structurally arranged to affect, observe, request, answer, share state with, wait for, or synchronize with one another.

They arrange semantic [[Interaction|interaction]] without determining the meaning of the carried value, the complete legal trace, the operational guarantees, or the realizing mechanism. A mode must therefore be described across several independent dimensions rather than reduced to a label such as *message-driven*, *request/reply*, *synchronous*, or *non-blocking*.

## Profile Dimensions

| Dimension | Question | Representative values |
| --- | --- | --- |
| Mediation family | Through what logical locus do participants interact? | direct invocation, explicit message passing, shared state, or retained artifact |
| Exchange morphology | How many related occurrences and directions form the exchange? | one-way, request/reply, publish/consume, request stream, response stream, bidirectional stream, or session |
| [[Synchrony and Asynchrony\|Synchronization]] | Which local occurrences remain distinct, and which are coordinated into one boundary-relative unit? | asynchronous send and receive, call/return wait, handoff rendezvous, barrier, critical section, transaction, or commit point |
| [[Interaction Control Flow\|Interaction control]] | Which participant actively drives each operation? | push, pull, poll, callback, queue, or source-to-sink driver |
| Topology | How are senders, receivers, and mediating loci related? | one-to-one, one-to-any, one-to-many, many-to-one, many-to-many, partitioned, replicated, or dynamically routed |
| Retention and cadence | Can accepted work outlive either participant or wait between stages? | direct handoff, buffered, queued, logged, replayable, expiring, or unbounded only as an invalid assumption |
| [[Progress Conditions\|Runtime progress]] | What can remain occupied or prevented from advancing while the logical interaction is pending? | OS-thread blocking, continuation suspension, cooperative yield, lock-free progress, wait-free progress, or progress conditional on another participant |

These dimensions constrain one another without collapsing into one axis. A rendezvous selects a synchronization relationship by definition. A direct call commonly combines caller-driven request/reply with control-flow synchrony and one call stack, but a runtime can dispatch the same interface asynchronously. Explicit message passing separates carrier emission from reception, yet a sender can still block on mailbox capacity or wait synchronously for a reply.

## Mediation Families

### Direct invocation

Direct invocation lets one participant activate an operation exposed by another through a call, dispatch table, object reference, or local interface. It commonly presents request/reply as one control-flow interval, but the callee may return a future, stream, callback registration, or acknowledgment that leaves later occurrences asynchronous.

An in-process call can still cross authority, commit, scheduling, or failure boundaries. Conversely, making a remote call resemble a local invocation does not remove network latency, serialization, partial failure, or ambiguous outcomes. See [[Fallacies of Distributed Computing|fallacies of distributed computing]].

### Explicit message passing

Explicit message passing uses a finite carrier emitted toward an address, channel, mailbox, endpoint, or mediating locus and separately admitted or received elsewhere. [[Messages and Envelopes|Messages and envelopes]] describe the carrier; [[Interaction Channels|interaction channels]] arrange the logical exchange and its directions; [[Interaction Protocols|interaction protocols]] constrain the legal conversation.

Message passing can support one-way send, correlated request/reply, publication, consumption, control signals, failure reports, and streaming frames. It does not by itself imply asynchrony, actor isolation, buffering, durability, reliable delivery, backpressure, location transparency, or non-blocking use of OS threads.

### Shared-state mediation

Shared-state interaction lets participants communicate by reading, writing, updating, locking, waiting on, or observing a common state locus. The locus may be a memory cell, register, object, table, log, file, lock, condition variable, transactional store, or replicated abstraction.

Shared state can realize request/reply-like reads, one-way writes, publish/observe patterns, compare-and-swap, transactions, barriers, and wait/notify protocols. It requires explicit visibility, consistency, synchronization, authority, and failure boundaries. A logically shared state abstraction may itself be realized by lower-level message passing.

### Retained artifact exchange

Participants may interact through a file, object, document, batch, log segment, or other retained artifact whose production and consumption are separate occurrences. Retention decouples availability and cadence but introduces identity, versioning, atomic publication, discovery, access control, compatibility, expiration, and recovery requirements. See [[Batch and File Exchange|batch and file exchange]].

## Exchange Morphologies

- **One-way:** one participant emits, writes, or signals without a modeled response continuation.
- **Request/reply:** a request establishes an obligation or continuation discharged by a later terminal response or declared terminal failure. The exchange can be synchronous or asynchronous and can use calls, messages, queues, streams, or shared state.
- **Publish/consume:** producers make values available through a mediating locus from which one or more consumers observe or claim them. Topics, queues, logs, multicast, files, and shared observable state differ in topology and guarantees.
- **Stream/session:** many related sends, receives, frames, or observations share a continuity, correlation, or conversational identity and may carry several higher-level exchanges. A stream may be full- or half-duplex, finite or open-ended, framed or byte-oriented, and synchronous or asynchronous at each operation. Its continuity and ordering guarantees remain scoped to its declared layer.

Message exchange patterns are the subset of these morphologies realized through explicit message carriers. The morphologies are broader: request/reply, publication, and observation can also be realized through direct invocation, retained artifacts, or shared state.

## Synchronization Profiles

Synchronization modes deliberately join otherwise separate occurrences for progress, visibility, observation, or commitment. Examples include a blocking channel handoff, CSP-style rendezvous, barrier, latch, semaphore, join, critical section, transaction, actor turn, and consensus decision.

Synchronization is not limited to shared memory and is not the opposite of message passing. A message protocol can synchronize sender and receiver through rendezvous, reply, acknowledgment, quorum, or commit, while shared-state participants can interact through asynchronous observation or polling.

## Representative Profiles

| Example | Interaction profile |
| --- | --- |
| Local function call | direct invocation; request/reply; caller-driven; usually control-flow synchronous; commonly one OS thread and call stack |
| Actor tell | explicit message passing; one-way; sender push; asynchronous send and receive; mailbox admission and scheduling are separate boundaries |
| Actor ask | explicit message passing; request/reply; asynchronous carrier occurrences with a correlated continuation that may later be awaited |
| Shared-memory read | shared-state mediation; request/reply-like observation; reader-driven; visibility and synchronization depend on the memory model |
| Rendezvous channel | explicit message passing with synchronous handoff; sender and receiver progress are joined at the channel boundary |
| Broker publication | explicit message passing; publish/consume; producer push followed by broker push or consumer pull; commonly buffered or retained |
| File exchange | retained artifact; publication and later consumption; asynchronous cadence; discovery, atomic visibility, and compatibility are explicit |

The same interaction can have different profiles at different layers. Two local actors may communicate through logical messages while their runtime realizes a mailbox with shared memory. A distributed shared-state abstraction may present reads and writes while replicas coordinate through messages. Lowering must preserve the declared upper-layer meanings and expose any changed latency, delivery, consistency, progress, and failure properties.

## Modeling Checks

- What mediation family and exchange morphology are selected at this boundary?
- Which local occurrences remain asynchronous, and which are joined by reply, acknowledgment, rendezvous, transaction, or commit?
- Who actively drives each operation, and in which direction does the carried value move?
- Where can accepted work wait, and what bounds, retention, overflow, and recovery policies apply?
- Does a logical wait occupy an OS thread, suspend a continuation, or prevent another participant from progressing?
- Which topology, placement, locality, and failure boundaries remain visible?
- Which interface and protocol roles give the occurrences semantic and conversational meaning?
- Which lower-level modes realize the profile, and which guarantees change during lowering?

## Formal relations

- `arranges`: [[Interaction]] — Classifies reusable boundary-relative edge profiles while preserving semantic participant roles and leaving protocol, guarantee, and realization claims explicit.
- `constrains`: [[Interaction Protocols]] — Restricts the mediation, morphology, synchronization, control, topology, retention, and progress profile within which a protocol may define legal traces.
- `distinguished_from`: [[Progress Conditions]] — Interaction modes describe structural profiles, while progress conditions state which runtime or protocol participants can advance under declared assumptions.
