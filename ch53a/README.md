# 53a - Project - Internal Diagnostics and Public Responses

The code of the chapter **53a - Project - Internal Diagnostics and Public Responses** of the Python tutorial (folder `10 - Web applications and production boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Give related failures a useful exception hierarchy and a consistent message contract.
- Capture one event time and build separate public and diagnostic representations.
- Follow an exception through a narrow handler and a single logging boundary.
- Test a real HTTP response locally, including its status separately from its JSON body.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `widget_errors.py` | Hierarchy and stable event representations › Keep traceback state distinct from event time (line 117) |  |
| `test_widget_errors.py` | Hierarchy and stable event representations › Check the core before adding an adapter (line 260) |  |
| `widget_service.py` | Raise, log once and return the HTTP response › Re-raise at a narrow service boundary (line 441) |  |
| `widget_app.py` | Raise, log once and return the HTTP response › Add the HTTP and logging boundary (line 482) |  |
| `test_widget_app.py` | Raise, log once and return the HTTP response › Check real response behavior and one record (line 543) |  |
| `error_demo.py` | Raise, log once and return the HTTP response › Run the complete demonstration (line 700) |  |
| `error_transfer.py` | Try it yourself (line 791) |  |
