"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "Okay, so I'm tired but I have homework to do. Booooooo",
            "Fatally, so. I'm hopelessly, tragically in love with you.",
            "Work is due sunday midnight, have up to 48 hours extra",
            "I am a student currently enrolled in the CodePath AI Engineering program.",
            "You can usually think of functional as the things a client/user should be able to do.",
            "Cassandra is good for a massive amount of load.",
            "Nested loops does not always mean n^2, could mean n x m instead.",
            "Update: it’s a burn.",
            "In anime, there is sub and dub. Dub is when it’s translated to a language other than japanese so you only have to listen. Sub is when it’s in japanese and has translated subtitles so you have to read as you watch.",
            "I don’t see how this is relevant.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 2,
        "texts": [
            # Likely human-style examples
            "Honestly, I don't really know what to think about this yet. I might change my mind after I look into it more",
            "I tried fixing the problem yesterday, but nothing worked. Then I realized I was looking at the wrong file the whole time.",

            # More formal, structured examples
            "Artificial intelligence has become an increasingly important part of modern society. It can improve efficiency, support decision-making, and help people complete complex tasks. However, its use also raises questions about reliability, accountability, and responsible implementation.",
            "There are several factors to consider when evaluating a software system. First, its functionality should meet the needs of its intended users. Second, its performance should remain consistent under expected workloads. Finally, the system should be maintainable and secure as it evolves.",

            # Borderline examples
            "I think technology is useful, but it depends on how people use it. Sometimes it saves time, and other times it creates more problems than it solves.",
            "He didn't offer a shred of pity. He simply turned his back on his older brother, walking away down the stone path without looking back once.",
        ],
    },
    {
        "name": "appeals are recorded correctly",
        "criterion": 3,
        "texts": [
            "To be or not to be.",
            "The first version of my solution did not work, so I went back.",
            "I have been learning how different parts of a web application communicate with each other.",
            "After several attempts, I finally found the issue.",
            "I do not understand. Please clarify what you are speaking about."
        ],
        "appeal_reasons": [
            "I wrote this submission myself and would like the decision reviewed.",
            "This is my own writing, and I believe the classification is incorrect.",
            "I disagree with the result because I wrote this text myself.",
            "I would like to appeal this decision because the writing is mine.",
            "Please review this classification. I wrote the submitted text myself.",
        ],
    },
    {
        "name": "invalid text or inputs return 400",
        "criterion": 4,
        "bodies": [
            {"text": "", "creator_id": "eval_empty_1"},
            {"text": "   ", "creator_id": "eval_space_only"},
            {"text": "\n\t", "creator_id": "eval_invalid_text"},
            {"text": None, "creator_id": "eval_invalid_inputs"},
            {"creator_id": "eval_missing_input"},
        ],
    },
    {
        "name": "every decision appears in audit log",
        "criterion": 5,
        "texts": [
            "I went to the store today and bought some groceries.",
            "The weather was nice, so I decided to take a walk.",
            "I have been working on my programming assignment all afternoon.",
            "Technology can make everyday tasks easier when it is used appropriately.",
            "I don't understand why this function keeps returning the wrong result.",
            "The best way to learn something new is to practice it consistently.",
            "I tried a different approach, and it finally worked.",
            "There are several ways to solve this problem, depending on the requirements.",
            "I think the original version was easier to understand.",
            "The application should return a useful error message when something goes wrong.",
            "I spent most of the morning reviewing my notes.",
            "This solution works, but I think it could be more efficient.",
            "Sometimes the simplest explanation is the most helpful one.",
            "I would rather have a reliable system than one with unnecessary features.",
            "The assignment instructions were a little confusing at first.",
            "I changed the function so it handles empty input correctly.",
            "The results were different than I expected.",
            "I need to test this with a few more examples before deciding.",
            "The program should keep a record of every completed submission.",
            "I finished the implementation and am checking the results now.",
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
