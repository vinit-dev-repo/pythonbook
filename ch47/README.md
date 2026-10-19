# 47 - Debugging and Profiling

The code of the chapter **47 - Debugging and Profiling** of the Python tutorial (folder `08 - Professional diagnostics`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to reproduce a wrong result, pause a program with `pdb`, and inspect the control flow that produced it
- How a regression test preserves a repair for an early return
- How `cProfile` and `pstats` identify repeated work in a correct program
- How to compare profiled evidence with repeated, unprofiled `timeit` measurements

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

The chapter saves these files more than once (for example a first version and a repaired one). This folder holds the version the chapter ends with, and the table points to that last version:

- `report.py`
- `test_report.py`

| File | Where it is in the chapter | Note |
|---|---|---|
| `report.py` | Keep the repair and add two summary strategies (line 185) | rewritten later in the chapter |
| `test_report.py` | Keep the repair and add two summary strategies (line 221) | rewritten later in the chapter |
| `profile_report.py` | Session B: profile repeated work (line 278) |  |
| `measure_report.py` | Session B: profile repeated work › Measure without profiler overhead (line 391) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_pause-at-the-decision-with-pdb.py` | Session A: reproduce, inspect, and repair a wrong result › Pause at the decision with `pdb` (line 163) | runs on its own |
