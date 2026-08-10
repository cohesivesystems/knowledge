---
realm: Principles
kind: principle
created: 2026-06-30
updated: 2026-08-03
aliases:
  - State Machine
  - Transition System
  - Labelled Transition System
  - Labeled Transition System
  - Moore Machine
  - Mealy Machine
  - Finite State Transducer
---

# State Machines

State machines are a modeling principle for [[Behavior|behavior]] described by current [[State|state]], admissible [[Transition|transitions]], inputs, and outputs.

A common input-output step form is:

$$
\operatorname{step}\colon \mathsf{Input} \times \mathsf{State}
\longrightarrow \mathsf{Output} \times \mathsf{State}
$$

This form makes explicit that an input is interpreted relative to current state, producing both an output and a next state. The output may be empty, observational, or effectful depending on the model boundary.

A deterministic machine assigns at most one next outcome to a state and input. A nondeterministic transition system admits a set of successors. [[Nondeterminism and Choice]] asks where that multiplicity comes from and how it is resolved; [[Scheduling]] selects enabled execution steps; [[Reduction, Evaluation, and Confluence|confluence]] asks whether different paths can later join or remain observationally equivalent.

State-machine thinking is not tied to functional programming, imperative programming, object orientation, actors, workflows, databases, or distributed protocols. The same transition structure may be expressed as a pure reducer, a method on a mutable object, an actor turn, a database transaction, a workflow step, an event-sourced aggregate, or a replicated log application. Those are realization choices over the same underlying behavioral shape.

## Common Forms

Labeled transition systems describe states connected by labeled transitions:

$$
s \xrightarrow{\mathrm{label}} s'
$$

The labels may represent inputs, events, actions, commands, observations, or protocol messages. A labeled transition system may be nondeterministic: a state and label can admit multiple possible successor states.

Moore machines separate transition from output:

$$
\begin{aligned}
\operatorname{transition}&\colon \mathsf{Input} \times \mathsf{State}
  \longrightarrow \mathsf{State}, \\
\operatorname{output}&\colon \mathsf{State}
  \longrightarrow \mathsf{Output}.
\end{aligned}
$$

The observable output depends on the resulting state, not directly on the input that produced it.

Mealy machines make output part of the transition step:

$$
\operatorname{step}\colon \mathsf{Input} \times \mathsf{State}
\longrightarrow \mathsf{Output} \times \mathsf{State}
$$

The output depends on both the input and the current state.

Finite state transducers are state machines with finite state sets and input/output alphabets. They translate input strings, traces, or event sequences into output strings, traces, or event sequences while moving through finite control states.

These forms are useful reference points, but Cohesive does not require every state machine to be finite, deterministic, total, or sequential. Version histories, distributed executions, workflows, CRDT replicas, and processes may need partial orders, branching histories, merge transitions, unavailable transitions, or observer-relative projections.

## Automata and State Machines

Automata theory gives a formal account of machines that consume symbols and recognize languages or produce output. A deterministic finite automaton is commonly written as:

$$
A=(Q,\Sigma,\delta,q_0,F),
\qquad
\delta\colon Q\times\Sigma\longrightarrow Q
$$

Here $Q$ is a finite state set, $\Sigma$ is an input alphabet, $q_0$ is the initial state, and $F$ is the set of accepting states. Extending $\delta$ from symbols to words gives:

$$
w\in L(A)
\quad\Longleftrightarrow\quad
\delta^{*}(q_0,w)\in F
$$

A nondeterministic automaton instead admits a set of successors:

$$
\delta\colon Q\times\Sigma\longrightarrow\mathcal{P}(Q)
$$

Finite-state transducers add output, while general state-machine models may use infinite state, typed inputs, guards, observations, effects, and partial transition functions. Automata therefore provide a precise mathematical foundation for state-machine behavior without making every domain entity, process, protocol, or runtime machine a language recognizer.

## Composition and Correspondence

State machines compose when the output of one machine is bound to an input of another. For machines $M_i=(S_i,I_i,O_i,\delta_i)$ and $M_j=(S_j,I_j,O_j,\delta_j)$, an output-to-input binding can be written as a partial map:

$$
b_{ij}\colon O_i\rightharpoonup I_j
$$

One composed step then has the form:

$$
\delta_i(x_i,s_i)=(o_i,s_i'),
\qquad
x_j=b_{ij}(o_i),
\qquad
\delta_j(x_j,s_j)=(o_j,s_j')
$$

The binding establishes correspondence, not identity. The emitting machine's output, the carried [[Interaction|interaction]], the receiving machine's input, and the receiving transition remain distinct roles and occurrences. The composition may be [[Synchrony and Asynchrony|synchronous or asynchronous]]. A synchronous interaction can coordinate the steps or make one participant wait, but it creates one transition or commit boundary only when the model declares a shared boundary. In asynchronous composition, emission, transport or admission, receipt, and the receiving transition progress as separate occurrences under explicit delivery, ordering, and recovery rules.

A process machine can coordinate one or more entity machines. Its state records process position, pending work, replies, timeouts, and recovery progress; each entity machine retains authority over its own state and transitions. The process machine may retain observer-relative snapshots or projections of entity state, but those copies do not transfer semantic authority from the entity machine. It issues commands or requests and consumes resulting events or observations through the entities' declared transition boundaries.

Participant machines can likewise correspond across organizational boundaries. In logistics, a shipper machine and a carrier machine may interact as follows:

$$
\begin{aligned}
\mathsf{Shipper}\colon\quad
&\mathsf{Planned}
\xrightarrow{\operatorname{emit}(\mathsf{Tender})}
\mathsf{Tendered}
\xrightarrow{\operatorname{receive}(\mathsf{Accepted})}
\mathsf{Assigned}, \\
\mathsf{Carrier}\colon\quad
&\mathsf{Available}
\xrightarrow{\operatorname{receive}(\mathsf{Tender})\,/\,\operatorname{emit}(\mathsf{Accepted})}
\mathsf{Assigned}.
\end{aligned}
$$

The two `Assigned` states are observer-relative states in different authority boundaries. Their correspondence is established by an [[Interaction Protocols|interaction protocol]], correlation, and evidence about the tender and acceptance; equal labels do not make them one state or one atomic transition.

## Finite-State Coherence and Enabled Transitions

For a sequential finite-state machine, let $a_q$ indicate whether state $q$ is active. A coherent configuration has exactly one active state:

$$
a_q\in\{0,1\},
\qquad
\sum_{q\in Q}a_q=1
$$

Let a transition $t$ have source $\operatorname{src}(t)$, input label $\operatorname{in}(t)$, guard $g_t$, output $\operatorname{out}(t)$, and target $\operatorname{dst}(t)$. It is enabled for input $x$ and observation context $c$ exactly when its source is active, its input matches, and its guard holds:

$$
\operatorname{enabled}(t,x,c)
\quad\Longleftrightarrow\quad
a_{\operatorname{src}(t)}=1
\;\land\;
\operatorname{in}(t)=x
\;\land\;
g_t(c)
$$

States are active or inactive; transitions are enabled or disabled. An enabled transition becomes the firing transition only after deterministic selection or explicit [[Nondeterminism and Choice|choice]] and [[Arbitration|arbitration]]. A coherent committed step deactivates the source, activates the selected target, and emits only the output attached to that selected transition.

For example:

$$
\mathsf{Draft}\xrightarrow{\mathsf{submit}}\mathsf{Submitted},
\qquad
\mathsf{Submitted}\xrightarrow{\mathsf{approve}}\mathsf{Approved},
\qquad
\mathsf{Submitted}\xrightarrow{\mathsf{reject}}\mathsf{Rejected}
$$

When $\mathsf{Submitted}$ is active, the `submit` transition is disabled because its source is inactive. The `approve` and `reject` transitions are structurally eligible; the current input and guards determine which are enabled. If `approve` is selected and committed, the next configuration satisfies:

$$
a'_{\mathsf{Approved}}=1,
\qquad
a'_q=0\quad\text{for every }q\neq\mathsf{Approved}
$$

Concurrent or hierarchical machines replace the single global one-hot condition with one coherent active configuration per exclusive region. Their product state records the active tuple, while synchronization constraints determine which regional transitions may fire together.

## Event Concurrency and Sequential State

State-machine notation usually presents one transition after another, but sequentiality is a property of the selected history shape rather than an unconditional part of the definition. Concurrent or distributed events may lack an established [[Happened-Before|happened-before]] order:

$$
e_1 \parallel e_2
\quad\Longleftrightarrow\quad
\neg(e_1\prec e_2)\;\land\;\neg(e_2\prec e_1)
$$

For an entity whose authoritative state history must remain linear, those concurrent inputs cannot both advance the same current version independently. [[Concurrency Control|Concurrency control]] must select or validate an admissible order $\pi$ before the inputs are committed as a sequential state history:

$$
s_{k+1}=\delta\!\left(e_{\pi(k)},s_k\right)
$$

$$
s_0
\xrightarrow{e_{\pi(1)}}s_1
\xrightarrow{e_{\pi(2)}}s_2
\xrightarrow{e_{\pi(3)}}\cdots
$$

This is one operational consequence of [[Event-State Duality|event-state duality]]. Events emphasize occurrence, causality, and potentially concurrent schedules; state samples emphasize the condition established at selected cuts. Folding events into one linear state history requires an ordering and admission rule. The resulting state sequence does not prove that the input events occurred sequentially before they reached the authority boundary, nor does it preserve every distinction in their original partial order.

Common serialization mechanisms establish different guarantees.

**Actor serialization.** The [[Actor Model|actor model]] makes serialized interpretation the default at one actor boundary. Concurrent sends remain unordered until mailbox delivery, arbitration, and scheduling select a reception order. Once selected, one mailbox turn typically interprets and commits one step of the actor's internal sequential state machine. This proves per-actor serialization only when the actor owns the relevant entity transition boundary.

**Expected-version or ETag checks.** Optimistic concurrency admits a transition computed from version $v$ only if $v$ is still current:

$$
\operatorname{commit}(s_v\to s_{v+1})
\quad\Longleftrightarrow\quad
\operatorname{currentVersion}=v
$$

A stale attempt is rejected and may be recomputed from a newer observation. The version check prevents two successors from committing from the same current version, but it does not itself make retries idempotent. When a client cannot know whether an earlier attempt committed, or when retry can repeat an external effect, a stable command or event identity and an explicit [[Idempotency|idempotency]] rule are also required.

**Distributed locks and leases.** A distributed lock or lease can serialize access when exclusive ownership remains valid through commit. In a distributed system, a fencing token or equivalent monotone ownership epoch is needed so the commit boundary can reject a delayed former holder after its lease expires. A lock changes access and progress behavior; it does not by itself establish semantic [[Authority|authority]] or make emitted effects atomic with the protected state.

Actor serialization, optimistic version checks, and locks can all realize a sequential entity machine, but they make different assumptions about ownership, failure, retry, scheduling, and [[Progress Conditions|progress]]. The model should state which boundary becomes sequential and which event relationships remain concurrent outside it.

## Cohesive Interpretation

In Cohesive terms, state machines relate:

- [[State|state]] as the condition being advanced.
- [[Transition|transitions]] as admissible movement between states.
- [[Command|commands]], [[Event|events]], observations, signals, or messages as inputs.
- Endogenous events, observations, acknowledgments, emitted [[Effect|effects]], or nil as outputs.
- [[Behavior|behavior]] as the resulting run, trace, or state history.

An [[Entity|entity]] can be modeled as a state machine when commands are interpreted against current entity state and committed as controlled transitions. A [[Process|process]] can be modeled as a state machine when its state records phase, pending work, timeouts, decisions, and emitted effects. A projection can be modeled as a state machine when source events are folded into derived observation state.

Cohesive provides multiple implementation paths by composing operational concerns:

- [[Reconstitution|Reconstitution]] recovers the state or observation needed to interpret the next input.
- [[Persistence|Persistence]] chooses which state, history, checkpoints, events, or effect records become durable truth.
- Execution serialization, [[Ordering|ordering]], and [[Concurrency Control|concurrency control]] determine which attempted transitions may be interpreted and committed together or one at a time.
- [[Effect Models|Effect models]] and [[Commit Boundaries|commit boundaries]] define which outputs are accepted, persisted, published, retried, acknowledged, or compensated.

This composition keeps the state-machine model separate from the mechanism that realizes it. A single behavioral model can be realized through current-state storage, event sourcing, actor identity serialization, workflow histories, replicated logs, CRDT merge rules, or database transactions when the chosen mechanisms preserve the required transition semantics.

## Sheaf View

[[Systems Sheaf Semantics|Systems sheaf semantics]] provides a way to examine state-machine behavior across observers, boundaries, cuts, and projections. A run, trace, state history, enabled-transition set, or output history can be treated as a section over a context.

Restriction maps can hide labels, select a time interval, project to one [[Observer|observer]], reduce state shape, or expose only a read model. Compatibility asks whether partial views of the machine agree where they overlap. Gluing and descent ask whether compatible local runs determine a coherent larger behavior.

This is especially useful when the state machine is distributed, observer-relative, partially observed, or non-sequential. The question is not only "what is the next state?" but also "which local state-machine views are compatible, and what global behavior do they determine, if any?"

Related concepts: [[State|state]], [[Transition|transition]], [[Behavior|behavior]], [[Event|event]], [[Command|command]], [[Observation|observation]], [[Observer|observer]], [[Entity|entity]], [[Process|process]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Reduction, Evaluation, and Confluence|reduction, evaluation, and confluence]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Reconstitution|reconstitution]], [[Persistence|persistence]], [[Effect Models|effects]], [[Ordering|ordering]], [[Concurrency Control|concurrency control]], [[Event-State Duality|event-state duality]], [[Algebras and Coalgebras|algebras and coalgebras]], [[Trace and Feedback|trace and feedback]], [[Systems Sheaf Semantics|systems sheaf semantics]], [[Sheaves and Gluing|sheaves and gluing]].
