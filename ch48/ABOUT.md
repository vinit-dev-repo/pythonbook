# 48 - Checking and Building a Python Package

The code of the chapter **48 - Checking and Building a Python Package** of the Python tutorial (folder `08 - Professional diagnostics`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What formatting, linting, static types, tests and builds each check
- How to observe an actual failure and repair with each tool
- How to check the final wheel in an environment outside your source folder

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `requirements-dev.txt` | Start with the package you already know (line 55) |  |
| `src/shop_report/cli.py` | State the types and tool scope (line 83) |  |
| `tests/test_cli.py` | State the types and tool scope (line 104) |  |
| `pyproject.toml` | State the types and tool scope (line 127) |  |
| `README.md` | Observe one defect at a time › 5. A build needs its declared files (line 260) |  |
| `consumer_check.py` | Try it yourself (line 347) |  |

## Terminal commands

| File | Where it is in the chapter | Note |
|---|---|---|
| `commands/01_start-with-the-package-you-already-know.ps1` | Start with the package you already know (line 63) | powershell commands to type in a terminal |
| `commands/02_state-the-types-and-tool-scope.sh` | State the types and tool scope (line 166) | bash commands to type in a terminal |
| `commands/03_1-formatting-checks-layout.sh` | Observe one defect at a time › 1. Formatting checks layout (line 185) | bash commands to type in a terminal |
| `commands/04_1-formatting-checks-layout.sh` | Observe one defect at a time › 1. Formatting checks layout (line 191) | bash commands to type in a terminal |
| `commands/05_2-lint-finds-an-unused-import.sh` | Observe one defect at a time › 2. Lint finds an unused import (line 207) | bash commands to type in a terminal |
| `commands/06_3-types-can-disagree-even-when-examples-pass.sh` | Observe one defect at a time › 3. Types can disagree even when examples pass (line 222) | bash commands to type in a terminal |
| `commands/07_5-a-build-needs-its-declared-files.sh` | Observe one defect at a time › 5. A build needs its declared files (line 253) | bash commands to type in a terminal |
| `commands/08_run-the-whole-repaired-sequence.sh` | Run the whole repaired sequence (line 280) | bash commands to type in a terminal |
| `commands/09_check-the-wheel-outside-the-checkout.ps1` | Check the wheel outside the checkout (line 311) | powershell commands to type in a terminal |
