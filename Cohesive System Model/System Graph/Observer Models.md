---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-08-23
aliases:
  - Observer Placement
  - Observer Placements
---

# Observer Models

Observer models describe how semantic [[Observer|observers]] are placed in the system graph.

At the structure level, an observer model defines placement, responsibility, logical execution context, and boundary participation for observation, interpretation, routing, hosting, projection, and event participation. This page describes structural use of the observer role, not the primitive definition of observer and not a specific runtime implementation.

Observer models may correspond to actors, services, request handlers, workflow activities, projection workers, process coordinators, entity command handlers, brokers, clients, schedulers, fibers, tasks, or infrastructure participants. Concrete mechanisms such as actor systems, HTTP pipelines, workflow engines, brokers, green-thread schedulers, or OS threads belong to substrate concerns such as [[Actor Systems|actor systems]], [[Application Hosts|application hosts]], [[Workflow Engines|workflow engines]], [[Brokers|brokers]], and [[Runtimes|runtimes]].

The same structural observer may be realized by different substrate contexts over time when the runtime preserves the logical execution context. Conversely, a single substrate mechanism, such as a worker thread, may realize many short-lived observers across different operations.

A transition interpreter or one finite process activation may realize an observer locus when it supplies the boundary, observations, authority, and interpretation rules for that decision. A persisted transition or process definition is not itself an observer, and an effect handler does not gain authority merely because a runtime registers or invokes it.

Observer models provide structure for:

- Boundaries of interpretation.
- Exogenous and endogenous event classification.
- Command interpretation.
- Routing and interaction.
- Projection and hosting responsibilities.
- Alignment between transition interpretation and the realization context that commits effects.
- Attribution of definition, revision, node, branch, activation, and causal provenance to observed decisions.

## Observation Dependencies

An observer model should declare its observation dependencies independently of the mechanism used to satisfy them. An observation dependency relates an observer placement to the subject, source, or [[Observable|observable]] whose evidence the observer requires. It describes required knowledge and semantic postconditions; it does not by itself select push delivery, polling, subscription, replay, shared-state access, or a broker.

Useful dependency forms include:

- A **state dependency** requires an admissible observation of selected state at a declared version, cut, freshness, and consistency expectation.
- A **transition dependency** requires evidence that a selected state change or occurrence happened, even when later state alone would not preserve its meaning.
- A **history dependency** requires a sufficiently complete ordered, causal, or otherwise structured sequence of occurrences.
- A **signal dependency** requires only evidence that prior knowledge may be stale and that the observer should inspect or reconcile with another source.

Each dependency should identify the source and its authority, required [[Shape|shape]], version or position, whether intermediate occurrences matter, tolerated uncertainty or staleness, and the observer-relative postcondition that establishes [[Semantic Propagation|semantic propagation]]. Delivery, ordering, retention, reconciliation, and recovery requirements then qualify the structural dependency. Two observers may depend on the same subject while requiring different views, histories, freshness, or recovery paths.

[[Endpoints|Messaging endpoints]], gateways, service activators, polling consumers, event-driven consumers, dispatchers, and competing consumers are possible endpoint or activation structures for observer models. They do not make a transport or messaging endpoint identical to the semantic observer: the model must still identify the boundary, state view, authority, and interpretation rules supplied at activation. One logical endpoint can activate many observer instances, and one observer responsibility can be reachable through several physical endpoints.

When an adapter returns a request result, signal, or external observation, the observer model determines how that input is admitted and interpreted. The adapter must not bypass the entity transition boundary to mutate authoritative state directly, and a runtime callback must not become hidden semantic decision structure.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Observer|observer]], [[Observable|observable]], [[Observation|observation]], [[Command|command]], [[Event|event]], [[Effect|effect]], [[Entity|entity]], [[Messages and Envelopes|messages and envelopes]], [[Interfaces|interfaces]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Interaction Channels|interaction channels]], [[Routing Models|routing models]], [[Consumer Coordination|consumer coordination]], [[Transition Models|transition models]], [[Process Graphs|process graphs]], [[Execution Kernel|execution kernel]], [[Boundaries|boundaries]], [[Realization|realization]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Semantic Propagation|semantic propagation]], [[Concurrency Control|concurrency control]].

## Formal relations

- `arranges`: [[Observer]] — Places semantic observer roles into model-specific interpretation, responsibility, execution-context, and boundary positions.
- `arranges`: [[Observable]] — Relates placed observer roles to the state, transition, history, or signal dependencies they require without selecting an acquisition mechanism.
