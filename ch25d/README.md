# 25d - Project - Inventory Inheritance and Regression Tests

The code of the chapter **25d - Project - Inventory Inheritance and Regression Tests** of the Python tutorial (folder `03 - Objects, protocols and testing`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How one stock invariant can govern five related concrete classes
- How `super()` lets several initializers prepare the same object
- How package files, shared fixtures and parameterized tests fit together
- How to test rejected changes, fixture lifetimes and a deliberately faulty implementation

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `app/__init__.py` | A real package and a reusable validator (line 95) |  |
| `app/utils/__init__.py` | A real package and a reusable validator (line 100) |  |
| `app/models/__init__.py` | A real package and a reusable validator (line 105) |  |
| `app/utils/validators.py` | A real package and a reusable validator (line 114) |  |
| `app/models/resource.py` | A real package and a reusable validator (line 145) |  |
| `tests/conftest.py` | Check the base before adding devices (line 231) |  |
| `tests/test_validators.py` | Check the base before adding devices (line 261) |  |
| `tests/test_resource.py` | Check the base before adding devices (line 326) |  |
| `app/models/devices.py` | Extending CPU and Storage (line 498) |  |
| `inventory_demo.py` | Extending CPU and Storage (line 580) |  |
| `tests/test_devices.py` | Fixtures, invalid transitions and regression (line 647) |  |
| `tests/test_fixtures.py` | Fixture reuse has a lifetime (line 815) |  |
| `inventory_transfer.py` | Try it yourself (line 890) |  |
