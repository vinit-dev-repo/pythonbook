# 52.1 - Why Files Are Not Enough, What SQLite Is, Connecting and Transactions

The code of the chapter **52.1 - Why Files Are Not Enough, What SQLite Is, Connecting and Transactions** of the Python tutorial (folder `09 - Data and database applications`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why plain files and CSV stop being enough once a program grows
- What SQLite is, and how Python exposes it through `sqlite3`
- How to connect, run SQL, and save your changes with `sqlite3`
- How a **transaction** groups changes and how `rollback()` cancels uncommitted changes

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_connecting-running-sql-and-saving.py` | Connecting, running SQL, and saving (line 85) | runs on its own |
| `examples/02_the-context-manager-pattern.py` | Connecting, running SQL, and saving › The context-manager pattern (line 114) | may use names from earlier examples |
| `examples/03_transactions-keeping-a-group-of-changes-all-or-n.py` | Transactions: keeping a group of changes all-or-nothing (line 150) | runs on its own |
| `examples/04_transactions-keeping-a-group-of-changes-all-or-n.py` | Transactions: keeping a group of changes all-or-nothing (line 175) | may use names from earlier examples |
| `examples/05_try-it-yourself.py` | Try it yourself (line 267) | runs on its own |
| `examples/06_transfer-lab-locate-a-database-failure.py` | Try it yourself › Transfer lab: locate a database failure (line 332) | runs on its own |
