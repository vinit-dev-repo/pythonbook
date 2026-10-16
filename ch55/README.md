# 55 - Writing Effective Python

The code of the chapter **55 - Writing Effective Python** of the Python tutorial (folder `11 - Design, craft and next steps`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- 39 ways to review and improve Python code
- When each habit helps, what it costs, and when another choice may be better
- Common mistakes involving shared values, errors, and iteration
- How to use the Zen of Python and a review checklist

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `crate_labels.py` | Organising and maintaining a project › Build and inspect module documentation (line 1361) |  |
| `benchmark_cases.py` | Organising and maintaining a project › Measurement lab: compare the same work across interpreters (line 1651) |  |
| `compare_benchmarks.py` | Organising and maintaining a project › Measurement lab: compare the same work across interpreters (line 1725) |  |
| `record_formats.py` | Apply shared Strategy and Command with Python callables › Select a result from an explicit registry (line 1791) |  |
| `compare_formats.py` | Apply shared Strategy and Command with Python callables › Select a result from an explicit registry (line 1832) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_item-1-start-with-a-function-or-module-when-you.py` | Creating objects › Item 1 — start with a function or module when you do not need a class (line 68) | runs on its own |
| `examples/02_item-2-use-dataclasses-for-data-holding-classes.py` | Creating objects › Item 2 — use dataclasses for data-holding classes (line 99) | may use names from earlier examples |
| `examples/03_item-2-use-dataclasses-for-data-holding-classes.py` | Creating objects › Item 2 — use dataclasses for data-holding classes (line 124) | may use names from earlier examples |
| `examples/04_item-3-classmethod-alternative-constructors-inst.py` | Creating objects › Item 3 — classmethod alternative constructors instead of many optional flags (line 152) | may use names from earlier examples |
| `examples/05_item-4-prefer-composition-over-inheritance.py` | Creating objects › Item 4 — prefer composition over inheritance (line 192) | may use names from earlier examples |
| `examples/06_item-5-prefer-dependency-injection-to-hard-wirin.py` | Creating objects › Item 5 — prefer dependency injection to hard-wiring a resource (line 233) | may use names from earlier examples |
| `examples/07_item-5-prefer-dependency-injection-to-hard-wirin.py` | Creating objects › Item 5 — prefer dependency injection to hard-wiring a resource (line 253) | may use names from earlier examples |
| `examples/08_item-6-return-a-defensive-copy-of-internal-mutab.py` | Creating objects › Item 6 — return a defensive copy of internal mutable data (line 284) | may use names from earlier examples |
| `examples/09_item-6-return-a-defensive-copy-of-internal-mutab.py` | Creating objects › Item 6 — return a defensive copy of internal mutable data (line 305) | may use names from earlier examples |
| `examples/10_item-7-keyword-only-arguments-for-clarity-at-cal.py` | APIs and functions › Item 7 — keyword-only arguments for clarity at call sites (line 348) | may use names from earlier examples |
| `examples/11_item-8-validate-arguments-at-the-top-of-a-functi.py` | APIs and functions › Item 8 — validate arguments at the top of a function (line 371) | may use names from earlier examples |
| `examples/12_item-8-validate-arguments-at-the-top-of-a-functi.py` | APIs and functions › Item 8 — validate arguments at the top of a function (line 394) | may use names from earlier examples |
| `examples/13_item-9-return-rich-objects-not-mystery-tuples.py` | APIs and functions › Item 9 — return rich objects, not mystery tuples (line 421) | may use names from earlier examples |
| `examples/14_item-10-avoid-returning-none-to-mean-failure.py` | APIs and functions › Item 10 — avoid returning None to mean failure (line 449) | may use names from earlier examples |
| `examples/15_item-11-return-an-empty-collection-when-there-ar.py` | APIs and functions › Item 11 — return an empty collection when there are no results (line 485) | may use names from earlier examples |
| `examples/16_item-11-return-an-empty-collection-when-there-ar.py` | APIs and functions › Item 11 — return an empty collection when there are no results (line 507) | may use names from earlier examples |
| `examples/17_item-12-keep-functions-small-and-single-purpose.py` | APIs and functions › Item 12 — keep functions small and single-purpose (line 530) | may use names from earlier examples |
| `examples/18_item-13-type-hints-as-living-documentation.py` | APIs and functions › Item 13 — type hints as living documentation (line 562) | may use names from earlier examples |
| `examples/19_item-14-use-typing-override-when-you-mean-to-ove.py` | APIs and functions › Item 14 — use @typing.override when you mean to override (line 587) | may use names from earlier examples |
| `examples/20_item-14-use-typing-override-when-you-mean-to-ove.py` | APIs and functions › Item 14 — use @typing.override when you mean to override (line 609) | may use names from earlier examples |
| `examples/21_item-15-use-typevar-generic-so-a-container-keeps.py` | APIs and functions › Item 15 — use TypeVar / Generic so a container keeps its element type (line 633) | may use names from earlier examples |
| `examples/22_item-15-use-typevar-generic-so-a-container-keeps.py` | APIs and functions › Item 15 — use TypeVar / Generic so a container keeps its element type (line 657) | may use names from earlier examples |
| `examples/23_item-15-use-typevar-generic-so-a-container-keeps.py` | APIs and functions › Item 15 — use TypeVar / Generic so a container keeps its element type (line 685) | may use names from earlier examples |
| `examples/24_item-16-choose-eafp-when-it-makes-the-action-cle.py` | Pythonic idioms › Item 16 — choose EAFP when it makes the action clearer (line 721) | may use names from earlier examples |
| `examples/25_item-17-comprehensions-over-map-filter-chains-bu.py` | Pythonic idioms › Item 17 — comprehensions over map/filter chains, but loops over clever one-liners (line 751) | may use names from earlier examples |
| `examples/26_item-18-declare-variables-where-you-use-them-in.py` | Pythonic idioms › Item 18 — declare variables where you use them, in the smallest scope (line 782) | may use names from earlier examples |
| `examples/27_item-18-declare-variables-where-you-use-them-in.py` | Pythonic idioms › Item 18 — declare variables where you use them, in the smallest scope (line 805) | may use names from earlier examples |
| `examples/28_item-19-unpacking-over-indexing.py` | Pythonic idioms › Item 19 — unpacking over indexing (line 833) | may use names from earlier examples |
| `examples/29_item-20-enumerate-and-zip-over-range-len.py` | Pythonic idioms › Item 20 — enumerate and zip over range(len(...)) (line 862) | may use names from earlier examples |
| `examples/30_item-21-f-strings-by-default.py` | Pythonic idioms › Item 21 — f-strings by default (line 904) | may use names from earlier examples |
| `examples/31_item-22-build-strings-with-join-not-in-a-loop.py` | Pythonic idioms › Item 22 — build strings with `"".join()`, not `+=` in a loop (line 926) | may use names from earlier examples |
| `examples/32_item-22-build-strings-with-join-not-in-a-loop.py` | Pythonic idioms › Item 22 — build strings with `"".join()`, not `+=` in a loop (line 962) | may use names from earlier examples |
| `examples/33_item-23-pathlib-over-os-path.py` | Pythonic idioms › Item 23 — pathlib over os.path (line 1016) | may use names from earlier examples |
| `examples/34_item-24-with-for-every-resource.py` | Pythonic idioms › Item 24 — with for every resource (line 1047) | may use names from earlier examples |
| `examples/35_item-25-mutable-default-arguments.py` | Common error patterns › Item 25 — mutable default arguments (line 1078) | may use names from earlier examples |
| `examples/36_item-25-mutable-default-arguments.py` | Common error patterns › Item 25 — mutable default arguments (line 1095) | may use names from earlier examples |
| `examples/37_item-26-late-binding-closures-in-loops.py` | Common error patterns › Item 26 — late-binding closures in loops (line 1120) | may use names from earlier examples |
| `examples/38_item-26-late-binding-closures-in-loops.py` | Common error patterns › Item 26 — late-binding closures in loops (line 1132) | may use names from earlier examples |
| `examples/39_item-27-is-vs-on-numbers-and-strings.py` | Common error patterns › Item 27 — is vs == on numbers and strings (line 1150) | may use names from earlier examples |
| `examples/40_item-28-shadowing-built-ins.py` | Common error patterns › Item 28 — shadowing built-ins (line 1181) | may use names from earlier examples |
| `examples/41_item-29-bare-except.py` | Common error patterns › Item 29 — bare except (line 1205) | may use names from earlier examples |
| `examples/42_item-30-floating-point-money.py` | Common error patterns › Item 30 — floating-point money (line 1233) | may use names from earlier examples |
| `examples/43_item-31-mutating-a-list-while-iterating-it.py` | Common error patterns › Item 31 — mutating a list while iterating it (line 1254) | may use names from earlier examples |
| `examples/44_item-31-mutating-a-list-while-iterating-it.py` | Common error patterns › Item 31 — mutating a list while iterating it (line 1271) | may use names from earlier examples |
| `examples/45_item-33-docstrings-on-public-things.py` | Organising and maintaining a project › Item 33 — docstrings on public things (line 1308) | may use names from earlier examples |
| `examples/46_item-34-document-the-exceptions-your-function-ra.py` | Organising and maintaining a project › Item 34 — document the exceptions your function raises (line 1329) | may use names from earlier examples |
| `examples/47_item-36-the-if-name-main-guard.py` | Organising and maintaining a project › Item 36 — the if __name__ == "__main__" guard (line 1442) | may use names from earlier examples |
| `examples/48_item-38-write-tests-as-you-go.py` | Organising and maintaining a project › Item 38 — write tests as you go (line 1478) | may use names from earlier examples |
| `examples/49_item-39-measure-before-optimizing.py` | Organising and maintaining a project › Item 39 — measure before optimizing (line 1504) | may use names from earlier examples |
| `examples/50_item-39-measure-before-optimizing.py` | Organising and maintaining a project › Item 39 — measure before optimizing (line 1525) | may use names from earlier examples |
| `examples/51_measurement-lab-batch-a-callable-and-keep-its-re.py` | Organising and maintaining a project › Measurement lab: batch a callable and keep its result (line 1570) | runs on its own |
| `examples/52_measurement-lab-setup-scope-and-command-line-tim.py` | Organising and maintaining a project › Measurement lab: setup, scope and command-line timing (line 1611) | runs on its own |
| `examples/53_compose-deferred-requests-and-state-the-failure.py` | Apply shared Strategy and Command with Python callables › Compose deferred requests and state the failure policy (line 1875) | runs on its own |
| `examples/54_the-zen-of-python-in-plain-words.py` | The Zen of Python, in plain words (line 1929) | may use names from earlier examples |
| `examples/55_try-it-yourself.py` | Try it yourself (line 2022) | may use names from earlier examples |
