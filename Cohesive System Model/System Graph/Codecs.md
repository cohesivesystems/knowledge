---
realm: System Graph
kind: structural-construct
created: 2026-11-05
updated: 2026-11-05
---

# Codecs

A codec declares a transformation between representations. It names input and output [[Shape|shapes]], direction, failure outcomes, and the distinctions it preserves or forgets. For a framed message, an incomplete prefix may require more input, while a complete malformed frame is a rejection. These are different outcomes.

A one-way projection can forget information without promising an inverse. A partial decoder can promise to recover each encoded source value while rejecting other inputs. A lossless re-encoding promises both round trips within its declared domain. A view that supports updates needs laws governing how an update is reflected in the source. Each stronger claim needs its own evidence.

Codecs can compose only with compatible intermediate representations. A guarantee transfers across the chain only at the required scope: preserving order within one connection does not establish per-entity order across reconnects. The graph describes the transformation and its obligations; a serializer, translator, or stream decoder may implement it.

## Formal relations

- `arranges`: [[Shape]] — Assigns shapes to the input and output roles of a transformation with declared preservation and failure behavior.
