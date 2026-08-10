---
realm: Principles
kind: discipline
created: 2026-08-06
updated: 2026-08-06
status: draft
aliases:
  - Session Type
  - Binary Session Types
  - Multiparty Session Types
---

# Session Types

Session types are behavioral types for structured communication. They describe how a participant may use a channel or protocol endpoint over the course of a conversation: which values or labels it sends and receives, which choices it makes or offers, how the interaction recurs, and when it completes.

A session type classifies communication behavior rather than merely the shape of one message. It is a discipline within [[Type Theory|type theory]], often informed by [[Linear Logic|linear logic]], and is commonly defined over a typed [[Process Calculi|process calculus]], especially variants of the π-calculus.

## Basic Structure

A representative binary session-type language includes:

$$
S ::= {!A.S}
\mid {?A.S}
\mid \oplus\{\ell_i:S_i\}_{i\in I}
\mid \mathbin{\&}\{\ell_i:S_i\}_{i\in I}
\mid \mu t.S
\mid t
\mid \mathsf{end}
$$

Under one common endpoint convention:

- $!A.S$ sends a value of type $A$, then continues as $S$.
- $?A.S$ receives a value of type $A$, then continues as $S$.
- $\oplus\{\ell_i:S_i\}$ internally selects and sends one label $\ell_i$.
- $\mathbin{\&}\{\ell_i:S_i\}$ externally offers branches and receives the peer's selected label.
- $\mu t.S$ and $t$ describe recursive protocol behavior.
- $\mathsf{end}$ marks completed use of the endpoint.

Notation and polarity conventions vary. Some systems describe a provider rather than a local endpoint, reverse send and receive symbols, distinguish input and output channel names, or use [[Linear Logic|linear propositions]] directly. The governing typing rules, not the typography alone, determine the protocol meaning.

## Duality and Linearity

For a binary session, the two endpoints have dual behavior. Sending is dual to receiving, internal selection is dual to external branching, and termination is dual to compatible termination:

$$
\begin{aligned}
\overline{!A.S} &= ?A.\overline{S}, \\
\overline{?A.S} &= !A.\overline{S}, \\
\overline{\oplus\{\ell_i:S_i\}} &= \mathbin{\&}\{\ell_i:\overline{S_i}\}, \\
\overline{\mathsf{end}} &= \mathsf{end}.
\end{aligned}
$$

Duality establishes protocol compatibility only within the selected calculus and typing context. Payload types, label sets, subtyping, recursion, delegation, cancellation, exceptions, and asynchronous buffering can require more than a simple syntactic dual.

Many session systems use [[Linear Logic|linear or affine typing]] so that an endpoint has one coherent owner and each protocol action advances its type according to one controlled use path. Linearity prevents accidental aliasing, duplicate use, or abandonment according to the system's rules; affine systems permit an endpoint to be discarded but not duplicated. Shared or replicated services require an explicit unrestricted, exponential, acquisition, or service discipline rather than silently duplicating a linear session endpoint.

## Binary and Multiparty Sessions

Binary session types describe two endpoint views. Multiparty session types begin with a global protocol over several named participant roles and project that protocol into local types for each participant.

A valid projection must preserve who sends, who receives, which participant chooses a branch, and what uninvolved participants must know to continue coherently. Not every global-looking interaction graph is projectable. Choice awareness, mergeability of local branches, causal consistency, recursion, and asynchronous communication impose well-formedness conditions.

Global and local types are related projections, not identical descriptions. The global type states a choreography-level protocol; a local type states what one participant must send, receive, select, or offer. Runtime endpoints and messages then realize those local roles at particular [[Boundaries|boundaries]].

## Typing Judgements and Guarantees

A process typing [[Judgement|judgement]] may have a form such as:

$$
\Gamma;\Delta \vdash P :: x:S
$$

It asserts, under shared context $\Gamma$ and linear session context $\Delta$, that process $P$ provides or uses endpoint $x$ according to session type $S$. Exact judgement forms differ among systems.

Common metatheoretic results include:

- **Subject reduction:** an operational communication step preserves typing while advancing endpoint types coherently.
- **Communication safety:** a well-typed endpoint does not send a payload or label where its peer expects an incompatible action.
- **Session fidelity:** observed protocol actions follow the sequence described by the session type.
- **Linearity or ownership safety:** endpoints are used according to the calculus's duplication and disposal rules.

Progress, lock freedom, deadlock freedom, orphan-message freedom, eventual reception, and global completion are stronger properties. Some session systems prove selected forms through global typing, logical foundations, priorities, dependency analyses, or restrictions on process composition. A bare claim that code “uses session types” does not establish all of them.

The proof boundary must include the actual operational semantics. Asynchronous queues, delegation, cancellation, crashes, reconnects, partial failure, and mixed typed-untyped components can change which guarantees survive.

## Propositions as Sessions

Session types extend the [[Curry–Howard Correspondence|Curry–Howard correspondence]] from values and functions toward communication. In propositions-as-sessions interpretations based on [[Linear Logic|linear logic]]:

- Linear propositions correspond to session protocols.
- Proofs correspond to communicating processes.
- Cut corresponds to composing two processes along a fresh private channel.
- Logical duality corresponds to compatible provider and client behavior.
- Cut elimination corresponds to communication or process reduction.

This account makes protocol structure proof relevant. A session-typed process can be evidence that it implements one endpoint of a proposition-shaped protocol. The correspondence belongs to a particular logical process calculus; it does not make every API schema, network connection, or workflow a proof.

The [[Linear Logic|logical exponential]] is often associated with shared or repeatable service use, while linear propositions describe single-use session structure. Its connection to π-calculus replication and runtime service populations is mediated by typing and operational rules. The symbols may resemble one another without denoting the same realization mechanism.

## Interaction Protocols and Process Graphs

Session types provide a formal account of part of an [[Interaction Protocols|interaction protocol]]: legal communication traces at participant endpoints. They can specify message direction, payload type, label choice, recursion, delegation, and termination.

A full Cohesive interaction protocol may also carry semantic obligations that a session type does not automatically express: authority, correlation, commitment, acknowledgment meaning, idempotency, delivery, timeout, cancellation, compensation, retention, recovery, compatibility, and business completion.

Likewise, a [[Process Graphs|process graph]] may span several sessions, include human or physical activity, coordinate durable cuts, and carry domain effects or recovery policy. A session is one protocol scope within that larger process unless the model explicitly identifies their boundaries.

## Realization Boundary

Session types can be realized through compile-time checking, generated endpoint APIs, protocol monitors, typestate objects, linear capabilities, channel libraries, actor protocols, RPC frameworks, or runtime state machines. These mechanisms differ in what they check and when.

A source-level type checker cannot by itself establish that:

- An untyped or independently deployed peer follows the dual protocol.
- The network or broker supplies delivery, ordering, durability, or bounded buffering.
- A crash-recovery path restores the same session state and endpoint ownership.
- A timeout, retry, or reconnect preserves linear use and message identity.
- Payload schemas retain semantic compatibility across deployed versions.
- The conversation's domain effects commit atomically with protocol advancement.

Compiler-like [[Realization|realization]] therefore needs traceability from semantic interactions and system-graph roles to session types, from types to generated or checked endpoints, and from endpoints to runtime channels and recovery material. Dynamic monitoring can detect selected violations but does not retroactively provide static proof or prevent all invalid effects.

## Modeling Checks

- Is the session binary or multiparty, and what are the participant roles?
- Which endpoint convention, polarity, and duality rules are used?
- Who owns each choice, and how do other participants learn the selected branch?
- Are endpoints linear, affine, shared, delegated, replicated, or recoverable?
- Which guarantees follow from the actual typing theorem, and which are operational assumptions?
- How do asynchronous queues, cancellation, timeout, failure, and recovery affect session state?
- Does the session describe one channel, one conversation, or one portion of a larger semantic process?
- Which semantic obligations remain outside the session type?

## External References

- Kohei Honda, Vasco T. Vasconcelos, and Makoto Kubo, [Language Primitives and Type Discipline for Structured Communication-Based Programming](https://doi.org/10.1007/BFb0053567), ESOP 1998, LNCS 1381:122-138.
- Luís Caires and Frank Pfenning, [Session Types as Intuitionistic Linear Propositions](https://doi.org/10.1007/978-3-642-15375-4_16), CONCUR 2010, LNCS 6269:222-236.
- Philip Wadler, [Propositions as Sessions](https://doi.org/10.1145/2364527.2364568), ICFP 2012:273-286.
- Kohei Honda, Nobuko Yoshida, and Marco Carbone, [Multiparty Asynchronous Session Types](https://doi.org/10.1145/1328438.1328472), POPL 2008:273-284.

Related concepts: [[Type Theory|type theory]], [[Linear Logic|linear logic]], [[Process Calculi|process calculi]], [[Interaction Protocols|interaction protocols]], [[Interfaces|interfaces]], [[Interaction|interaction]], [[Process|process]], [[Process Graphs|process graphs]], [[Concurrency|concurrency]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Duality and Symmetry|duality and symmetry]], [[Safety and Liveness|safety and liveness]], [[Deadlock and Livelock|deadlock and livelock]], [[Delivery Semantics|delivery semantics]], [[Ordering|ordering]], [[Recovery|recovery]], [[Compatibility and Evolution|compatibility and evolution]], [[Realization|realization]].

## Formal relations

- `refines`: [[Type Theory]] — Extends typing from value and function structure to ordered communication behavior at protocol endpoints.
- `constrains`: [[Interaction Protocols]] — Restricts legal participant-local communication traces while leaving domain meaning and unencoded operational obligations explicit.
