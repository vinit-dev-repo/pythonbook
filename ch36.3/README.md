# 36.3 - contextlib, Nesting, Failed Entry, Generator Errors and Dynamic Resources

The code of the chapter **36.3 - contextlib, Nesting, Failed Entry, Generator Errors and Dynamic Resources** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- A tour of `contextlib`'s ready-made helpers
- How to nest several context managers at once, and in which order they close
- What happens when entry fails, when the `as` target fails and when cleanup fails
- How an exception from the block reaches the generator at its `yield`
- How `ExitStack` closes the files that opened when a later open fails

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_a-tour-of-contextlib.py` | A tour of `contextlib` (line 52) | runs on its own |
| `examples/02_a-tour-of-contextlib.py` | A tour of `contextlib` (line 67) | may use names from earlier examples |
| `examples/03_a-tour-of-contextlib.py` | A tour of `contextlib` (line 90) | may use names from earlier examples |
| `examples/04_nesting-context-managers.py` | Nesting context managers (line 120) | may use names from earlier examples |
| `examples/05_nesting-context-managers.py` | Nesting context managers (line 138) | may use names from earlier examples |
| `examples/06_nesting-context-managers.py` | Nesting context managers (line 153) | may use names from earlier examples |
| `examples/07_observe-failed-entry-binding-and-cleanup.py` | Observe failed entry, binding and cleanup (line 193) | may use names from earlier examples |
| `examples/08_an-exception-travels-back-to-yield.py` | An exception travels back to `yield` (line 275) | may use names from earlier examples |
| `examples/09_an-exception-travels-back-to-yield.py` | An exception travels back to `yield` (line 330) | may use names from earlier examples |
| `examples/10_dynamic-resources-the-second-open-fails.py` | Dynamic resources: the second open fails (line 368) | may use names from earlier examples |
| `examples/11_try-it-yourself.py` | Try it yourself (line 429) | runs on its own |
