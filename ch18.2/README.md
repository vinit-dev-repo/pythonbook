# 18.2 - Timer, Logger, Stacking and Memoization

The code of the chapter **18.2 - Timer, Logger, Stacking and Memoization** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to write a timer and a logger, and how to stack several decorators together
- Why decorator order changes what is measured and printed
- How to remember answers a function already worked out (memoization), by hand and with `functools.lru_cache`
- How a bounded cache evicts entries, and why a cached mutable result is shared

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_a-timer.py` | A timer (line 43) | runs on its own |
| `examples/02_a-timer.py` | A timer (line 62) | may use names from earlier examples |
| `examples/03_a-logger.py` | A logger (line 91) | may use names from earlier examples |
| `examples/04_stacking-decorators.py` | Stacking decorators (line 130) | may use names from earlier examples |
| `examples/05_stacking-decorators.py` | Stacking decorators (line 149) | runs on its own |
| `examples/06_by-hand-with-a-cache-dictionary.py` | Memoization: remembering answers › By hand, with a cache dictionary (line 180) | may use names from earlier examples |
| `examples/07_the-built-in-version-functools-lru-cache.py` | Memoization: remembering answers › The built-in version: `functools.lru_cache` (line 215) | may use names from earlier examples |
| `examples/08_the-built-in-version-functools-lru-cache.py` | Memoization: remembering answers › The built-in version: `functools.lru_cache` (line 238) | may use names from earlier examples |
| `examples/09_the-built-in-version-functools-lru-cache.py` | Memoization: remembering answers › The built-in version: `functools.lru_cache` (line 279) | may use names from earlier examples |
| `examples/10_the-built-in-version-functools-lru-cache.py` | Memoization: remembering answers › The built-in version: `functools.lru_cache` (line 313) | may use names from earlier examples |
| `examples/11_try-it-yourself.py` | Try it yourself (line 369) | may use names from earlier examples |
