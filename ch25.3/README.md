# 25.3 - unittest, doctest and Mocks

The code of the chapter **25.3 - unittest, doctest and Mocks** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How `unittest` organises tests as `TestCase` methods, and how it compares with pytest
- How `setUp`, `tearDown` and `addCleanup` work, including when setup fails
- How `doctest` checks the examples in docstrings
- How `Mock` and `patch` replace a dependency, and which name to patch
- How to control time by passing it in as an argument

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `test_calculator_unittest.py` | unittest: the standard-library way (line 46) |  |
| `cleanup_unittest_demo.py` | unittest: the standard-library way › Check cleanup when unittest setup fails (line 152) |  |
| `weather_logic.py` | Replacing an external dependency with a mock › Test the weather caller, not just the replacement (line 351) |  |
| `test_weather_logic.py` | Replacing an external dependency with a mock › Test the weather caller, not just the replacement (line 359) |  |
| `weather_source.py` | Replacing an external dependency with a mock › Patch the name the caller reads (line 394) |  |
| `weather_report.py` | Replacing an external dependency with a mock › Patch the name the caller reads (line 400) |  |
| `test_wrong_target.py` | Replacing an external dependency with a mock › Patch the name the caller reads (line 417) |  |
| `test_weather_report.py` | Replacing an external dependency with a mock › Patch the name the caller reads (line 430) |  |
| `waiting.py` | Replacing an external dependency with a mock › Control time through an explicit input (line 465) |  |
| `test_waiting.py` | Replacing an external dependency with a mock › Control time through an explicit input (line 471) |  |
| `test_unit_practice.py` | Try it yourself (line 516) |  |
| `halves.py` | Try it yourself (line 537) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_setup-and-teardown.py` | unittest: the standard-library way › setUp and tearDown (line 97) | runs on its own |
| `examples/02_doctest-check-examples-in-docstrings.py` | doctest: check examples in docstrings (line 225) | may use names from earlier examples |
| `examples/03_replacing-an-external-dependency-with-a-mock.py` | Replacing an external dependency with a mock (line 293) | may use names from earlier examples |
| `examples/04_replacing-an-external-dependency-with-a-mock.py` | Replacing an external dependency with a mock (line 318) | may use names from earlier examples |
| `examples/05_try-it-yourself.py` | Try it yourself (line 556) | may use names from earlier examples |
