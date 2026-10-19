# 44.3 - Queues, Thread Pools, Thread Safety and Choosing a Tool

The code of the chapter **44.3 - Queues, Thread Pools, Thread Safety and Choosing a Tool** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why `queue.Queue` is the safest way to move data between threads
- How a finite batch with two consumers shuts down cleanly and accounts for every task
- How `ThreadPoolExecutor` runs jobs on a pool of worker threads
- Which built-in operations you can trust, and a table for picking the right tool

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `queue_lifecycle.py` | queue.Queue: the safe way to hand off work › A finite batch with two consumers (line 100) |  |
| `test_queue_lifecycle.py` | queue.Queue: the safe way to hand off work › A finite batch with two consumers (line 181) |  |
| `exercise5_queue.py` | Try it yourself (line 377) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_queue-queue-the-safe-way-to-hand-off-work.py` | queue.Queue: the safe way to hand off work (line 43) | runs on its own |
| `examples/02_threadpoolexecutor-preview.py` | ThreadPoolExecutor preview (line 239) | runs on its own |
| `examples/03_try-it-yourself.py` | Try it yourself (line 322) | runs on its own |
