# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.
Clearly AI-generated writing and clearly human-written writing should have combined confidence scores that differ by at least 0.30.



**Why this target:** The system should produce meaningfully different scores for writing from different sources. If the scores are too similar, the system is not providing useful information to distinguish between them.



---

## 2.

Only 1 out of 10 pieces of writing that I personally wrote should receive the high-confidence AI label.



**Why this target:** Incorrectly accusing a real writer of using AI is one of the most serious mistakes this system can make. I want to prioritize protecting human writers, even if that means missing some AI-generated content.




---

## 3.

All three labels (high-confidence AI, high-confidence human, and unsure) must be reachable through at least one test submission each.



**Why this target:** The system needs to communicate different levels of confidence rather than forcing every submission into an AI or human category. The unsure label is especially important when the signals do not provide enough evidence for a confident decision.



---

## 4.

Every valid appeal submitted with an existing content_id and non-empty reasoning must be recorded in the audit log, and the corresponding submission status must change to under_review.



**Why this target:** Writers should have a reliable way to challenge an incorrect decision. Recording the appeal and updating the status ensures their concerns are not lost or ignored.



---

## 5.

Requests with missing text, empty text, or text exceeding 10,000 characters must be rejected with an HTTP 400 response and a JSON error message.



**Why this target:** Invalid submissions should not be processed by the detection system. Returning a clear error response helps prevent unexpected behavior and makes it easier for applications using the service to understand what went wrong.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
