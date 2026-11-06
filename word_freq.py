#!/usr/bin/env python3
"""Print the 10 most frequent words in a piece of English text.

Common stop words such as "the" and "and" are skipped.

The text can be given as a file path argument or piped through standard input.
"""

import re
import sys
from collections import Counter

# Common English words that carry little meaning on their own. These are
# skipped when counting so the results show the more interesting words.
STOP_WORDS = frozenset("""
a about above after again against all am an and any are as at be because been
before being below between both but by can could did do does doing down during
each few for from further had has have having he her here hers herself him
himself his how i if in into is it its itself just me more most my myself no
nor not now of off on once only or other our ours ourselves out over own same
she should so some such than that the their theirs them themselves then there
these they this those through to too under until up very was we were what when
where which while who whom why will with would you your yours yourself
yourselves
""".split())


def top_words(text, n=10):
    """Return the n most common words in text as (word, count) pairs."""
    # Lowercase the text and extract words (letters plus inner apostrophes,
    # so contractions like "don't" stay as one word).
    words = re.findall(r"[a-z]+(?:'[a-z]+)*", text.lower())
    return Counter(w for w in words if w not in STOP_WORDS).most_common(n)


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
