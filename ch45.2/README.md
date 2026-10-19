# 45.2 - Exchanging Data between Processes with Queue, Pipe and Value

The code of the chapter **45.2 - Exchanging Data between Processes with Queue, Pipe and Value** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to pass data between processes safely with `Queue`, `Pipe` and shared memory
- How to observe a child's reply, exit status and cleanup
- How to share one counter with `Value` and its lock

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `process_lifecycle.py` | Exchanging data between processes › Observe child completion and release resources (line 111) |  |
| `test_process_lifecycle.py` | Exchanging data between processes › Observe child completion and release resources (line 281) |  |
| `exercise_process.py` | Exchanging data between processes › Practice: diagnose two child outcomes (line 346) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_multiprocessing-queue.py` | Exchanging data between processes › multiprocessing.Queue (line 45) | runs on its own |
| `examples/02_pipe.py` | Exchanging data between processes › Pipe (line 72) | runs on its own |
| `examples/03_shared-storage-with-value.py` | Exchanging data between processes › Shared storage with `Value` (line 389) | runs on its own |
| `examples/04_try-it-yourself.py` | Try it yourself (line 445) | runs on its own |
