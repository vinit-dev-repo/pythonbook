# 23 - Inheritance and Polymorphism

The code of the chapter **23 - Inheritance and Polymorphism** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How a child class can reuse methods and class attributes from a parent class
- `super()` — calling the next method in the MRO
- When inheritance is the right tool, and when composition is better
- The four pillars of OOP, in plain words: encapsulation, abstraction, inheritance, polymorphism
- Method Resolution Order (MRO) — the order Python searches for a method
- `__slots__` — controlling instance storage in a compatible inheritance hierarchy

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `class_counts.py` | Overriding methods › Count completed initializations (line 291) |  |
| `c3_order.py` | Method Resolution Order (MRO) › C3 preserves earlier ordering decisions (line 1001) |  |
| `selected_method.py` | Method Resolution Order (MRO) › Select one method without reversing every lookup (line 1052) |  |
| `inspect_frameworks.py` | Method Resolution Order (MRO) › Find the owner of a method in a library (line 1153) |  |
| `slot_boundaries.py` | `__slots__`: a fixed attribute list › Slot names describe storage, not default values (line 1329) |  |
| `measure_slots.py` | `__slots__`: a fixed attribute list › Measure a concrete slot workload (line 1378) |  |
| `measure_slot_memory.py` | `__slots__`: a fixed attribute list › Measure retained allocations separately from time (line 1440) |  |
| `super_contracts.py` | The diamond: when two parents share a grandparent › Cooperative arguments and explicit operator calls (line 1716) |  |
| `changing_bases.py` | The diamond: when two parents share a grandparent › A changed base affects existing instances (line 1806) |  |
| `mixed_dispatch.py` | The diamond: when two parents share a grandparent › Mixing explicit calls with a cooperative chain can repeat work (line 1859) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_inheritance-a-child-class-reuses-a-parent-class.py` | Inheritance: a child class reuses a parent class (line 63) | runs on its own |
| `examples/02_every-class-inherits-from-object.py` | Inheritance: a child class reuses a parent class › Every class inherits from `object` (line 95) | may use names from earlier examples |
| `examples/03_overriding-methods.py` | Overriding methods (line 121) | may use names from earlier examples |
| `examples/04_asking-about-instances-and-subclasses.py` | Overriding methods › Asking about instances and subclasses (line 152) | may use names from earlier examples |
| `examples/05_a-new-child-operation-changes-what-a-client-can.py` | Overriding methods › A new child operation changes what a client can ask for (line 201) | may use names from earlier examples |
| `examples/06_inherited-factories-receive-the-derived-class.py` | Overriding methods › Inherited factories receive the derived class (line 237) | may use names from earlier examples |
| `examples/07_subclass-priority-in-operators.py` | Overriding methods › Subclass priority in operators (line 358) | may use names from earlier examples |
| `examples/08_extending-instead-of-replacing-super.py` | Overriding methods › Extending instead of replacing: `super()` (line 423) | may use names from earlier examples |
| `examples/09_a-read-only-override-can-affect-base-initializat.py` | Overriding methods › A read-only override can affect base initialization (line 464) | may use names from earlier examples |
| `examples/10_inheritance-vs-composition-is-a-vs-has-a.py` | Inheritance vs composition: "is-a" vs "has-a" (line 569) | may use names from earlier examples |
| `examples/11_1-encapsulation-keeping-the-inside-private.py` | The four pillars of OOP › 1. Encapsulation — keeping the inside private (line 625) | may use names from earlier examples |
| `examples/12_1-encapsulation-keeping-the-inside-private.py` | The four pillars of OOP › 1. Encapsulation — keeping the inside private (line 643) | raises an error on purpose |
| `examples/13_mangling-separates-parent-and-child-field-names.py` | The four pillars of OOP › Mangling separates parent and child field names (line 667) | may use names from earlier examples |
| `examples/14_2-abstraction-hiding-the-how.py` | The four pillars of OOP › 2. Abstraction — hiding the how (line 716) | may use names from earlier examples |
| `examples/15_2-abstraction-hiding-the-how.py` | The four pillars of OOP › 2. Abstraction — hiding the how (line 728) | raises an error on purpose |
| `examples/16_2-abstraction-hiding-the-how.py` | The four pillars of OOP › 2. Abstraction — hiding the how (line 742) | may use names from earlier examples |
| `examples/17_an-abstract-name-is-not-a-signature-test.py` | The four pillars of OOP › An abstract name is not a signature test (line 769) | may use names from earlier examples |
| `examples/18_a-concrete-helper-can-use-a-child-implementation.py` | The four pillars of OOP › A concrete helper can use a child implementation (line 814) | may use names from earlier examples |
| `examples/19_4-polymorphism-same-call-different-behaviour.py` | The four pillars of OOP › 4. Polymorphism — same call, different behaviour (line 869) | may use names from earlier examples |
| `examples/20_4-polymorphism-same-call-different-behaviour.py` | The four pillars of OOP › 4. Polymorphism — same call, different behaviour (line 894) | may use names from earlier examples |
| `examples/21_4-polymorphism-same-call-different-behaviour.py` | The four pillars of OOP › 4. Polymorphism — same call, different behaviour (line 918) | may use names from earlier examples |
| `examples/22_method-resolution-order-mro.py` | Method Resolution Order (MRO) (line 941) | may use names from earlier examples |
| `examples/23_multiple-inheritance.py` | Method Resolution Order (MRO) › Multiple inheritance (line 960) | may use names from earlier examples |
| `examples/24_reusing-a-narrow-behavior-with-a-mixin.py` | Method Resolution Order (MRO) › Reusing a narrow behavior with a mixin (line 1106) | may use names from earlier examples |
| `examples/25_slots-a-fixed-attribute-list.py` | `__slots__`: a fixed attribute list (line 1225) | raises an error on purpose |
| `examples/26_slots-and-dictionaries-across-a-hierarchy.py` | `__slots__`: a fixed attribute list › Slots and dictionaries across a hierarchy (line 1262) | may use names from earlier examples |
| `examples/27_the-diamond-when-two-parents-share-a-grandparent.py` | The diamond: when two parents share a grandparent (line 1510) | may use names from earlier examples |
| `examples/28_the-diamond-when-two-parents-share-a-grandparent.py` | The diamond: when two parents share a grandparent (line 1551) | may use names from earlier examples |
| `examples/29_the-diamond-when-two-parents-share-a-grandparent.py` | The diamond: when two parents share a grandparent (line 1586) | may use names from earlier examples |
| `examples/30_one-receiver-with-an-explicit-stopping-point.py` | The diamond: when two parents share a grandparent › One receiver, with an explicit stopping point (line 1607) | may use names from earlier examples |
| `examples/31_self-super-and-an-explicitly-named-class.py` | The diamond: when two parents share a grandparent › Self, super, and an explicitly named class (line 1653) | may use names from earlier examples |
| `examples/32_try-it-yourself.py` | Try it yourself (line 1926) | may use names from earlier examples |
