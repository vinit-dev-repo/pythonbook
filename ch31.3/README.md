# 31.3 - Calling a Class, Class Lookup and Attribute Hooks

The code of the chapter **31.3 - Calling a Class, Class Lookup and Attribute Hooks** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Follow what Python runs when code calls `Dog(...)`, and say when `__init__` is skipped.
- Say how a class reads a name from its bases and from its metaclass, and why instances do not see the metaclass.
- Use `__getattr__`, `__getattribute__`, `__setattr__` and `__delattr__`, and avoid their recursion trap.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `meta_call_levels.py` | Classes, metaclasses, and `__call__` › Calling a metaclass has one more type level (line 72) |  |
| `class_lookup.py` | A class reads from its bases and its metaclass (line 169) |  |
| `deletion_hook.py` | Attribute access hooks: metaprogramming beyond creation › Deletion uses a separate hook (line 358) |  |
| `computed_hooks.py` | Attribute access hooks: metaprogramming beyond creation › Compute a value without storing it (line 402) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_classes-metaclasses-and-call.py` | Classes, metaclasses, and `__call__` (line 49) | runs on its own |
| `examples/02_singleton-via-metaclass-call.py` | Classes, metaclasses, and `__call__` › Singleton via metaclass `__call__` (line 126) | may use names from earlier examples |
| `examples/03_getattr-the-missing-only-fallback.py` | Attribute access hooks: metaprogramming beyond creation › `__getattr__`: the missing-only fallback (line 260) | may use names from earlier examples |
| `examples/04_getattribute-every-attribute-read.py` | Attribute access hooks: metaprogramming beyond creation › `__getattribute__`: every attribute read (line 290) | may use names from earlier examples |
| `examples/05_setattr-the-same-trap-on-writing.py` | Attribute access hooks: metaprogramming beyond creation › `__setattr__`: the same trap, on writing (line 322) | may use names from earlier examples |
| `examples/06_practical-application-an-attribute-access-logger.py` | Attribute access hooks: metaprogramming beyond creation › Practical application: an attribute-access logger (line 493) | may use names from earlier examples |
| `examples/07_try-it-yourself.py` | Try it yourself (line 555) | runs on its own |
