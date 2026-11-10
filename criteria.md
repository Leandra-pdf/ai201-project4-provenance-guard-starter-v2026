# Acceptance criteria — Provenance Guard
> Updates were made her because I mixed up my progress after unit 7.

## 1. Protect human-written content

No more than 1 out of 10 pieces of writing that I personally wrote should receive the high-confidence AI label.

**Why this target:** Incorrectly accusing a real writer of using AI is one of the most serious mistakes this system can make. I want to prioritize protecting human writers, even if that means missing some AI-generated content.

---

## 2. Label coverage

All three labels (high-confidence AI, high-confidence human, and unsure) must be reached through at least one test submission each.

**Why this target:** The system needs to communicate different levels of confidence rather than forcing every submission into an AI or human category. The unsure label is especially important when the signals do not provide enough evidence for a confident decision.

---

## 3. Appeals are recorded correctly

Every valid appeal submitted with an existing `content_id` and non-empty reasoning must be accepted and change the submission's status to `under_review`.

**Why this target:** Writers should have a reliable way to challenge an incorrect decision. Recording the appeal and updating the status ensures their concerns are not lost or ignored.

---

## 4. Invalid submissions are rejected

Requests with missing text, empty text, whitespace-only text, or non-string text must be rejected with an HTTP 400 response and a JSON error message.

**Why this target:** Invalid submissions should not be processed by the detection system. Returning a clear error response helps prevent unexpected behavior and makes it easier for applications using the service to understand what went wrong.

---

## 5. Every decision is auditable

Every successfully processed submission must receive a unique `content_id`, and its decision must be recorded in the audit log. The target is 20 out of 20 decisions recorded.

**Why this target:** Every classification should be traceable. Keeping a record of the decision and its associated scores makes it possible to review outcomes, investigate disputes, and maintain accountability.
