# 22.2 - Hashing, Truth, Calls and Formats

The code of the chapter **22.2 - Hashing, Truth, Calls and Formats** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why `__eq__` and `__hash__` must agree, and what breaks in dicts and sets if they do not
- How `__bool__` and `__len__` decide the truth of an object
- How `__call__` makes an object callable and lets it keep state
- How `__format__` receives the format specification of an f-string

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_defining-eq-makes-instances-unhashable-by-defaul.py` | Hashing and equality: they must agree › Defining `__eq__` makes instances unhashable by default (line 47) | runs on its own |
| `examples/02_defining-eq-makes-instances-unhashable-by-defaul.py` | Hashing and equality: they must agree › Defining `__eq__` makes instances unhashable by default (line 70) | may use names from earlier examples |
| `examples/03_defining-eq-makes-instances-unhashable-by-defaul.py` | Hashing and equality: they must agree › Defining `__eq__` makes instances unhashable by default (line 100) | may use names from earlier examples |
| `examples/04_what-breaks-if-the-hash-disagrees-with-equality.py` | Hashing and equality: they must agree › What breaks if the hash disagrees with equality (line 133) | may use names from earlier examples |
| `examples/05_a-collision-is-not-an-equality-claim.py` | Hashing and equality: they must agree › A collision is not an equality claim (line 164) | may use names from earlier examples |
| `examples/06_bool-and-len.py` | `__bool__` and `__len__` (line 204) | may use names from earlier examples |
| `examples/07_bool-and-len.py` | `__bool__` and `__len__` (line 230) | may use names from earlier examples |
| `examples/08_default-truth-and-method-requirements.py` | `__bool__` and `__len__` › Default truth and method requirements (line 256) | may use names from earlier examples |
| `examples/09_call-objects-you-can-call-like-a-function.py` | `__call__`: objects you can call like a function (line 313) | may use names from earlier examples |
| `examples/10_format.py` | `__format__` (line 348) | may use names from earlier examples |
| `examples/11_forwarding-a-format-to-a-stored-value.py` | `__format__` › Forwarding a format to a stored value (line 372) | may use names from earlier examples |
| `examples/12_try-it-yourself.py` | Try it yourself (line 429) | may use names from earlier examples |
