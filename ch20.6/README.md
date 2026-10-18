# 20.6 - Depth Sessions and Composed Practice

The code of the chapter **20.6 - Depth Sessions and Composed Practice** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to prepare, register, run and clean up a module namespace by hand
- How to follow module references and plan a reload of a declared group
- How to measure cached import and lookup fairly
- How startup options and path files change what Python can import
- How to combine the chapter's ideas in seven short tasks

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `manual_namespace/loader.py` | Depth session: preparing and running a module namespace › Register the module before execution (line 55) |  |
| `manual_namespace/check.py` | Depth session: preparing and running a module namespace › Run code in a module dictionary (line 80) |  |
| `manual_namespace/check_failure.py` | Depth session: preparing and running a module namespace › Bind the caller and clean up a failed execution (line 138) |  |
| `dependency_lab/model.py` | Depth session: inspecting module dependencies › Following module references without reloading (line 186) |  |
| `dependency_lab/walk_modules.py` | Depth session: inspecting module dependencies › Pending work, seen objects and repeated paths (line 216) |  |
| `dependency_lab/check.py` | Depth session: inspecting module dependencies › Pending work, seen objects and repeated paths (line 248) |  |
| `reload_group.py` | Depth session: inspecting module dependencies › Reloading a declared group in dependency order (line 314) |  |
| `import_measure/check.py` | Depth session: measuring cached import and lookup (line 433) |  |
| `startup_inputs.py` | Depth session: startup settings and path files › Observe the environment at interpreter startup (line 488) |  |
| `path_file_lab.py` | Depth session: startup settings and path files › A path file is processed by `site` (line 542) |  |
| `startup_hooks.py` | Depth session: startup settings and path files › Interactive startup is different from a script (line 593) |  |
| `import_practice/formatting.py` | Composed import practice › 1. Build a reusable library and caller (line 646) |  |
| `import_practice/library.py` | Composed import practice › 1. Build a reusable library and caller (line 653) |  |
| `import_practice/caller.py` | Composed import practice › 1. Build a reusable library and caller (line 663) |  |
| `import_practice/client_from.py` | Composed import practice › 2. Compare explicit and star bindings (line 685) |  |
| `import_practice/client_star.py` | Composed import practice › 2. Compare explicit and star bindings (line 693) |  |
| `import_practice/check_guard.py` | Composed import practice › 3. Check the guarded demonstration (line 713) |  |
| `import_practice/nested_module.py` | Composed import practice › 4. Inspect a nested client's namespace (line 730) |  |
| `import_practice/nested_from.py` | Composed import practice › 4. Inspect a nested client's namespace (line 735) |  |
| `import_practice/check_nested.py` | Composed import practice › 4. Inspect a nested client's namespace (line 740) |  |
| `import_practice_package/myapp/utils/formatting.py` | Composed import practice › 5. Place the library inside a package (line 765) |  |
| `import_practice_package/myapp/utils/library.py` | Composed import practice › 5. Place the library inside a package (line 771) |  |
| `import_practice_package/myapp/utils/__init__.py` | Composed import practice › 5. Place the library inside a package (line 781) |  |
| `import_practice_package/myapp/__init__.py` | Composed import practice › 5. Place the library inside a package (line 788) |  |
| `import_practice_package/check.py` | Composed import practice › 5. Place the library inside a package (line 795) |  |
| `import_practice_reload/library.py` | Composed import practice › 6. Edit and reload a callable (line 822) |  |
| `import_practice_reload/check.py` | Composed import practice › 6. Edit and reload a callable (line 828) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_try-it-yourself.py` | Try it yourself (line 898) | runs on its own |
