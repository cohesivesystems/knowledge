---
realm: Operational Concerns
kind: operational-concern
created: 2026-11-05
updated: 2026-11-05
---

# Receipt

A receipt is an attributable record of what happened to an identified input, operation, or attempt at a particular [[Boundaries|boundary]]. Its contract determines what fact the issuing participant can attest to and which work that fact covers. The term *receipt of a message* can also name the arrival itself. A receiver receipt records evidence about that occurrence.

A start receipt can establish that a participant admitted a request while the requested work is still pending. An operation receipt can record a decision, including rejection, or refer to a separately retained result. When a participant durably associates the receipt with the exact operation and its inputs, it can consult that evidence during replay. Reusing the recorded outcome is valid only for work covered by the original receipt. An aggregate receipt likewise needs evidence for each child outcome it claims.

An [[Acknowledgments|acknowledgment]] reports a fact to another participant. It may carry or cite a receipt. A participant can also retain a receipt in its own history without sending an acknowledgment.

In [[Delivery Progress and Settlement|delivery progress and settlement]], the receiver can record durable handling before the provider changes delivery state. A settlement receipt records the provider’s change, identifies the deliveries or cursor range it covers, and can cite the receiver’s progress. A provider-issued *receipt handle* serves a different role: it grants authority to request settlement for an attempt. Evidence that settlement occurred comes from the result of exercising that authority.

[[Assurance and Evidence|Assurance]] determines whether a receipt supports a larger claim. For example, a receipt for a local commit supports a claim about that commit. Establishing an external effect requires evidence from a boundary that can observe the effect.
