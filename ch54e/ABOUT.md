# 54e - Capstone - Configuring and Operating an Expense Ledger

The code of the chapter **54e - Capstone - Configuring and Operating an Expense Ledger** of the Python tutorial (folder `10 - Web applications and production boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## About this chapter

This capstone joins settings, a command line, validation, transactions, logs, tests, packaging and an installed-client check in one local program. You will build it in three working milestones. At the end of each milestone, the files shown so far form a runnable package.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

The chapter saves these files more than once (for example a first version and a repaired one). This folder holds the version the chapter ends with, and the table points to that last version:

- `pyproject.toml`
- `src/expense_ledger/cli.py`
- `tests/test_cli.py`

| File | Where it is in the chapter | Note |
|---|---|---|
| `src/expense_ledger/config.py` | Milestone 1 — select and check settings (line 65) |  |
| `src/expense_ledger/__init__.py` | Milestone 1 — select and check settings (line 210) |  |
| `src/expense_ledger/__main__.py` | Milestone 1 — select and check settings (line 215) |  |
| `tests/test_config.py` | Milestone 1 — select and check settings (line 268) |  |
| `ledger.example.json` | Milestone 1 — select and check settings (line 430) |  |
| `requirements-dev.txt` | Milestone 1 — select and check settings (line 468) |  |
| `README.md` | Milestone 1 — select and check settings (line 477) |  |
| `src/expense_ledger/ledger.py` | Milestone 2 — keep persistent rows together (line 506) |  |
| `src/expense_ledger/cli.py` | Milestone 2 — keep persistent rows together (line 817) | rewritten later in the chapter |
| `batch_ok.json` | Milestone 2 — keep persistent rows together (line 974) |  |
| `batch_conflict.json` | Milestone 2 — keep persistent rows together (line 983) |  |
| `tests/test_ledger.py` | Milestone 2 — keep persistent rows together (line 997) |  |
| `tests/test_cli.py` | Milestone 2 — keep persistent rows together (line 1306) | rewritten later in the chapter |
| `pyproject.toml` | Milestone 3 — check, build and operate the installed package (line 1501) | rewritten later in the chapter |
| `RUNBOOK.md` | Local operating runbook (line 1574) |  |
| `assessment_batch.json` | Independent installed-client task (line 1639) |  |
| `assess_ledger.py` | Independent installed-client task (line 1667) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_milestone-1-select-and-check-settings.py` | Milestone 1 — select and check settings (line 223) | runs on its own |
| `examples/02_milestone-1-select-and-check-settings.py` | Milestone 1 — select and check settings (line 396) | may use names from earlier examples |

## Terminal commands

| File | Where it is in the chapter | Note |
|---|---|---|
| `commands/01_milestone-1-select-and-check-settings.ps1` | Milestone 1 — select and check settings (line 485) | powershell commands to type in a terminal |
| `commands/02_milestone-2-keep-persistent-rows-together.ps1` | Milestone 2 — keep persistent rows together (line 1482) | powershell commands to type in a terminal |
| `commands/03_set-up-and-check.ps1` | Set up and check (line 1584) | powershell commands to type in a terminal |
| `commands/04_operate.ps1` | Operate (line 1600) | powershell commands to type in a terminal |
| `commands/05_final-package-check-sequence.ps1` | Final package check sequence (line 1931) | powershell commands to type in a terminal |
| `commands/06_final-package-check-sequence.ps1` | Final package check sequence (line 1945) | powershell commands to type in a terminal |
