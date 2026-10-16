# 06 - Lists, Tuples and Strings

The code of the chapter **06 - Lists, Tuples and Strings** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a **sequence** is, and the three you'll use daily: `list`s, `tuple`s, `string`s
- Lists: creating, reading, changing, and the everyday list methods
- Tuples: what "immutable" means, and when a tuple beats a list
- Slicing — selecting items with `[start:stop:step]`, for lists *and* strings
- Why `b = a` does not copy a list, and the three ways to actually copy one
- Unpacking — pulling values out of a sequence into separate names
- Strings in depth: quoting, escapes, methods, and f-strings
- Unicode characters — why emoji work

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_lists.py` | Lists (line 61) | runs on its own |
| `examples/02_indexing.py` | Indexing (line 82) | may use names from earlier examples |
| `examples/03_negative-indexes.py` | Negative indexes (line 118) | may use names from earlier examples |
| `examples/04_len.py` | `len()` (line 136) | may use names from earlier examples |
| `examples/05_changing-a-list-append-insert-remove-pop.py` | Changing a list: append, insert, remove, pop (line 166) | may use names from earlier examples |
| `examples/06_checking-membership-with-in.py` | Checking membership with in (line 206) | may use names from earlier examples |
| `examples/07_iterating-over-a-list.py` | Iterating over a list (line 225) | may use names from earlier examples |
| `examples/08_nesting.py` | Nesting (line 249) | may use names from earlier examples |
| `examples/09_changing-a-list-while-you-loop-over-it.py` | Changing a list while you loop over it (line 273) | may use names from earlier examples |
| `examples/10_changing-a-list-while-you-loop-over-it.py` | Changing a list while you loop over it (line 296) | may use names from earlier examples |
| `examples/11_changing-a-list-while-you-loop-over-it.py` | Changing a list while you loop over it (line 320) | may use names from earlier examples |
| `examples/12_tuples.py` | Tuples (line 341) | may use names from earlier examples |
| `examples/13_why-immutable-and-when-to-prefer-a-tuple.py` | Why immutable, and when to prefer a tuple (line 357) | raises an error on purpose |
| `examples/14_the-one-item-tuple-trap.py` | The one-item tuple trap (line 386) | may use names from earlier examples |
| `examples/15_slicing.py` | Slicing (line 420) | may use names from earlier examples |
| `examples/16_the-step.py` | The step (line 441) | may use names from earlier examples |
| `examples/17_negative-steps-reversing.py` | Negative steps: reversing (line 464) | may use names from earlier examples |
| `examples/18_slicing-strings.py` | Slicing strings (line 485) | may use names from earlier examples |
| `examples/19_why-b-a-does-not-copy.py` | Why `b = a` does not copy? (line 510) | may use names from earlier examples |
| `examples/20_shallow-copy.py` | Shallow copy (line 537) | may use names from earlier examples |
| `examples/21_deep-copy.py` | Deep copy (line 582) | may use names from earlier examples |
| `examples/22_deep-copy.py` | Deep copy (line 615) | may use names from earlier examples |
| `examples/23_deep-copy.py` | Deep copy (line 650) | may use names from earlier examples |
| `examples/24_how-deep-can-a-deep-copy-go.py` | How deep can a deep copy go? (line 691) | may use names from earlier examples |
| `examples/25_unpacking.py` | Unpacking (line 727) | may use names from earlier examples |
| `examples/26_swapping-with-unpacking.py` | Swapping with unpacking (line 748) | may use names from earlier examples |
| `examples/27_extended-unpacking-with-rest.py` | Extended unpacking with `*rest` (line 770) | may use names from earlier examples |
| `examples/28_extended-unpacking-with-rest.py` | Extended unpacking with `*rest` (line 783) | may use names from earlier examples |
| `examples/29_extended-unpacking-with-rest.py` | Extended unpacking with `*rest` (line 806) | may use names from earlier examples |
| `examples/30_quoting.py` | Quoting (line 839) | may use names from earlier examples |
| `examples/31_escape-characters.py` | Escape characters (line 873) | may use names from earlier examples |
| `examples/32_multi-line-strings.py` | Multi-line strings (line 893) | may use names from earlier examples |
| `examples/33_strings-are-immutable-sequences.py` | Strings are immutable sequences (line 914) | raises an error on purpose |
| `examples/34_strings-are-immutable-sequences.py` | Strings are immutable sequences (line 929) | may use names from earlier examples |
| `examples/35_common-string-methods.py` | Common string methods (line 979) | may use names from earlier examples |
| `examples/36_split-only-where-the-format-permits-it.py` | Split only where the format permits it (line 1019) | may use names from earlier examples |
| `examples/37_split-only-where-the-format-permits-it.py` | Split only where the format permits it (line 1038) | may use names from earlier examples |
| `examples/38_split-only-where-the-format-permits-it.py` | Split only where the format permits it (line 1050) | may use names from earlier examples |
| `examples/39_remove-an-exact-ending-or-a-set-of-characters.py` | Remove an exact ending or a set of characters (line 1076) | may use names from earlier examples |
| `examples/40_replace-once-and-keep-the-result.py` | Replace once and keep the result (line 1111) | may use names from earlier examples |
| `examples/41_replace-once-and-keep-the-result.py` | Replace once and keep the result (line 1129) | may use names from earlier examples |
| `examples/42_replace-once-and-keep-the-result.py` | Replace once and keep the result (line 1142) | may use names from earlier examples |
| `examples/43_replace-once-and-keep-the-result.py` | Replace once and keep the result (line 1156) | may use names from earlier examples |
| `examples/44_replace-once-and-keep-the-result.py` | Replace once and keep the result (line 1182) | may use names from earlier examples |
| `examples/45_f-strings-in-depth.py` | f-strings in depth (line 1205) | may use names from earlier examples |
| `examples/46_expressions-inside-the-braces.py` | Expressions inside the braces (line 1218) | may use names from earlier examples |
| `examples/47_formatting-numbers.py` | Formatting numbers (line 1240) | may use names from earlier examples |
| `examples/48_older-ways-to-format-text.py` | Older ways to format text (line 1267) | may use names from earlier examples |
| `examples/49_older-ways-to-format-text.py` | Older ways to format text (line 1289) | may use names from earlier examples |
| `examples/50_unicode-characters.py` | Unicode characters (line 1313) | may use names from earlier examples |
| `examples/51_can-you-create-your-own-character.py` | Can you create your own character? (line 1343) | may use names from earlier examples |
| `examples/52_try-it-yourself.py` | Try it yourself (line 1396) | may use names from earlier examples |
