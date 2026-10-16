# 43 - From Coroutines to async-await

The code of the chapter **43 - From Coroutines to async-await** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a **coroutine** is, and how it compares with threads and processes
- How to write modern async code with `async def`, `await`, the **event loop**, and `asyncio.run`
- How a timed test shows the difference between `asyncio.sleep` and `time.sleep`
- How to run several tasks with `create_task`, `gather`, and `TaskGroup`
- How to set time limits, choose work for async code, and call blocking functions safely
- `async for` and `async with`, and a small worked project that fetches several things at once
- How a local HTTP client/server lab preserves request identity, counts completed outcomes and waits for file writes
- How group failure cancels a waiting sibling, finishes cleanup and reaches an `except*` handler
- Optional history: generator-coroutine `send`, states, priming, `close`, `throw` and `yield from` for reading older code

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `await_ready.py` | Awaiting a ready operation need not suspend (line 292) |  |
| `group_lifecycle.py` | Failure, sibling cancellation and cleanup (line 530) |  |
| `test_group_lifecycle.py` | Failure, sibling cancellation and cleanup (line 636) |  |
| `async_limits.py` | Limit active work with an async semaphore (line 700) |  |
| `async_counter.py` | Shared state across a suspending await (line 806) |  |
| `test_async_limits.py` | Shared state across a suspending await (line 881) |  |
| `exercise_async_limits.py` | Practice: capacity and shared updates (line 948) |  |
| `to_thread_lifecycle.py` | A timed-out wait can leave a worker running (line 1167) |  |
| `test_to_thread_lifecycle.py` | Check the actual task and worker states (line 1274) |  |
| `exercise_to_thread_lifecycle.py` | Practice: preserve a result without abandoning work (line 1335) |  |
| `artifact_fixture.py` | Lab: collect local artifacts and report completed outcomes (line 1602) |  |
| `collect_artifacts.py` | Lab: collect local artifacts and report completed outcomes (line 1652) |  |
| `catalog_service.py` | Serve one catalog through TCP and HTTP (line 1827) |  |
| `exercise_group.py` | Try it yourself (line 2701) |  |
| `push_work_orders.py` | Legacy transfer project: export selected work orders (line 2787) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_async-def-defines-a-coroutine.py` | `async def` defines a coroutine (line 92) | runs on its own |
| `examples/02_await-pause-here-until-this-finishes.py` | `await`: pause here until this finishes (line 119) | may use names from earlier examples |
| `examples/03_asyncio-sleep-compared-with-time-sleep.py` | `asyncio.sleep` compared with `time.sleep` (line 171) | may use names from earlier examples |
| `examples/04_asyncio-sleep-compared-with-time-sleep.py` | `asyncio.sleep` compared with `time.sleep` (line 183) | may use names from earlier examples |
| `examples/05_asyncio-sleep-compared-with-time-sleep.py` | `asyncio.sleep` compared with `time.sleep` (line 205) | may use names from earlier examples |
| `examples/06_asyncio-sleep-compared-with-time-sleep.py` | `asyncio.sleep` compared with `time.sleep` (line 227) | may use names from earlier examples |
| `examples/07_creating-tasks-schedule-now-and-await-later.py` | Creating tasks: schedule now and await later (line 259) | may use names from earlier examples |
| `examples/08_gather-run-several-operations-and-collect-result.py` | `gather`: run several operations and collect results (line 336) | may use names from earlier examples |
| `examples/09_gather-run-several-operations-and-collect-result.py` | `gather`: run several operations and collect results (line 364) | may use names from earlier examples |
| `examples/10_observe-a-surviving-sibling-after-gather-fails.py` | Observe a surviving sibling after `gather` fails (line 396) | may use names from earlier examples |
| `examples/11_taskgroup-manage-related-tasks-3-11.py` | `TaskGroup`: manage related tasks (3.11+) (line 455) | may use names from earlier examples |
| `examples/12_stop-a-group-early-with-cancel-3-15.py` | Stop a group early with `cancel()` (3.15) (line 491) | may use names from earlier examples |
| `examples/13_timeouts-limit-how-long-code-waits.py` | Timeouts: limit how long code waits (line 989) | may use names from earlier examples |
| `examples/14_timeouts-limit-how-long-code-waits.py` | Timeouts: limit how long code waits (line 1013) | may use names from earlier examples |
| `examples/15_calls-between-async-and-regular-functions.py` | Calls between async and regular functions (line 1067) | may use names from earlier examples |
| `examples/16_calls-between-async-and-regular-functions.py` | Calls between async and regular functions (line 1083) | may use names from earlier examples |
| `examples/17_calls-between-async-and-regular-functions.py` | Calls between async and regular functions (line 1104) | may use names from earlier examples |
| `examples/18_calls-between-async-and-regular-functions.py` | Calls between async and regular functions (line 1125) | may use names from earlier examples |
| `examples/19_async-for-and-async-with.py` | `async for` and `async with` (line 1383) | may use names from earlier examples |
| `examples/20_async-generators-and-early-cleanup.py` | Async generators and early cleanup (line 1425) | may use names from earlier examples |
| `examples/21_mini-project-fetching-several-things-concurrentl.py` | Mini project: fetching several things concurrently (line 1483) | runs on its own |
| `examples/22_bridge-a-callback-to-an-awaitable-result.py` | Bridge a callback to an awaitable result (line 1542) | runs on its own |
| `examples/23_generators-can-receive-values-too.py` | Generators can receive values too (line 1990) | may use names from earlier examples |
| `examples/24_generator-states.py` | Generator states (line 2025) | may use names from earlier examples |
| `examples/25_priming-advance-before-sending-data.py` | Priming: advance before sending data (line 2049) | raises an error on purpose |
| `examples/26_priming-advance-before-sending-data.py` | Priming: advance before sending data (line 2065) | may use names from earlier examples |
| `examples/27_close-and-throw.py` | `close()` and `throw()` (line 2096) | may use names from earlier examples |
| `examples/28_close-and-throw.py` | `close()` and `throw()` (line 2119) | may use names from earlier examples |
| `examples/29_yield-from-forwards-generator-operations.py` | `yield from` forwards generator operations (line 2154) | may use names from earlier examples |
| `examples/30_yield-from-can-also-capture-a-return-value.py` | `yield from` can also capture a return value (line 2193) | may use names from earlier examples |
| `examples/31_coroutine-pipelines-the-old-way.py` | Coroutine pipelines, the old way (line 2225) | may use names from earlier examples |
| `examples/32_a-running-mean-and-a-completed-group-are-differe.py` | A running mean and a completed group are different results (line 2313) | may use names from earlier examples |
| `examples/33_delegation-to-an-ordinary-iterator-and-close-bou.py` | Delegation to an ordinary iterator and close boundaries (line 2388) | may use names from earlier examples |
| `examples/34_a-small-discrete-event-simulation.py` | A small discrete-event simulation (line 2473) | may use names from earlier examples |
| `examples/35_a-small-discrete-event-simulation.py` | A small discrete-event simulation (line 2566) | may use names from earlier examples |
| `examples/36_try-it-yourself.py` | Try it yourself (line 2627) | may use names from earlier examples |
