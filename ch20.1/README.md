# 20.1 - Import Steps, Module Objects and sys.modules

The code of the chapter **20.1 - Import Steps, Module Objects and sys.modules** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What Python does when it runs `import something`
- Why a module is an object and how to inspect it
- Why a second import does not run the module again, and how `sys.modules` stores it
- How a circular import can read a name too early

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `greetings.py` | A module is an object (line 84) |  |
| `module_objects/check.py` | A module is an object › Creating a module object without a file (line 129) |  |
| `counter.py` | `sys.modules` is the cache (line 183) |  |
| `inspection/labels.py` | `sys.modules` is the cache › Inspecting and documenting a module (line 212) |  |
| `inspection/check.py` | `sys.modules` is the cache › Inspecting and documenting a module (line 223) |  |
| `caller_binding/item.py` | `sys.modules` is the cache › Deleting a caller name is not deleting the cache (line 263) |  |
| `caller_binding/check.py` | `sys.modules` is the cache › Deleting a caller name is not deleting the cache (line 269) |  |
| `cache_failure/dependency.py` | `sys.modules` is the cache › A failed first import and a blocked name (line 327) |  |
| `cache_failure/broken.py` | `sys.modules` is the cache › A failed first import and a blocked name (line 332) |  |
| `cache_failure/check.py` | `sys.modules` is the cache › A failed first import and a blocked name (line 338) |  |
| `circular_early/a.py` | `sys.modules` is the cache › A circular import: reading too early (line 374) |  |
| `circular_early/b.py` | `sys.modules` is the cache › A circular import: reading too early (line 380) |  |
| `circular_early/check.py` | `sys.modules` is the cache › A circular import: reading too early (line 386) |  |
| `circular_late/a.py` | `sys.modules` is the cache › A circular import: reading too early (line 405) |  |
| `circular_late/b.py` | `sys.modules` is the cache › A circular import: reading too early (line 412) |  |
| `circular_late/check.py` | `sys.modules` is the cache › A circular import: reading too early (line 420) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_a-module-is-an-object.py` | A module is an object (line 92) | runs on its own |
| `examples/02_a-module-is-an-object.py` | A module is an object (line 114) | may use names from earlier examples |
| `examples/03_sys-modules-is-the-cache.py` | `sys.modules` is the cache (line 189) | may use names from earlier examples |
| `examples/04_sys-modules-is-the-cache.py` | `sys.modules` is the cache (line 200) | may use names from earlier examples |
| `examples/05_deleting-a-caller-name-is-not-deleting-the-cache.py` | `sys.modules` is the cache › Deleting a caller name is not deleting the cache (line 293) | may use names from earlier examples |
| `examples/06_try-it-yourself.py` | Try it yourself (line 468) | may use names from earlier examples |
