# 35a - Project - Accounts and Transaction Confirmations

The code of the chapter **35a - Project - Accounts and Transaction Confirmations** of the Python tutorial (folder `04 - Iteration and resource management`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How account-specific state composes with a fixed display offset and shared class settings
- How to compare counter conventions and state precisely when a transaction consumes an ID
- How to encode and parse a confirmation without confusing a displayed local time with its UTC instant
- How to prepare a result before committing a balance, and prove that tests detect faulty implementations

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

The chapter saves these files more than once (for example a first version and a repaired one). This folder holds the version the chapter ends with, and the table points to that last version:

- `confirmations.py`
- `test_accounts.py`

| File | Where it is in the chapter | Note |
|---|---|---|
| `account_timezone.py` | Identity, validated state and display offsets › A fixed offset is a value (line 76) |  |
| `account.py` | Identity, validated state and display offsets › The complete Account class (line 169) |  |
| `counter_demo.py` | Counters and transaction decisions (line 633) |  |
| `confirmations.py` | Encoding and parsing confirmations (line 722) | rewritten later in the chapter |
| `account_demo.py` | Encoding and parsing confirmations (line 806) |  |
| `account_failures.py` | Testing the assembled account system (line 870) |  |
| `test_accounts.py` | Testing the assembled account system (line 955) | rewritten later in the chapter |
| `account_transfer.py` | Try it yourself (line 1366) |  |
