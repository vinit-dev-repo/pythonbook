# 34.3 - Pipelines, yield from, Return Values and Practical Patterns

The code of the chapter **34.3 - Pipelines, yield from, Return Values and Practical Patterns** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to connect generators in a lazy pipeline with low extra memory use
- What `yield from` does, and how it flattens nested data
- What happens if a generator uses `return`
- Where a generator fits in practice

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_generator-pipelines.py` | Generator pipelines (line 46) | runs on its own |
| `examples/02_two-input-formats-one-record-writer.py` | Generator pipelines › Two input formats, one record writer (line 93) | runs on its own |
| `examples/03_walk-a-directory-tree-and-prune-work.py` | Generator pipelines › Walk a directory tree and prune work (line 174) | runs on its own |
| `examples/04_yield-from-delegating-to-a-sub-generator.py` | `yield from`: delegating to a sub-generator (line 233) | may use names from earlier examples |
| `examples/05_flattening-nested-structures.py` | `yield from`: delegating to a sub-generator › Flattening nested structures (line 261) | may use names from earlier examples |
| `examples/06_generator-return-values.py` | Generator return values (line 300) | may use names from earlier examples |
| `examples/07_end-with-return-not-an-escaping-stopiteration.py` | Generator return values › End with `return`, not an escaping `StopIteration` (line 333) | runs on its own |
| `examples/08_try-it-yourself.py` | Try it yourself (line 411) | runs on its own |
