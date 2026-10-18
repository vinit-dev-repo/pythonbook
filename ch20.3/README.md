# 20.3 - Reloading Modules and the Main Guard

The code of the chapter **20.3 - Reloading Modules and the Main Guard** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to reload a module, and why you rarely should
- How `if __name__ == "__main__":` and the direct-run name work
- Why an imported name or a saved function can still show old values after a reload

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `reload_demo/settings.py` | Reloading a module (line 52) |  |
| `reload_demo/check.py` | Reloading a module (line 58) |  |
| `reload_function/message.py` | Reloading a module › A saved function is not a live module lookup (line 101) |  |
| `reload_function/check.py` | Reloading a module › A saved function is not a live module lookup (line 109) |  |
| `reload_nested/child.py` | Reloading a module › Reloading a parent does not reload its child (line 149) |  |
| `reload_nested/parent.py` | Reloading a module › Reloading a parent does not reload its child (line 154) |  |
| `reload_nested/check.py` | Reloading a module › Reloading a parent does not reload its child (line 162) |  |
| `greet.py` | `__main__` revisited (line 209) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_reloading-a-module.py` | Reloading a module (line 42) | runs on its own |
| `examples/02_main-revisited.py` | `__main__` revisited (line 228) | may use names from earlier examples |
| `examples/03_try-it-yourself.py` | Try it yourself (line 275) | may use names from earlier examples |
