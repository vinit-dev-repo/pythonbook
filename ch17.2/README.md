# 17.2 - Nested Functions, nonlocal and Closures

The code of the chapter **17.2 - Nested Functions, nonlocal and Closures** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How a nested function reads and changes the bindings of its enclosing function with `nonlocal`
- What a closure retains, and why separate factory calls give independent counters
- How late binding affects loop variables, and how a saved default changes that
- Where closures help: counters, accumulators and small caches

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_nested-functions-and-nonlocal.py` | Nested functions and `nonlocal` (line 45) | raises an error on purpose |
| `examples/02_nested-functions-and-nonlocal.py` | Nested functions and `nonlocal` (line 71) | may use names from earlier examples |
| `examples/03_an-enclosing-binding-can-receive-its-value-later.py` | Nested functions and `nonlocal` › An enclosing binding can receive its value later (line 95) | may use names from earlier examples |
| `examples/04_closures-keep-enclosing-bindings.py` | Closures keep enclosing bindings (line 142) | may use names from earlier examples |
| `examples/05_closures-keep-enclosing-bindings.py` | Closures keep enclosing bindings (line 169) | may use names from earlier examples |
| `examples/06_closures-keep-enclosing-bindings.py` | Closures keep enclosing bindings (line 179) | may use names from earlier examples |
| `examples/07_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 206) | may use names from earlier examples |
| `examples/08_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 225) | may use names from earlier examples |
| `examples/09_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 238) | may use names from earlier examples |
| `examples/10_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 258) | may use names from earlier examples |
| `examples/11_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 298) | may use names from earlier examples |
| `examples/12_what-closures-are-good-for.py` | Closures keep enclosing bindings › What closures are good for (line 327) | may use names from earlier examples |
| `examples/13_what-closures-are-good-for.py` | Closures keep enclosing bindings › What closures are good for (line 350) | may use names from earlier examples |
| `examples/14_try-it-yourself.py` | Try it yourself (line 405) | may use names from earlier examples |
