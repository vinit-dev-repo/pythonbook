# 36.4 - Transfer Projects, a Managed CSV Stream and Aligned Record Streams

The code of the chapter **36.4 - Transfer Projects, a Managed CSV Stream and Aligned Record Streams** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How a context manager owns a file until the last use of the rows that come from it
- How a class and a generator implement the same managed stream
- How `ExitStack` owns several files and the generators that read them
- How to check keys, mask, project and group aligned streams without losing data to a spent iterator

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `managed_csv_records.py` | Transfer project: own a lazy CSV stream until its last use (line 76) |  |
| `aligned_records.py` | Transfer project: combine four aligned record streams (line 363) |  |
| `site_report.py` | Transfer project: combine four aligned record streams (line 464) |  |
| `group_lifetime_lab.py` | Transfer project: combine four aligned record streams › Diagnose an exhausted mask and shared groups (line 563) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_try-it-yourself.py` | Try it yourself (line 658) | runs on its own |
