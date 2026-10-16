# 46 - Logging

The code of the chapter **46 - Logging** of the Python tutorial (folder `08 - Professional diagnostics`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why logs are more useful than many temporary `print()` statements
- The five severity levels, and why a low-level message may not appear
- The four main parts of the logging system and how they work together
- How to build a logger tree with `getLogger(__name__)`
- How to log to the console and a file at the same time, at different detail levels
- How to log exceptions properly, with their full traceback
- How to rotate log files so they do not keep growing
- How to configure a whole app's logging in one place with `dictConfig`

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_why-logging-helps-more-than-print.py` | Why logging helps more than `print()` (line 53) | runs on its own |
| `examples/02_the-five-severity-levels.py` | The five severity levels (line 97) | runs on its own |
| `examples/03_quick-start-basicconfig.py` | Quick start: basicConfig (line 124) | may use names from earlier examples |
| `examples/04_named-loggers-and-the-logger-tree.py` | Named loggers and the logger tree (line 183) | may use names from earlier examples |
| `examples/05_named-loggers-and-the-logger-tree.py` | Named loggers and the logger tree (line 200) | runs on its own |
| `examples/06_multiple-loggers-and-handlers-worked-example.py` | Multiple loggers and handlers, worked example (line 223) | may use names from earlier examples |
| `examples/07_logging-exceptions-properly.py` | Logging exceptions properly (line 272) | runs on its own |
| `examples/08_size-based-rotation.py` | Size-based rotation (line 320) | may use names from earlier examples |
| `examples/09_time-based-rotation.py` | Time-based rotation (line 348) | may use names from earlier examples |
| `examples/10_configuring-bigger-apps-dictconfig.py` | Configuring bigger apps: dictConfig (line 374) | may use names from earlier examples |
| `examples/11_a-complete-logging-setup.py` | A complete logging setup (line 433) | may use names from earlier examples |
| `examples/12_good-habits.py` | Good habits (line 523) | may use names from earlier examples |
| `examples/13_try-it-yourself.py` | Try it yourself (line 559) | may use names from earlier examples |
