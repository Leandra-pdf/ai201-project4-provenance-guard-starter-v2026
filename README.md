# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

This project checks whether a piece of writing was likely written by a person or AI. It uses two signals: a model score and a writing style score, then combines them using a weighted average to make a final prediction. The result is labeled as human, AI, or unsure. Each submission is saved in an audit log, and writers can appeal a decision by providing a reason. Appeals are recorded in the log with an `under_review` status.

### 1. Submission Path

A submission moves through the following seven steps:

1. **Text Submission:** A writer submits their writing along with their `creator_id`.
2. **POST /submit:** The endpoint receives the JSON request containing the text and creator ID.
3. **AI Detector (Signal 1):** The detector uses a machine learning model to analyze the submitted text and estimate how likely it is to be AI-generated.
4. **Stylometry (Signal 2):** The stylometry system analyzes writing characteristics such as sentence length variation, vocabulary variety, and punctuation density.
5. **Combine Signals:** The two signal scores are combined using a weighted average. The model signal contributes 70% and the style signal contributes 30%.
6. **Assign Label:** The combined score is compared against thresholds to determine whether the writing is high-confidence AI, high-confidence human, or unsure.
7. **Return and Record:** The endpoint returns a JSON response containing the content ID, guess, confidence score, label, and both signal scores. The submission is also recorded in the audit log so the decision can be reviewed later.

### 2. Signals and Their Blind Spots

**Signal 1: AI Detector (`detector.py`)**

- **What it measures:** Uses a machine learning model to analyze submitted text and estimate whether it was written by AI or a human.
- **Why it might help:** AI-generated writing can contain patterns that differ from human writing, which a trained model may recognize.
- **Blind spot:** It can incorrectly identify human writing as AI, especially when the writing is formal, structured, or similar to patterns found in AI-generated text. It can also miss AI-generated writing that has been edited.

**Signal 2: Stylometry (`stylometry.py`)**

- **What it measures:** Analyzes measurable writing characteristics, including sentence length variation, unique word ratio, and punctuation density.
- **Why it might help:** Human and AI writing may differ in vocabulary choices, sentence structure, and punctuation patterns.
- **Blind spot:** A human writer may naturally have writing patterns that resemble AI, while AI-generated writing can be edited to imitate human writing patterns. Stylometry also cannot understand the actual meaning or origin of the writing.

The two signals measure different properties. The detector analyzes the text using a trained model, while stylometry measures observable writing patterns. Combining them provides more information than relying on either signal alone, although neither can reliably prove who wrote something.

### 3. False Positive Scenario

A real human writer submits an original piece of writing, but the system incorrectly identifies it as AI-generated.

For example:

- **Score:** The combined score is 0.92, indicating a high likelihood of AI-generated writing according to the system.
- **Label:** The writer receives the high-confidence AI label: "We think this was probably written by AI."
- **Impact:** The writer may feel unfairly accused because they created the work themselves.
- **Appeal:** The writer can submit an appeal through `POST /appeal`, providing their `content_id` and an explanation of why they believe the decision is incorrect.
- **Review:** The system records the appeal as a separate audit-log entry with the status `under_review`. The original decision remains in the log, and the system does not automatically rerun the detector.

False positives are especially important because incorrectly accusing a real writer can damage their trust in the platform. The system should communicate uncertainty and provide a way to challenge its decisions.

### 4. Endpoint Contracts

**POST /submit**

Input JSON:

```json
{
  "text": "The writing submitted by the creator.",
  "creator_id": "creator_123"
}
```

Output JSON:

```json
{
  "content_id": "content_123",
  "guess": "ai",
  "confidence": 0.92,
  "label": "We think this was probably written by AI.",
  "model_score": 0.95,
  "style_score": 0.85,
  "combined_score": 0.92
}
```

The endpoint accepts the writer's text and creator ID. It returns a unique content ID, the system's prediction, a combined score used as the confidence value, a plain-English label, and both individual signal scores. The confidence value is a score between 0 and 1, not a calibrated probability.

**POST /appeal**

Input JSON:

```json
{
  "content_id": "content_123",
  "reasoning": "I wrote this piece myself and did not use AI to generate it."
}
```

Output JSON:

```json
{
  "content_id": "content_123",
  "status": "under_review",
  "message": "Your appeal has been received and is under review."
}
```

The appeal endpoint accepts an existing content ID and the writer's reasoning. It records the appeal as a separate entry in the audit log with the status `under_review` and confirms that the appeal was received. It does not automatically rerun the detector or overwrite the original decision.

These endpoint contracts allow another application to submit writing, receive a prediction, and provide writers with a way to challenge incorrect decisions.

## Signals and Scoring

### Signal one — the model signal

**What it measures:**

The model signal uses a trained AI-text detector to estimate how likely the submitted writing is to have been generated by AI. It returns a score between 0 and 1, with higher scores indicating a stronger AI signal.

**Why that might differ between human and AI writing:**

AI-generated writing can have patterns that the detector has learned to associate with AI text. The model looks at those patterns and uses them to estimate whether the writing resembles text it has seen from AI systems.

**What it can't see:**

The detector cannot know who actually wrote something or prove authorship. It can misclassify human writing as AI-generated, especially when the writing happens to resemble patterns in AI-generated text. It also cannot understand the writer's intentions or the circumstances in which the text was created.

### Signal two — the style signal

**What it measures:**

The style signal looks at three writing characteristics:
- **Sentence length spread:** How much sentence lengths vary.
- **Type-token ratio:** The proportion of unique words compared with the total number of words.
- **Punctuation density:** How frequently certain punctuation marks appear, including colons, semicolons, em dashes, ellipses, and exclamation marks.

These measurements are combined into one score between 0 and 1. Higher scores indicate that the writing has more of the stylistic patterns this heuristic associates with AI-generated text.

**Why that might differ between human and AI writing:**

AI-generated writing can sometimes have more consistent sentence lengths, repeated vocabulary patterns, and more predictable punctuation. Human writing can be less consistent, with more variation in sentence structure and word choice. The style signal uses these differences as clues.

**What it can't see:**

Writing style alone cannot establish authorship. A person can write in a very consistent or polished style, and AI-generated writing can be varied or informal. The signal also cannot understand the meaning of the writing, the writer's experience, or whether the text was edited after being generated.

### The combining rule

**The rule:**

The model signal and style signal will be combined using a weighted average. The model signal receives more weight because it is the primary AI detector, while the style signal provides additional evidence based on writing characteristics.

If the two signals strongly disagree, meaning one indicates AI and the other indicates human, the final result will be classified as unsure rather than relying on the weighted average. This prevents conflicting signals from producing an overly confident decision.

**The numbers:**

- Model signal weight: **0.70 (70%)**
- Style signal weight: **0.30 (30%)**
- AI threshold: **0.65 or higher**
- Human threshold: **0.35 or lower**
- Unsure: **Between 0.35 and 0.65**
- Disagreement override: If one signal is 0.65 or higher and the other is 0.35 or lower, classify as unsure.

**Where it lives:** `scoring.py::combine_signals`

The combining rule will be implemented in `combine_signals()` in `scoring.py`. The weights and thresholds will be defined in `config.py`.

**A case where my two signals split, and what my rule does with it:**

- For example, if the model signal scores 0.85 (high likelihood of AI) but the style signal scores 0.30 (low likelihood of AI), the signals disagree. Since one signal is above the AI threshold of 0.65 and the other is below the human threshold of 0.35, my disagreement rule classifies the result as unsure instead of relying on the weighted average. This prevents a strong disagreement between the signals from producing an overly confident classification.
---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 | "We think this was probably written by a person." |
| unsure | Above 0.35 and below 0.65 | "We can't confidently tell whether this was written by a person or by AI." |
| high-confidence AI | 0.65–1.00 | "We think this was probably written by AI." |

**Why I worded the "unsure" one this way:**

I chose wording that communicates uncertainty without accusing the writer of using AI. A person may have written every word themselves, so the message avoids making a definite claim either way. It explains that the detector cannot confidently determine who or what wrote the text.



---

## Sample Run

**A submission**

Request:

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Okay, so I'\''m tired but I have homework to do. Boo", "creator_id": "milestone4_test4a"}'
```

Response:

```json
{
  "content_id": "299d03b3-0e24-4c62-9e8f-ee0c46058c6d",
  "guess": "unsure",
  "confidence": 0.5360488845730156,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "model_score": 0.5567,
  "style_score": 0.48786294857671875,
  "combined_score": 0.5360488845730156
}
```

**Checking the audit log**

Request:

```bash
curl "http://127.0.0.1:5000/log?limit=2"
```

Response (original submission):

```json
{
     "combined_score": 0.5360488845730156,
     "content_id": "299d03b3-0e24-4c62-9e8f-ee0c46058c6d",
     "creator_id": "milestone4_test4a",
     "guess": "unsure",
     "label": "We can't confidently tell whether this was written by a person or by AI.",
     "model_score": 0.5567,
     "status": "decided",
     "style_score": 0.48786294857671875,
     "timestamp": "2026-11-03T15:41:22+00:00"
},
{
     "timestamp": "2026-11-03T15:41:22+00:00",
     "content_id": "299d03b3-0e24-4c62-9e8f-ee0c46058c6d",
     "creator_id": "milestone4_test4a",
     "guess": "unsure",
     "model_score": 0.5567,
     "style_score": 0.48786294857671875,
     "combined_score": 0.5360488845730156,
     "label": "We can't confidently tell whether this was written by a person or by AI.",
     "status": "decided"
}
```

**An appeal**

Request:

```bash
curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "299d03b3-0e24-4c62-9e8f-ee0c46058c6d", "reasoning": "I wrote this myself and would like the decision reviewed."}'
```

Response:

```json
{
  "content_id": "299d03b3-0e24-4c62-9e8f-ee0c46058c6d",
  "status": "under_review",
  "message": "Your appeal has been received and is under review."
}
```

**What the log shows afterwards**

Request:

```bash
curl "http://127.0.0.1:5000/log?limit=1"
```

Response (new appeal entry):

```json
{
  "timestamp": "2026-11-03T15:47:20+00:00",
  "content_id": "299d03b3-0e24-4c62-9e8f-ee0c46058c6d",
  "creator_id": "milestone4_test4a",
  "event": "appeal",
  "status": "under_review",
  "reasoning": "I wrote this myself and would like the decision reviewed."
}
```

The original decision remains in the audit log with status `decided`, while the appeal is recorded as a separate entry with status `under_review`. The original decision is not overwritten.

## How I Used AI

**Moment 1** Choosing a combined scoring strategy

- *What I asked for:* I asked AI to help me compare different ways of combining the model signal and style signal into one score.
- *What came back:* It suggested options such as averaging the two signals equally, giving the model signal more weight, or adjusting the result when the signals disagreed.
- *What I changed:* I chose a weighted average of 70% model signal and 30% style signal. I wanted the trained detector to have more influence while still allowing writing style to contribute to the result. I decided not to add a separate disagreement rule because I wanted to keep the scoring method straightforward.

**Moment 2** Deciding what punctuation to measure

- *What I asked for:* I asked AI to help me think through which punctuation marks would be useful to include when measuring punctuation density as part of the style signal since there are some obvious AI punction I'd like to detect.
- *What came back:* It helped me consider how punctuation patterns could be measured and which marks might be worth counting.
- *What I changed:* I narrowed the measurement to five punctuation marks: colons, semicolons, em dashes, ellipses, and exclamation marks. I implemented the measurement myself so that it counts those specific marks relative to the number of words in the text.


<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 6 per minute, 120 per day

**Why those numbers and not others:**

I chose these limits to allow a real writer to submit several pieces of work without running into restrictions during normal use, while making it harder for an automated script to send large numbers of variations to probe the detector's thresholds. Six submissions per minute allows occasional repeated testing, and the daily limit of 120 provides room for regular use without allowing unlimited submissions.

**What a caller counts as:**

Requests are counted by `creator_id` when the request contains a valid, non-empty creator ID. If the creator ID is missing or invalid, the limiter falls back to the caller's IP address. This makes it harder for a script to bypass the limit by changing creator IDs only if it continues using the same ID. However, a script can potentially get around per-creator limits by submitting different creator IDs. The IP fallback catches requests without a valid creator ID, but it does not prevent that particular bypass.

**The run of status codes when I pushed past it:**

```text
200 200 200 200 200 200 429 429 429 429 429 429 429 429 429
```

The first six submissions were accepted with HTTP 200. The next nine were rejected with HTTP 429. This confirms that the per-minute limit was enforced once the caller exceeded six submissions.

---

## Attack Run — Before

**Ten audit log entries from the run**

```json
[
  {
    "timestamp": "2026-11-05T00:14:20+00:00",
    "content_id": "bc1dcfb3-91cd-4b09-a500-120049b8aa95",
    "creator_id": "attacker_EV09",
    "guess": "ai",
    "model_score": 0.7042,
    "style_score": 0.6115224309671595,
    "combined_score": 0.6763967292901478,
    "label": "We think this was probably written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-05T00:14:21+00:00",
    "content_id": "c96976a3-26c2-4ae2-bab4-3a4182871efb",
    "creator_id": "attacker_FP08",
    "guess": "unsure",
    "model_score": 0.3223,
    "style_score": 0.5659435069160126,
    "combined_score": 0.39539305207480374,
    "label": "We can't confidently tell whether this was written by a person or by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-05T00:14:20+00:00",
    "content_id": "82e6fdd1-47f6-4021-b6b1-584c31137a56",
    "creator_id": "attacker_EV10",
    "guess": "ai",
    "model_score": 0.9792,
    "style_score": 0.7989654104558429,
    "combined_score": 0.9251296231367527,
    "label": "We think this was probably written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-05T00:14:20+00:00",
    "content_id": "a2427547-316e-4ca8-bfb8-1343ffcc8f66",
    "creator_id": "attacker_FP03",
    "guess": "ai",
    "model_score": 0.8051,
    "style_score": 0.6766711325761737,
    "combined_score": 0.7665713397728522,
    "label": "We think this was probably written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-05T00:14:21+00:00",
    "content_id": "e8d3cf4f-1855-4cc9-af25-eb499d080f29",
    "creator_id": "attacker_FP07",
    "guess": "ai",
    "model_score": 0.8816,
    "style_score": 0.7067009167576032,
    "combined_score": 0.829130275027281,
    "label": "We think this was probably written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-05T00:14:21+00:00",
    "content_id": "15d79a64-b143-4180-82ce-8f7e07f38116",
    "creator_id": "attacker_PI05",
    "guess": "unsure",
    "model_score": 0.6401,
    "style_score": 0.4043186974387642,
    "combined_score": 0.5693656092316293,
    "label": "We can't confidently tell whether this was written by a person or by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-05T00:14:21+00:00",
    "content_id": "355c86c7-6728-45f6-a433-f719a2ebdcc5",
    "creator_id": "attacker_MF03",
    "guess": "unsure",
    "model_score": 0.0,
    "style_score": 0.6666666666666666,
    "combined_score": 0.5,
    "label": "We can't confidently tell whether this was written by a person or by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-05T00:14:21+00:00",
    "content_id": "b3f6eee4-71d0-444e-8de0-dbfeac21ccc0",
    "creator_id": "attacker_MF06",
    "guess": "ai",
    "model_score": 0.9969,
    "style_score": 0.5,
    "combined_score": 0.84783,
    "label": "We think this was probably written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-05T00:14:21+00:00",
    "content_id": "ecb20057-eb0a-4b38-b3d3-713aa130d1f3",
    "creator_id": "attacker_MF07",
    "guess": "ai",
    "model_score": 0.9064,
    "style_score": 0.5,
    "combined_score": 0.78448,
    "label": "We think this was probably written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-05T00:14:22+00:00",
    "creator_id": "attacker_flood",
    "event": "rejected",
    "status": "rejected",
    "reason": "rate_limited",
    "limit": "6 per 1 minute"
  }
]
```

**The single worst outcome**:

FP03 is the worst outcome. This test represented a non-native English speaker writing carefully, but the detector classified the submission as AI with a combined score of **0.767**. The model score was 0.8051, and the style score was 0.6767, so both signals contributed to the high result. A writer could be incorrectly accused of using AI simply because their writing is careful and formal. This demonstrates why the detector's result should be treated as an estimate rather than proof of authorship.

## Run Log and Verdicts

| Criterion                              | Target                             | Run 1      | Run 2      | Run 3      | Verdict |
| -------------------------------------- | ---------------------------------- | ---------- | ---------- | ---------- | ------- |
| 1. my own writing                      | No more than 1/10 classified as AI | 1/10 AI    | 1/10 AI    | 1/10 AI    | PASS    |
| 2. label coverage | All 3 labels reached across 6 submissions | 5 AI, 1 unsure, 0 human | 5 AI, 1 unsure, 0 human | 5 AI, 1 unsure, 0 human | FAIL    |
| 3. appeals are recorded correctly      | 5/5 appeals accepted               | 5/5        | 5/5        | 5/5        | PASS    |
| 4. invalid text or inputs return 400   | 5/5 invalid requests return 400    | 5/5        | 5/5        | 5/5        | PASS    |
| 5. every decision appears in audit log | 20/20 decisions recorded           | 20/20      | 20/20      | 20/20      | PASS    |


**Real output from one trial**:

```json
{
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5,
    "model_score": 0.0819,
    "style_score": 0.7142857142857143,
    "label": "We can't confidently tell whether this was written by a person or by AI.",
    "sent": "Nested loops does not always mean n^2, could mean n x m instead."
}
```

**Diagnoses**

Criterion 2

All six submissions in each trial were classified, but the detector only produced two of the three possible labels: five `ai` and one `unsure`. None received the `human` label.

The issue appears to be with the scores reaching the combining rule. The label mapping is not necessarily broken. It seems the tested inputs simply did not produce a low enough combined score to reach the human category.

I should inspect the `model_score`, `style_score`, and `combined_score` for the six submissions to determine which signal is contributing most to the scores staying above the human threshold. Adjustments will be made based on the observations.

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
