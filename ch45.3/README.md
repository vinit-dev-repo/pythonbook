# 45.3 - Pool, concurrent.futures, submit and Future States

The code of the chapter **45.3 - Pool, concurrent.futures, submit and Future States** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- `Pool` and the modern, unified `concurrent.futures` executors
- How `submit` and `as_completed` give results as they finish
- How a future ends as a value, an error or a cancellation, and what shutdown does

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `future_lifecycle.py` | concurrent.futures: the modern, unified interface › Futures can succeed, fail or be cancelled (line 199) |  |
| `buffered_map.py` | concurrent.futures: the modern, unified interface › Worker count does not bound all submitted work (line 372) |  |
| `test_future_lifecycle.py` | concurrent.futures: the modern, unified interface › Worker count does not bound all submitted work (line 430) |  |
| `exercise_futures.py` | Try it yourself (line 558) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_pool-mapping-over-many-inputs.py` | Pool: mapping over many inputs (line 43) | runs on its own |
| `examples/02_pool-mapping-over-many-inputs.py` | Pool: mapping over many inputs (line 67) | runs on its own |
| `examples/03_concurrent-futures-the-modern-unified-interface.py` | concurrent.futures: the modern, unified interface (line 100) | runs on its own |
| `examples/04_submit-and-as-completed-results-as-they-finish.py` | concurrent.futures: the modern, unified interface › submit and as_completed: results as they finish (line 135) | may use names from earlier examples |
| `examples/05_try-it-yourself.py` | Try it yourself (line 514) | runs on its own |
