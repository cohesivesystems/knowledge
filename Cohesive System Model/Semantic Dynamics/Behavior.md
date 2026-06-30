---
realm: Semantic Dynamics
kind: semantic-construct
---

# Behavior

Behavior is a time-varying [[Value|value]]: a trajectory through state space:

$$\text{time}\to\text{value}$$

This follows the classic Functional Reactive Programming notion of behavior introduced by Conal Elliott and Paul Hudak: a first-class value that varies over time.

For an [[Entity|entity]], behavior can be viewed as both an event schedule and a state history. The event schedule emphasizes occurrences and ordering. The state history emphasizes samples of state at versions, times, or cuts through the behavior.

Events do not accumulate into behavior by themselves. An [[Observer|observer]] interprets an event schedule through an accumulator, integrator, scanner, or transition function, then supplies a hold or interpolation function that maps the resulting history to values over time:

```txt
event schedule
+ initial value
+ interpretation function
+ interpolation function
-> behavior
```

For endogenous events in a sequential entity, the interpretation function can be viewed as a state action. Once an event has been interpreted and committed within a boundary, it may be identified with a function on state:

```txt
event : State -> State
```

Folding a schedule of endogenous events applies or composes those state actions from an initial state:

```txt
s1 = e1(s0)
s2 = e2(s1)
s3 = e3(s2)
```

The fold produces state samples or a state history. A behavior is produced when an interpolation rule, often "hold latest" for discrete entity state, maps that history into a time-varying value:

```txt
behavior(t) = interpolate(t, state history)
```

Behavior connects state and events:

- [[Event|Events]] can be folded, integrated, scanned, switched, or transformed by an observer to produce behavior.
- Behavior can be sampled, compared, or observed for changes that emit events.
- Folding committed events produces state samples.
- Comparing or observing state samples can produce events.

In FRP, switching changes which behavior is currently followed. In event-sourced models, this appears when an endogenous event changes the active lifecycle mode, process behavior, projection rule, routing policy, or interpreter for future events. The event does not only update a value; it can change the rule that will produce or interpret later values.

[[Event-State Duality]] does not imply that event schedules and state histories are isomorphic. They are dual views of behavior whose transformations are model-dependent and often lossy.

## External References

- Conal Elliott and Paul Hudak, [Functional Reactive Animation](https://dl.acm.org/doi/10.1145/258948.258973), Proceedings of the Second ACM SIGPLAN International Conference on Functional Programming, ICFP '97, pages 263-273, 1997. Author copy: [conal.net/papers/icfp97](https://conal.net/papers/icfp97/).

Related concepts: [[Value|value]], [[State|state]], [[Observation|observation]], [[Event|event]], [[Event-State Duality|event-state duality]], [[Algebras and Coalgebras|algebras and coalgebras]], [[Fixed Points and Recursion|fixed points and recursion]], [[Trace and Feedback|trace and feedback]], [[Entity|entity]], [[Version|version]], [[Flows|flow]].
