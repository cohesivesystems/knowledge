---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-27
updated: 2026-07-27
aliases:
  - Distributed Control Flow
  - EIP Control Flow
  - Interaction Drive
  - Push and Pull
---

# Interaction Control Flow

Interaction control flow identifies which participant or mediating locus actively drives each operation at a distributed interaction boundary.

It is distinct from **data flow**, which identifies the direction in which a carried value moves. In a push interaction, the carried value and driving operation both point from the sender toward the recipient. In a pull interaction, a consumer actively fetches from a provider, so the data moves from provider to consumer while the driving operation points from consumer to provider.

The term is deliberately qualified as *interaction* control flow because control flow is overloaded. It does not by itself mean:

- Branching, looping, token progression, or sequencing within a semantic [[Process|process]] or [[Process Graphs|process graph]].
- Host-language evaluation order or whether a logical operation waits synchronously for a result.
- [[Orchestration and Choreography|Orchestration]] authority or ownership of a larger process decision surface.
- A control plane or [[Operational Control|operational control]] operation.
- **Flow control**, which applies backpressure, credits, buffering, admission, batching, throttling, or shedding in response to capacity.

These notions can interact, but none can be inferred from another.

## Boundary Roles

Active and passive are port roles at a declared boundary, not intrinsic properties of a whole component.

| Role | Activity at the boundary | Data direction | Interaction-control direction |
| --- | --- | --- | --- |
| **sender** | actively pushes a value to a recipient | sender to sink | sender to sink |
| **sink** | passively accepts a pushed value | sender to sink | sender to sink |
| **source** | passively makes a value available to be fetched | source to fetcher | fetcher to source |
| **fetcher** | actively requests or polls for a value | source to fetcher | fetcher to source |

The initiating operation is itself a local occurrence. It does not determine whether the carried value is interpreted as a [[Command|command]], [[Event|event]], [[Observation|observation]], request, reply, signal, or other semantic role. That interpretation remains observer- and boundary-relative.

## Composed Stages

The same roles apply independently at the input and output ports of an integration stage:

| Stage role | Input port | Output port | Operational consequence |
| --- | --- | --- | --- |
| **pusher** | passive | active | accepts pushed input and actively pushes output; adjacent activity generally follows the data direction |
| **puller** | active | passive | fetches input when downstream demand reaches it and makes output available to be fetched; adjacent activity generally runs opposite the data direction |
| **queue** | passive | passive | accepts input from an active producer and exposes output to an active consumer; separates arrival and departure cadence through retained or buffered state |
| **driver** | active | active | fetches from a source and pushes to a sink; owns cadence and can apply polling, batching, concurrency, or rate policy |

A queue therefore changes which side drives each adjacent operation and allows production and consumption rates to vary independently. This temporal decoupling does not make capacity unlimited: the queue still needs explicit [[Interaction|flow control]], retention, overflow, expiration, retry, and recovery policies.

A driver can slow fetch cadence when a target is constrained and may preserve order when its scheduling and concurrency rules do so. Unlike a durable queue, however, a driver does not inherently retain accepted work across interruption. Buffering, durability, ordering, and acknowledgment remain separate guarantees.

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

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Interaction|interaction]], [[Flow Views|flow views]], [[Interaction Channels|interaction channels]], [[Consumer Coordination|consumer coordination]], [[Brokers|brokers]], [[Messages and Envelopes|messages and envelopes]], [[Observer Models|observer models]], [[Process Theories|process theories]], [[Process Graphs|process graphs]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Trace and Feedback|trace and feedback]], [[Rate Limiting|rate limiting]], [[Scheduling|scheduling]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Durability|durability]], [[Recovery|recovery]], [[Operational Control|operational control]], [[Execution Kernel|execution kernel]].
