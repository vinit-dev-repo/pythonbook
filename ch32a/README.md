# 32a - Project - From a Read-Only Deck to a Mutable Sequence

The code of the chapter **32a - Project - From a Read-Only Deck to a Mutable Sequence** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How a small `__len__`/`__getitem__` interface already enables several sequence fallbacks
- Why shuffle needs item assignment and why a class-level patch reaches existing instances
- How five `MutableSequence` primitives unlock inherited list-like helpers
- How sequence order, shallow copies, and mutable containers limit the claims we make

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `cards.py` | Session 1: a complete read interface (line 43) |  |
| `frenchdeck.py` | Session 1: a complete read interface (line 62) |  |
| `deck_demo.py` | Session 1: a complete read interface (line 102) |  |
| `shuffle_demo.py` | Session 2: shuffle exposes a missing operation (line 158) |  |
| `mutable_deck.py` | Session 3: declare a mutable card container (line 229) |  |
| `test_deck.py` | Session 3: declare a mutable card container (line 305) |  |
| `hand_transfer.py` | Try it yourself (line 514) |  |
