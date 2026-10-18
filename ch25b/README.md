# 25b - Project - Testing a Timer with Two Clocks

The code of the chapter **25b - Project - Testing a Timer with Two Clocks** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How a `Timer` has idle, running, and stopped states
- Why duration needs a monotonic counter while timestamps need an aware wall clock
- How injected zero-argument clock callables make transitions reproducible
- How candidate validation before commit preserves `Timer` fields on failure

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `timer.py` | A Timer with two kinds of clock (line 66) |  |
| `controlled_clocks.py` | A Timer with two kinds of clock (line 177) |  |
| `timer_demo.py` | A Timer with two kinds of clock (line 221) |  |
| `test_timer.py` | Testing Timer transitions and failures (line 304) |  |
| `timer_transfer.py` | Try it yourself (line 634) |  |
