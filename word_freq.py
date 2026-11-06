#!/usr/bin/env python3
"""Print the 10 most frequent words in a piece of English text.

The text can be given as a file path argument or piped through standard input.
"""

import re
import sys
from collections import Counter


def top_words(text, n=10):
    """Return the n most common words in text as (word, count) pairs."""
    # Lowercase the text and extract words (letters plus inner apostrophes,
    # so contractions like "don't" stay as one word).
    words = re.findall(r"[a-z]+(?:'[a-z]+)*", text.lower())
    return Counter(words).most_common(n)


def main():
    # Read from the file given on the command line, or from stdin otherwise.
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    for word, count in top_words(text):
        print(f"{word}\t{count}")


if __name__ == "__main__":
    main()
