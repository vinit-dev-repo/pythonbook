# 45.1 - Why Multiprocessing, Process, the Main Guard and Comparing CPU-Bound Work

The code of the chapter **45.1 - Why Multiprocessing, Process, the Main Guard and Comparing CPU-Bound Work** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why GIL-enabled CPython threads do not execute pure-Python bytecode on several cores simultaneously, and how processes can
- How to start real parallel work with `multiprocessing.Process`
- Why process-starting code needs the `__main__` guard, especially on Windows
- How to measure serial code, threads and processes on your own Python build

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_multiprocessing-process-a-mirror-of-thread.py` | multiprocessing.Process: a mirror of Thread (line 75) | runs on its own |
| `examples/02_compare-cpu-bound-work.py` | Compare CPU-bound work (line 119) | runs on its own |
| `examples/03_compare-cpu-bound-work.py` | Compare CPU-bound work (line 189) | may use names from earlier examples |
| `examples/04_try-it-yourself.py` | Try it yourself (line 224) | runs on its own |
