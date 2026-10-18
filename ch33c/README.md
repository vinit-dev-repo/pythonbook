# 33c - Project - When Inserting Hooks Changes the Contract

The code of the chapter **33c - Project - When Inserting Hooks Changes the Contract** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How replacing hooks on an existing class retains class identity while changing behavior
- Why object-level calls inside inserted hooks avoid recursion but displace earlier hooks
- Why an internal `self.attribute` read is intercepted too
- Why explicit special-method lookup and `str(instance)` can follow different routes

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `hook_insertion.py` | Experiment 1: same class, displaced hooks (line 42) |  |
| `record_fixture.py` | Experiment 1: same class, displaced hooks (line 65) |  |
| `hook_demo.py` | Experiment 1: same class, displaced hooks (line 98) |  |
| `test_hook_insertion.py` | Experiment 2: unchanged identity does not preserve access behavior (line 182) |  |
| `counter_transfer.py` | Try it yourself (line 301) |  |
