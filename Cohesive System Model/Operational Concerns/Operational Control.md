---
realm: Operational Concerns
kind: operational-concern
created: 2026-07-27
updated: 2026-07-27
aliases:
  - Control Plane
  - Messaging Control
---

# Operational Control

Operational control describes authorized interventions that inspect or change how a running system admits, routes, schedules, pauses, drains, replays, quarantines, purges, resumes, or tests work.

Control interactions are ordinary modeled interactions with unusually broad operational authority. A control bus, administration API, CLI, workflow signal, operator console, or infrastructure controller may carry them. The control medium does not define their authority or semantic effect.

## Control Operations

Examples include:

- Pause, resume, drain, stop, restart, or cancel a consumer, route, process, or host.
- Enable a detour, shadow path, validation step, diagnostic route, or maintenance lane.
- Change admission, concurrency, priority, partition assignment, retry, retention, or routing policy.
- Quarantine, repair, replay, skip, reset, or purge selected material.
- Inject a test message or synthetic transaction and observe its path.

Each operation should declare target identity and scope, requesting authority, expected configuration or ownership version, idempotency basis, safe point, acknowledgment meaning, audit evidence, rollback or recovery path, and effect on in-flight work. A stale controller or former owner must not retain authority merely because it can still reach the control endpoint.

Control-plane success is boundary-relative. Acceptance of a pause command does not prove every worker has stopped; a purge acknowledgment does not prove downstream copies or committed effects were removed; enabling a detour does not prove all routes observe the new revision simultaneously.

## External References

- Gregor Hohpe and Bobby Woolf, [Control Bus](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ControlBus.html), [Detour](https://www.enterpriseintegrationpatterns.com/patterns/messaging/Detour.html), and [Channel Purger](https://www.enterpriseintegrationpatterns.com/patterns/messaging/ChannelPurger.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Authority|authority]], [[Interaction|interaction]], [[Infrastructure Graph|infrastructure graph]], [[Routing Models|routing models]], [[Consumer Coordination|consumer coordination]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Scheduling|scheduling]], [[Acknowledgments|acknowledgments]], [[Idempotency|idempotency]], [[Recovery|recovery]], [[Observability and Provenance|observability and provenance]], [[Application Hosts|application hosts]], [[Infrastructure|infrastructure]].
