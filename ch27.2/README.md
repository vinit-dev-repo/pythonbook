# 27.2 - Decorator Classes and Configured Decorators

The code of the chapter **27.2 - Decorator Classes and Configured Decorators** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Explain why a callable decorator instance does not automatically bind like a method.
- Write a decorator class that counts attempts and keeps its own state for each function.
- Trace configured decoration separately from later wrapper calls.
- Keep timing totals in a function wrapper without losing the receiver.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `call_timings.py` | Retain timing totals without losing the receiver (line 382) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_decorator-classes.py` | Decorator classes (line 42) | runs on its own |
| `examples/02_a-wrapper-object-keeps-its-own-state.py` | Decorator classes › A wrapper object keeps its own state (line 88) | runs on its own |
| `examples/03_method-binding-has-two-receivers.py` | Decorator classes › Method binding has two receivers (line 163) | runs on its own |
| `examples/04_dispatch-on-a-method-argument.py` | Decorator classes › Dispatch on a method argument (line 248) | runs on its own |
| `examples/05_a-configured-decorator-creates-a-wrapper-functio.py` | A configured decorator creates a wrapper function (line 310) | runs on its own |
| `examples/06_try-it-yourself.py` | Try it yourself (line 482) | runs on its own |
