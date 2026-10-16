# 27 - Callable Objects and Class Decorators

The code of the chapter **27 - Callable Objects and Class Decorators** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Distinguish callable objects from calls with valid arguments.
- Build attribute and method tools, and reason about the state each callable retains.
- Explain why a callable decorator instance does not automatically bind like a method.
- Trace configured decoration separately from later wrapper calls.
- Add behavior to a class, or return a replacement while preserving the intended object identities.
- Diagnose accidental shared state and distinguish it from deliberate caching and registration.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `call_timings.py` | Retain timing totals without losing the receiver (line 744) |  |
| `development_decoration.py` | Choose development-only decoration explicitly (line 1366) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_functions-classes-and-other-objects.py` | Functions, classes, and other objects (line 57) | runs on its own |
| `examples/02_callables-objects-that-you-can-call.py` | Callables: objects that you can call (line 90) | may use names from earlier examples |
| `examples/03_being-callable-is-not-enough.py` | Being callable is not enough (line 132) | runs on its own |
| `examples/04_being-callable-is-not-enough.py` | Being callable is not enough (line 169) | runs on its own |
| `examples/05_reading-attributes-with-operator-attrgetter.py` | Reading attributes with `operator.attrgetter` (line 224) | may use names from earlier examples |
| `examples/06_follow-nested-attribute-names.py` | Follow nested attribute names (line 248) | runs on its own |
| `examples/07_build-a-tool-then-use-it.py` | Build a tool, then use it (line 281) | runs on its own |
| `examples/08_build-a-tool-then-use-it.py` | Build a tool, then use it (line 331) | runs on its own |
| `examples/09_decorator-classes.py` | Decorator classes (line 390) | may use names from earlier examples |
| `examples/10_a-wrapper-object-keeps-its-own-state.py` | A wrapper object keeps its own state (line 436) | runs on its own |
| `examples/11_method-binding-has-two-receivers.py` | Method binding has two receivers (line 520) | runs on its own |
| `examples/12_dispatch-on-a-method-argument.py` | Dispatch on a method argument (line 613) | runs on its own |
| `examples/13_a-configured-decorator-creates-a-wrapper-functio.py` | A configured decorator creates a wrapper function (line 669) | runs on its own |
| `examples/14_decorating-classes.py` | Decorating classes (line 823) | may use names from earlier examples |
| `examples/15_decorating-classes.py` | Decorating classes (line 852) | runs on its own |
| `examples/16_returning-the-value-that-the-name-needs.py` | Returning the value that the name needs (line 881) | runs on its own |
| `examples/17_returning-the-value-that-the-name-needs.py` | Returning the value that the name needs (line 906) | runs on its own |
| `examples/18_one-reusable-method-for-local-classes.py` | One reusable method for local classes (line 937) | runs on its own |
| `examples/19_completing-an-ordering-carefully.py` | Completing an ordering carefully (line 994) | runs on its own |
| `examples/20_completing-an-ordering-carefully.py` | Completing an ordering carefully (line 1068) | runs on its own |
| `examples/21_a-decorator-can-replace-a-class-name-with-a-cons.py` | A decorator can replace a class name with a construction function (line 1120) | runs on its own |
| `examples/22_a-shared-wrapper-can-silently-overwrite-an-earli.py` | A shared wrapper can silently overwrite an earlier record (line 1156) | runs on its own |
| `examples/23_a-shared-wrapper-can-silently-overwrite-an-earli.py` | A shared wrapper can silently overwrite an earlier record (line 1201) | runs on its own |
| `examples/24_deliberate-first-instance-caching.py` | Deliberate first-instance caching (line 1242) | runs on its own |
| `examples/25_registration-can-leave-later-calls-unchanged.py` | Registration can leave later calls unchanged (line 1297) | runs on its own |
| `examples/26_try-it-yourself.py` | Try it yourself (line 1453) | may use names from earlier examples |
| `examples/27_try-it-yourself.py` | Try it yourself (line 1487) | may use names from earlier examples |
