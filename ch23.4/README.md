# 23.4 - The Diamond and Cooperative super()

The code of the chapter **23.4 - The Diamond and Cooperative super()** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why naming the parent class in each method runs a shared grandparent twice
- How `super()` selects the next implementation in the MRO of the receiver
- How to follow one receiver through a chain and where a chain stops
- How to pass arguments through a cooperative chain, and what goes wrong when explicit calls are mixed in

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `super_contracts.py` | The diamond: when two parents share a grandparent › Cooperative arguments and explicit operator calls (line 242) |  |
| `changing_bases.py` | The diamond: when two parents share a grandparent › A changed base affects existing instances (line 330) |  |
| `mixed_dispatch.py` | The diamond: when two parents share a grandparent › Mixing explicit calls with a cooperative chain can repeat work (line 381) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-diamond-when-two-parents-share-a-grandparent.py` | The diamond: when two parents share a grandparent (line 49) | runs on its own |
| `examples/02_the-diamond-when-two-parents-share-a-grandparent.py` | The diamond: when two parents share a grandparent (line 88) | may use names from earlier examples |
| `examples/03_the-diamond-when-two-parents-share-a-grandparent.py` | The diamond: when two parents share a grandparent (line 122) | may use names from earlier examples |
| `examples/04_one-receiver-with-an-explicit-stopping-point.py` | The diamond: when two parents share a grandparent › One receiver, with an explicit stopping point (line 140) | may use names from earlier examples |
| `examples/05_self-super-and-an-explicitly-named-class.py` | The diamond: when two parents share a grandparent › Self, super, and an explicitly named class (line 182) | may use names from earlier examples |
| `examples/06_try-it-yourself.py` | Try it yourself (line 447) | may use names from earlier examples |
