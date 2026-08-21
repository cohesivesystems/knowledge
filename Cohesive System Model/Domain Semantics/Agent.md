---
realm: Domain Semantics
kind: semantic-construct
created: 2026-08-20
updated: 2026-08-20
status: draft
aliases:
  - Agents
---

# Agent

An agent is an [[Observer|observer]] role whose modeled responsibility is to interpret [[Observation|observations]] and select or initiate actions in service of a purpose, objective, commitment, or obligation.

An agent acts through an [[Observer|observer]] context. Its decisions are relative to a [[Boundaries|boundary]], available observations, state or history, [[Policy|policies]], possible actions, and the [[Authority|authority]] and capabilities under which it acts. The observer supplies the locus of interpretation; agency adds an attributable role in choosing or initiating what happens next.

An agent role identifies:

- The purpose, objective, commitment, or obligation orienting its behavior.
- The observations and state available at its boundary.
- The actions it may select, including [[Interaction|interactions]], [[Command|commands]], and [[Effect|effects]].
- The policies, constraints, and decision rules governing selection.
- The authority and capabilities under which actions are proposed, attempted, accepted, or committed.
- The identity, role, or other attribution needed to associate decisions and actions with the agent at the modeled boundary.
- Any state, history, feedback, adaptation, delegation, or escalation needed for continuity.

Agency is boundary-relative and graded. An agent may be reactive or deliberative, deterministic or nondeterministic, transient or durable, tightly constrained or broadly delegated. Choice here identifies responsibility for selecting among available actions; it does not require randomness, learning, consciousness, personhood, or unrestricted autonomy. Autonomy describes how much selection is delegated within the agent boundary, while authority describes which resulting acts or claims count for a governed subject.

## Related Roles

| Term | Role | Relationship to agent |
| --- | --- | --- |
| participant | Anything assigned a role in a relation, [[Interaction|interaction]], or [[Process|process]]. | An agent is a participant with a modeled interpretation-and-action role. Stores, channels, entities, and other participants can participate without being modeled as agents. |
| [[Observer|observer]] | The participant, context, or execution locus relative to which inputs, state, and events acquire meaning. | An agent acts through an observer context and additionally owns a modeled role in choosing or initiating action. |
| agent | A purpose-, commitment-, or obligation-directed observer role that selects or initiates actions under policies and constraints. | Agency is semantic and does not prescribe addressing, concurrency, or runtime substrate. |
| actor | An isolated, addressable execution role that receives messages and commonly serializes their handling. | An actor may realize an agent, but actors may instead realize routers, projections, entity hosts, or other observer roles. An agent may be realized without an actor system. |
| [[Entity|entity]] | An enduring identifiable subject with evolving authoritative state. | An agent may be modeled as an entity when its identity, state, history, and lifecycle matter. Agency alone does not establish entity identity or transition authority. |
| [[Process|process]] | Coherent work unfolding across occurrences, participants, and time. | An agent may participate in or coordinate a process. The process describes the work; the agent describes a role that selects or initiates actions within it. |

## Realization

People, organizational roles, software components, actor activations, workflow roles, robots, and AI-enabled systems can realize agents when they preserve the declared observer context, decision scope, action repertoire, policy, attribution, and authority boundaries.

An AI model can supply inference, planning, prediction, or action selection within an agent realization. The model alone supplies neither the complete observer boundary nor the purposes, state, action interfaces, authority, continuity, and operational controls required by the agent role. Those belong to the surrounding system description and realization.

Agency does not grant authority. An agent may recommend, propose, request, or attempt an action while another observer, entity transition, person, policy, or protocol retains authority to accept and commit the result. Likewise, technical capability to perform an action is evidence about realization, not semantic authority to make that action count.

Related concepts: [[Observer|observer]], [[Observation|observation]], [[Interaction|interaction]], [[Process|process]], [[Entity|entity]], [[Actor Model|actor model]], [[Actor Systems|actor systems]], [[Policy|policy]], [[Authority|authority]], [[Identity|identity]], [[State|state]], [[Behavior|behavior]], [[Nondeterminism and Choice|nondeterminism and choice]], [[Command|command]], [[Effect|effect]], [[Boundaries|boundaries]], [[Realization|realization]].

## Formal relations

- `refines`: [[Observer]] — Adds an attributable decision-and-action role oriented by purposes, commitments, obligations, and policies to the observer's boundary-relative interpretation context.
- `distinguished_from`: [[Entity]] — An agent is a decision-and-action role, whereas an entity is an enduring identifiable subject with authoritative evolving state; one modeled subject may be both when those roles align.
- `distinguished_from`: [[Actor Model]] — An agent is a semantic decision-and-action role, whereas an actor is an addressable message-driven execution role that may realize an agent.
