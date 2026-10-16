# 44 - Threads, Locks and Race Conditions

The code of this chapter of the Python tutorial, extracted byte for byte from the certified chapter. The chapter explains every line; read it there.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

- `exercise5_queue.py`
- `exercise_lock_order.py`
- `exercise_race.py`
- `lock_order.py`
- `lock_timeout.py`
- `locked_update.py`
- `queue_lifecycle.py`
- `race_schedule.py`
- `test_queue_lifecycle.py`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Section | Note |
|---|---|---|
| `examples/01_the-gil-is-finally-becoming-optional.py` | The GIL is finally becoming optional | runs on its own |
| `examples/02_creating-threads.py` | Creating threads | runs on its own |
| `examples/03_naming-threads-for-readable-demos.py` | Naming threads for readable demos | runs on its own |
| `examples/04_an-uncontrolled-stress-run.py` | An uncontrolled stress run | runs on its own |
| `examples/05_lock-protect-a-critical-section.py` | Lock: protect a critical section | runs on its own |
| `examples/06_what-with-lock-does-underneath.py` | What `with lock:` does underneath | runs on its own |
| `examples/07_rlock-a-lock-a-thread-can-re-take.py` | RLock: a lock a thread can re-take | may use names from earlier examples |
| `examples/08_semaphore-allow-a-limited-number-of-threads.py` | Semaphore: allow a limited number of threads | runs on its own |
| `examples/09_event-signal-waiting-threads.py` | Event: signal waiting threads | runs on its own |
| `examples/10_condition-wait-until-something-is-true.py` | Condition: wait until something is true | runs on its own |
| `examples/11_queue-queue-the-safe-way-to-hand-off-work.py` | queue.Queue: the safe way to hand off work | runs on its own |
| `examples/12_threadpoolexecutor-preview.py` | ThreadPoolExecutor preview | runs on its own |
| `examples/13_try-it-yourself.py` | Try it yourself | runs on its own |
