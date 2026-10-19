# 43.1 - Coroutines, async and await, Tasks, TaskGroup, Limits and Timeouts

The code of the chapter **43.1 - Coroutines, async and await, Tasks, TaskGroup, Limits and Timeouts** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a **coroutine** is, and how it compares with threads and processes
- How to write modern async code with `async def`, `await`, the **event loop**, and `asyncio.run`
- How a timed test shows the difference between `asyncio.sleep` and `time.sleep`
- How to run several tasks with `create_task`, `gather`, and `TaskGroup`
- How group failure cancels a waiting sibling, finishes cleanup and reaches an `except*` handler
- How to limit active work with a semaphore, protect a shared update with a lock, and set time limits

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `await_ready.py` | Modern async: `async def` and `await` › Awaiting a ready operation need not suspend (line 267) |  |
| `group_lifecycle.py` | Modern async: `async def` and `await` › Failure, sibling cancellation and cleanup (line 496) |  |
| `test_group_lifecycle.py` | Modern async: `async def` and `await` › Failure, sibling cancellation and cleanup (line 601) |  |
| `async_limits.py` | Modern async: `async def` and `await` › Limit active work with an async semaphore (line 661) |  |
| `async_counter.py` | Modern async: `async def` and `await` › Shared state across a suspending await (line 771) |  |
| `test_async_limits.py` | Modern async: `async def` and `await` › Shared state across a suspending await (line 844) |  |
| `exercise_async_limits.py` | Modern async: `async def` and `await` › Practice: capacity and shared updates (line 908) |  |
| `exercise_group.py` | Try it yourself (line 1097) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_async-def-defines-a-coroutine.py` | Modern async: `async def` and `await` › `async def` defines a coroutine (line 82) | runs on its own |
| `examples/02_await-pause-here-until-this-finishes.py` | Modern async: `async def` and `await` › `await`: pause here until this finishes (line 107) | may use names from earlier examples |
| `examples/03_asyncio-sleep-compared-with-time-sleep.py` | Modern async: `async def` and `await` › `asyncio.sleep` compared with `time.sleep` (line 152) | may use names from earlier examples |
| `examples/04_asyncio-sleep-compared-with-time-sleep.py` | Modern async: `async def` and `await` › `asyncio.sleep` compared with `time.sleep` (line 164) | may use names from earlier examples |
| `examples/05_asyncio-sleep-compared-with-time-sleep.py` | Modern async: `async def` and `await` › `asyncio.sleep` compared with `time.sleep` (line 186) | may use names from earlier examples |
| `examples/06_asyncio-sleep-compared-with-time-sleep.py` | Modern async: `async def` and `await` › `asyncio.sleep` compared with `time.sleep` (line 208) | may use names from earlier examples |
| `examples/07_creating-tasks-schedule-now-and-await-later.py` | Modern async: `async def` and `await` › Creating tasks: schedule now and await later (line 236) | may use names from earlier examples |
| `examples/08_gather-run-several-operations-and-collect-result.py` | Modern async: `async def` and `await` › `gather`: run several operations and collect results (line 308) | may use names from earlier examples |
| `examples/09_gather-run-several-operations-and-collect-result.py` | Modern async: `async def` and `await` › `gather`: run several operations and collect results (line 337) | may use names from earlier examples |
| `examples/10_observe-a-surviving-sibling-after-gather-fails.py` | Modern async: `async def` and `await` › Observe a surviving sibling after `gather` fails (line 367) | may use names from earlier examples |
| `examples/11_taskgroup-manage-related-tasks-3-11.py` | Modern async: `async def` and `await` › `TaskGroup`: manage related tasks (3.11+) (line 425) | may use names from earlier examples |
| `examples/12_stop-a-group-early-with-cancel-3-15.py` | Modern async: `async def` and `await` › Stop a group early with `cancel()` (3.15) (line 459) | may use names from earlier examples |
| `examples/13_timeouts-limit-how-long-code-waits.py` | Modern async: `async def` and `await` › Timeouts: limit how long code waits (line 947) | may use names from earlier examples |
| `examples/14_timeouts-limit-how-long-code-waits.py` | Modern async: `async def` and `await` › Timeouts: limit how long code waits (line 970) | may use names from earlier examples |
| `examples/15_try-it-yourself.py` | Try it yourself (line 1025) | may use names from earlier examples |
