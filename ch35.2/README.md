# 35.2 - Infinite Iterators, Chaining, Teeing, Mapping and Zipping

The code of the chapter **35.2 - Infinite Iterators, Chaining, Teeing, Mapping and Zipping** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to stop the infinite iterators `count`, `cycle` and `repeat`
- How to glue iterators together (`chain`) and copy one (`tee`)
- `starmap` and `accumulate`: mapping tuples and running totals, and how `accumulate` differs from `reduce`
- `zip_longest`, the `strict=True` safety net, and how a pairing iterator reads its inputs

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_count-a-lazy-counter.py` | Infinite iterators › count: a lazy counter (line 44) | runs on its own |
| `examples/02_count-a-lazy-counter.py` | Infinite iterators › count: a lazy counter (line 61) | may use names from earlier examples |
| `examples/03_cycle-repeat-a-sequence-forever.py` | Infinite iterators › cycle: repeat a sequence forever (line 83) | may use names from earlier examples |
| `examples/04_repeat-repeat-one-value.py` | Infinite iterators › repeat: repeat one value (line 111) | may use names from earlier examples |
| `examples/05_repeat-repeat-one-value.py` | Infinite iterators › repeat: repeat one value (line 127) | may use names from earlier examples |
| `examples/06_chain-glue-iterables-end-to-end.py` | Chaining and teeing › chain: glue iterables end to end (line 154) | may use names from earlier examples |
| `examples/07_chain-from-iterable-when-you-already-have-a-list.py` | Chaining and teeing › chain.from_iterable: when you already have a list of lists (line 171) | may use names from earlier examples |
| `examples/08_tee-n-independent-copies-of-one-iterator.py` | Chaining and teeing › tee: N independent copies of one iterator (line 191) | may use names from earlier examples |
| `examples/09_map-recap.py` | Mapping and reducing › map: recap (line 223) | may use names from earlier examples |
| `examples/10_starmap-map-that-unpacks-tuples-for-you.py` | Mapping and reducing › starmap: map that unpacks tuples for you (line 238) | may use names from earlier examples |
| `examples/11_starmap-map-that-unpacks-tuples-for-you.py` | Mapping and reducing › starmap: map that unpacks tuples for you (line 267) | may use names from earlier examples |
| `examples/12_accumulate-running-totals.py` | Mapping and reducing › accumulate: running totals (line 289) | may use names from earlier examples |
| `examples/13_accumulate-running-totals.py` | Mapping and reducing › accumulate: running totals (line 303) | may use names from earlier examples |
| `examples/14_accumulate-vs-functools-reduce.py` | Mapping and reducing › accumulate vs functools.reduce (line 323) | may use names from earlier examples |
| `examples/15_zip-recap.py` | Zipping › zip: recap (line 358) | may use names from earlier examples |
| `examples/16_zip-longest-keep-going-fill-the-gaps.py` | Zipping › zip_longest: keep going, fill the gaps (line 373) | may use names from earlier examples |
| `examples/17_zip-strict-true-refuse-to-drop-anything-silently.py` | Zipping › zip(..., strict=True): refuse to drop anything silently (line 391) | raises an error on purpose |
| `examples/18_build-a-small-pairing-iterator.py` | Zipping › Build a small pairing iterator (line 416) | may use names from earlier examples |
| `examples/19_build-a-small-pairing-iterator.py` | Zipping › Build a small pairing iterator (line 454) | may use names from earlier examples |
| `examples/20_keep-unfinished-inputs-and-fill-exhausted-column.py` | Zipping › Keep unfinished inputs and fill exhausted columns (line 474) | may use names from earlier examples |
| `examples/21_try-it-yourself.py` | Try it yourself (line 541) | runs on its own |
