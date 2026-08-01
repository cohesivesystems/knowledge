---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-27
updated: 2026-08-01
aliases:
  - Distributed Control Flow
  - EIP Control Flow
  - Interaction Drive
  - Push and Pull
---

# Interaction Control Flow

Interaction control flow identifies which participant or mediating locus actively drives each operation at a distributed interaction boundary.

It is distinct from **data flow**, which identifies the direction in which a carried value moves. In a push interaction, the carried value and driving operation both point from the sender toward the recipient. In a pull interaction, a consumer actively fetches from a provider, so the data moves from provider to consumer while the driving operation points from consumer to provider.

The term is deliberately qualified as *interaction* control flow because [[Control Flow|control flow]] is overloaded. It does not by itself mean:

- Branching, looping, token progression, or sequencing within a semantic [[Process|process]] or [[Process Graphs|process graph]].
- Host-language evaluation order or whether a logical operation waits synchronously for a result.
- [[Orchestration and Choreography|Orchestration]] authority or ownership of a larger process decision surface.
- A control plane or [[Operational Control|operational control]] operation.
- **[[Flow Control|Flow control]]**, which applies backpressure, credits, buffering, admission, batching, throttling, or shedding in response to capacity.

These notions can interact, but none can be inferred from another.

## Activation and Continuation

Interaction-control roles are boundary-relative and may compose across layers. A participant can actively poll a broker at one boundary, after which the broker client or runtime actively dispatches a delivery into a passive callback at another. The implementation therefore contains a pull followed by a push even when the public interface presents only one of them.

Callback invocation is runtime activation, not automatically semantic process progression. The callback outcome becomes relevant to [[Control Flow|process control flow]] only when an authorized observer admits and interprets it as an observation, decision, event, or effect result that enables or selects a successor. [[Scheduling]] then determines when an enabled callback, handler, or continuation executes and whether its work is cooperatively yielded or preempted. Process progression, interaction drive, and execution opportunity may correspond in a realization, but they remain distinct relations.

## Boundary Roles

Active and passive are port roles at a declared boundary, not intrinsic properties of a whole component.

| Role        | Activity at the boundary                        | Data direction    | Interaction-control direction |
| ----------- | ----------------------------------------------- | ----------------- | ----------------------------- |
| **sender**  | actively pushes a value to a recipient          | sender to sink    | sender -> sink                |
| **sink**    | passively accepts a pushed value                | sender to sink    | sender -> sink                |
| **source**  | passively makes a value available to be fetched | source to fetcher | fetcher -> source             |
| **fetcher** | actively requests or polls for a value          | source to fetcher | fetcher -> source             |

The initiating operation is itself a local occurrence. It does not determine whether the carried value is interpreted as a [[Command|command]], [[Event|event]], [[Observation|observation]], request, reply, signal, or other semantic role. That interpretation remains observer- and boundary-relative.

## Composed Stages

The same roles apply independently at the input and output ports of an integration stage:

| Stage role | Input port | Output port | Operational consequence |
| --- | --- | --- | --- |
| **pusher** | passive | active | accepts pushed input and actively pushes output; adjacent activity generally follows the data direction |
| **puller** | active | passive | fetches input when downstream demand reaches it and makes output available to be fetched; adjacent activity generally runs opposite the data direction |
| **queue** | passive | passive | accepts input from an active producer and exposes output to an active consumer; separates arrival and departure cadence through retained or buffered state |
| **driver** | active | active | fetches from a source and pushes to a sink; owns cadence and can apply polling, batching, concurrency, or rate policy |

A queue therefore changes which side drives each adjacent operation and allows production and consumption rates to vary independently. This temporal decoupling does not make capacity unlimited: the queue still needs explicit [[Flow Control|flow-control]], [[Rate Limiting|rate-limiting]], capacity, [[Retention Expiration and Quarantine|retention, overflow, and expiration]], [[Retry|retry]], and [[Recovery|recovery]] policies.

A driver can slow fetch cadence when a target is constrained and may preserve order when its scheduling and concurrency rules do so. Unlike a durable queue, however, a driver does not inherently retain accepted work across interruption. Buffering, durability, ordering, and acknowledgment remain separate guarantees.

## Request, Acknowledgment, and Polling

A request/acknowledgment/poll protocol composes several interaction edges around one long-lived semantic [[Process|process]]. It does not make the process durable by itself. Durability requires the process identity, accepted work, progress, status, and terminal outcome to survive the failures claimed by the model.

| Phase | Protocol meaning | Interaction-control framing |
| --- | --- | --- |
| **start request** | A client requests that the receiver create, admit, or begin the process. | The client is an active sender and the receiving endpoint is a passive sink at the start edge. |
| **acknowledgment** | The receiver reports a precisely named boundary fact, such as durable admission and a process identity. It does not imply process completion. | On the response edge, the receiver supplies the acknowledgment and the client receives it. [[Acknowledgments|Acknowledgment]] names what is claimed; reply names its role in discharging a request. |
| **process execution** | The process advances through independently durable activations or cuts after admission. | Its internal scheduling, queues, timers, callbacks, or workers have their own interaction-control roles; no continuing client operation should be inferred. |
| **status poll** | The client makes a new request, usually interpreted as a [[Query|query]], for an [[Observation|observation]] of process status or result. | The client is an active fetcher and the status endpoint is a passive source. The poll operation points toward the source while status data returns toward the fetcher. |
| **terminal observation** | A poll reports that the process completed, failed, was cancelled, or reached another declared terminal disposition. | The response discharges that poll request. Whether it also completes a broader conversation depends on the separately declared process and correlation protocol. |

The initial acknowledgment has two coherent interpretations. If the start request asks only for durable admission, an accepted acknowledgment is its terminal reply; later polls are independent requests correlated by process identity. If the original semantic request asks for the eventual process result, the acknowledgment is nonterminal at that boundary—even if it terminates an HTTP exchange or another lower-level call—and the original terminal-response or terminal-failure obligation remains live while polling supplies supplemental observations. The contract must state which interpretation applies and must not confuse delivery or admission acknowledgment with process completion.

Polling therefore realizes a client-driven pull interface over process status; it does not simulate the process's durability. Poll cadence, backoff, caching, stale observations, authorization, terminal-result retention, and the distinction among request, conversation, and process identities remain explicit operational concerns. See [[Correlation and Conversations|correlation and conversations]], [[Durability|durability]], and [[Process Graphs|process graphs]].

## Modeling Requirements

For each relevant interaction port or edge, state:

- The abstraction layer and boundary at which the role is observed.
- The direction of carried data or messages.
- Which participant actively initiates push, fetch, poll, callback, or delivery.
- Whether a component is passive or active at each port.
- Single-item or batch cardinality, cadence, concurrency, and scheduling ownership.
- Where accepted work can wait and whether that buffer is bounded and durable.
- How backpressure and flow-control information travel.
- Ordering, acknowledgment, failure, retry, and completion meanings.

An arrow should identify whether it denotes data movement, interaction control, causal precedence, process progression, or another relation. One unqualified arrow cannot safely stand for all of them.

Visual projections may use EIP's active and passive port affordances to make compatible connections apparent. The canonical graph should still store the boundary, role, direction, and cardinality explicitly rather than relying on a glyph as the only source of meaning.

These roles are abstraction-relative. A managed service may appear as a pusher at its public output while internally using a queue, a worker pool, and active drivers. Lowering an interaction through the [[Execution Kernel|execution kernel]] may likewise introduce or remove queues and drivers, but the realization must preserve the declared semantic correspondence and make any changed latency, ordering, capacity, durability, or recovery guarantees explicit.

## External References

- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), Enterprise Integration Patterns, 2024.
- Gregor Hohpe and Bobby Woolf, [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/), Addison-Wesley Professional, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Interaction|interaction]], [[Control Flow|control flow]], [[Flow Control|flow control]], [[Flow Views|flow views]], [[Interaction Channels|interaction channels]], [[Consumer Coordination|consumer coordination]], [[Brokers|brokers]], [[Messages and Envelopes|messages and envelopes]], [[Observer Models|observer models]], [[Process Theories|process theories]], [[Process Graphs|process graphs]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Correlation and Conversations|correlation and conversations]], [[Acknowledgments|acknowledgments]], [[Trace and Feedback|trace and feedback]], [[Rate Limiting|rate limiting]], [[Scheduling|scheduling]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Durability|durability]], [[Recovery|recovery]], [[Operational Control|operational control]], [[Execution Kernel|execution kernel]].
