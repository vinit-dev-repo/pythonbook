# 35.1 - What itertools Is, Aggregators, Slicing, Filtering and takewhile and dropwhile

The code of the chapter **35.1 - What itertools Is, Aggregators, Slicing, Filtering and takewhile and dropwhile** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What `itertools` provides, which tools read input immediately, and which tools produce output lazily
- How `min`, `max`, `sum`, `any` and `all` consume input, and what short-circuiting means
- How to select values of an iterator by position without creating a list
- How `filterfalse` and `compress` select items by truth values
- How `takewhile` and `dropwhile` split a stream at the first failing item

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-itertools-is.py` | What itertools is (line 45) | runs on its own |
| `examples/02_aggregators-recap-min-max-sum-any-all.py` | Aggregators recap: min, max, sum, any, all (line 92) | may use names from earlier examples |
| `examples/03_aggregators-recap-min-max-sum-any-all.py` | Aggregators recap: min, max, sum, any, all (line 105) | may use names from earlier examples |
| `examples/04_empty-input-and-the-state-left-after-a-reduction.py` | Aggregators recap: min, max, sum, any, all › Empty input and the state left after a reduction (line 132) | runs on its own |
| `examples/05_slicing-an-iterator-islice.py` | Slicing an iterator: islice (line 179) | raises an error on purpose |
| `examples/06_slicing-an-iterator-islice.py` | Slicing an iterator: islice (line 194) | may use names from earlier examples |
| `examples/07_slicing-an-iterator-islice.py` | Slicing an iterator: islice (line 214) | may use names from earlier examples |
| `examples/08_filter-recap.py` | Selecting and filtering › filter: recap (line 249) | may use names from earlier examples |
| `examples/09_filterfalse-the-opposite-of-filter.py` | Selecting and filtering › filterfalse: the opposite of filter (line 262) | may use names from earlier examples |
| `examples/10_compress-pick-by-a-mask.py` | Selecting and filtering › compress: pick by a mask (line 282) | may use names from earlier examples |
| `examples/11_takewhile-and-dropwhile.py` | takewhile and dropwhile (line 325) | may use names from earlier examples |
| `examples/12_try-it-yourself.py` | Try it yourself (line 376) | runs on its own |
