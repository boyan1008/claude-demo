# Word Frequency Counter

A small Python script that prints the 10 most frequent words in a piece of English text.

## Requirements

Python 3.6 or newer. No third-party packages are needed.

## Usage

Pass a text file as an argument:

```bash
python3 word_freq.py input.txt
```

Or pipe text through standard input:

```bash
echo "the cat and the dog and the bird" | python3 word_freq.py
```

Output is one word per line, followed by a tab and its count, sorted from most to least frequent:

```
the	3
and	2
cat	1
dog	1
bird	1
```

## Notes

- Words are matched case-insensitively ("The" and "the" count as the same word).
- Punctuation and digits are ignored; contractions such as "don't" are kept as one word.
- Common words like "the" and "and" are not filtered out.
