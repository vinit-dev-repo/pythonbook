# 17 - Scopes, Closures and Higher-Order Functions

The code of the chapter **17 - Scopes, Closures and Higher-Order Functions** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How ordinary function-body names resolve to local, enclosing or global bindings, and where built-ins fit
- Why assigning to a name inside a function can produce a confusing `UnboundLocalError`
- `global` and `nonlocal` — reaching outside a function's own local scope
- What a **closure** retains, and how late binding affects both global loop variables and enclosing function variables
- What a **higher-order function** is, and how to inspect a function like any other object
- `functools.reduce`, `functools.partial`, and the `operator` module

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-a-scope-is.py` | What a scope is (line 50) | raises an error on purpose |
| `examples/02_the-legb-rule.py` | The LEGB rule (line 107) | may use names from earlier examples |
| `examples/03_recover-a-shadowed-built-in-explicitly.py` | The LEGB rule › Recover a shadowed built-in explicitly (line 138) | may use names from earlier examples |
| `examples/04_local-scope-is-created-fresh-every-call.py` | Local scope is created fresh, every call (line 170) | may use names from earlier examples |
| `examples/05_the-assignment-makes-it-local-rule.py` | The assignment-makes-it-local rule (line 198) | raises an error on purpose |
| `examples/06_the-global-keyword.py` | The assignment-makes-it-local rule › The `global` keyword (line 230) | may use names from earlier examples |
| `examples/07_the-global-keyword.py` | The assignment-makes-it-local rule › The `global` keyword (line 255) | may use names from earlier examples |
| `examples/08_nested-functions-and-nonlocal.py` | Nested functions and `nonlocal` (line 298) | raises an error on purpose |
| `examples/09_nested-functions-and-nonlocal.py` | Nested functions and `nonlocal` (line 325) | may use names from earlier examples |
| `examples/10_an-enclosing-binding-can-receive-its-value-later.py` | Nested functions and `nonlocal` › An enclosing binding can receive its value later (line 353) | may use names from earlier examples |
| `examples/11_closures-keep-enclosing-bindings.py` | Closures keep enclosing bindings (line 399) | may use names from earlier examples |
| `examples/12_closures-keep-enclosing-bindings.py` | Closures keep enclosing bindings (line 427) | may use names from earlier examples |
| `examples/13_closures-keep-enclosing-bindings.py` | Closures keep enclosing bindings (line 438) | may use names from earlier examples |
| `examples/14_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 468) | may use names from earlier examples |
| `examples/15_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 488) | may use names from earlier examples |
| `examples/16_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 504) | may use names from earlier examples |
| `examples/17_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 525) | may use names from earlier examples |
| `examples/18_the-late-binding-loop-trap.py` | Closures keep enclosing bindings › The late-binding loop trap (line 567) | may use names from earlier examples |
| `examples/19_what-closures-are-good-for.py` | Closures keep enclosing bindings › What closures are good for (line 599) | may use names from earlier examples |
| `examples/20_what-closures-are-good-for.py` | Closures keep enclosing bindings › What closures are good for (line 622) | may use names from earlier examples |
| `examples/21_higher-order-functions.py` | Higher-order functions (line 660) | may use names from earlier examples |
| `examples/22_functions-are-objects-introspection.py` | Higher-order functions › Functions are objects: introspection (line 686) | may use names from earlier examples |
| `examples/23_functions-are-objects-introspection.py` | Higher-order functions › Functions are objects: introspection (line 709) | may use names from earlier examples |
| `examples/24_inspect-and-bind-a-call-without-running-its-body.py` | Higher-order functions › Inspect and bind a call without running its body (line 728) | may use names from earlier examples |
| `examples/25_inspect-and-bind-a-call-without-running-its-body.py` | Higher-order functions › Inspect and bind a call without running its body (line 773) | may use names from earlier examples |
| `examples/26_argument-failures-occur-before-the-body-starts.py` | Higher-order functions › Argument failures occur before the body starts (line 800) | may use names from earlier examples |
| `examples/27_choose-where-persistent-state-lives.py` | Higher-order functions › Choose where persistent state lives (line 853) | may use names from earlier examples |
| `examples/28_reducing-a-whole-sequence-to-one-value.py` | Reducing a whole sequence to one value (line 905) | may use names from earlier examples |
| `examples/29_reducing-a-whole-sequence-to-one-value.py` | Reducing a whole sequence to one value (line 933) | may use names from earlier examples |
| `examples/30_reducing-a-whole-sequence-to-one-value.py` | Reducing a whole sequence to one value (line 956) | may use names from earlier examples |
| `examples/31_functools-partial-pre-filling-arguments.py` | `functools.partial`: pre-filling arguments (line 984) | may use names from earlier examples |
| `examples/32_functools-partial-pre-filling-arguments.py` | `functools.partial`: pre-filling arguments (line 997) | may use names from earlier examples |
| `examples/33_inspect-saved-arguments-and-reserve-a-position.py` | `functools.partial`: pre-filling arguments › Inspect saved arguments and reserve a position (line 1028) | may use names from earlier examples |
| `examples/34_inspect-saved-arguments-and-reserve-a-position.py` | `functools.partial`: pre-filling arguments › Inspect saved arguments and reserve a position (line 1049) | may use names from earlier examples |
| `examples/35_the-operator-module.py` | The `operator` module (line 1083) | may use names from earlier examples |
| `examples/36_the-operator-module.py` | The `operator` module (line 1097) | may use names from earlier examples |
| `examples/37_practice-combine-values-under-a-stated-contract.py` | Practice: combine values under a stated contract (line 1122) | may use names from earlier examples |
| `examples/38_lambdas-revisited.py` | Lambdas revisited (line 1175) | may use names from earlier examples |
| `examples/39_lambdas-revisited.py` | Lambdas revisited (line 1191) | may use names from earlier examples |
| `examples/40_a-lambda-can-create-a-callback-with-its-own-capt.py` | Lambdas revisited › A lambda can create a callback with its own captured value (line 1218) | runs on its own |
| `examples/41_a-lambda-can-create-a-callback-with-its-own-capt.py` | Lambdas revisited › A lambda can create a callback with its own captured value (line 1253) | runs on its own |
| `examples/42_try-it-yourself.py` | Try it yourself (line 1310) | may use names from earlier examples |
| `examples/43_try-it-yourself.py` | Try it yourself (line 1365) | may use names from earlier examples |
