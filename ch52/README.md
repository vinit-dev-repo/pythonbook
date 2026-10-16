# 52 - SQLite from Python

The code of the chapter **52 - SQLite from Python** of the Python tutorial (folder `09 - Data and database applications`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Why plain files and CSV stop being enough once a program grows
- What SQLite is, and how Python exposes it through `sqlite3`
- How to connect, run SQL, and save your changes with `sqlite3`
- How to use `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`
- How to read results back as Python objects, including dict-like rows
- Why SQL values need placeholders instead of f-strings
- How a **transaction** groups changes and how `rollback()` cancels uncommitted changes
- How to enable and check SQLite foreign keys for each connection
- When to use SQLite and when a client-server database may fit better
- What an **ORM** is, and where a library like SQLAlchemy fits in once you outgrow raw SQL

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_connecting-running-sql-and-saving.py` | Connecting, running SQL, and saving (line 73) | runs on its own |
| `examples/02_the-context-manager-pattern.py` | Connecting, running SQL, and saving › The context-manager pattern (line 106) | may use names from earlier examples |
| `examples/03_transactions-keeping-a-group-of-changes-all-or-n.py` | Transactions: keeping a group of changes all-or-nothing (line 137) | runs on its own |
| `examples/04_transactions-keeping-a-group-of-changes-all-or-n.py` | Transactions: keeping a group of changes all-or-nothing (line 163) | may use names from earlier examples |
| `examples/05_creating-a-table-create-table.py` | SQL: the language databases understand › Creating a table: `CREATE TABLE` (line 259) | may use names from earlier examples |
| `examples/06_adding-rows-insert.py` | SQL: the language databases understand › Adding rows: `INSERT` (line 291) | may use names from earlier examples |
| `examples/07_adding-rows-insert.py` | SQL: the language databases understand › Adding rows: `INSERT` (line 317) | may use names from earlier examples |
| `examples/08_reading-rows-select.py` | SQL: the language databases understand › Reading rows: `SELECT` (line 343) | may use names from earlier examples |
| `examples/09_reading-rows-select.py` | SQL: the language databases understand › Reading rows: `SELECT` (line 365) | may use names from earlier examples |
| `examples/10_fetching-results-three-ways.py` | SQL: the language databases understand › Fetching results three ways (line 411) | may use names from earlier examples |
| `examples/11_fetching-results-three-ways.py` | SQL: the language databases understand › Fetching results three ways (line 430) | may use names from earlier examples |
| `examples/12_changing-rows-update-and-removing-them-delete.py` | SQL: the language databases understand › Changing rows: `UPDATE`, and removing them: `DELETE` (line 450) | may use names from earlier examples |
| `examples/13_changing-rows-update-and-removing-them-delete.py` | SQL: the language databases understand › Changing rows: `UPDATE`, and removing them: `DELETE` (line 469) | may use names from earlier examples |
| `examples/14_foreign-keys-enable-and-verify-each-connection.py` | Foreign keys: enable and verify each connection (line 520) | runs on its own |
| `examples/15_orms-generate-database-operations.py` | ORMs generate database operations (line 602) | runs on its own |
| `examples/16_try-it-yourself.py` | Try it yourself (line 658) | may use names from earlier examples |
| `examples/17_transfer-lab-locate-a-database-failure.py` | Try it yourself › Transfer lab: locate a database failure (line 710) | runs on its own |
