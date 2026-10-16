# 29a - Project - Counting Calls Without Losing the Receiver

The code of the chapter **29a - Project - Counting Calls Without Losing the Receiver** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## About this chapter

A call counter needs to know both which operation ran and which inventory received it. Start with a decorator that loses the receiver, then build one that supports standalone functions and instance methods. Compare an object wrapper with a closure, and check that saved wrappers keep the right subject.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `binding_stages.py` | Session 1 — failures show the missing piece (line 53) |  |
| `counted.py` | Session 2 — fresh wrappers, durable subject counts (line 173) |  |
| `inventory.py` | Session 2 — fresh wrappers, durable subject counts (line 245) |  |
| `binding_demo.py` | Session 2 — fresh wrappers, durable subject counts (line 278) |  |
| `test_binding.py` | Session 3 — retained closure, same contract (line 375) |  |
| `ticket_transfer.py` | Transfer — two ticket offices (line 496) |  |
