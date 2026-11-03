"""
Signal two: the style signal.

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    Measure how much sentence lengths vary relative to their average.
    Higher values mean more variation.

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """

    sentence_list = sentences(text)

    sentence_lengths = []

    for sentence in sentence_list:
        sentence_lengths.append(len(words(sentence)))

    # A single sentence has no measurable spread.
    if len(sentence_lengths) < 2:
        return 0.0

    average_length = statistics.mean(sentence_lengths)

    if average_length == 0:
        return 0.0

    spread = statistics.stdev(sentence_lengths)

    return spread / average_length


def type_token_ratio(text: str) -> float:
    """
    Measure vocabulary variety by dividing unique words by total words.
    Higher values mean more varied vocabulary.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    word_list = words(text)

    if len(word_list) == 0:
        return 0.0

    unique_words = set(word_list)

    return len(unique_words) / len(word_list)



def punctuation_density(text: str) -> float:
    """
    Measure punctuation relative to the number of words.
    Higher values mean more punctuation per word.

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    word_list = words(text)

    if len(word_list) == 0:
        return 0.0

    # punctuation_marks = re.findall(r"[^\w\s]", text) # all punct counts
    punctuation_marks = re.findall(r"[:;—…!]", text)

    return len(punctuation_marks) / len(word_list)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    Combine the three writing-style measurements into a 0–1
    AI-likelihood score. Higher means more likely AI.

    Low sentence variation, low vocabulary variety, and lower
    punctuation density increase the score.
    """
    if len(words(text)) == 0:
        return 0.5

    spread = sentence_length_spread(text)
    vocabulary = type_token_ratio(text)
    punctuation = punctuation_density(text)

    # Low sentence variation is treated as more AI-like.
    spread_score = 1 / (1 + spread)

    # Lower vocabulary variety is treated as more AI-like.
    vocabulary_score = 1 - vocabulary

    # Normalize punctuation density to a 0–1 scale.
    # A density of 0.2 or higher reaches the maximum.
    punctuation_score = 1 - min(punctuation / 0.2, 1.0)

    # Give each measurement equal weight.
    combined_score = (
        spread_score + vocabulary_score + punctuation_score
    ) / 3

    return combined_score


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    # print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
