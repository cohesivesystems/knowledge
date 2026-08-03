---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-28
updated: 2026-08-02
aliases:
  - Backpressure and Flow Control
  - Capacity Flow Control
---

# Flow Control

Flow control regulates how much work may be admitted or remain in flight between participants in response to available capacity.

Backpressure is capacity feedback over an [[Interaction|interaction]] edge: a receiver, channel, broker, runtime, or dependency reports that it cannot accept or process work at the offered rate. Flow control is the protocol that turns capacity state or feedback into changed admission, demand, buffering, scheduling, batching, throttling, blocking, or shedding behavior.

Feedback and regulation are distinct occurrences. A capacity report, credit, acknowledgment, queue-depth observation, or demand grant does not regulate anything unless the responsible participant changes what it admits or offers. A buffer can delay when pressure becomes visible, but it does not remove the need for a bound and an overflow policy.

## Scope and Boundary

A flow-control claim must identify the constrained resource and the boundary at which its capacity is observed. The resource may be receiver concurrency, queue space, memory, network receive capacity, database connections, worker permits, downstream request budget, or another finite capability.

End-to-end flow control may compose several local loops. TCP receive-window control, a broker's admission policy, a consumer's fetch demand, and an application's worker limit can each protect a different boundary. Success at one layer does not prove that another layer has capacity or that application work completed.

The unit of control may be messages, bytes, records, requests, tasks, cost units, permits, or weighted work. A protocol must not treat unlike units as interchangeable without an explicit conversion or conservative bound.

## TCP Receive-Window Flow Control

TCP realizes byte-oriented flow control independently in each direction of a full-duplex connection. The receiving endpoint advertises a **receive window** in the TCP header: the number of additional data octets it is currently willing to accept beginning at the sequence position named by the acknowledgment field. Window scaling can increase the range represented by the header's 16-bit Window field.

The advertised window commonly reflects space in the receiving TCP buffer. As bytes arrive, unconsumed data occupies that buffer and the available window contracts. As the receiving application reads bytes, the implementation can advance the right edge of the window and advertise newly available capacity.

At the sender, acknowledged position, next-send position, and the peer's advertised window form a sliding admission bound. RFC 9293 expresses the currently usable window as:

```text
U = SND.UNA + SND.WND - SND.NXT
```

`SND.UNA` is the oldest unacknowledged sequence position, `SND.NXT` is the next sequence position to send, and `SND.WND` is the peer's advertised window. Newly transmitted bytes consume `U`; acknowledgments and window updates can make more sequence space usable. TCP uses sufficiently recent acknowledgment and sequence information when accepting a window update so that an older segment does not normally replace newer capacity information.

The acknowledgment number and advertised window have different meanings even though they travel in the same segment. The acknowledgment advances knowledge of transport receipt; the window reports current receive capacity. Neither means that the receiving application has read the bytes, interpreted an application message, completed work, or committed a domain transition.

If the receiver advertises a zero window, the sender stops transmitting new data under the normal window rule. TCP retains progress detection through **zero-window probes**: the sender periodically probes so that a later window reopening can be reported reliably even if an earlier window-update segment was lost. A receiver may keep the window closed indefinitely, so this preserves the ability to resume but does not guarantee progress.

TCP also avoids pathological tiny window movements. Sender and receiver silly-window-syndrome avoidance delay small transmissions or small window updates until a useful amount of capacity is available, subject to escape timers that prevent the optimization from creating permanent deadlock. Receivers should avoid shrinking an already advertised right window edge, although senders must remain robust if it occurs.

### Flow Control versus Congestion Control

TCP receive-window flow control protects the receiving endpoint and its per-connection buffer. TCP congestion control separately limits traffic in response to capacity and contention along the network path. A sender must obey both constraints: receiver capacity can be available while the network path is congested, or network capacity can be available while the receiver's window is exhausted.

This transport loop is not end-to-end application flow control. Socket send and receive buffers can delay when pressure reaches application code, and one TCP window governs a byte stream rather than the messages, requests, tenants, or logical streams [[Multiplexing and Demultiplexing|multiplexed]] over it. An application protocol still needs explicit queue bounds, concurrency limits, demand or credit semantics, overload behavior, and downstream propagation when those distinctions matter.

## Push and Pull

Flow control can be realized with either interaction-control direction:

- In a **push path**, a downstream participant or mediator returns credits, windows, readiness, refusal, or pressure information so the upstream sender can reduce, pause, batch, block, or shed offered work.
- In a **pull path**, the consumer controls demand through fetch cadence, batch size, cursor advancement, subscription demand, lease acquisition, or concurrency permits. Pull limits what is requested, but prefetched or already admitted work still requires explicit bounds.
- In a **mediated path**, a queue or broker accepts work from producers and exposes it to consumers under separate capacity loops. Durable buffering separates cadence; it does not create unlimited capacity.

[[Interaction Control Flow|Interaction control flow]] determines which participant has a natural place to observe capacity and regulate progress. It does not itself define the flow-control policy.

## Mechanism Families

Common mechanism families include:

- Credit, permit, token, or advertised-window protocols.
- Explicit demand and bounded subscription protocols.
- Bounded buffers with refusal, blocking, overflow, or shedding behavior.
- High-water and low-water marks with pause and resume behavior.
- Consumer concurrency, fetch-size, batch-size, and prefetch limits.
- Acknowledgment, cursor, or lease rules that release capacity when responsibility advances.
- Rendezvous or blocking handoff that admits work only when both sides are ready.
- [[Control Models|Adaptive control models]] that change admission or offered rate from observed latency, queue depth, saturation, or failure evidence.

These mechanisms provide flow control only at their declared boundaries. A broker acknowledgment may release producer-side capacity without proving consumer capacity; a consumer acknowledgment may release a queue slot without proving a downstream domain transition committed.

## Channel Flow and Lifecycle

A channel binding can require one or more provider-neutral regulation forms:

- **bounded buffer** limits admitted in-flight work under an explicit overflow policy;
- **demand** lets the consumer request additional elements or iterator advancement;
- **credit** grants a count or quantity that delivery consumes; and
- **no semantic flow control** states that the channel contract relies on another boundary or accepts unregulated offering.

Flow regulation should be modeled separately from stream lifecycle. Terminal completion, half-close, independently completed directions, cancellation of one invocation or direction, connection termination, reconnect, and bounded resume are protocol states rather than capacity signals. They interact—a cancellation can release credits and a half-closed direction can stop demand—but one does not define the other.

The correspondence between messaging and [[Network Channels|network-channel]] flow control is frequently many-to-many. One transport receive window can couple several multiplexed logical channels; one messaging demand signal can regulate broker prefetch, worker permits, and network reads at different boundaries. A realization must identify which resource each loop protects and how pressure crosses codecs, buffers, brokers, and endpoint adapters.

## Distinctions

| Concept | Governing question |
| --- | --- |
| **flow control** | How much work may progress in response to available capacity? |
| **backpressure** | How does constrained capacity become feedback to a participant that can regulate work? |
| **[[Interaction Control Flow|interaction control flow]]** | Which participant actively pushes, fetches, polls, or delivers at this boundary? |
| **[[Rate Limiting|rate limiting]]** | How quickly may work proceed under a declared time-based policy or budget? |
| **[[Admission Control and Load Shedding|admission control]]** | Should this work be accepted at this boundary under current policy and capacity? |
| **scheduling** | Which admitted work should run next, when, and with which resources? |
| **buffering** | Where can an arrival and its consumption be separated temporarily? |
| **congestion control** | How should offered load adapt to contention or saturation in a shared path or network? |
| **[[Control Theory|feedback control]]** | How do observations of behavior regulate future action toward an objective? |

These concerns often cooperate. A capacity feedback loop may change a rate limit, an admission controller may refuse work when credits are exhausted, and a scheduler may allocate the remaining permits fairly. None of those compositions makes the terms synonymous.

## Modeling Requirements

For each flow-control loop, state:

- The constrained resource, capacity owner, boundary, and unit.
- Which observations or feedback indicate available or exhausted capacity.
- Which participant regulates admission or offered work and through which actuator.
- Initial capacity, maximum in-flight work, buffer bounds, and overflow behavior.
- Feedback delay, update frequency, hysteresis, and stale-information policy.
- Controller state, selected algorithm, action bounds, and initialization or restart behavior when regulation is adaptive.
- The identity, epoch, lease, or sequence rules for duplicated, lost, delayed, or reordered credits and acknowledgments.
- Fairness, priority, starvation, ordering, and partition interactions.
- Whether circular waits, exhausted credits, or failed consumers can deadlock progress.
- Restart, reconstitution, retry, cancellation, and recovery behavior.
- What telemetry demonstrates that the loop is stable rather than oscillating, saturating, or amplifying retries.

Flow control can enforce a capacity safety property; it is not by itself a liveness guarantee. A bounded system may remain permanently paused, starve one participant, or deadlock. Liveness requires explicit progress assumptions, scheduling, recovery, and fairness rules.

A delayed, oscillating, or incorrectly scoped flow-control loop can contribute to [[Metastability|metastability]] when its response amplifies retries, synchronizes resumed work, or protects one boundary by moving unbounded pressure to another.

## External References

- IETF, [RFC 9293: Transmission Control Protocol, Section 3.8.6, “Managing the Window”](https://www.rfc-editor.org/rfc/rfc9293.html#section-3.8.6), 2022.
- Reactive Streams, [Reactive Streams Specification](https://github.com/reactive-streams/reactive-streams-jvm#specification).
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Interaction|interaction]], [[Control Flow|control flow]], [[Control Theory|control theory]], [[Control Models|control models]], [[Additive Increase Multiplicative Decrease|AIMD]], [[PID Control|PID control]], [[Interaction Control Flow|interaction control flow]], [[Trace and Feedback|trace and feedback]], [[Queueing Theory|queueing theory]], [[Scalability|scalability]], [[Admission Control and Load Shedding|admission control and load shedding]], [[Metastability|metastability]], [[Rate Limiting|rate limiting]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Safety and Liveness|safety and liveness]], [[Progress Conditions|progress conditions]], [[Deadlock and Livelock|deadlock and livelock]], [[Delivery Semantics|delivery semantics]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Acknowledgments|acknowledgments]], [[Consumer Coordination|consumer coordination]], [[Interaction Protocols|interaction protocols]], [[Interaction Channels|interaction channels]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Brokers|brokers]], [[Network Channels|network channels]], [[Network|network]], [[Runtimes|runtimes]], [[Ordering|ordering]], [[Retry|retry]], [[Recovery|recovery]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]].
