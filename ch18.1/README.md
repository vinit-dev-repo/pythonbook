# 18.1 - Writing a Decorator, @ and wraps

The code of the chapter **18.1 - Writing a Decorator, @ and wraps** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- The problem decorators solve, and why they save you from editing every function by hand
- How to build a decorator from scratch, step by step, with no magic
- What happens when a decorated function is defined, and what happens only when it is called
- Why wrappers need `*args`/`**kwargs`, and why `functools.wraps` matters

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_building-a-decorator-from-first-principles.py` | Building a decorator from first principles (line 67) | runs on its own |
| `examples/02_the-syntax-decoration-when-a-function-is-defined.py` | The `@` syntax: decoration when a function is defined (line 111) | may use names from earlier examples |
| `examples/03_the-syntax-decoration-when-a-function-is-defined.py` | The `@` syntax: decoration when a function is defined (line 118) | may use names from earlier examples |
| `examples/04_the-syntax-decoration-when-a-function-is-defined.py` | The `@` syntax: decoration when a function is defined (line 136) | may use names from earlier examples |
| `examples/05_fitting-any-function-args-and-kwargs.py` | Fitting any function: `*args` and `**kwargs` (line 185) | may use names from earlier examples |
| `examples/06_the-name-problem-and-functools-wraps.py` | The name problem, and `functools.wraps` (line 224) | may use names from earlier examples |
| `examples/07_the-name-problem-and-functools-wraps.py` | The name problem, and `functools.wraps` (line 243) | may use names from earlier examples |
| `examples/08_try-it-yourself.py` | Try it yourself (line 304) | may use names from earlier examples |
