---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-29
---

# Time

## Semantic Role

Time is the dimension in which occurrences, changes, histories, and behaviors are ordered or compared.

In the model, [[Value|values]] and [[Observation|observations]] do not carry intrinsic occurrence time. Time belongs to [[Event|events]], version histories, and [[Behavior|behaviors]].

## Entity Histories

For an [[Entity|entity]], time is reflected operationally by its ordered sequence of versions. A state becomes current at the version or time produced by the event that caused it.

## Representations

Time may be represented by clocks, event positions, versions, sequence numbers, workflow history positions, stream offsets, or other ordering mechanisms depending on the realization substrate.

## Wall-Clock and Civil Time

**Wall-clock time** is time as reported by a physical or civil clock, such as UTC timestamps or local calendar time. It is useful for deadlines, schedules, retention windows, human interpretation, and external correlation, but it does not by itself define causal order or prove that a semantic transition committed.

Time data structures carry different semantics. An **instant** identifies a globally comparable point, usually represented in UTC. A **duration** measures an elapsed amount rather than a calendar position. **Civil time** combines calendar fields with an offset or timezone. A local or relative time such as `2pm` is not a global instant until a date, timezone, calendar, or scheduling context supplies the missing interpretation. Recurring civil times may not correspond to uniform durations because calendar and timezone rules can change.

## Clocks and Uncertainty

A wall clock estimates a time-of-day coordinate. Its readings can jump or repeat because of synchronization, administrator changes, leap handling, virtualization, restore, or hardware behavior. A monotonic clock instead supports elapsed-time measurement within its continuity boundary and should not be interpreted as a civil timestamp.

Distributed clock readings have uncertainty from offset, drift, synchronization delay, and process pauses. Timestamp comparison therefore does not establish [[Happened-Before|happened-before]] or semantic causation unless the model supplies stronger clock bounds and a protocol that uses them. Last-write-wins ordering by physical timestamp is a conflict-resolution policy under those assumptions, not a discovery of the true causal order.

Timeout and lease logic must name the clock and continuity boundary it depends on. A timeout proves that an observer did not see an expected occurrence before its local deadline; it does not prove that the remote participant failed. A lease based on bounded clock error or elapsed time also requires target-side fencing or another authority check when a former holder may continue acting after expiry.

## Occurrence and Observation Times

One semantic occurrence can acquire several later time observations: source occurrence time, ingestion time, processing time, commit time, and visibility time. These timestamps describe different events and may appear in different orders across participants.

Source occurrence time is contextual evidence. It may come from an untrusted device, a civil-time report, an estimated sensor clock, or a participant whose clock uncertainty is unknown. The receiving observer should preserve the source, basis, precision, and uncertainty needed for interpretation rather than silently treating every timestamp as one global instant.

[[Temporal Completeness|Temporal completeness]] uses these distinctions when windows, watermarks, triggers, and late-input policies decide when a time-bounded result is sufficiently complete to emit or finalize.

## Logical and Causal Time

**Logical clocks** model time as event ordering rather than wall-clock measurement. In distributed systems, this may produce partial orders where some events are concurrent or incomparable.

The clock or version map is order-preserving with respect to Lamport's happened-before relation:
$$
A \prec B \Rightarrow \operatorname{version}(A) \le \operatorname{version}(B)
$$

Here $A \prec B$ means that event or observation `A` happens before `B`. The implication is one-way for ordinary logical clocks: ordered versions preserve happened-before, but comparing versions does not always recover the full causal relation unless the version representation carries enough causal metadata.

**Vector clocks** refine logical time by tracking causal position across multiple participants. They are useful when a model must distinguish causally ordered events or state observations from concurrent or incomparable ones rather than forcing everything into one total order. A [[Version|version]] in a distributed or replicated history may use vector-clock-like metadata as its realization.

Logical and causal time also support the notion of a consistent cut: a causally closed selection of events, versions, or observations used to define a coherent snapshot across distributed participants.

[[Synchrony and Asynchrony]] relates to time but is not the same distinction. Timing-model synchrony assumes bounds, rounds, or clocks. Commit or observation synchrony may instead be logical: several events are treated as one boundary-relative unit even if they did not occur at the same wall-clock instant.

## External References

- Leslie Lamport, [Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf), Communications of the ACM, 21(7):558-565, July 1978.
- Friedemann Mattern, [Virtual Time and Global States of Distributed Systems](https://homes.cs.washington.edu/~arvind/cs425/doc/mattern89virtual.pdf), 1989.

Related concepts: [[Value|value]], [[Event|event]], [[Observation|observation]], [[Observer|observer]], [[Behavior|behavior]], [[Version|version]], [[State|state]], [[Ordering|ordering]], [[Happened-Before|happened-before]], [[Uncertainty|uncertainty]], [[Authority|authority]], [[Failure Models|failure models]], [[Temporal Completeness|temporal completeness]], [[Synchrony and Asynchrony|synchrony and asynchrony]], [[Consistency Models|consistency models]].
