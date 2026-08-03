---
realm: System Graph
kind: structural-construct
created: 2026-07-27
updated: 2026-08-02
aliases:
  - Message Routing
  - Message Router
  - Routing Model
---

# Routing Models

Routing models describe how an interaction selects destinations, recipients, paths, or next processing loci in the system graph.

Routing may depend on message content, contract type, target identity, policy, authority, subscription, topology, current observations, availability, capacity, or route state. A routing decision is an observer-relative interpretation and policy decision; a broker rule, service-discovery table, gateway configuration, or workflow edge is its possible realization.

When routing or dispatch distributes admitted work among several eligible capacity-bearing destinations, [[Load Balancing|load balancing]] states the operational policy and objectives of that distribution. The routing model records the structural choice and eligible topology; load balancing qualifies how that choice should behave under workload, capacity, locality, fairness, and failure conditions.

## Routing Structures

- A **content-based router** selects a path from the carried value or envelope.
- A **dynamic router** uses observations or registrations that can change independently of the sender.
- A **recipient list** selects several destinations for one emission.
- A **routing slip** carries or derives a remaining sequence of processing loci.
- A **filter** admits or suppresses a value for a path under a declared policy.
- A **dispatcher or selective consumer** assigns admitted work among eligible receiving observers.
- A **message broker** centralizes some destination and path selection while remaining a substrate participant rather than semantic authority.

Routing does not by itself establish that a receiver admitted, processed, committed, or completed the intended work. It must be combined with [[Interaction Channels|channels]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Consumer Coordination|consumer coordination]], and explicit failure and fallback meanings.

[[Multiplexing and Demultiplexing|Demultiplexing]] is a qualified routing role: it uses a discriminator to recover one logical lane or [[Endpoints|endpoint]] from a shared locus. General routing may instead choose among alternative paths, create a recipient set, or change topology without reversing a prior multiplexing relation.

Routing models should preserve route provenance: which definition, rule, observation, policy, branch, and revision selected the path. Dynamic routing and retries must also state whether a later attempt may choose a different destination and what that means for idempotency, ordering, and authority.

## External References

- Enterprise Integration Patterns, [Message Routing patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html).
- Gregor Hohpe and Bobby Woolf, [Content-Based Router](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ContentBasedRouter.html) and [Process Manager](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ProcessManager.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Flow Views|flow views]], [[Process Graphs|process graphs]], [[Observer Models|observer models]], [[Policy Scopes|policy scopes]], [[Interaction|interaction]], [[Interfaces|interfaces]], [[Interaction Bindings|interaction bindings]], [[Endpoints|endpoints]], [[Interaction Channels|interaction channels]], [[Multiplexing and Demultiplexing|multiplexing and demultiplexing]], [[Messages and Envelopes|messages and envelopes]], [[Flow Operators|flow operators]], [[Consumer Coordination|consumer coordination]], [[Load Balancing|load balancing]], [[Ordering|ordering]], [[Idempotency|idempotency]], [[Network Channels|network channels]], [[Brokers|brokers]].
