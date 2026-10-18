# 31c - Project - Attribute Policies Through a Wrapper

The code of the chapter **31c - Project - Attribute Policies Through a Wrapper** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## About this chapter

Build a wrapper that checks selected attribute reads and writes before they reach another object. `Private('secret')` refuses a listed name; `Public('label', 'reveal', 'rename')` admits only listed names. A permitted method still runs on its own target, so its internal access is different from an external request through the wrapper.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

The chapter saves these files more than once (for example a first version and a repaired one). This folder holds the version the chapter ends with, and the table points to that last version:

- `attribute_policy.py`
- `policy_models.py`

| File | Where it is in the chapter | Note |
|---|---|---|
| `tracer_lab.py` | Session 1 - trace, collide and repair › A target method does not supply every wrapper operation (line 46) |  |
| `trace_limits.py` | Session 1 - trace, collide and repair › A target method does not supply every wrapper operation (line 92) |  |
| `naive_policy.py` | Session 1 - trace, collide and repair › Start with one real target (line 156) |  |
| `test_private_contract.py` | Session 1 - trace, collide and repair › Repair storage and check the Private policy (line 227) |  |
| `attribute_policy.py` | Session 2 - share the mechanism, preserve the behavior › Add Public without duplicating the wrapper (line 292) | rewritten later in the chapter |
| `policy_models.py` | Session 2 - share the mechanism, preserve the behavior › Retain normal target lookup and property writes (line 339) | rewritten later in the chapter |
| `policy_demo.py` | Session 2 - share the mechanism, preserve the behavior › Retain normal target lookup and property writes (line 390) |  |
| `test_policy.py` | Session 2 - share the mechanism, preserve the behavior › Check the complete ordinary read/write contract (line 520) |  |
| `ticket_counter.py` | Try it yourself (line 672) |  |
