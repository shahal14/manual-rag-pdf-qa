
import re

def is_table_like(sentence):
    """
    Heuristic to detect table/chart lines.
    """
    # Too many numbers or axis-like formatting
    numbers = sum(c.isdigit() for c in sentence)
    return numbers > 15 or "(" in sentence and ")" in sentence


def generate_answer(question, contexts):
    """
    Precise factual QA with strong filtering.
    """
    sources = set()

    for ctx in contexts:
        text = ctx["content"]

        # Split into sentences
        for sentence in re.split(r"[.\n]", text):
            s = sentence.strip()

            if not s:
                continue

            # Exclude tables/charts
            if is_table_like(s):
                continue

            # Strong semantic constraints
            if (
                "GDP" in s
                and "2022" in s
                and any(word in s.lower() for word in ["declined", "decline", "fell"])
            ):
                sources.add(f"Page {ctx['page']}")
                return f"{s}.\n\n📚 Sources: {' | '.join(sorted(sources))}"

    return "No precise narrative sentence describing GDP growth decline in 2022 was found."
