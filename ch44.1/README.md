# 44.1 - Processes, Threads, the GIL, Race Conditions and Locks

The code of the chapter **44.1 - Processes, Threads, the GIL, Race Conditions and Locks** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What processes and threads are, and how they differ
- Concurrency versus parallelism, and why threads on the standard GIL-enabled CPython build do not speed up CPU-bound pure-Python maths
- How to start, join and name threads
- What a **race condition** is, and how to run an example that shows one
- How a `Lock` protects a whole read-modify-write

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `race_schedule.py` | A race condition › Deliberately expose one lost update (line 215) |  |
| `locked_update.py` | Lock: protect a critical section › A small protected counterpart (line 393) |  |
| `exercise_race.py` | Try it yourself (line 478) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-gil-is-finally-becoming-optional.py` | The GIL, honestly › The GIL is finally becoming optional (line 108) | runs on its own |
| `examples/02_creating-threads.py` | Creating threads (line 141) | runs on its own |
| `examples/03_naming-threads-for-readable-demos.py` | Creating threads › Naming threads for readable demos (line 179) | runs on its own |
| `examples/04_an-uncontrolled-stress-run.py` | A race condition › An uncontrolled stress run (line 267) | runs on its own |
| `examples/05_lock-protect-a-critical-section.py` | Lock: protect a critical section (line 348) | runs on its own |
| `examples/06_what-with-lock-does-underneath.py` | Lock: protect a critical section › What `with lock:` does underneath (line 436) | runs on its own |
| `examples/07_try-it-yourself.py` | Try it yourself (line 529) | runs on its own |
