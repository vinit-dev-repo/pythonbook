# 31.2 - Writing Metaclasses, Class Factories and Choosing a Hook

The code of the chapter **31.2 - Writing Metaclasses, Class Factories and Choosing a Hook** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Write a metaclass that rejects or registers classes, and pass keywords to it.
- Use `__prepare__` and a callable class factory, and say when a factory result is not a class.
- Choose among a class decorator, `__init_subclass__`, `__set_name__` and a metaclass, simplest first.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `namespace_policy.py` | `__prepare__`: choosing the namespace, briefly (line 208) |  |
| `class_factories.py` | A class factory can be an ordinary callable (line 268) |  |
| `metaclass_keywords.py` | Choose among class-creation tools › Apply a forwarded class keyword (line 389) |  |
| `lifecycle_model.py` | Choose among class-creation tools › Observe import, class creation and instance construction (line 449) |  |
| `lifecycle_import.py` | Choose among class-creation tools › Observe import, class creation and instance construction (line 562) |  |
| `base_paths.py` | Choose among class-creation tools › Walk every base-class path (line 625) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_inheriting-from-type-your-own-metaclass.py` | Inheriting from `type`: your own metaclass (line 41) | runs on its own |
| `examples/02_worked-example-every-class-must-define-x.py` | Inheriting from `type`: your own metaclass › Worked example: every class must define X (line 69) | may use names from earlier examples |
| `examples/03_worked-example-auto-register-every-subclass.py` | Inheriting from `type`: your own metaclass › Worked example: auto-register every subclass (line 100) | may use names from earlier examples |
| `examples/04_metaclass-keyword-and-metaclass-parameters.py` | `metaclass=` keyword and metaclass parameters (line 142) | may use names from earlier examples |
| `examples/05_prepare-choosing-the-namespace-briefly.py` | `__prepare__`: choosing the namespace, briefly (line 173) | may use names from earlier examples |
| `examples/06_init-subclass-the-modern-hook-and-the-one-to-rea.py` | Choose among class-creation tools › `__init_subclass__`: the modern hook, and the one to reach for first (line 356) | may use names from earlier examples |
| `examples/07_try-it-yourself.py` | Try it yourself (line 700) | runs on its own |
