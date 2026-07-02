---
realm: Domain Semantics
kind: semantic-construct
---

# Observable

An observable is a probe, projection, measurement, or field accessor that produces an [[Observation|observation]] from [[State|state]].

Observables define how state becomes visible to an [[Observer|observer]]. Different observables may produce different observations from the same underlying state.

An observable is not itself the state. It is the access path, view, or measurement by which state is shaped into a usable [[Value|value]] with a declared [[Shape|shape]].

A [[Query|query]] selects, invokes, or parameterizes an observable relative to an observer, boundary, authority, and consistency expectation.

## Examples

Examples of observables include:

- A field accessor such as `order.status`, which observes one dimension of order state.
- A current-state observable for an [[Entity|entity]], such as the accessor, [[Reconstitution|reconstitution]] procedure, projection, or subscription that produces an entity-scoped observation at a declared [[Version|version]], boundary, and consistency expectation.
- A [[Projections|projection]] or read model such as account balance derived from ledger events.
- A metric, probe, or sensor such as queue depth, process memory, CPU load, or room temperature.
- A UI view such as a filtered task list, selected row, or visible validation state.
- A policy-shaped view such as a customer profile with private fields redacted for a particular observer.
- A computation such as available inventory for a SKU and location under a selected freshness rule.

In each case, the observable defines what can be seen and how it is shaped. The resulting observation carries the value, subject, source, version, observer, or other provenance needed for the model.

## Distinctions

The current state of an entity is not itself an observable. It is state. The way an observer obtains that current state is an observable.

```txt
entity state
  -> current-state observable
  -> entity-scoped observation
```

The observable may read authoritative persistence, reconstitute an aggregate, query a read-side projection, inspect a cache, or subscribe to the latest value emitted by a runtime. Each choice can produce a different observation of the same entity state because each is relative to a boundary, authority, version, and consistency expectation.

An observable is also distinct from the [[Observation|observation]] it produces. The observable is the rule, access path, or measuring apparatus. The observation is the contextualized value that results.

A projection may realize an observable, especially on the query side of [[CQRS]], but not every observable is a maintained projection. Some observables are direct accessors, derived computations, transient measurements, subscriptions, or probes.

## Reactive Programming and Physics Usage

Reactive programming often uses "observable" for a subscribable source that emits values over time. In this model, that is an operational realization of an observable when the emitted values are observations of state. When the emitted values are occurrence-bearing, the same runtime mechanism may instead be better understood as an [[Event|event]] source or event stream. The distinction depends on whether the stream is exposing changing state, reporting occurrences, or deriving a [[Behavior|behavior]].

The physics analogy is useful but informal. A physical observable names something measurable about a system, while an observation is the result obtained through a particular measurement context. Similarly, in this model an observable is not the underlying state. It is the rule, probe, or apparatus by which state becomes visible to an observer.

Related concepts: [[State|state]], [[Value|value]], [[Shape|shape]], [[Observation|observation]], [[Query|query]], [[Observer|observer]], [[Projections|projection]], [[Entity|entity]], [[Version|version]], [[Event|event]], [[Behavior|behavior]], [[CQRS]].
