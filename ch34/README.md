# 34 - Generators

The code of the chapter **34 - Generators** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How generators replace a manual iterator class
- How `yield` changes a function call and pauses execution
- When the body of a generator function starts to run
- How generators satisfy the iterator protocol automatically
- How to use a generator method to build a re-iterable object
- Generator expressions, and how they compare to list comprehensions in memory use
- How to connect generators in a lazy pipeline with low extra memory use
- What `yield from` does, and how it flattens nested data
- What happens if a generator uses `return`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_a-first-generator-step-by-step.py` | A first generator, step by step (line 77) | runs on its own |
| `examples/02_a-first-generator-step-by-step.py` | A first generator, step by step (line 112) | raises an error on purpose |
| `examples/03_generators-are-iterators.py` | Generators ARE iterators (line 136) | may use names from earlier examples |
| `examples/04_an-infinite-generator-fibonacci.py` | An infinite generator: Fibonacci (line 175) | may use names from earlier examples |
| `examples/05_an-infinite-generator-fibonacci.py` | An infinite generator: Fibonacci (line 194) | may use names from earlier examples |
| `examples/06_making-a-re-iterable-object-with-a-generator.py` | Making a re-iterable object with a generator (line 217) | may use names from earlier examples |
| `examples/07_a-card-deck-example-nested-yield.py` | A card-deck example: nested `yield` (line 256) | may use names from earlier examples |
| `examples/08_generator-expressions.py` | Generator expressions (line 303) | may use names from earlier examples |
| `examples/09_observe-creation-and-consumption-separately.py` | Observe creation and consumption separately (line 330) | runs on its own |
| `examples/10_from-stored-matches-to-lazy-text-traversal.py` | From stored matches to lazy text traversal (line 387) | runs on its own |
| `examples/11_produce-cyclic-starts-without-storing-every-resu.py` | Produce cyclic starts without storing every result (line 469) | may use names from earlier examples |
| `examples/12_memory-list-comprehension-vs-generator-expressio.py` | Memory: list comprehension vs generator expression (line 509) | may use names from earlier examples |
| `examples/13_numeric-progressions-state-the-number-policy.py` | Numeric progressions: state the number policy (line 555) | runs on its own |
| `examples/14_numeric-progressions-state-the-number-policy.py` | Numeric progressions: state the number policy (line 638) | runs on its own |
| `examples/15_generator-pipelines.py` | Generator pipelines (line 673) | may use names from earlier examples |
| `examples/16_two-input-formats-one-record-writer.py` | Two input formats, one record writer (line 721) | runs on its own |
| `examples/17_walk-a-directory-tree-and-prune-work.py` | Walk a directory tree and prune work (line 802) | runs on its own |
| `examples/18_yield-from-delegating-to-a-sub-generator.py` | `yield from`: delegating to a sub-generator (line 854) | may use names from earlier examples |
| `examples/19_flattening-nested-structures.py` | Flattening nested structures (line 885) | may use names from earlier examples |
| `examples/20_generator-return-values.py` | Generator return values (line 923) | may use names from earlier examples |
| `examples/21_end-with-return-not-an-escaping-stopiteration.py` | End with `return`, not an escaping `StopIteration` (line 959) | runs on its own |
| `examples/22_try-it-yourself.py` | Try it yourself (line 1035) | may use names from earlier examples |
