# 43 - From Coroutines to async-await

The code of this chapter of the Python tutorial, extracted byte for byte from the certified chapter. The chapter explains every line; read it there.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

- `artifact_fixture.py`
- `async_counter.py`
- `async_limits.py`
- `await_ready.py`
- `catalog_service.py`
- `collect_artifacts.py`
- `exercise_async_limits.py`
- `exercise_group.py`
- `exercise_to_thread_lifecycle.py`
- `group_lifecycle.py`
- `push_work_orders.py`
- `test_async_limits.py`
- `test_group_lifecycle.py`
- `test_to_thread_lifecycle.py`
- `to_thread_lifecycle.py`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Section | Note |
|---|---|---|
| `examples/01_async-def-defines-a-coroutine.py` | `async def` defines a coroutine | runs on its own |
| `examples/02_await-pause-here-until-this-finishes.py` | `await`: pause here until this finishes | may use names from earlier examples |
| `examples/03_asyncio-sleep-compared-with-time-sleep.py` | `asyncio.sleep` compared with `time.sleep` | may use names from earlier examples |
| `examples/04_asyncio-sleep-compared-with-time-sleep.py` | `asyncio.sleep` compared with `time.sleep` | may use names from earlier examples |
| `examples/05_asyncio-sleep-compared-with-time-sleep.py` | `asyncio.sleep` compared with `time.sleep` | may use names from earlier examples |
| `examples/06_asyncio-sleep-compared-with-time-sleep.py` | `asyncio.sleep` compared with `time.sleep` | may use names from earlier examples |
| `examples/07_creating-tasks-schedule-now-and-await-later.py` | Creating tasks: schedule now and await later | may use names from earlier examples |
| `examples/08_gather-run-several-operations-and-collect-result.py` | `gather`: run several operations and collect results | may use names from earlier examples |
| `examples/09_gather-run-several-operations-and-collect-result.py` | `gather`: run several operations and collect results | may use names from earlier examples |
| `examples/10_observe-a-surviving-sibling-after-gather-fails.py` | Observe a surviving sibling after `gather` fails | may use names from earlier examples |
| `examples/11_taskgroup-manage-related-tasks-3-11.py` | `TaskGroup`: manage related tasks (3.11+) | may use names from earlier examples |
| `examples/12_stop-a-group-early-with-cancel-3-15.py` | Stop a group early with `cancel()` (3.15) | may use names from earlier examples |
| `examples/13_timeouts-limit-how-long-code-waits.py` | Timeouts: limit how long code waits | may use names from earlier examples |
| `examples/14_timeouts-limit-how-long-code-waits.py` | Timeouts: limit how long code waits | may use names from earlier examples |
| `examples/15_calls-between-async-and-regular-functions.py` | Calls between async and regular functions | may use names from earlier examples |
| `examples/16_calls-between-async-and-regular-functions.py` | Calls between async and regular functions | may use names from earlier examples |
| `examples/17_calls-between-async-and-regular-functions.py` | Calls between async and regular functions | may use names from earlier examples |
| `examples/18_calls-between-async-and-regular-functions.py` | Calls between async and regular functions | may use names from earlier examples |
| `examples/19_async-for-and-async-with.py` | `async for` and `async with` | may use names from earlier examples |
| `examples/20_async-generators-and-early-cleanup.py` | Async generators and early cleanup | may use names from earlier examples |
| `examples/21_mini-project-fetching-several-things-concurrentl.py` | Mini project: fetching several things concurrently | runs on its own |
| `examples/22_bridge-a-callback-to-an-awaitable-result.py` | Bridge a callback to an awaitable result | runs on its own |
| `examples/23_generators-can-receive-values-too.py` | Generators can receive values too | may use names from earlier examples |
| `examples/24_generator-states.py` | Generator states | may use names from earlier examples |
| `examples/25_priming-advance-before-sending-data.py` | Priming: advance before sending data | raises an error on purpose |
| `examples/26_priming-advance-before-sending-data.py` | Priming: advance before sending data | may use names from earlier examples |
| `examples/27_close-and-throw.py` | `close()` and `throw()` | may use names from earlier examples |
| `examples/28_close-and-throw.py` | `close()` and `throw()` | may use names from earlier examples |
| `examples/29_yield-from-forwards-generator-operations.py` | `yield from` forwards generator operations | may use names from earlier examples |
| `examples/30_yield-from-can-also-capture-a-return-value.py` | `yield from` can also capture a return value | may use names from earlier examples |
| `examples/31_coroutine-pipelines-the-old-way.py` | Coroutine pipelines, the old way | may use names from earlier examples |
| `examples/32_a-running-mean-and-a-completed-group-are-differe.py` | A running mean and a completed group are different results | may use names from earlier examples |
| `examples/33_delegation-to-an-ordinary-iterator-and-close-bou.py` | Delegation to an ordinary iterator and close boundaries | may use names from earlier examples |
| `examples/34_a-small-discrete-event-simulation.py` | A small discrete-event simulation | may use names from earlier examples |
| `examples/35_a-small-discrete-event-simulation.py` | A small discrete-event simulation | may use names from earlier examples |
| `examples/36_try-it-yourself.py` | Try it yourself | may use names from earlier examples |
