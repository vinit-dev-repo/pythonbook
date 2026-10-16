# 44 - Threads, Locks and Race Conditions

The code of the chapter **44 - Threads, Locks and Race Conditions** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What processes and threads are, and how they differ
- Concurrency vs parallelism, and why threads on the standard GIL-enabled CPython build do not speed up CPU-bound pure-Python maths
- How to start, join and name threads
- What a **race condition** is, and how to run an example that shows one
- How `Lock`, `RLock`, `Semaphore`, `Event` and `Condition` fix different problems
- What a **deadlock** is, and three ways to avoid one
- Why `queue.Queue` is the safest way to move data between threads

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `race_schedule.py` | A race condition › Deliberately expose one lost update (line 215) |  |
| `locked_update.py` | Lock: protect a critical section › A small protected counterpart (line 403) |  |
| `lock_order.py` | Deadlock: everyone waiting forever (line 474) |  |
| `lock_timeout.py` | Deadlock: everyone waiting forever › Three fixes for deadlock (line 578) |  |
| `queue_lifecycle.py` | queue.Queue: the safe way to hand off work › A finite batch with two consumers (line 892) |  |
| `test_queue_lifecycle.py` | queue.Queue: the safe way to hand off work › A finite batch with two consumers (line 971) |  |
| `exercise_race.py` | Try it yourself (line 1105) |  |
| `exercise_lock_order.py` | Try it yourself (line 1174) |  |
| `exercise5_queue.py` | Try it yourself (line 1194) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-gil-is-finally-becoming-optional.py` | The GIL, honestly › The GIL is finally becoming optional (line 109) | runs on its own |
| `examples/02_creating-threads.py` | Creating threads (line 140) | runs on its own |
| `examples/03_naming-threads-for-readable-demos.py` | Creating threads › Naming threads for readable demos (line 180) | runs on its own |
| `examples/04_an-uncontrolled-stress-run.py` | A race condition › An uncontrolled stress run (line 271) | runs on its own |
| `examples/05_lock-protect-a-critical-section.py` | Lock: protect a critical section (line 356) | runs on its own |
| `examples/06_what-with-lock-does-underneath.py` | Lock: protect a critical section › What `with lock:` does underneath (line 447) | runs on its own |
| `examples/07_rlock-a-lock-a-thread-can-re-take.py` | RLock: a lock a thread can re-take (line 635) | may use names from earlier examples |
| `examples/08_semaphore-allow-a-limited-number-of-threads.py` | Semaphore: allow a limited number of threads (line 677) | runs on its own |
| `examples/09_event-signal-waiting-threads.py` | Event: signal waiting threads (line 724) | runs on its own |
| `examples/10_condition-wait-until-something-is-true.py` | Condition: wait until something is true (line 777) | runs on its own |
| `examples/11_queue-queue-the-safe-way-to-hand-off-work.py` | queue.Queue: the safe way to hand off work (line 832) | runs on its own |
| `examples/12_threadpoolexecutor-preview.py` | ThreadPoolExecutor preview (line 1026) | runs on its own |
| `examples/13_try-it-yourself.py` | Try it yourself (line 1155) | runs on its own |
