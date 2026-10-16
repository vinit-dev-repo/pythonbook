# 25 - Testing Your Code

The code of the chapter **25 - Testing Your Code** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why tests are useful and which problems they help you find
- What a test is, in plain words
- How to write and run tests with `pytest`, the modern default
- How to test that an error is correctly raised
- How to avoid copy-pasting near-identical tests with `parametrize`
- How to share setup between tests with `fixtures`
- The standard-library alternative, `unittest`, and when you'll meet it
- How `doctest` checks examples inside documentation
- What to actually test: the happy path, the edges, and the errors
- An introduction to mocking, coverage, and test-driven development

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

The chapter saves these files more than once (for example a first version and a repaired one). This folder holds the version the chapter ends with, and the table points to that last version:

- `calculator.py`
- `multiples.py`
- `test_coverage_demo.py`
- `test_multiples.py`

| File | Where it is in the chapter | Note |
|---|---|---|
| `test_calculator.py` | Writing a test file (line 190) |  |
| `test_exceptions.py` | Testing for exceptions: `pytest.raises` (line 305) |  |
| `test_parameters.py` | Parametrize: one test, many inputs (line 339) |  |
| `test_average.py` | Check a complete example: average (line 386) |  |
| `selection.py` | Choose the expected subset independently (line 507) |  |
| `test_selection.py` | Choose the expected subset independently (line 513) |  |
| `labels.py` | Use a round trip alongside known values (line 540) |  |
| `test_labels.py` | Use a round trip alongside known values (line 549) |  |
| `catalog.py` | Check the state after an operation (line 589) |  |
| `test_catalog.py` | Check the state after an operation (line 629) |  |
| `test_weak_replacement.py` | Make sure a test can catch the defect (line 720) |  |
| `test_calculator_unittest.py` | unittest: the standard-library way (line 1081) |  |
| `cleanup_unittest_demo.py` | Check cleanup when unittest setup fails (line 1199) |  |
| `weather_logic.py` | Test the weather caller, not just the replacement (line 1406) |  |
| `test_weather_logic.py` | Test the weather caller, not just the replacement (line 1415) |  |
| `weather_source.py` | Patch the name the caller reads (line 1453) |  |
| `weather_report.py` | Patch the name the caller reads (line 1459) |  |
| `test_wrong_target.py` | Patch the name the caller reads (line 1478) |  |
| `test_weather_report.py` | Patch the name the caller reads (line 1492) |  |
| `waiting.py` | Control time through an explicit input (line 1528) |  |
| `test_waiting.py` | Control time through an explicit input (line 1534) |  |
| `calculator.py` | A note on coverage (line 1569) | rewritten later in the chapter |
| `test_coverage_demo.py` | A note on coverage (line 1619) | rewritten later in the chapter |
| `test_multiples.py` | Test-driven development (line 1699) | rewritten later in the chapter |
| `multiples.py` | Test-driven development (line 1725) | rewritten later in the chapter |
| `boundaries.py` | Return a status without confusing it with the result (line 1767) |  |
| `driver_demo.py` | Run three invocations and inspect surviving state (line 1798) |  |
| `decorator_demo.py` | A decorator with a different failure contract (line 1879) |  |
| `test_practice.py` | Try it yourself (line 1958) |  |
| `test_palindrome.py` | Try it yourself (line 2019) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-a-test-actually-is.py` | What a test actually is (line 89) | runs on its own |
| `examples/02_what-a-test-actually-is.py` | What a test actually is (line 112) | may use names from earlier examples |
| `examples/03_the-arrange-act-assert-pattern.py` | The Arrange-Act-Assert pattern (line 439) | may use names from earlier examples |
| `examples/04_naming-tests-so-they-read-like-sentences.py` | Naming tests so they read like sentences (line 461) | may use names from earlier examples |
| `examples/05_check-a-relation-the-contract-promises.py` | Check a relation the contract promises (line 484) | may use names from earlier examples |
| `examples/06_make-sure-a-test-can-catch-the-defect.py` | Make sure a test can catch the defect (line 743) | a fragment, not a complete program |
| `examples/07_fixtures-shared-setup.py` | Fixtures: shared setup (line 779) | may use names from earlier examples |
| `examples/08_a-fixture-can-request-another-fixture.py` | A fixture can request another fixture (line 819) | may use names from earlier examples |
| `examples/09_rerun-the-old-checks-after-changing-setup.py` | Rerun the old checks after changing setup (line 852) | may use names from earlier examples |
| `examples/10_setup-yield-and-teardown.py` | Setup, yield and teardown (line 881) | may use names from earlier examples |
| `examples/11_observe-cleanup-after-it-happens.py` | Observe cleanup after it happens (line 921) | may use names from earlier examples |
| `examples/12_setup-can-fail-before-yield.py` | Setup can fail before yield (line 991) | may use names from earlier examples |
| `examples/13_setup-and-teardown.py` | setUp and tearDown (line 1136) | may use names from earlier examples |
| `examples/14_doctest-check-examples-in-docstrings.py` | doctest: check examples in docstrings (line 1270) | may use names from earlier examples |
| `examples/15_replacing-an-external-dependency-with-a-mock.py` | Replacing an external dependency with a mock (line 1336) | may use names from earlier examples |
| `examples/16_replacing-an-external-dependency-with-a-mock.py` | Replacing an external dependency with a mock (line 1365) | may use names from earlier examples |
| `examples/17_try-it-yourself.py` | Try it yourself (line 2029) | may use names from earlier examples |
| `examples/18_try-it-yourself.py` | Try it yourself (line 2038) | may use names from earlier examples |

## Terminal commands

| File | Where it is in the chapter | Note |
|---|---|---|
| `commands/01_check-the-state-after-an-operation.sh` | Check the state after an operation (line 706) | bash commands to type in a terminal |
| `commands/02_make-sure-a-test-can-catch-the-defect.sh` | Make sure a test can catch the defect (line 750) | bash commands to type in a terminal |
