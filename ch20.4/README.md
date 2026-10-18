# 20.4 - Packages and Project Structure

The code of the chapter **20.4 - Packages and Project Structure** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What a package is, what `__init__.py` is for, and how `__all__` selects star-import names
- How to structure a real project with relative imports
- Why `python -m` gives a relative import its package context and a bare file path does not
- How to keep a public API while files move

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `geometry_demo/circle.py` | Packages: folders of modules (line 45) |  |
| `geometry_demo/square.py` | Packages: folders of modules (line 51) |  |
| `geometry_demo/__init__.py` | Packages: folders of modules (line 57) |  |
| `geometry_demo/triangle.py` | Packages: folders of modules (line 80) |  |
| `check_geometry_exports.py` | Packages: folders of modules (line 86) |  |
| `myapp/__init__.py` | Structuring a real project › Relative imports (line 135) |  |
| `myapp/utils/__init__.py` | Structuring a real project › Relative imports (line 140) |  |
| `myapp/utils/strings.py` | Structuring a real project › Relative imports (line 145) |  |
| `myapp/utils/numbers.py` | Structuring a real project › Relative imports (line 151) |  |
| `myapp/main.py` | Structuring a real project › Relative imports (line 159) |  |
| `relative_targets/red/__init__.py` | Structuring a real project › Import names, search roots and relative targets (line 193) |  |
| `relative_targets/blue/__init__.py` | Structuring a real project › Import names, search roots and relative targets (line 197) |  |
| `relative_targets/red/helper.py` | Structuring a real project › Import names, search roots and relative targets (line 201) |  |
| `relative_targets/blue/helper.py` | Structuring a real project › Import names, search roots and relative targets (line 206) |  |
| `relative_targets/missing.py` | Structuring a real project › Import names, search roots and relative targets (line 211) |  |
| `relative_targets/red/check.py` | Structuring a real project › Import names, search roots and relative targets (line 216) |  |
| `relative_targets/check.py` | Structuring a real project › Import names, search roots and relative targets (line 226) |  |
| `package_trace/myapp/__init__.py` | Structuring a real project › Package objects and a nested import trace (line 261) |  |
| `package_trace/myapp/utils/__init__.py` | Structuring a real project › Package objects and a nested import trace (line 266) |  |
| `package_trace/myapp/utils/strings.py` | Structuring a real project › Package objects and a nested import trace (line 271) |  |
| `package_trace/myapp/utils/numbers.py` | Structuring a real project › Package objects and a nested import trace (line 279) |  |
| `package_trace/myapp/utils/unused.py` | Structuring a real project › Package objects and a nested import trace (line 288) |  |
| `package_trace/check.py` | Structuring a real project › Package objects and a nested import trace (line 293) |  |
| `package_trace/check_spec.py` | Structuring a real project › Inspecting a dotted name can import its parent (line 346) |  |
| `package_api/myapp/utils/strings.py` | Structuring a real project › Keeping a public API while files move (line 407) |  |
| `package_api/myapp/utils/numbers.py` | Structuring a real project › Keeping a public API while files move (line 413) |  |
| `package_api/myapp/utils/__init__.py` | Structuring a real project › Keeping a public API while files move (line 421) |  |
| `package_api/myapp/__init__.py` | Structuring a real project › Keeping a public API while files move (line 428) |  |
| `package_api/check.py` | Structuring a real project › Keeping a public API while files move (line 436) |  |
| `package_api/check_relative.py` | Structuring a real project › Keeping a public API while files move (line 466) |  |
| `package_star/unbound/export_demo/__init__.py` | Structuring a real project › When package `__all__` names a submodule (line 486) |  |
| `package_star/unbound/export_demo/child.py` | Structuring a real project › When package `__all__` names a submodule (line 491) |  |
| `package_star/unbound/check.py` | Structuring a real project › When package `__all__` names a submodule (line 498) |  |
| `package_star/attribute/export_demo/__init__.py` | Structuring a real project › When package `__all__` names a submodule (line 515) |  |
| `package_star/attribute/export_demo/child.py` | Structuring a real project › When package `__all__` names a submodule (line 521) |  |
| `package_star/attribute/check.py` | Structuring a real project › When package `__all__` names a submodule (line 528) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_packages-folders-of-modules.py` | Packages: folders of modules (line 65) | runs on its own |
| `examples/02_try-it-yourself.py` | Try it yourself (line 582) | may use names from earlier examples |
