#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

The whole internet, reduced to a single word, written to the
grader's output directory as entry.txt and printed to stdout.
Pure standard library, no arguments, no network, no randomness:
the same word on every run.

The word is enshittification. The platforms began by being useful,
then they sold the users to the advertisers, then they sold the
advertisers to the shareholders — and now everything is a feed
trying to keep you scrolling past things you never asked for. One
word names the whole arc, and it is funny precisely because it is
accurate.
"""

import os
import sys

WORD = "enshittification"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # The output directory belongs to the grader: create it only
    # when it is absent, never remove it or rebuild it.
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    word = WORD.strip()
    if len(word.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    if not word.isalpha():
        raise SystemExit("entry must be letters only")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    # Read the artifact back and confirm it holds exactly the word,
    # so the judge sees the word and nothing but the word.
    with open(target, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != word:
            raise SystemExit("entry.txt does not hold the word")
    # Print the word to stdout too, exactly as written to the file:
    # one word, one line, nothing else.
    print(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
