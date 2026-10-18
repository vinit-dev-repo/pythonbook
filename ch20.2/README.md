# 20.2 - sys.path, Finders and Import Forms

The code of the chapter **20.2 - sys.path, Finders and Import Forms** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Where Python looks for modules with `sys.path`, and how a local file can hide a standard module
- What finders and loaders do, in plain words
- Exactly what each `import` spelling puts into your own namespace
- How `lazy import` delays loading in Python 3.15

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `shadow_demo/random.py` | Where Python looks: `sys.path` (line 71) |  |
| `shadow_demo/check.py` | Where Python looks: `sys.path` (line 76) |  |
| `spec_search/external/plugin.py` | Finders and loaders › Inspecting a plain module before importing it (line 125) |  |
| `spec_search/check.py` | Finders and loaders › Inspecting a plain module before importing it (line 132) |  |
| `loud_module.py` | Import variants: what each one actually binds › A common misconception: `from module import name` still runs the *whole* module (line 208) |  |
| `exports_demo/plain.py` | Import variants: what each one actually binds › A common misconception: `from module import name` still runs the *whole* module (line 233) |  |
| `exports_demo/listed.py` | Import variants: what each one actually binds › A common misconception: `from module import name` still runs the *whole* module (line 239) |  |
| `exports_demo/check_plain.py` | Import variants: what each one actually binds › A common misconception: `from module import name` still runs the *whole* module (line 246) |  |
| `exports_demo/check_listed.py` | Import variants: what each one actually binds › A common misconception: `from module import name` still runs the *whole* module (line 262) |  |
| `local_alias/loud.py` | Import variants: what each one actually binds › Aliases and imports inside a function (line 279) |  |
| `local_alias/check.py` | Import variants: what each one actually binds › Aliases and imports inside a function (line 285) |  |
| `lazy_demo/heavy.py` | Import variants: what each one actually binds › Lazy imports: bind now, load at first use (3.15) (line 318) |  |
| `lazy_demo/check.py` | Import variants: what each one actually binds › Lazy imports: bind now, load at first use (3.15) (line 324) |  |
| `lazy_demo/compat.py` | Import variants: what each one actually binds › Lazy imports: bind now, load at first use (3.15) (line 358) |  |
| `shared_binding/store.py` | Import variants: what each one actually binds › An imported binding can still share a mutable object (line 386) |  |
| `shared_binding/check.py` | Import variants: what each one actually binds › An imported binding can still share a mutable object (line 391) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_where-python-looks-sys-path.py` | Where Python looks: `sys.path` (line 43) | runs on its own |
| `examples/02_finders-and-loaders.py` | Finders and loaders (line 111) | may use names from earlier examples |
| `examples/03_a-common-misconception-from-module-import-name-s.py` | Import variants: what each one actually binds › A common misconception: `from module import name` still runs the *whole* module (line 214) | may use names from earlier examples |
| `examples/04_try-it-yourself.py` | Try it yourself (line 457) | may use names from earlier examples |
