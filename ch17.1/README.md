# 17.1 - Scopes, LEGB and Local Names

The code of the chapter **17.1 - Scopes, LEGB and Local Names** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a scope is, and why a name made inside a function cannot be used outside it
- How LEGB orders local, enclosing, global and built-in names, and how a local name can hide a built-in
- Why assigning to a name inside a function can produce `UnboundLocalError`
- How `global` reaches a module name on purpose

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-a-scope-is.py` | What a scope is (line 43) | raises an error on purpose |
| `examples/02_the-legb-rule.py` | The LEGB rule (line 101) | may use names from earlier examples |
| `examples/03_recover-a-shadowed-built-in-explicitly.py` | The LEGB rule › Recover a shadowed built-in explicitly (line 128) | may use names from earlier examples |
| `examples/04_local-scope-is-created-fresh-every-call.py` | Local scope is created fresh, every call (line 161) | may use names from earlier examples |
| `examples/05_the-assignment-makes-it-local-rule.py` | The assignment-makes-it-local rule (line 191) | raises an error on purpose |
| `examples/06_the-global-keyword.py` | The assignment-makes-it-local rule › The `global` keyword (line 220) | may use names from earlier examples |
| `examples/07_the-global-keyword.py` | The assignment-makes-it-local rule › The `global` keyword (line 244) | may use names from earlier examples |
| `examples/08_try-it-yourself.py` | Try it yourself (line 304) | may use names from earlier examples |
