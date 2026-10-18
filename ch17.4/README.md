# 17.4 - partial, operator, Combining and Lambdas

The code of the chapter **17.4 - partial, operator, Combining and Lambdas** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How `functools.partial` pre-fills arguments, how to inspect it, and how `Placeholder` reserves a position
- How `operator.itemgetter`, `add` and `mul` replace small lambdas
- How to state a contract for a helper that combines values
- How lambdas make sort keys and callbacks, and when `def` reads better

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_functools-partial-pre-filling-arguments.py` | `functools.partial`: pre-filling arguments (line 41) | runs on its own |
| `examples/02_functools-partial-pre-filling-arguments.py` | `functools.partial`: pre-filling arguments (line 54) | may use names from earlier examples |
| `examples/03_inspect-saved-arguments-and-reserve-a-position.py` | `functools.partial`: pre-filling arguments › Inspect saved arguments and reserve a position (line 80) | may use names from earlier examples |
| `examples/04_inspect-saved-arguments-and-reserve-a-position.py` | `functools.partial`: pre-filling arguments › Inspect saved arguments and reserve a position (line 100) | may use names from earlier examples |
| `examples/05_the-operator-module.py` | The `operator` module (line 135) | may use names from earlier examples |
| `examples/06_the-operator-module.py` | The `operator` module (line 148) | may use names from earlier examples |
| `examples/07_practice-combine-values-under-a-stated-contract.py` | Practice: combine values under a stated contract (line 175) | may use names from earlier examples |
| `examples/08_lambdas-revisited.py` | Lambdas revisited (line 229) | may use names from earlier examples |
| `examples/09_lambdas-revisited.py` | Lambdas revisited (line 244) | may use names from earlier examples |
| `examples/10_a-lambda-can-create-a-callback-with-its-own-capt.py` | Lambdas revisited › A lambda can create a callback with its own captured value (line 268) | runs on its own |
| `examples/11_a-lambda-can-create-a-callback-with-its-own-capt.py` | Lambdas revisited › A lambda can create a callback with its own captured value (line 302) | runs on its own |
| `examples/12_try-it-yourself.py` | Try it yourself (line 362) | may use names from earlier examples |
