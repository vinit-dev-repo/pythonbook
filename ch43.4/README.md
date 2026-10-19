# 43.4 - Generator Coroutines, send, yield from and a Simulation

The code of the chapter **43.4 - Generator Coroutines, send, yield from and a Simulation** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Optional history: generator-coroutine `send`, states, priming, `close`, `throw` and `yield from` for reading older code
- How older code built pipelines and a small event simulation from generators
- Why modern `async` and `await` replaced this style

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `push_work_orders.py` | Try it yourself › Legacy transfer project: export selected work orders (line 743) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_generators-can-receive-values-too.py` | Optional history: coroutines built from generators › Generators can receive values too (line 47) | runs on its own |
| `examples/02_generator-states.py` | Optional history: coroutines built from generators › Generator states (line 80) | may use names from earlier examples |
| `examples/03_priming-advance-before-sending-data.py` | Optional history: coroutines built from generators › Priming: advance before sending data (line 103) | raises an error on purpose |
| `examples/04_priming-advance-before-sending-data.py` | Optional history: coroutines built from generators › Priming: advance before sending data (line 118) | may use names from earlier examples |
| `examples/05_close-and-throw.py` | Optional history: coroutines built from generators › `close()` and `throw()` (line 147) | may use names from earlier examples |
| `examples/06_close-and-throw.py` | Optional history: coroutines built from generators › `close()` and `throw()` (line 169) | may use names from earlier examples |
| `examples/07_yield-from-forwards-generator-operations.py` | Optional history: coroutines built from generators › `yield from` forwards generator operations (line 201) | may use names from earlier examples |
| `examples/08_yield-from-can-also-capture-a-return-value.py` | Optional history: coroutines built from generators › `yield from` can also capture a return value (line 237) | may use names from earlier examples |
| `examples/09_coroutine-pipelines-the-old-way.py` | Optional history: coroutines built from generators › Coroutine pipelines, the old way (line 266) | may use names from earlier examples |
| `examples/10_a-running-mean-and-a-completed-group-are-differe.py` | Optional history: coroutines built from generators › A running mean and a completed group are different results (line 352) | may use names from earlier examples |
| `examples/11_delegation-to-an-ordinary-iterator-and-close-bou.py` | Optional history: coroutines built from generators › Delegation to an ordinary iterator and close boundaries (line 424) | may use names from earlier examples |
| `examples/12_a-small-discrete-event-simulation.py` | Optional history: coroutines built from generators › A small discrete-event simulation (line 507) | may use names from earlier examples |
| `examples/13_a-small-discrete-event-simulation.py` | Optional history: coroutines built from generators › A small discrete-event simulation (line 601) | may use names from earlier examples |
| `examples/14_try-it-yourself.py` | Try it yourself (line 657) | runs on its own |
