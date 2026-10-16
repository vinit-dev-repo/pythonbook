# 18 - Function Decorators

The code of the chapter **18 - Function Decorators** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- The problem decorators solve, and why they save you from editing every function by hand
- How to build a decorator from scratch, step by step, with no magic
- What happens when a decorated function is defined, and what happens only when it is called
- Why wrappers need `*args`/`**kwargs`, and why `functools.wraps` matters
- How to write a timer, a logger, and stack several decorators together
- How to remember answers a function already worked out (memoization), by hand and with `functools.lru_cache`
- How to write a decorator that takes its own arguments (a decorator factory)
- How to make one function behave differently depending on the *type* of its argument (dispatching)

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `parameter_rules.py` | Check named parameters before the body runs (line 913) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_building-a-decorator-from-first-principles.py` | Building a decorator from first principles (line 79) | runs on its own |
| `examples/02_the-syntax-decoration-when-a-function-is-defined.py` | The `@` syntax: decoration when a function is defined (line 122) | may use names from earlier examples |
| `examples/03_the-syntax-decoration-when-a-function-is-defined.py` | The `@` syntax: decoration when a function is defined (line 129) | may use names from earlier examples |
| `examples/04_the-syntax-decoration-when-a-function-is-defined.py` | The `@` syntax: decoration when a function is defined (line 148) | may use names from earlier examples |
| `examples/05_fitting-any-function-args-and-kwargs.py` | Fitting any function: `*args` and `**kwargs` (line 196) | may use names from earlier examples |
| `examples/06_the-name-problem-and-functools-wraps.py` | The name problem, and `functools.wraps` (line 233) | may use names from earlier examples |
| `examples/07_the-name-problem-and-functools-wraps.py` | The name problem, and `functools.wraps` (line 253) | may use names from earlier examples |
| `examples/08_a-timer.py` | A timer (line 297) | may use names from earlier examples |
| `examples/09_a-timer.py` | A timer (line 316) | may use names from earlier examples |
| `examples/10_a-logger.py` | A logger (line 343) | may use names from earlier examples |
| `examples/11_stacking-decorators.py` | Stacking decorators (line 379) | may use names from earlier examples |
| `examples/12_stacking-decorators.py` | Stacking decorators (line 398) | runs on its own |
| `examples/13_by-hand-with-a-cache-dictionary.py` | Memoization: remembering answers › By hand, with a cache dictionary (line 432) | may use names from earlier examples |
| `examples/14_the-built-in-version-functools-lru-cache.py` | Memoization: remembering answers › The built-in version: `functools.lru_cache` (line 470) | may use names from earlier examples |
| `examples/15_the-built-in-version-functools-lru-cache.py` | Memoization: remembering answers › The built-in version: `functools.lru_cache` (line 496) | may use names from earlier examples |
| `examples/16_the-built-in-version-functools-lru-cache.py` | Memoization: remembering answers › The built-in version: `functools.lru_cache` (line 539) | may use names from earlier examples |
| `examples/17_the-built-in-version-functools-lru-cache.py` | Memoization: remembering answers › The built-in version: `functools.lru_cache` (line 572) | may use names from earlier examples |
| `examples/18_decorator-factories-decorators-with-arguments.py` | Decorator factories: decorators with arguments (line 612) | may use names from earlier examples |
| `examples/19_decorator-factories-decorators-with-arguments.py` | Decorator factories: decorators with arguments (line 655) | may use names from earlier examples |
| `examples/20_decorator-factories-decorators-with-arguments.py` | Decorator factories: decorators with arguments (line 669) | may use names from earlier examples |
| `examples/21_configure-registration-without-a-call-wrapper.py` | Decorator factories: decorators with arguments › Configure registration without a call wrapper (line 703) | runs on its own |
| `examples/22_configure-the-timer-s-printed-precision.py` | Decorator factories: decorators with arguments › Configure the timer's printed precision (line 760) | runs on its own |
| `examples/23_two-ways-to-tell-a-decorator-what-to-do.py` | Two ways to tell a decorator what to do (line 812) | may use names from earlier examples |
| `examples/24_two-ways-to-tell-a-decorator-what-to-do.py` | Two ways to tell a decorator what to do (line 851) | may use names from earlier examples |
| `examples/25_the-naive-way-a-chain-of-isinstance-checks.py` | Dispatching: different behaviour by type › The naive way: a chain of `isinstance` checks (line 994) | may use names from earlier examples |
| `examples/26_a-hand-rolled-registry.py` | Dispatching: different behaviour by type › A hand-rolled registry (line 1014) | may use names from earlier examples |
| `examples/27_a-hand-rolled-registry.py` | Dispatching: different behaviour by type › A hand-rolled registry (line 1049) | may use names from earlier examples |
| `examples/28_functools-singledispatch-the-built-in-version.py` | Dispatching: different behaviour by type › `functools.singledispatch`: the built-in version (line 1070) | may use names from earlier examples |
| `examples/29_functools-singledispatch-the-built-in-version.py` | Dispatching: different behaviour by type › `functools.singledispatch`: the built-in version (line 1109) | may use names from earlier examples |
| `examples/30_try-it-yourself.py` | Try it yourself (line 1175) | may use names from earlier examples |
| `examples/31_try-it-yourself.py` | Try it yourself (line 1241) | runs on its own |
