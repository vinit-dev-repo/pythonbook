# 43.2 - Blocking Calls, to_thread, async for, Async Generators and a Fetch Project

The code of the chapter **43.2 - Blocking Calls, to_thread, async for, Async Generators and a Fetch Project** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to tell work that async helps from work that it does not help
- How to call blocking functions safely with `asyncio.to_thread`, and why a timeout cannot stop a running worker thread
- `async for` and `async with`, and the async iterator protocol
- How an async generator closes early with `aclosing`
- A small worked project that fetches several things at once

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `to_thread_lifecycle.py` | What `async` is for, and what it is NOT for › A timed-out wait can leave a worker running (line 155) |  |
| `test_to_thread_lifecycle.py` | What `async` is for, and what it is NOT for › Check the actual task and worker states (line 260) |  |
| `exercise_to_thread_lifecycle.py` | What `async` is for, and what it is NOT for › Practice: preserve a result without abandoning work (line 320) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_calls-between-async-and-regular-functions.py` | What `async` is for, and what it is NOT for › Calls between async and regular functions (line 59) | runs on its own |
| `examples/02_calls-between-async-and-regular-functions.py` | What `async` is for, and what it is NOT for › Calls between async and regular functions (line 75) | may use names from earlier examples |
| `examples/03_calls-between-async-and-regular-functions.py` | What `async` is for, and what it is NOT for › Calls between async and regular functions (line 96) | may use names from earlier examples |
| `examples/04_calls-between-async-and-regular-functions.py` | What `async` is for, and what it is NOT for › Calls between async and regular functions (line 117) | may use names from earlier examples |
| `examples/05_async-for-and-async-with.py` | `async for` and `async with` (line 369) | may use names from earlier examples |
| `examples/06_async-generators-and-early-cleanup.py` | Async generators and early cleanup (line 413) | may use names from earlier examples |
| `examples/07_mini-project-fetching-several-things-concurrentl.py` | Mini project: fetching several things concurrently (line 474) | runs on its own |
| `examples/08_try-it-yourself.py` | Try it yourself (line 551) | runs on its own |
