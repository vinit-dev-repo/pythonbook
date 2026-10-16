# 20 - The Import System in Depth

The code of the chapter **20 - The Import System in Depth** of the Python tutorial (folder `02 - Language and first tools`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What Python does when it runs `import something`
- Why a module is an object and how to inspect it
- Why a second import does not run the module again, and how `sys.modules` stores it
- Where Python looks for modules with `sys.path`, and how a local file can hide a standard module
- What finders and loaders do, in plain words
- Exactly what each `import` spelling puts into your own namespace
- How to reload a module, and why you rarely should
- How `if __name__ == "__main__":` and `python -m` work
- What a package is, what `__init__.py` is for, and how to structure a real project with relative imports
- What namespace packages are and how Python imports code from a ZIP file
- How to install a src-layout project, build a wheel, and test it in a fresh consumer environment

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `greetings.py` | A module is an object (line 107) |  |
| `module_objects/check.py` | Creating a module object without a file (line 157) |  |
| `counter.py` | `sys.modules` is the cache (line 208) |  |
| `inspection/labels.py` | Inspecting and documenting a module (line 240) |  |
| `inspection/check.py` | Inspecting and documenting a module (line 251) |  |
| `caller_binding/item.py` | Deleting a caller name is not deleting the cache (line 295) |  |
| `caller_binding/check.py` | Deleting a caller name is not deleting the cache (line 301) |  |
| `cache_failure/dependency.py` | A failed first import and a blocked name (line 366) |  |
| `cache_failure/broken.py` | A failed first import and a blocked name (line 371) |  |
| `cache_failure/check.py` | A failed first import and a blocked name (line 377) |  |
| `circular_early/a.py` | A circular import: reading too early (line 418) |  |
| `circular_early/b.py` | A circular import: reading too early (line 424) |  |
| `circular_early/check.py` | A circular import: reading too early (line 430) |  |
| `circular_late/a.py` | A circular import: reading too early (line 452) |  |
| `circular_late/b.py` | A circular import: reading too early (line 459) |  |
| `circular_late/check.py` | A circular import: reading too early (line 467) |  |
| `shadow_demo/random.py` | Where Python looks: `sys.path` (line 529) |  |
| `shadow_demo/check.py` | Where Python looks: `sys.path` (line 534) |  |
| `spec_search/external/plugin.py` | Inspecting a plain module before importing it (line 587) |  |
| `spec_search/check.py` | Inspecting a plain module before importing it (line 595) |  |
| `loud_module.py` | A common misconception: `from module import name` still runs the *whole* module (line 668) |  |
| `exports_demo/plain.py` | A common misconception: `from module import name` still runs the *whole* module (line 694) |  |
| `exports_demo/listed.py` | A common misconception: `from module import name` still runs the *whole* module (line 700) |  |
| `exports_demo/check_plain.py` | A common misconception: `from module import name` still runs the *whole* module (line 707) |  |
| `exports_demo/check_listed.py` | A common misconception: `from module import name` still runs the *whole* module (line 723) |  |
| `local_alias/loud.py` | Aliases and imports inside a function (line 744) |  |
| `local_alias/check.py` | Aliases and imports inside a function (line 750) |  |
| `lazy_demo/heavy.py` | Lazy imports: bind now, load at first use (3.15) (line 787) |  |
| `lazy_demo/check.py` | Lazy imports: bind now, load at first use (3.15) (line 793) |  |
| `lazy_demo/compat.py` | Lazy imports: bind now, load at first use (3.15) (line 827) |  |
| `shared_binding/store.py` | An imported binding can still share a mutable object (line 857) |  |
| `shared_binding/check.py` | An imported binding can still share a mutable object (line 862) |  |
| `reload_demo/settings.py` | Reloading a module (line 922) |  |
| `reload_demo/check.py` | Reloading a module (line 928) |  |
| `reload_function/message.py` | A saved function is not a live module lookup (line 976) |  |
| `reload_function/check.py` | A saved function is not a live module lookup (line 984) |  |
| `reload_nested/child.py` | Reloading a parent does not reload its child (line 1028) |  |
| `reload_nested/parent.py` | Reloading a parent does not reload its child (line 1033) |  |
| `reload_nested/check.py` | Reloading a parent does not reload its child (line 1041) |  |
| `greet.py` | `__main__` revisited (line 1086) |  |
| `geometry_demo/circle.py` | Packages: folders of modules (line 1144) |  |
| `geometry_demo/square.py` | Packages: folders of modules (line 1150) |  |
| `geometry_demo/__init__.py` | Packages: folders of modules (line 1156) |  |
| `geometry_demo/triangle.py` | Packages: folders of modules (line 1180) |  |
| `check_geometry_exports.py` | Packages: folders of modules (line 1186) |  |
| `myapp/__init__.py` | Relative imports (line 1238) |  |
| `myapp/utils/__init__.py` | Relative imports (line 1243) |  |
| `myapp/utils/strings.py` | Relative imports (line 1248) |  |
| `myapp/utils/numbers.py` | Relative imports (line 1254) |  |
| `myapp/main.py` | Relative imports (line 1262) |  |
| `relative_targets/red/__init__.py` | Import names, search roots and relative targets (line 1300) |  |
| `relative_targets/blue/__init__.py` | Import names, search roots and relative targets (line 1304) |  |
| `relative_targets/red/helper.py` | Import names, search roots and relative targets (line 1308) |  |
| `relative_targets/blue/helper.py` | Import names, search roots and relative targets (line 1313) |  |
| `relative_targets/missing.py` | Import names, search roots and relative targets (line 1318) |  |
| `relative_targets/red/check.py` | Import names, search roots and relative targets (line 1323) |  |
| `relative_targets/check.py` | Import names, search roots and relative targets (line 1333) |  |
| `package_trace/myapp/__init__.py` | Package objects and a nested import trace (line 1370) |  |
| `package_trace/myapp/utils/__init__.py` | Package objects and a nested import trace (line 1375) |  |
| `package_trace/myapp/utils/strings.py` | Package objects and a nested import trace (line 1380) |  |
| `package_trace/myapp/utils/numbers.py` | Package objects and a nested import trace (line 1388) |  |
| `package_trace/myapp/utils/unused.py` | Package objects and a nested import trace (line 1397) |  |
| `package_trace/check.py` | Package objects and a nested import trace (line 1402) |  |
| `package_trace/check_spec.py` | Inspecting a dotted name can import its parent (line 1458) |  |
| `package_api/myapp/utils/strings.py` | Keeping a public API while files move (line 1526) |  |
| `package_api/myapp/utils/numbers.py` | Keeping a public API while files move (line 1532) |  |
| `package_api/myapp/utils/__init__.py` | Keeping a public API while files move (line 1540) |  |
| `package_api/myapp/__init__.py` | Keeping a public API while files move (line 1547) |  |
| `package_api/check.py` | Keeping a public API while files move (line 1555) |  |
| `package_api/check_relative.py` | Keeping a public API while files move (line 1586) |  |
| `package_star/unbound/export_demo/__init__.py` | When package `__all__` names a submodule (line 1608) |  |
| `package_star/unbound/export_demo/child.py` | When package `__all__` names a submodule (line 1613) |  |
| `package_star/unbound/check.py` | When package `__all__` names a submodule (line 1621) |  |
| `package_star/attribute/export_demo/__init__.py` | When package `__all__` names a submodule (line 1638) |  |
| `package_star/attribute/export_demo/child.py` | When package `__all__` names a submodule (line 1644) |  |
| `package_star/attribute/check.py` | When package `__all__` names a submodule (line 1652) |  |
| `namespace_demo/dir1/tools/alpha.py` | Namespace packages: packages without `__init__.py` (line 1693) |  |
| `namespace_demo/dir2/tools/beta.py` | Namespace packages: packages without `__init__.py` (line 1698) |  |
| `namespace_demo/check.py` | Namespace packages: packages without `__init__.py` (line 1705) |  |
| `namespace_demo/regular/tools/__init__.py` | Namespace packages: packages without `__init__.py` (line 1739) |  |
| `namespace_demo/check_regular.py` | Namespace packages: packages without `__init__.py` (line 1744) |  |
| `namespace_growth/dir1/tools/alpha.py` | A namespace search path can grow (line 1773) |  |
| `namespace_growth/dir2/tools/beta.py` | A namespace search path can grow (line 1779) |  |
| `namespace_growth/dir1/tools/shared/first.py` | A namespace search path can grow (line 1784) |  |
| `namespace_growth/dir2/tools/shared/second.py` | A namespace search path can grow (line 1789) |  |
| `namespace_growth/dir2/tools/regular/__init__.py` | A namespace search path can grow (line 1794) |  |
| `namespace_growth/concrete/tools.py` | A namespace search path can grow (line 1799) |  |
| `namespace_growth/check.py` | A namespace search path can grow (line 1804) |  |
| `namespace_growth/check_concrete.py` | A namespace search path can grow (line 1851) |  |
| `zip_demo/archive_module.py` | Importing from ZIP archives (line 1885) |  |
| `zip_demo/check.py` | Importing from ZIP archives (line 1890) |  |
| `package_api/check_zip.py` | The same package API inside a ZIP (line 1928) |  |
| `manual_namespace/loader.py` | Register the module before execution (line 2014) |  |
| `manual_namespace/check.py` | Run code in a module dictionary (line 2041) |  |
| `manual_namespace/check_failure.py` | Bind the caller and clean up a failed execution (line 2102) |  |
| `dependency_lab/model.py` | Following module references without reloading (line 2149) |  |
| `dependency_lab/walk_modules.py` | Pending work, seen objects and repeated paths (line 2181) |  |
| `dependency_lab/check.py` | Pending work, seen objects and repeated paths (line 2214) |  |
| `reload_group.py` | Reloading a declared group in dependency order (line 2282) |  |
| `import_measure/check.py` | Depth session: measuring cached import and lookup (line 2398) |  |
| `startup_inputs.py` | Observe the environment at interpreter startup (line 2448) |  |
| `path_file_lab.py` | A path file is processed by `site` (line 2500) |  |
| `startup_hooks.py` | Interactive startup is different from a script (line 2553) |  |
| `import_practice/formatting.py` | 1. Build a reusable library and caller (line 2606) |  |
| `import_practice/library.py` | 1. Build a reusable library and caller (line 2613) |  |
| `import_practice/caller.py` | 1. Build a reusable library and caller (line 2623) |  |
| `import_practice/client_from.py` | 2. Compare explicit and star bindings (line 2646) |  |
| `import_practice/client_star.py` | 2. Compare explicit and star bindings (line 2654) |  |
| `import_practice/check_guard.py` | 3. Check the guarded demonstration (line 2675) |  |
| `import_practice/nested_module.py` | 4. Inspect a nested client's namespace (line 2693) |  |
| `import_practice/nested_from.py` | 4. Inspect a nested client's namespace (line 2698) |  |
| `import_practice/check_nested.py` | 4. Inspect a nested client's namespace (line 2703) |  |
| `import_practice_package/myapp/utils/formatting.py` | 5. Place the library inside a package (line 2729) |  |
| `import_practice_package/myapp/utils/library.py` | 5. Place the library inside a package (line 2735) |  |
| `import_practice_package/myapp/utils/__init__.py` | 5. Place the library inside a package (line 2745) |  |
| `import_practice_package/myapp/__init__.py` | 5. Place the library inside a package (line 2752) |  |
| `import_practice_package/check.py` | 5. Place the library inside a package (line 2759) |  |
| `import_practice_reload/library.py` | 6. Edit and reload a callable (line 2787) |  |
| `import_practice_reload/check.py` | 6. Edit and reload a callable (line 2793) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_a-module-is-an-object.py` | A module is an object (line 115) | runs on its own |
| `examples/02_a-module-is-an-object.py` | A module is an object (line 138) | may use names from earlier examples |
| `examples/03_sys-modules-is-the-cache.py` | `sys.modules` is the cache (line 214) | may use names from earlier examples |
| `examples/04_sys-modules-is-the-cache.py` | `sys.modules` is the cache (line 226) | may use names from earlier examples |
| `examples/05_deleting-a-caller-name-is-not-deleting-the-cache.py` | Deleting a caller name is not deleting the cache (line 328) | may use names from earlier examples |
| `examples/06_where-python-looks-sys-path.py` | Where Python looks: `sys.path` (line 501) | may use names from earlier examples |
| `examples/07_finders-and-loaders.py` | Finders and loaders (line 569) | may use names from earlier examples |
| `examples/08_a-common-misconception-from-module-import-name-s.py` | A common misconception: `from module import name` still runs the *whole* module (line 674) | may use names from earlier examples |
| `examples/09_reloading-a-module.py` | Reloading a module (line 911) | may use names from earlier examples |
| `examples/10_main-revisited.py` | `__main__` revisited (line 1106) | may use names from earlier examples |
| `examples/11_packages-folders-of-modules.py` | Packages: folders of modules (line 1164) | may use names from earlier examples |
| `examples/12_try-it-yourself.py` | Try it yourself (line 2865) | may use names from earlier examples |
