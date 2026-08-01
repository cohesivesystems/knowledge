---
realm: System Graph
kind: structural-construct
created: 2026-07-27
updated: 2026-08-01
aliases:
  - Integration Flow Operators
  - Pipes and Filters
---

# Flow Operators

Flow operators are compositional structures that transform, select, divide, combine, order, or distribute values moving through [[Flow Views|flow views]].

An operator describes graph structure and declared interpretation, not a specific framework callback or broker feature. Operators may appear inside a finite process activation, a projection pipeline, a stream processor, an integration flow, or a runtime data path.

## Operator Families

- **Transform** maps one shaped value into another while preserving or explicitly changing meaning.
- **Filter** selects or projects values under a declared predicate, policy, or shape.
- **Enrich** combines a carried value with explicit observations or referenced material.
- **Split** maps one composite input into correlated parts. It is distinct from the control-activation side of [[Fork and Join|fork and join]].
- **Aggregate or join** combines correlated parts under a completeness, window, quorum, or terminal rule. Value aggregation is distinct from a control-flow join even when one process node performs both.
- **Resequence** emits admitted values according to a declared ordering space.
- **Scatter-gather** distributes related requests or work and combines selected replies or results.
- **Composed processing** connects several operators while preserving the identity and completion rule of the larger flow.

Split, aggregation, and scatter-gather require explicit correlation, cardinality, completion, timeout, duplicate, missing-part, late-part, cancellation, and failure meanings. An aggregator cannot infer completeness merely because no more messages are currently visible. [[Temporal Completeness|Temporal completeness]] states how windows, watermarks, triggers, and late-input policy qualify that decision for time-bounded asynchronous input. Without a rule for a missing, skipped, cancelled, or failed part, the operator can create a structural [[Deadlock and Livelock|deadlock]]. A resequencer cannot wait indefinitely without a gap, expiration, or recovery policy.

Aggregation is distinct from [[Multiplexing and Demultiplexing|multiplexing]]. Aggregation combines several values into a new composite value under a semantic or structural completion rule; multiplexing lets distinguishable logical flows share a locus while retaining their identities.

Operators that make business decisions belong inside an authorized [[Transition Models|transition model]] or [[Process Graphs|process graph]], not as hidden adapter callbacks. Pure structural transformation may be lowered into broker rules, stream processors, generated code, workflow nodes, queries, or in-process functions when their semantics and guarantees correspond.

An operator's transformation meaning is distinct from its [[Interaction Control Flow|interaction-control role]]. The same transform can accept pushed input and push output, fetch input and expose output for downstream fetch, buffer between two active participants, or actively fetch and push as a driver. Those choices affect cadence, buffering, latency, scheduling, backpressure, and recovery without redefining the transform itself, so executable flow views should declare both the operator and its per-port activity where the distinction is operationally significant.

## External References

- Gregor Hohpe and Bobby Woolf, [Pipes and Filters](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PipesAndFilters.html), [Splitter](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Sequencer.html), [Aggregator](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Aggregator.html), and [Resequencer](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Resequencer.html), *Enterprise Integration Patterns*, 2003.
- Enterprise Integration Patterns, [Message Routing and Transformation patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html).
- Gregor Hohpe, [Control Flow—The Other Half of Integration Patterns](https://www.enterpriseintegrationpatterns.com/ramblings/queues_control_flow.html), 2024.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Flow Views|flow views]], [[Process Graphs|process graphs]], [[Fork and Join|fork and join]], [[Transition Models|transition models]], [[Routing Models|routing models]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Messages and Envelopes|messages and envelopes]], [[Interaction Channels|interaction channels]], [[Interaction Control Flow|interaction control flow]], [[Shape|shape]], [[Observation|observation]], [[Correlation and Conversations|correlation and conversations]], [[Ordering|ordering]], [[Consistent Cuts|consistent cuts]], [[Temporal Completeness|temporal completeness]], [[Deadlock and Livelock|deadlock and livelock]], [[Compositionality|compositionality]].
