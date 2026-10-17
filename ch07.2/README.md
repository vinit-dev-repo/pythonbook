# 07.2 - Hashable Keys and How Lookup Works

The code of the chapter **07.2 - Hashable Keys and How Lookup Works** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why dictionary keys must be **hashable**, in plain words
- How a dictionary turns a hash into a slot, and what a collision is
- Which values can be keys, and what `frozendict` adds

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_how-a-dictionary-uses-the-hash.py` | Keys must be hashable › How a dictionary uses the hash (line 47) | runs on its own |
| `examples/02_how-a-dictionary-uses-the-hash.py` | Keys must be hashable › How a dictionary uses the hash (line 67) | may use names from earlier examples |
| `examples/03_which-values-can-be-keys.py` | Keys must be hashable › Which values can be keys (line 83) | may use names from earlier examples |
| `examples/04_which-values-can-be-keys.py` | Keys must be hashable › Which values can be keys (line 94) | raises an error on purpose |
| `examples/05_which-values-can-be-keys.py` | Keys must be hashable › Which values can be keys (line 110) | raises an error on purpose |
| `examples/06_a-dictionary-that-cannot-change-frozendict-3-15.py` | Keys must be hashable › A dictionary that cannot change: `frozendict` (3.15) (line 141) | may use names from earlier examples |
| `examples/07_a-dictionary-that-cannot-change-frozendict-3-15.py` | Keys must be hashable › A dictionary that cannot change: `frozendict` (3.15) (line 160) | raises an error on purpose |
| `examples/08_equal-keys-must-have-equal-hashes.py` | Keys must be hashable › Equal keys must have equal hashes (line 181) | may use names from earlier examples |
