# 29 - Descriptors

The code of the chapter **29 - Descriptors** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How one mechanism supports `@property`, methods, and `__slots__`
- What a **descriptor** is and which three methods it can define
- How data descriptors and non-data descriptors differ, and why the difference matters
- How to build a descriptor and fix each problem in order
- The exact order Python uses when it looks up `obj.attribute`
- How to build two reusable descriptors: a checked field and an attribute that computes once

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `registration_transfer.py` | Binding behavior to one instance › Build a third behavior: sign-in counts (line 847) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_what-a-descriptor-is.py` | What a descriptor is (line 74) | runs on its own |
| `examples/02_the-protocol-get-set-delete.py` | The protocol: `__get__`, `__set__`, `__delete__` (line 116) | may use names from earlier examples |
| `examples/03_reading-through-the-class-and-deleting-a-managed.py` | The protocol: `__get__`, `__set__`, `__delete__` › Reading through the class, and deleting a managed value (line 144) | runs on its own |
| `examples/04_step-1-the-naive-version.py` | Build a descriptor step by step › Step 1 — the naive version (line 219) | may use names from earlier examples |
| `examples/05_the-wrong-way-storing-on-the-descriptor-two-inst.py` | The storage problem › The wrong way: storing on the descriptor — two instances trample each other (line 256) | may use names from earlier examples |
| `examples/06_a-better-way-a-dictionary-keyed-by-the-instance.py` | The storage problem › A better way: a dictionary keyed by the instance (line 279) | may use names from earlier examples |
| `examples/07_the-memory-leak-and-weak-references-fixing-it.py` | The storage problem › The memory leak, and weak references fixing it (line 320) | may use names from earlier examples |
| `examples/08_the-modern-answer-set-name.py` | The storage problem › The modern answer: `__set_name__` (line 358) | may use names from earlier examples |
| `examples/09_attribute-lookup-the-exact-order.py` | Attribute lookup — the exact order (line 433) | may use names from earlier examples |
| `examples/10_a-writer-without-a-getter-and-a-delete-only-desc.py` | Attribute lookup — the exact order › A writer without a getter, and a delete-only descriptor (line 455) | runs on its own |
| `examples/11_replacing-the-descriptor-on-its-owner-class.py` | Attribute lookup — the exact order › Replacing the descriptor on its owner class (line 505) | runs on its own |
| `examples/12_when-a-getter-raises-attributeerror.py` | Attribute lookup — the exact order › When a getter raises `AttributeError` (line 547) | runs on its own |
| `examples/13_why-instance-attributes-do-not-override-data-des.py` | Attribute lookup — the exact order › Why instance attributes do not override data descriptors (line 581) | may use names from earlier examples |
| `examples/14_property-is-a-descriptor.py` | `property` IS a descriptor (line 609) | may use names from earlier examples |
| `examples/15_functions-are-descriptors-how-methods-work.py` | Functions are descriptors: how methods work (line 682) | may use names from earlier examples |
| `examples/16_functions-are-descriptors-how-methods-work.py` | Functions are descriptors: how methods work (line 707) | may use names from earlier examples |
| `examples/17_binding-behavior-to-one-instance.py` | Binding behavior to one instance (line 743) | may use names from earlier examples |
| `examples/18_binding-behavior-to-one-instance.py` | Binding behavior to one instance (line 820) | may use names from earlier examples |
| `examples/19_descriptors-and-inheritance-found-through-the-mr.py` | Descriptors and inheritance: found through the MRO (line 943) | may use names from earlier examples |
| `examples/20_a-subclass-can-shadow-the-descriptor-and-lose-th.py` | Descriptors and inheritance: found through the MRO › A subclass can shadow the descriptor — and lose the protection (line 997) | may use names from earlier examples |
| `examples/21_application-1-a-reusable-validation-family.py` | Application 1: a reusable validation family (line 1037) | may use names from earlier examples |
| `examples/22_continue-the-bounded-field-lab.py` | Application 1: a reusable validation family › Continue the bounded-field lab (line 1144) | may use names from earlier examples |
| `examples/23_when-validation-also-changes-a-value.py` | Application 1: a reusable validation family › When validation also changes a value (line 1170) | runs on its own |
| `examples/24_application-2-a-lazy-cached-attribute.py` | Application 2: a lazy (cached) attribute (line 1233) | may use names from earlier examples |
| `examples/25_transfer-invalidate-a-lazy-cached-value.py` | Application 2: a lazy (cached) attribute › Transfer — invalidate a lazy cached value (line 1291) | may use names from earlier examples |
| `examples/26_a-cache-that-does-not-cause-a-leak-weakvaluedict.py` | Application 2: a lazy (cached) attribute › A cache that does not cause a leak: `WeakValueDictionary` (line 1316) | may use names from earlier examples |
| `examples/27_try-it-yourself.py` | Try it yourself (line 1370) | may use names from earlier examples |
