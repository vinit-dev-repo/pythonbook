# 25.2 - What to Test, Parametrize, State Checks and Fixtures

The code of the chapter **25.2 - What to Test, Parametrize, State Checks and Fixtures** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- The three kinds of case a function needs: normal, edge and error
- How `pytest.raises` checks an error and `parametrize` runs one test over a table of inputs
- How the Arrange-Act-Assert shape and clear names make a test readable
- How to take expected results from the contract, and how to check the state after a rejected operation
- How fixtures share fresh setup, and how `yield`, finalizers and setup failures affect cleanup

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `test_exceptions.py` | What to actually test › Testing for exceptions: `pytest.raises` (line 58) |  |
| `test_parameters.py` | What to actually test › Parametrize: one test, many inputs (line 87) |  |
| `calculator.py` | What to actually test › Check a complete example: average (line 121) |  |
| `test_average.py` | What to actually test › Check a complete example: average (line 129) |  |
| `selection.py` | What to actually test › Choose the expected subset independently (line 235) |  |
| `test_selection.py` | What to actually test › Choose the expected subset independently (line 241) |  |
| `labels.py` | What to actually test › Use a round trip alongside known values (line 266) |  |
| `test_labels.py` | What to actually test › Use a round trip alongside known values (line 275) |  |
| `catalog.py` | What to actually test › Check the state after an operation (line 312) |  |
| `test_catalog.py` | What to actually test › Check the state after an operation (line 353) |  |
| `test_weak_replacement.py` | What to actually test › Make sure a test can catch the defect (line 436) |  |
| `test_practice.py` | Try it yourself (line 777) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-arrange-act-assert-pattern.py` | What to actually test › The Arrange-Act-Assert pattern (line 177) | runs on its own |
| `examples/02_naming-tests-so-they-read-like-sentences.py` | What to actually test › Naming tests so they read like sentences (line 196) | may use names from earlier examples |
| `examples/03_check-a-relation-the-contract-promises.py` | What to actually test › Check a relation the contract promises (line 214) | may use names from earlier examples |
| `examples/04_make-sure-a-test-can-catch-the-defect.py` | What to actually test › Make sure a test can catch the defect (line 457) | a fragment, not a complete program |
| `examples/05_fixtures-shared-setup.py` | What to actually test › Fixtures: shared setup (line 490) | may use names from earlier examples |
| `examples/06_a-fixture-can-request-another-fixture.py` | What to actually test › A fixture can request another fixture (line 525) | may use names from earlier examples |
| `examples/07_rerun-the-old-checks-after-changing-setup.py` | What to actually test › Rerun the old checks after changing setup (line 551) | may use names from earlier examples |
| `examples/08_setup-yield-and-teardown.py` | What to actually test › Setup, yield and teardown (line 577) | may use names from earlier examples |
| `examples/09_observe-cleanup-after-it-happens.py` | What to actually test › Observe cleanup after it happens (line 613) | may use names from earlier examples |
| `examples/10_setup-can-fail-before-yield.py` | What to actually test › Setup can fail before yield (line 674) | may use names from earlier examples |

## Terminal commands

| File | Where it is in the chapter | Note |
|---|---|---|
| `commands/01_check-the-state-after-an-operation.sh` | What to actually test › Check the state after an operation (line 425) | bash commands to type in a terminal |
| `commands/02_make-sure-a-test-can-catch-the-defect.sh` | What to actually test › Make sure a test can catch the defect (line 463) | bash commands to type in a terminal |
