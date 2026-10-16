# 50 - Pandas

The code of the chapter **50 - Pandas** of the Python tutorial (folder `09 - Data and database applications`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What pandas is for, and when to reach for it instead of NumPy
- The two core objects: `Series` and `DataFrame`, and how their **index** works
- How to build a DataFrame by hand, and how to load one from a file
- How to look at a new dataset for the first time
- How to select rows, columns and cells with `loc` and `iloc`
- How to handle missing data, sort, filter, and add new columns
- How `groupby` splits data into groups, does maths on each, and combines the results

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `table_formats.py` | Loading data › Load the same records from JSON and Excel (line 348) |  |
| `table_ownership.py` | Selecting data › A selected column is a separate pandas object (line 681) |  |
| `nullable_counts.py` | Missing data › Nullable counts and unknown truth (line 795) |  |
| `energy_report.py` | Transfer analysis: keep row identity through cleaning (line 1216) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_series-a-labelled-column.py` | The two core objects › Series: a labelled column (line 82) | runs on its own |
| `examples/02_series-a-labelled-column.py` | The two core objects › Series: a labelled column (line 99) | may use names from earlier examples |
| `examples/03_dataframe-a-table-of-series-sharing-one-index.py` | The two core objects › DataFrame: a table of Series sharing one index (line 130) | may use names from earlier examples |
| `examples/04_dataframe-a-table-of-series-sharing-one-index.py` | The two core objects › DataFrame: a table of Series sharing one index (line 149) | may use names from earlier examples |
| `examples/05_indexes-in-depth-why-labels-matter.py` | Indexes in depth: why labels matter (line 173) | may use names from earlier examples |
| `examples/06_indexes-in-depth-why-labels-matter.py` | Indexes in depth: why labels matter (line 208) | may use names from earlier examples |
| `examples/07_creating-dataframes-by-hand.py` | Creating DataFrames by hand (line 241) | may use names from earlier examples |
| `examples/08_loading-data.py` | Loading data (line 266) | may use names from earlier examples |
| `examples/09_loading-data.py` | Loading data (line 299) | may use names from earlier examples |
| `examples/10_loading-data.py` | Loading data (line 319) | may use names from earlier examples |
| `examples/11_check-a-new-dataset.py` | Check a new dataset (line 409) | may use names from earlier examples |
| `examples/12_check-a-new-dataset.py` | Check a new dataset (line 433) | may use names from earlier examples |
| `examples/13_check-a-new-dataset.py` | Check a new dataset (line 454) | may use names from earlier examples |
| `examples/14_columns.py` | Selecting data › Columns (line 489) | may use names from earlier examples |
| `examples/15_rows-and-cells-loc-vs-iloc.py` | Selecting data › Rows and cells: `loc` vs `iloc` (line 524) | may use names from earlier examples |
| `examples/16_rows-and-cells-loc-vs-iloc.py` | Selecting data › Rows and cells: `loc` vs `iloc` (line 556) | may use names from earlier examples |
| `examples/17_boolean-filtering.py` | Selecting data › Boolean filtering (line 575) | may use names from earlier examples |
| `examples/18_boolean-filtering.py` | Selecting data › Boolean filtering (line 589) | may use names from earlier examples |
| `examples/19_boolean-filtering.py` | Selecting data › Boolean filtering (line 603) | may use names from earlier examples |
| `examples/20_do-not-assign-through-chained-indexing.py` | Selecting data › Do not assign through chained indexing (line 628) | may use names from earlier examples |
| `examples/21_do-not-assign-through-chained-indexing.py` | Selecting data › Do not assign through chained indexing (line 647) | may use names from earlier examples |
| `examples/22_do-not-assign-through-chained-indexing.py` | Selecting data › Do not assign through chained indexing (line 671) | may use names from earlier examples |
| `examples/23_missing-data.py` | Missing data (line 715) | may use names from earlier examples |
| `examples/24_missing-data.py` | Missing data (line 741) | may use names from earlier examples |
| `examples/25_basic-analysis.py` | Basic analysis (line 841) | may use names from earlier examples |
| `examples/26_sorting-and-filtering.py` | Sorting and filtering (line 883) | may use names from earlier examples |
| `examples/27_manipulating.py` | Manipulating (line 932) | may use names from earlier examples |
| `examples/28_manipulating.py` | Manipulating (line 952) | may use names from earlier examples |
| `examples/29_manipulating.py` | Manipulating (line 979) | may use names from earlier examples |
| `examples/30_groupby-split-apply-combine.py` | Groupby: split, apply, combine (line 1013) | may use names from earlier examples |
| `examples/31_groupby-split-apply-combine.py` | Groupby: split, apply, combine (line 1029) | may use names from earlier examples |
| `examples/32_groupby-split-apply-combine.py` | Groupby: split, apply, combine (line 1057) | may use names from earlier examples |
| `examples/33_groupby-split-apply-combine.py` | Groupby: split, apply, combine (line 1071) | may use names from earlier examples |
| `examples/34_closing-mini-analysis-load-clean-filter-group-so.py` | Closing mini-analysis: load, clean, filter, group, sort, save (line 1093) | may use names from earlier examples |
| `examples/35_practice-audit-a-small-delivery-report.py` | Practice: audit a small delivery report (line 1141) | may use names from earlier examples |
| `examples/36_practice-audit-a-small-delivery-report.py` | Practice: audit a small delivery report (line 1152) | may use names from earlier examples |
| `examples/37_try-it-yourself.py` | Try it yourself (line 1356) | may use names from earlier examples |
