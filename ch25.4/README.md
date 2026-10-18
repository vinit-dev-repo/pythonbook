# 25.4 - Coverage, TDD and a Callable Boundary

The code of the chapter **25.4 - Coverage, TDD and a Callable Boundary** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What line coverage measures, and why 100% coverage does not prove correctness
- How red, green, refactor drives a function from a failing test
- How `safe_call` keeps the status of a call apart from its result
- How a logging decorator that re-raises differs from a reporting boundary

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

The chapter saves these files more than once (for example a first version and a repaired one). This folder holds the version the chapter ends with, and the table points to that last version:

- `multiples.py`
- `test_coverage_demo.py`
- `test_multiples.py`

| File | Where it is in the chapter | Note |
|---|---|---|
| `calculator.py` | A note on coverage (line 53) |  |
| `test_coverage_demo.py` | A note on coverage (line 100) | rewritten later in the chapter |
| `test_multiples.py` | Test-driven development (line 175) | rewritten later in the chapter |
| `multiples.py` | Test-driven development (line 198) | rewritten later in the chapter |
| `boundaries.py` | A callable boundary and a small driver › Return a status without confusing it with the result (line 238) |  |
| `driver_demo.py` | A callable boundary and a small driver › Run three invocations and inspect surviving state (line 265) |  |
| `decorator_demo.py` | A callable boundary and a small driver › A decorator with a different failure contract (line 340) |  |
| `test_palindrome.py` | Try it yourself (line 413) |  |
| `test_triple.py` | Try it yourself (line 441) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_try-it-yourself.py` | Try it yourself (line 423) | runs on its own |
| `examples/02_try-it-yourself.py` | Try it yourself (line 432) | may use names from earlier examples |
| `examples/03_try-it-yourself.py` | Try it yourself (line 457) | may use names from earlier examples |
