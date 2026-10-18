# 31.1 - What a Metaclass Is, type and How a Class Is Built

The code of the chapter **31.1 - What a Metaclass Is, type and How a Class Is Built** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Say what a **metaclass** is and how it relates to a class object.
- Explain how `type` acts as the default metaclass, and build a class by calling it.
- Follow the steps that Python runs for a `class` statement.
- Say which method builds an object and which one sets it up.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `type_links.py` | `type` is the default metaclass › Instance-of and subclass-of are different links (line 91) |  |
| `record_factory_lab.py` | `type` is the default metaclass › Build a mutable record class with `type` (line 156) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_type-is-the-default-metaclass.py` | `type` is the default metaclass (line 60) | runs on its own |
| `examples/02_creating-a-class-without-the-class-statement.py` | `type` is the default metaclass › Creating a class WITHOUT the `class` statement (line 116) | may use names from earlier examples |
| `examples/03_new-vs-init-on-ordinary-classes-first.py` | `__new__` vs `__init__` on ordinary classes, first (line 275) | may use names from earlier examples |
| `examples/04_when-to-override-new.py` | `__new__` vs `__init__` on ordinary classes, first › When to override `__new__` (line 305) | may use names from earlier examples |
| `examples/05_try-it-yourself.py` | Try it yourself (line 358) | runs on its own |
