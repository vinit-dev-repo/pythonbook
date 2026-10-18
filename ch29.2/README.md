# 29.2 - Building a Descriptor, Storage and Attribute Lookup

The code of the chapter **29.2 - Building a Descriptor, Storage and Attribute Lookup** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Build a descriptor and fix each problem in order.
- Explain why a descriptor must not keep per-instance values on itself, and store them with `__set_name__`.
- Name the exact order Python uses when it looks up `obj.attribute`.

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_step-1-the-naive-version.py` | Build a descriptor step by step › Step 1: the naive version (line 47) | runs on its own |
| `examples/02_the-wrong-way-storing-on-the-descriptor-so-two-i.py` | The storage problem › The wrong way: storing on the descriptor, so two instances trample each other (line 87) | may use names from earlier examples |
| `examples/03_a-better-way-a-dictionary-keyed-by-the-instance.py` | The storage problem › A better way: a dictionary keyed by the instance (line 108) | may use names from earlier examples |
| `examples/04_the-memory-leak-and-weak-references-fixing-it.py` | The storage problem › The memory leak, and weak references fixing it (line 149) | may use names from earlier examples |
| `examples/05_the-modern-answer-set-name.py` | The storage problem › The modern answer: `__set_name__` (line 189) | may use names from earlier examples |
| `examples/06_attribute-lookup-the-exact-order.py` | Attribute lookup: the exact order (line 267) | may use names from earlier examples |
| `examples/07_a-writer-without-a-getter-and-a-delete-only-desc.py` | Attribute lookup: the exact order › A writer without a getter, and a delete-only descriptor (line 288) | runs on its own |
| `examples/08_replacing-the-descriptor-on-its-owner-class.py` | Attribute lookup: the exact order › Replacing the descriptor on its owner class (line 337) | runs on its own |
| `examples/09_when-a-getter-raises-attributeerror.py` | Attribute lookup: the exact order › When a getter raises `AttributeError` (line 376) | runs on its own |
| `examples/10_why-instance-attributes-do-not-override-data-des.py` | Attribute lookup: the exact order › Why instance attributes do not override data descriptors (line 407) | may use names from earlier examples |
| `examples/11_try-it-yourself.py` | Try it yourself (line 454) | runs on its own |
