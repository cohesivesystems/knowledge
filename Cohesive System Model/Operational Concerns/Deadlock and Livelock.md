---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-28
updated: 2026-07-28
status: draft
aliases:
  - Deadlock
  - Livelock
  - Deadlock Freedom
  - Livelock Freedom
---

# Deadlock and Livelock

Deadlock and livelock are failures of [[Safety and Liveness|liveness]] in which enabled or accepted work does not reach its declared completion boundary.

The distinction is about the shape of the non-progressing execution. In deadlock, participants cannot take the steps required for progress because they are waiting on conditions that the blocked configuration cannot produce. In livelock, participants continue taking steps, but those steps repeatedly interfere, restart, reverse, or avoid commitment without producing the required useful outcome.

Both notions are boundary-relative. A runtime may schedule threads, a broker may deliver messages, or a protocol may change local state while an end-to-end [[Process|process]] remains stuck. Activity is not evidence of useful progress unless it advances the obligation named by the liveness claim.

## Deadlock

A deadlock is a persistent configuration in which a set of participants or operations waits for conditions that can be satisfied only by members of the same blocked dependency structure. Deadlock may affect the whole system or only one connected subset.

A wait-for graph makes a common resource deadlock visible: an edge from participant $A$ to participant $B$ means that $A$ waits for a resource, message, permit, or transition controlled by $B$. A cycle is direct evidence of deadlock under the relevant exclusivity and non-preemption assumptions. More general message-passing, workflow, or distributed deadlocks may also involve missing producers, orphaned obligations, exhausted credits, incompatible protocol states, or barriers whose membership can no longer arrive, so not every useful model reduces to a simple lock cycle.

Classic resource deadlock depends on four jointly necessary conditions within its model:

- Mutual exclusion over some resource.
- Holding one resource while waiting for another.
- No preemption of held resources.
- Circular wait among participants.

Prevention can rule out at least one condition through global resource ordering, atomic acquisition, preemption or cancellation, bounded ownership, or avoiding exclusive resources. Detection and recovery may instead identify a wait cycle or stuck protocol, select a victim, release or fence its resources, roll back work, or restore a participant capable of discharging the wait.

## Distributed Deadlock Detection

In a distributed system, no observer necessarily sees the complete wait-for relation at one moment. Lock ownership, in-flight messages, leases, process positions, and dependency edges may be observed at different times. Combining individually valid but causally incompatible observations can produce a **phantom deadlock**: an apparent cycle that never existed in any coherent global state.

Distributed detection must therefore state which [[Consistent Cuts|consistent cut]], probe epoch, dependency query, or snapshot its conclusion describes. It must account for waits that ended while evidence was in flight, messages that can still discharge a wait, and ownership that moved to a new epoch. A reported cycle may need revalidation or stabilization before the system aborts work or revokes authority.

Failure detection introduces a separate ambiguity. A silent participant may be blocked, slow, paused, partitioned, crashed, or already complete with an unobserved result. Declaring it dead changes the dependency graph but does not prove that its former actions have stopped. Leases and fencing can bound authority only when expiry assumptions hold and the receiving boundary rejects stale owners.

Distributed detection is therefore an observation and recovery protocol, not only a graph algorithm. It needs correlation, causality, identity, timeout, authority, and victim-selection rules, plus durable evidence of any abort or ownership change used to restore progress.

## Livelock

A livelock is an execution in which relevant participants continue to take steps but the declared useful outcome never occurs.

Examples include:

- Two conflict handlers repeatedly yielding or rolling back in response to one another.
- Optimistic transactions repeatedly failing validation and retrying without any attempt committing.
- Participants continually releasing and reacquiring resources in ways that recreate the same conflict.
- Repeated leader elections, view changes, or failure-detector reactions that prevent useful decisions.
- A workflow repeatedly compensating and re-entering the same path without reaching a terminal disposition.
- Requests continually timing out and retrying while useful throughput remains zero.

Livelock prevention usually requires progress structure rather than mere activity: asymmetric priority, monotone epochs, randomized or coordinated backoff, bounded retry, fair scheduling, an arbiter, contention management, or a rule that makes some participant's successful step irreversible. Detection should measure useful commits, departures, or terminal dispositions separately from attempts, state changes, messages, retries, and CPU utilization.

## Starvation, Fairness, and Priority Inversion

Starvation occurs when one eligible participant or operation is denied progress indefinitely while other work continues to complete. Unlike deadlock, the system as a whole can progress; unlike livelock, the starved participant need not keep taking steps.

[[Fairness]] states which starvation-like executions are excluded. Weak fairness can require an action that remains continuously enabled to occur eventually, while strong fairness can protect an action enabled infinitely often. Neither form necessarily gives a finite response-time bound, and fairness at one scheduler, broker, or runtime boundary does not automatically propagate to an end-to-end process.

**Priority inversion** occurs when higher-priority work waits directly or indirectly for lower-priority work. If unrelated medium-priority work repeatedly preempts the lower-priority owner, the higher-priority waiter can be delayed far beyond the lower-priority critical section. Priority inheritance and priority-ceiling protocols can bound or reduce this inversion within their scheduling and resource model, but they do not eliminate arbitrary protocol, workflow, or distributed deadlocks.

Starvation prevention and priority control must identify eligibility, priority scope, resource ownership, preemption rules, and the layer responsible for enforcement. Static priority alone can create starvation; dynamic aging, fair queues, inheritance, ceilings, quotas, or explicit [[Arbitration|arbitration]] may be needed.

## Flow-Control and Workflow Deadlocks

Deadlock can arise from capacity and process structure without an ordinary mutex:

- In a cycle of bounded channels, each participant may wait to emit into a full downstream channel while refusing or being unable to consume the item that would release its own upstream capacity.
- Credit-based flow may stop when every participant waits for an acknowledgment, permit, or cursor advance whose production itself requires another exhausted credit.
- A broker or queue may decouple producer and consumer time while still participating in a larger cyclic wait once its finite capacity or in-flight bound is exhausted.
- A workflow join may wait for a branch that was skipped, cancelled, expired, or never enabled, while the process lacks a rule that removes that branch from the join's completion set.
- An aggregation or scatter-gather step may wait forever when correlation cardinality, missing-part, timeout, or terminal failure semantics are undefined.

[[Flow Control|Flow control]] should therefore model cycles across adjacent capacity loops, not only the safety of each local buffer. Adding a queue can move a wait or enlarge the amount of work admitted before deadlock becomes visible; it does not prove global progress.

For [[Process Graphs|process graphs]], deadlock freedom depends on branch enabling, token movement, join mode, waits, cancellation regions, and terminal outcomes. Petri-net and workflow-net analysis supplies reachability, boundedness, liveness, and soundness techniques for detecting structural deadlocks, livelocks, unreachable work, and improper completion. Those structural results remain relative to the modeled process and do not automatically cover failed external participants, lost messages, runtime resource exhaustion, or incorrect realization.

## Typing out Deadlock

Some deadlocks can be eliminated statically by a typing discipline. Session types describe the permitted communication sequence over a channel: which participant sends or receives, which payload or branch is valid, and which continuation follows. Multiparty session types can describe a global protocol and project compatible local roles for its participants.

A sufficiently strong session-type or behavioral-type system can reject programs whose communication dependencies admit a stuck configuration. Depending on the calculus, the proof may arise from global protocol progress, linear-logic structure, usage or priority types, acyclic channel dependencies, or restrictions on how sessions are shared and composed. For well-typed closed processes under the type system's operational assumptions, deadlock freedom can therefore be a theorem rather than a runtime recovery policy.

The guarantee belongs to the specific typing discipline, not to the phrase *session types* in general. Basic session fidelity can prove that the two endpoints agree on message order and shape without ruling out every deadlock created by interleaving several individually well-typed sessions. Shared resources, dynamic participants, external services, message loss, crashes, unfair scheduling, unrestricted recursion, and calls outside the typed boundary also remain outside a theorem unless the formal model includes them.

The claim must state:

- Which processes, roles, channels, and resources are inside the typed boundary.
- Whether communication is synchronous or asynchronous and which delivery assumptions apply.
- Whether the theorem guarantees communication safety, protocol fidelity, local progress, global progress, lock freedom, or deadlock freedom.
- Which fairness, termination, failure, and environmental assumptions are required.
- Whether compilation and the runtime preserve the typed communication and progress structure.

Deadlock freedom also does not imply livelock freedom. A process may always have another valid reduction while following its session protocol forever without reaching the completion required by an application-level process. Excluding that behavior needs an appropriate termination, productivity, lock-freedom, fairness, or protocol-level progress property.

## Timeouts, Cancellation, and Recovery Safety

A timeout is evidence that a declared interval elapsed without the expected observation. It does not prove deadlock, failure, or absence of commitment. A timeout can let one participant stop waiting, but repeated timeout, rollback, and reacquisition may transform a blocking wait into livelock, starvation, retry amplification, or [[Metastability|metastability]].

Cancellation must state which obligation changes:

- The requester no longer needs the result.
- No new attempt should begin.
- An in-flight attempt should cooperatively stop at a safe point.
- A process branch should no longer count toward a join.
- A completed or late result should be ignored, reconciled, or compensated.

These meanings are not interchangeable. Cancellation cannot erase an already committed [[Effect|effect]], and loss of interest by one participant does not automatically revoke another participant's authority. A late completion may still need acknowledgment, deduplication, compensation, or a terminal record so that it does not leave an orphaned wait elsewhere.

Recovery that breaks a deadlock must preserve safety while restoring progress. Victim selection, rollback, lease expiry, fencing, lock release, process repair, or operator intervention should identify the affected commit and authority boundaries. Releasing a local resource while an old owner can still commit externally may replace deadlock with duplicate effects or split authority. A fence is effective only when the target validates it; a rollback is effective only within the boundary that can still reverse or compensate the work.

## Distinctions

| Concept | Shape of the execution | Governing question |
| --- | --- | --- |
| **deadlock** | Required steps are permanently disabled by unresolved waits. | Can the blocked configuration itself enable any step that discharges the wait? |
| **livelock** | Steps continue, but no required useful outcome completes. | Does activity advance the declared obligation? |
| **starvation** | Other work may complete while one eligible participant is perpetually denied progress. | Which participant is not progressing? |
| **blocking** | Progress depends on another participant and may still resume. | Is the wait necessarily permanent under the stated assumptions? |
| **[[Metastability|metastability]]** | A history-dependent degraded regime is sustained after its trigger disappears. | What feedback preserves the degraded regime, and what crosses the recovery barrier? |

The concepts can overlap without becoming synonymous. A retry storm can be both metastable and livelocked when retry feedback sustains overload while no request completes. A lock cycle can be deadlocked without metastability because a permanently unsatisfied wait does not by itself constitute a feedback-amplified operating regime.

## Modeling Requirements

For any deadlock- or livelock-freedom claim, identify:

- The participant and resource boundary.
- The useful completion, commit, departure, or terminal disposition whose absence constitutes non-progress.
- The waits, enabling conditions, resource ownership, protocol states, and responsibility transfers.
- Whether distributed dependency evidence belongs to one consistent cut or requires revalidation before recovery acts.
- Whether delayed, failed, partitioned, cancelled, or crashed participants remain part of the progress assumption.
- The [[Scheduling|scheduling]], [[Fairness|fairness]], priority, retry, timeout, and recovery assumptions.
- The cancellation meaning, late-result disposition, and safety boundary for releasing, fencing, rolling back, or compensating work.
- The scope and assumptions of any type-system, protocol-progress, workflow-soundness, or other static exclusion proof.
- The evidence used to distinguish slow progress from permanent deadlock, livelock, or starvation.
- The prevention, detection, victim selection, rollback, fencing, or external [[Operational Control|operational control]] action used to restore progress.

## External References

- Edward G. Coffman Jr., M. J. Elphick, and Arie Shoshani, [System Deadlocks](https://doi.org/10.1145/356586.356588), *ACM Computing Surveys* 3(2):67–78, 1971.
- K. Mani Chandy, Jayadev Misra, and Laura M. Haas, [Distributed Deadlock Detection](https://doi.org/10.1145/357360.357365), *ACM Transactions on Computer Systems* 1(2):144–156, 1983.
- Lui Sha, Ragunathan Rajkumar, and John P. Lehoczky, [Priority Inheritance Protocols: An Approach to Real-Time Synchronization](https://doi.org/10.1109/12.57058), *IEEE Transactions on Computers* 39(9):1175–1185, 1990.
- Kohei Honda, Nobuko Yoshida, and Marco Carbone, [Multiparty Asynchronous Session Types](https://doi.org/10.1145/2827695), *Journal of the ACM* 63(1), Article 9, 2016.
- Ornela Dardha and Jorge A. Pérez, [Comparing Type Systems for Deadlock Freedom](https://doi.org/10.1016/j.jlamp.2021.100717), *Journal of Logical and Algebraic Methods in Programming* 124:100717, 2022.
- Wil M. P. van der Aalst, Kees M. van Hee, Arthur H. M. ter Hofstede, Natalia Sidorova, H. M. W. Verbeek, Marc Voorhoeve, and Moe Thandar Wynn, [Soundness of Workflow Nets: Classification, Decidability, and Analysis](https://doi.org/10.1007/s00165-010-0161-4), *Formal Aspects of Computing* 23:333–363, 2011.

Related concepts: [[Safety and Liveness|safety and liveness]], [[Progress Conditions|progress conditions]], [[Process Theories|process theories]], [[Interaction|interaction]], [[Interaction Protocols|interaction protocols]], [[Coordination|coordination]], [[Concurrency Control|concurrency control]], [[Scheduling|scheduling]], [[Fairness|fairness]], [[Arbitration|arbitration]], [[Retry|retry]], [[Flow Control|flow control]], [[Trace and Feedback|trace and feedback]], [[Metastability|metastability]], [[Consistent Cuts|consistent cuts]], [[Causality|causality]], [[Uncertainty|uncertainty]], [[Authority|authority]], [[Effects|effects]], [[Commit Boundaries|commit boundaries]], [[Recovery|recovery]], [[Operational Control|operational control]], [[Process|process]], [[Process Graphs|process graphs]], [[Workflow Patterns|workflow patterns]], [[Flow Operators|flow operators]], [[Interaction Channels|interaction channels]], [[Runtimes|runtimes]], [[Workflow Engines|workflow engines]], [[Actor Systems|actor systems]].
