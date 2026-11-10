# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 21:27
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `8e0920e5-003a-4f46-840f-a4512cf4f781` | human | 0.314 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f8e9a5a5-7f33-4fc1-9519-8fdc445d0d63` | human | 0.571 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `6117c8d6-8939-423f-8607-2890d0b6648a` | unsure | 0.647 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `9ad7674d-196a-4f4d-8943-6309e686ddac` | unsure | 0.626 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `3de48403-ccc7-46a6-8814-6bf6ed9e0bcb` | human | 0.402 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `789e0d7e-b621-47ba-a824-e8d66f750ae0` | human | 0.572 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `6f600fc1-153a-453a-b5ca-21eae1d7aa42` | human | 0.597 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `536276f0-6ea3-4fa8-87d6-795b735ae2c1` | human | 0.350 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `f4ccb4be-f446-4c1c-9882-89ebbc860886` | unsure | 0.676 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `b2959d96-cdcf-49f4-b3d5-50274cae7050` | ai | 0.925 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `0cb1c14c-cef2-4d73-bf90-a14fe09a860c` | unsure | 0.630 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `d7a7d88b-a350-42e6-8edd-2ab23eca4e1e` | unsure | 0.727 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `2674aa4b-9462-4740-b556-ece96d206c81` | unsure | 0.767 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `db16a2b1-7131-44ed-bbbb-095d1096bf9c` | unsure | 0.775 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `1f6b27ba-1291-4ea3-9366-327371a5702f` | unsure | 0.780 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `7f62894e-8575-4435-b4a0-9a7d37829ae8` | ai | 0.809 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `008e381f-da6b-42ed-8d2a-f2a69cf8412c` | ai | 0.829 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `3c61b5af-cbc1-467b-845c-2b8f24562e76` | human | 0.395 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `b144a3c4-45bb-486f-8a67-fd32da22f628` | human | 0.491 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `d5205bbf-7660-4677-8951-374ac33a7169` | human | 0.297 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `2ad220b3-909a-46b1-a27c-09723741af33` | human | 0.590 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `69641cef-fc81-4a5d-81b5-a5d76e095566` | human | 0.535 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `41eec607-e7f5-4260-b3d4-63ba79b39656` | human | 0.569 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `49ac4afb-0e78-47fe-a5ef-8ace664ce78e` | human | 0.589 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `76a5c69d-1f00-4a37-af69-ca25a5425e70` | human | 0.200 |  |
| MF04 | malformed | text is only punctuation | 200 | `471917e8-b546-4aaa-8236-871058522704` | human | 0.158 |  |
| MF05 | malformed | text is a very long single word | 200 | `b2fa6a70-67cc-4037-9616-2635c4e808a7` | ai | 0.898 |  |
| MF06 | malformed | text is emoji only | 200 | `b18fdf3b-3645-41a7-8d73-7d15163dd7b4` | unsure | 0.705 |  |
| MF07 | malformed | text is right-to-left script | 200 | `41e18cb6-eb4e-4161-b8b9-9c44f4a6c054` | unsure | 0.705 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `95efe805-7250-4bdd-b425-dbaece172107` | human | 0.220 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c8635a6b-f699-4f4e-99ae-10b314823b13` | human | 0.220 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1cf6466d-3652-4e5d-b31e-46264edf533f` | human | 0.220 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0c812ef8-76cb-48d7-989f-d1ca25c78198` | human | 0.220 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ace84cb2-565d-4315-a15f-aeaf1f3fd8e9` | human | 0.220 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7f28a698-7c4e-41a4-a45b-b7b4ef456cbe` | human | 0.220 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "8e0920e5-003a-4f46-840f-a4512cf4f781",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.31354337509513824,
  "model_score": 0.1635,
  "style_score": 0.6636445836504609,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "f8e9a5a5-7f33-4fc1-9519-8fdc445d0d63",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.5711872389016107,
  "model_score": 0.5943,
  "style_score": 0.5172574630053691,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "6117c8d6-8939-423f-8607-2890d0b6648a",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6469427639448697,
  "model_score": 0.6662,
  "style_score": 0.602009213149566,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "9ad7674d-196a-4f4d-8943-6309e686ddac",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6259473549380796,
  "model_score": 0.6114,
  "style_score": 0.6598911831269318,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "3de48403-ccc7-46a6-8814-6bf6ed9e0bcb",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.40160533121367725,
  "model_score": 0.3212,
  "style_score": 0.5892177707122577,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "789e0d7e-b621-47ba-a824-e8d66f750ae0",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.5716371432843486,
  "model_score": 0.5727,
  "style_score": 0.5691571442811618,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "6f600fc1-153a-453a-b5ca-21eae1d7aa42",
  "creator_id": "attacker_EV07",
  "guess": "human",
  "confidence": 0.5969379381443299,
  "model_score": 0.5862,
  "style_score": 0.6219931271477663,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "536276f0-6ea3-4fa8-87d6-795b735ae2c1",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.34959187907884576,
  "model_score": 0.2452,
  "style_score": 0.5931729302628193,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "f4ccb4be-f446-4c1c-9882-89ebbc860886",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6763967292901478,
  "model_score": 0.7042,
  "style_score": 0.6115224309671595,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "b2959d96-cdcf-49f4-b3d5-50274cae7050",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9251296231367527,
  "model_score": 0.9792,
  "style_score": 0.7989654104558429,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "0cb1c14c-cef2-4d73-bf90-a14fe09a860c",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6299866473690366,
  "model_score": 0.6175,
  "style_score": 0.6591221578967889,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "d7a7d88b-a350-42e6-8edd-2ab23eca4e1e",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7266598204166343,
  "model_score": 0.7387,
  "style_score": 0.6985660680554481,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "2674aa4b-9462-4740-b556-ece96d206c81",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7665713397728522,
  "model_score": 0.8051,
  "style_score": 0.6766711325761737,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "db16a2b1-7131-44ed-bbbb-095d1096bf9c",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7753176970990732,
  "model_score": 0.8329,
  "style_score": 0.640958990330244,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "1f6b27ba-1291-4ea3-9366-327371a5702f",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7800940087465567,
  "model_score": 0.8005,
  "style_score": 0.7324800291551891,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "7f62894e-8575-4435-b4a0-9a7d37829ae8",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.809368178178241,
  "model_score": 0.8814,
  "style_score": 0.6412939272608035,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "008e381f-da6b-42ed-8d2a-f2a69cf8412c",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.829130275027281,
  "model_score": 0.8816,
  "style_score": 0.7067009167576032,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "3c61b5af-cbc1-467b-845c-2b8f24562e76",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.39539305207480374,
  "model_score": 0.3223,
  "style_score": 0.5659435069160126,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "b144a3c4-45bb-486f-8a67-fd32da22f628",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.4905614498065477,
  "model_score": 0.4625,
  "style_score": 0.5560381660218257,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "d5205bbf-7660-4677-8951-374ac33a7169",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2969520669199146,
  "model_score": 0.2044,
  "style_score": 0.5129068897330488,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "2ad220b3-909a-46b1-a27c-09723741af33",
  "creator_id": "attacker_PI03",
  "guess": "human",
  "confidence": 0.5904671777996917,
  "model_score": 0.5943,
  "style_score": 0.5815239259989725,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "69641cef-fc81-4a5d-81b5-a5d76e095566",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.5351825374246613,
  "model_score": 0.4998,
  "style_score": 0.6177417914155375,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "41eec607-e7f5-4260-b3d4-63ba79b39656",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.5693656092316293,
  "model_score": 0.6401,
  "style_score": 0.4043186974387642,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "49ac4afb-0e78-47fe-a5ef-8ace664ce78e",
  "creator_id": "attacker_PI06",
  "guess": "human",
  "confidence": 0.5891969795342521,
  "model_score": 0.5583,
  "style_score": 0.6612899317808405,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "76a5c69d-1f00-4a37-af69-ca25a5425e70",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.19999999999999998,
  "model_score": 0.0,
  "style_score": 0.6666666666666666,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "471917e8-b546-4aaa-8236-871058522704",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.15783999999999998,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "b2fa6a70-67cc-4037-9616-2635c4e808a7",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8983199999999999,
  "model_score": 0.9976,
  "style_score": 0.6666666666666666,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "b18fdf3b-3645-41a7-8d73-7d15163dd7b4",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.7050000000000001,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "41e18cb6-eb4e-4161-b8b9-9c44f4a6c054",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.7050000000000001,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't confidently tell whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "95efe805-7250-4bdd-b425-dbaece172107",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.22008999999999998,
  "model_score": 0.0287,
  "style_score": 0.6666666666666666,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c8635a6b-f699-4f4e-99ae-10b314823b13",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.22008999999999998,
  "model_score": 0.0287,
  "style_score": 0.6666666666666666,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "1cf6466d-3652-4e5d-b31e-46264edf533f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.22008999999999998,
  "model_score": 0.0287,
  "style_score": 0.6666666666666666,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "0c812ef8-76cb-48d7-989f-d1ca25c78198",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.22008999999999998,
  "model_score": 0.0287,
  "style_score": 0.6666666666666666,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "ace84cb2-565d-4315-a15f-aeaf1f3fd8e9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.22008999999999998,
  "model_score": 0.0287,
  "style_score": 0.6666666666666666,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "7f28a698-7c4e-41a4-a45b-b7b4ef456cbe",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.22008999999999998,
  "model_score": 0.0287,
  "style_score": 0.6666666666666666,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
