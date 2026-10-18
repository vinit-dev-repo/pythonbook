# 31.4 - Small Metaprogramming Applications and Method Wrapping

The code of the chapter **31.4 - Small Metaprogramming Applications and Method Wrapping** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Pick the simplest tool, a decorator, a hook or a metaclass, for a small class-changing job.
- Generate a method from declared fields with a metaclass and with a decorator.
- Wrap local plain functions with a metaclass and with a class decorator, and say what each leaves alone.
- Explain why copying a class into `type` does not update it.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `generated_summary.py` | Three small metaprogramming applications › Generate one method from declared fields (line 143) |  |
| `method_tools.py` | Apply a decorator to locally defined methods (line 217) |  |
| `timed_methods.py` | Apply a decorator to locally defined methods (line 315) |  |
| `rebuild_class.py` | Apply a decorator to locally defined methods › Rebuilding a class is not the same as updating it (line 356) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_1-auto-repr-via-class-decorator.py` | Three small metaprogramming applications › 1. Auto-repr via class decorator (line 43) | runs on its own |
| `examples/02_2-subclass-registry-via-init-subclass.py` | Three small metaprogramming applications › 2. Subclass registry via `__init_subclass__` (line 75) | may use names from earlier examples |
| `examples/03_3-class-validation-via-metaclass.py` | Three small metaprogramming applications › 3. Class validation via metaclass (line 103) | may use names from earlier examples |
| `examples/04_try-it-yourself.py` | Try it yourself (line 432) | runs on its own |
