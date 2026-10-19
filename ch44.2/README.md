# 44.2 - Deadlock, RLock, Semaphore, Event and Condition

The code of the chapter **44.2 - Deadlock, RLock, Semaphore, Event and Condition** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a **deadlock** is, and three ways to avoid one
- How an `RLock` lets one thread take the same lock again
- How a `Semaphore` limits the threads inside a block
- How an `Event` signals many waiting threads
- How a `Condition` makes a thread wait until a state is true

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `lock_order.py` | Deadlock: everyone waiting forever (line 43) |  |
| `lock_timeout.py` | Deadlock: everyone waiting forever › Three fixes for deadlock (line 144) |  |
| `exercise_lock_order.py` | Try it yourself (line 479) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_rlock-a-lock-a-thread-can-re-take.py` | RLock: a lock a thread can re-take (line 203) | runs on its own |
| `examples/02_semaphore-allow-a-limited-number-of-threads.py` | Semaphore: allow a limited number of threads (line 245) | runs on its own |
| `examples/03_event-signal-waiting-threads.py` | Event: signal waiting threads (line 295) | runs on its own |
| `examples/04_condition-wait-until-something-is-true.py` | Condition: wait until something is true (line 351) | runs on its own |
| `examples/05_try-it-yourself.py` | Try it yourself (line 422) | runs on its own |
| `examples/06_try-it-yourself.py` | Try it yourself (line 460) | runs on its own |
