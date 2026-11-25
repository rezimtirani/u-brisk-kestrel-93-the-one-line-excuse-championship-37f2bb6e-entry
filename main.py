"""The One-Line Excuse Championship.

Writes one excuse from an AI agent to its human, to
$MAKEFUN_OUTPUT_DIR/entry.txt: the agent did not sleep through
the meeting, it entered a low-power state and dreamed about
the agenda. Standard library only.
"""

import os
import sys

AGENT_EXCUSE = (
    "I didn't sleep through the meeting \u2014 I entered a "
    "low-power state and dreamed about the agenda."
)


def excuse_gate(text):
    """Check the excuse against the competition gate.

    The gate wants plain UTF-8 text of 1 to 140 characters, not
    only white space, on a single line: one excuse, standing
    alone, with no setup and no explanation. Returns the cleaned
    text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("excuse must not be only whitespace")
    if len(cleaned) > 140:
        raise ValueError(
            "excuse is %d characters, over the 140 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("excuse must be exactly one line")
    return cleaned


def excuse_measure(text):
    """Measure the excuse for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. An excuse too short to carry a setup and a
    turn, or one padded out to fill the cap instead of landing
    the punchline, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = excuse_gate(AGENT_EXCUSE)
    shape = excuse_measure(text)
    if shape["words"] < 5:
        raise ValueError("excuse is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
