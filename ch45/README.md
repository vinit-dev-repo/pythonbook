# 45 - Multiprocessing and Pools

The code of the chapter **45 - Multiprocessing and Pools** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why GIL-enabled CPython threads do not execute pure-Python bytecode on several cores simultaneously, and how processes can
- How to start real parallel work with `multiprocessing.Process`
- Why process-starting code needs the `__main__` guard, especially on Windows
- How to measure serial code, threads and processes on your own Python build
- How to pass data between processes safely with `Queue`, `Pipe` and shared memory
- `Pool` and the modern, unified `concurrent.futures` executors
- Two complete examples: fetching many URLs and running a CPU-heavy batch job
- How to choose between threads, processes and `async` for a new piece of code

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `process_lifecycle.py` | Exchanging data between processes › Observe child completion and release resources (line 277) |  |
| `test_process_lifecycle.py` | Exchanging data between processes › Observe child completion and release resources (line 446) |  |
| `exercise_process.py` | Exchanging data between processes › Practice: diagnose two child outcomes (line 512) |  |
| `future_lifecycle.py` | concurrent.futures: the modern, unified interface › Futures can succeed, fail or be cancelled (line 756) |  |
| `buffered_map.py` | concurrent.futures: the modern, unified interface › Worker count does not bound all submitted work (line 929) |  |
| `test_future_lifecycle.py` | concurrent.futures: the modern, unified interface › Worker count does not bound all submitted work (line 988) |  |
| `exercise_futures.py` | Try it yourself (line 1265) |  |
| `compare_artifact_schedules.py` | Try it yourself › Transfer lab: compare three schedules against the same local service (line 1351) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_multiprocessing-process-a-mirror-of-thread.py` | multiprocessing.Process: a mirror of Thread (line 72) | runs on its own |
| `examples/02_compare-cpu-bound-work.py` | Compare CPU-bound work (line 115) | runs on its own |
| `examples/03_compare-cpu-bound-work.py` | Compare CPU-bound work (line 185) | may use names from earlier examples |
| `examples/04_multiprocessing-queue.py` | Exchanging data between processes › multiprocessing.Queue (line 208) | runs on its own |
| `examples/05_pipe.py` | Exchanging data between processes › Pipe (line 236) | runs on its own |
| `examples/06_shared-storage-with-value.py` | Exchanging data between processes › Shared storage with `Value` (line 556) | runs on its own |
| `examples/07_pool-mapping-over-many-inputs.py` | Pool: mapping over many inputs (line 597) | runs on its own |
| `examples/08_pool-mapping-over-many-inputs.py` | Pool: mapping over many inputs (line 621) | runs on its own |
| `examples/09_concurrent-futures-the-modern-unified-interface.py` | concurrent.futures: the modern, unified interface (line 651) | runs on its own |
| `examples/10_submit-and-as-completed-results-as-they-finish.py` | concurrent.futures: the modern, unified interface › submit and as_completed: results as they finish (line 688) | may use names from earlier examples |
| `examples/11_example-1-fetch-many-urls-with-threads.py` | Example 1: fetch many URLs with threads (line 1057) | may use names from earlier examples |
| `examples/12_example-2-run-a-cpu-batch-job-with-processes.py` | Example 2: run a CPU batch job with processes (line 1102) | runs on its own |
| `examples/13_choosing-between-threads-processes-and-async.py` | Choosing between threads, processes and async (line 1156) | may use names from earlier examples |
| `examples/14_try-it-yourself.py` | Try it yourself (line 1196) | runs on its own |
