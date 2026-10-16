# 09 - Functions

The code of the chapter **09 - Functions** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a function is, and why reusing code matters
- Defining a function with `def`, calling it, and what `return` really does
- The difference between parameters and arguments
- Positional arguments, keyword arguments, and default values
- The mutable default argument trap — and how to avoid it
- `*args` and `**kwargs`, and unpacking values into a call
- Keyword-only arguments
- Docstrings and type annotations
- Lambdas, `map()`, `filter()`, and useful built-ins: `round`, `sorted`, `min`/`max`, `zip`
- That functions are values, and can be passed around like any other value

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-a-function-is.py` | What a function is? (line 55) | runs on its own |
| `examples/02_defining-calling-and-return.py` | Defining, calling, and `return` (line 80) | may use names from earlier examples |
| `examples/03_defining-calling-and-return.py` | Defining, calling, and `return` (line 113) | may use names from earlier examples |
| `examples/04_no-return-means-none.py` | No `return` means `None` (line 136) | may use names from earlier examples |
| `examples/05_reaching-a-definition-is-different-from-calling.py` | Reaching a definition is different from calling it (line 166) | may use names from earlier examples |
| `examples/06_parameters-and-arguments.py` | Parameters and arguments (line 207) | may use names from earlier examples |
| `examples/07_functions-are-values-too.py` | Functions are values too (line 227) | may use names from earlier examples |
| `examples/08_select-an-action-from-a-dictionary.py` | Select an action from a dictionary (line 262) | may use names from earlier examples |
| `examples/09_reuse-an-operation-across-compatible-sequences.py` | Reuse an operation across compatible sequences (line 301) | may use names from earlier examples |
| `examples/10_positional-and-keyword-arguments.py` | Positional and keyword arguments (line 344) | may use names from earlier examples |
| `examples/11_positional-and-keyword-arguments.py` | Positional and keyword arguments (line 358) | may use names from earlier examples |
| `examples/12_positional-and-keyword-arguments.py` | Positional and keyword arguments (line 369) | may use names from earlier examples |
| `examples/13_default-values.py` | Default values (line 391) | may use names from earlier examples |
| `examples/14_the-mutable-default-trap.py` | The mutable default trap (line 420) | may use names from earlier examples |
| `examples/15_the-mutable-default-trap.py` | The mutable default trap (line 454) | may use names from earlier examples |
| `examples/16_the-mutable-default-trap.py` | The mutable default trap (line 473) | may use names from earlier examples |
| `examples/17_defaults-retain-their-definition-time-value.py` | Defaults retain their definition-time value (line 516) | may use names from earlier examples |
| `examples/18_distinguishing-omission-from-an-explicit-none.py` | Distinguishing omission from an explicit `None` (line 545) | may use names from earlier examples |
| `examples/19_distinguishing-omission-from-an-explicit-none.py` | Distinguishing omission from an explicit `None` (line 580) | may use names from earlier examples |
| `examples/20_args-collecting-extra-positional-arguments.py` | `*args`: collecting extra positional arguments (line 614) | may use names from earlier examples |
| `examples/21_args-collecting-extra-positional-arguments.py` | `*args`: collecting extra positional arguments (line 633) | may use names from earlier examples |
| `examples/22_args-collecting-extra-positional-arguments.py` | `*args`: collecting extra positional arguments (line 649) | may use names from earlier examples |
| `examples/23_kwargs-collecting-extra-keyword-arguments.py` | `**kwargs`: collecting extra keyword arguments (line 666) | may use names from earlier examples |
| `examples/24_kwargs-collecting-extra-keyword-arguments.py` | `**kwargs`: collecting extra keyword arguments (line 683) | may use names from earlier examples |
| `examples/25_unpacking-iterables-into-a-call.py` | Unpacking iterables into a call (line 709) | may use names from earlier examples |
| `examples/26_unpacking-iterables-into-a-call.py` | Unpacking iterables into a call (line 726) | may use names from earlier examples |
| `examples/27_keyword-only-arguments.py` | Keyword-only arguments (line 752) | may use names from earlier examples |
| `examples/28_keyword-only-arguments.py` | Keyword-only arguments (line 765) | raises an error on purpose |
| `examples/29_combine-several-argument-sources.py` | Combine several argument sources (line 792) | may use names from earlier examples |
| `examples/30_docstrings.py` | Docstrings (line 830) | may use names from earlier examples |
| `examples/31_docstrings.py` | Docstrings (line 845) | may use names from earlier examples |
| `examples/32_dir-listing-an-object-s-names.py` | `dir()`: listing an object's names (line 870) | may use names from earlier examples |
| `examples/33_dir-listing-an-object-s-names.py` | `dir()`: listing an object's names (line 887) | may use names from earlier examples |
| `examples/34_dir-listing-an-object-s-names.py` | `dir()`: listing an object's names (line 900) | may use names from earlier examples |
| `examples/35_dir-listing-an-object-s-names.py` | `dir()`: listing an object's names (line 923) | may use names from earlier examples |
| `examples/36_type-annotations.py` | Type annotations (line 943) | may use names from earlier examples |
| `examples/37_lambdas-one-line-nameless-functions.py` | Lambdas: one-line nameless functions (line 970) | may use names from earlier examples |
| `examples/38_lambdas-one-line-nameless-functions.py` | Lambdas: one-line nameless functions (line 982) | may use names from earlier examples |
| `examples/39_lambdas-one-line-nameless-functions.py` | Lambdas: one-line nameless functions (line 989) | may use names from earlier examples |
| `examples/40_comprehensions-map-and-filter.py` | Comprehensions, `map()`, and `filter()` (line 1015) | may use names from earlier examples |
| `examples/41_comprehensions-map-and-filter.py` | Comprehensions, `map()`, and `filter()` (line 1034) | may use names from earlier examples |
| `examples/42_map-and-filter-with-lambdas.py` | `map()` and `filter()` with lambdas (line 1059) | may use names from earlier examples |
| `examples/43_map-and-filter-with-lambdas.py` | `map()` and `filter()` with lambdas (line 1081) | may use names from earlier examples |
| `examples/44_round.py` | `round()` (line 1099) | may use names from earlier examples |
| `examples/45_round.py` | `round()` (line 1112) | may use names from earlier examples |
| `examples/46_sorted.py` | `sorted()` (line 1129) | may use names from earlier examples |
| `examples/47_min-and-max.py` | `min()` and `max()` (line 1150) | may use names from earlier examples |
| `examples/48_zip.py` | `zip()` (line 1172) | may use names from earlier examples |
| `examples/49_zip.py` | `zip()` (line 1189) | may use names from earlier examples |
| `examples/50_try-it-yourself.py` | Try it yourself (line 1229) | may use names from earlier examples |
| `examples/51_try-it-yourself.py` | Try it yourself (line 1245) | may use names from earlier examples |
