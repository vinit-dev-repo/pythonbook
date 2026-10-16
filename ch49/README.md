# 49 - NumPy

The code of the chapter **49 - NumPy** of the Python tutorial (folder `09 - Data and database applications`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why plain Python lists are slow for number-crunching, and what NumPy does differently
- What an array, a dtype, a shape and an axis are, in plain words
- How to build arrays from lists and from scratch
- How to reshape, stack and split arrays — and the difference between a **view** and a **copy**
- How to pick out data with indexing, slicing, fancy indexing and masks
- How **ufuncs** and **broadcasting** let you skip loops entirely
- How to summarise arrays with `sum`, `mean`, `std` and friends, along a chosen axis
- How to save numeric arrays and distinguish read-only, temporary and persistent mapped edits

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `axis_selection.py` | Slicing › Omitted axes and a new dimension (line 577) |  |
| `selected_updates.py` | Fancy indexing › Reading a selection versus assigning to it (line 638) |  |
| `array_file_worker.py` | Store an array and control mapped writes (line 958) |  |
| `array_file_workflow.py` | Store an array and control mapped writes (line 983) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_a-speed-demo.py` | Why NumPy exists › A speed demo (line 71) | runs on its own |
| `examples/02_creating-arrays-from-lists.py` | Creating arrays from lists (line 132) | may use names from earlier examples |
| `examples/03_creating-arrays-from-lists.py` | Creating arrays from lists (line 148) | may use names from earlier examples |
| `examples/04_creating-arrays-from-lists.py` | Creating arrays from lists (line 163) | may use names from earlier examples |
| `examples/05_creating-arrays-from-lists.py` | Creating arrays from lists (line 182) | may use names from earlier examples |
| `examples/06_creating-arrays-from-lists.py` | Creating arrays from lists (line 195) | may use names from earlier examples |
| `examples/07_creating-arrays-from-scratch.py` | Creating arrays from scratch (line 220) | may use names from earlier examples |
| `examples/08_arange-vs-linspace-the-difference-that-matters.py` | Creating arrays from scratch › `arange` vs `linspace`: the difference that matters (line 250) | may use names from earlier examples |
| `examples/09_random-arrays.py` | Creating arrays from scratch › Random arrays (line 271) | may use names from earlier examples |
| `examples/10_reshaping-arrays.py` | Reshaping arrays (line 295) | may use names from earlier examples |
| `examples/11_reshaping-arrays.py` | Reshaping arrays (line 310) | may use names from earlier examples |
| `examples/12_reshaping-arrays.py` | Reshaping arrays (line 322) | may use names from earlier examples |
| `examples/13_reshaping-arrays.py` | Reshaping arrays (line 340) | may use names from earlier examples |
| `examples/14_reshaping-arrays.py` | Reshaping arrays (line 354) | may use names from earlier examples |
| `examples/15_reshaping-arrays.py` | Reshaping arrays (line 367) | may use names from earlier examples |
| `examples/16_reshaping-arrays.py` | Reshaping arrays (line 388) | may use names from earlier examples |
| `examples/17_stacking-and-splitting.py` | Stacking and splitting (line 415) | may use names from earlier examples |
| `examples/18_stacking-and-splitting.py` | Stacking and splitting (line 434) | may use names from earlier examples |
| `examples/19_stacking-and-splitting.py` | Stacking and splitting (line 454) | may use names from earlier examples |
| `examples/20_indexing.py` | Indexing (line 475) | may use names from earlier examples |
| `examples/21_slicing.py` | Slicing (line 529) | may use names from earlier examples |
| `examples/22_slicing.py` | Slicing (line 554) | may use names from earlier examples |
| `examples/23_fancy-indexing.py` | Fancy indexing (line 615) | may use names from earlier examples |
| `examples/24_boolean-masks.py` | Boolean masks (line 670) | may use names from earlier examples |
| `examples/25_boolean-masks.py` | Boolean masks (line 691) | may use names from earlier examples |
| `examples/26_universal-functions-ufuncs.py` | Universal functions (ufuncs) (line 714) | may use names from earlier examples |
| `examples/27_broadcasting.py` | Universal functions (ufuncs) › Broadcasting (line 768) | may use names from earlier examples |
| `examples/28_broadcasting.py` | Universal functions (ufuncs) › Broadcasting (line 789) | may use names from earlier examples |
| `examples/29_elementwise-multiplication-and-matrix-multiplica.py` | Universal functions (ufuncs) › Elementwise multiplication and matrix multiplication (line 813) | may use names from earlier examples |
| `examples/30_elementwise-multiplication-and-matrix-multiplica.py` | Universal functions (ufuncs) › Elementwise multiplication and matrix multiplication (line 836) | may use names from earlier examples |
| `examples/31_math-and-stats-methods-and-the-axis-rule-again.py` | Math and stats methods, and the axis rule again (line 864) | may use names from earlier examples |
| `examples/32_math-and-stats-methods-and-the-axis-rule-again.py` | Math and stats methods, and the axis rule again (line 885) | may use names from earlier examples |
| `examples/33_math-and-stats-methods-and-the-axis-rule-again.py` | Math and stats methods, and the axis rule again (line 910) | may use names from earlier examples |
| `examples/34_math-and-stats-methods-and-the-axis-rule-again.py` | Math and stats methods, and the axis rule again (line 933) | may use names from earlier examples |
| `examples/35_worked-example-a-week-of-city-temperatures.py` | Worked example: a week of city temperatures (line 1048) | may use names from earlier examples |
| `examples/36_practice-analyze-a-second-temperature-sample.py` | Practice: analyze a second temperature sample (line 1101) | may use names from earlier examples |
| `examples/37_try-it-yourself.py` | Try it yourself (line 1152) | may use names from earlier examples |
