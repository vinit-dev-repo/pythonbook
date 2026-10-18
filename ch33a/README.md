# 33a - Project - Forwarding Selected Python Operations

The code of the chapter **33a - Project - Forwarding Selected Python Operations** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why direct special-method lookup can succeed while an operator still fails
- How to forward five selected operations through an existing attribute policy
- How policy denial differs from an unsupported operand, target validation, and a bad call signature
- Where a wrapper's policy ends when it returns a raw result or iterator

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `attribute_policy.py` | Session 1: observe a missing operation, then forward it › Keep the target contract small (line 55) |  |
| `reading_list.py` | Session 1: observe a missing operation, then forward it › Keep the target contract small (line 92) |  |
| `operator_policy.py` | Session 1: observe a missing operation, then forward it › Put five forwarding methods on the wrapper type (line 140) |  |
| `operator_demo.py` | Session 2: policy decisions and returned-object boundaries (line 214) |  |
| `test_operator_policy.py` | Session 2: policy decisions and returned-object boundaries (line 311) |  |
| `route_transfer.py` | Build a Route policy (line 520) |  |
