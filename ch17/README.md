# 17 - Scopes, Closures and Higher-Order Functions

The code of this chapter of the Python tutorial, extracted byte for byte from the certified chapter. The chapter explains every line; read it there.

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Section | Note |
|---|---|---|
| `examples/01_what-a-scope-is.py` | What a scope is | raises an error on purpose |
| `examples/02_the-legb-rule.py` | The LEGB rule | may use names from earlier examples |
| `examples/03_recover-a-shadowed-built-in-explicitly.py` | Recover a shadowed built-in explicitly | may use names from earlier examples |
| `examples/04_local-scope-is-created-fresh-every-call.py` | Local scope is created fresh, every call | may use names from earlier examples |
| `examples/05_the-assignment-makes-it-local-rule.py` | The assignment-makes-it-local rule | raises an error on purpose |
| `examples/06_the-global-keyword.py` | The `global` keyword | may use names from earlier examples |
| `examples/07_the-global-keyword.py` | The `global` keyword | may use names from earlier examples |
| `examples/08_nested-functions-and-nonlocal.py` | Nested functions and `nonlocal` | raises an error on purpose |
| `examples/09_nested-functions-and-nonlocal.py` | Nested functions and `nonlocal` | may use names from earlier examples |
| `examples/10_an-enclosing-binding-can-receive-its-value-later.py` | An enclosing binding can receive its value later | may use names from earlier examples |
| `examples/11_closures-keep-enclosing-bindings.py` | Closures keep enclosing bindings | may use names from earlier examples |
| `examples/12_closures-keep-enclosing-bindings.py` | Closures keep enclosing bindings | may use names from earlier examples |
| `examples/13_closures-keep-enclosing-bindings.py` | Closures keep enclosing bindings | may use names from earlier examples |
| `examples/14_the-late-binding-loop-trap.py` | The late-binding loop trap | may use names from earlier examples |
| `examples/15_the-late-binding-loop-trap.py` | The late-binding loop trap | may use names from earlier examples |
| `examples/16_the-late-binding-loop-trap.py` | The late-binding loop trap | may use names from earlier examples |
| `examples/17_the-late-binding-loop-trap.py` | The late-binding loop trap | may use names from earlier examples |
| `examples/18_the-late-binding-loop-trap.py` | The late-binding loop trap | may use names from earlier examples |
| `examples/19_what-closures-are-good-for.py` | What closures are good for | may use names from earlier examples |
| `examples/20_what-closures-are-good-for.py` | What closures are good for | may use names from earlier examples |
| `examples/21_higher-order-functions.py` | Higher-order functions | may use names from earlier examples |
| `examples/22_functions-are-objects-introspection.py` | Functions are objects: introspection | may use names from earlier examples |
| `examples/23_functions-are-objects-introspection.py` | Functions are objects: introspection | may use names from earlier examples |
| `examples/24_inspect-and-bind-a-call-without-running-its-body.py` | Inspect and bind a call without running its body | may use names from earlier examples |
| `examples/25_inspect-and-bind-a-call-without-running-its-body.py` | Inspect and bind a call without running its body | may use names from earlier examples |
| `examples/26_argument-failures-occur-before-the-body-starts.py` | Argument failures occur before the body starts | may use names from earlier examples |
| `examples/27_choose-where-persistent-state-lives.py` | Choose where persistent state lives | may use names from earlier examples |
| `examples/28_reducing-a-whole-sequence-to-one-value.py` | Reducing a whole sequence to one value | may use names from earlier examples |
| `examples/29_reducing-a-whole-sequence-to-one-value.py` | Reducing a whole sequence to one value | may use names from earlier examples |
| `examples/30_reducing-a-whole-sequence-to-one-value.py` | Reducing a whole sequence to one value | may use names from earlier examples |
| `examples/31_functools-partial-pre-filling-arguments.py` | `functools.partial`: pre-filling arguments | may use names from earlier examples |
| `examples/32_functools-partial-pre-filling-arguments.py` | `functools.partial`: pre-filling arguments | may use names from earlier examples |
| `examples/33_inspect-saved-arguments-and-reserve-a-position.py` | Inspect saved arguments and reserve a position | may use names from earlier examples |
| `examples/34_inspect-saved-arguments-and-reserve-a-position.py` | Inspect saved arguments and reserve a position | may use names from earlier examples |
| `examples/35_the-operator-module.py` | The `operator` module | may use names from earlier examples |
| `examples/36_the-operator-module.py` | The `operator` module | may use names from earlier examples |
| `examples/37_practice-combine-values-under-a-stated-contract.py` | Practice: combine values under a stated contract | may use names from earlier examples |
| `examples/38_lambdas-revisited.py` | Lambdas revisited | may use names from earlier examples |
| `examples/39_lambdas-revisited.py` | Lambdas revisited | may use names from earlier examples |
| `examples/40_a-lambda-can-create-a-callback-with-its-own-capt.py` | A lambda can create a callback with its own captured value | runs on its own |
| `examples/41_a-lambda-can-create-a-callback-with-its-own-capt.py` | A lambda can create a callback with its own captured value | runs on its own |
| `examples/42_try-it-yourself.py` | Try it yourself | may use names from earlier examples |
| `examples/43_try-it-yourself.py` | Try it yourself | may use names from earlier examples |
