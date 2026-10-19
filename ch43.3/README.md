# 43.3 - Futures, a Local Artifact Lab and a TCP and HTTP Catalog Service

The code of the chapter **43.3 - Futures, a Local Artifact Lab and a TCP and HTTP Catalog Service** of the Python tutorial (folder `07 - Concurrency`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How to bridge a callback to an awaitable result with a future
- How a local HTTP client/server lab preserves request identity, counts completed outcomes and waits for file writes
- How a TCP server finds the end of each message, and how one search function serves both TCP and HTTP

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `artifact_fixture.py` | Lab: collect local artifacts and report completed outcomes (line 109) |  |
| `collect_artifacts.py` | Lab: collect local artifacts and report completed outcomes (line 159) |  |
| `catalog_service.py` | Serve one catalog through TCP and HTTP (line 335) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_bridge-a-callback-to-an-awaitable-result.py` | Bridge a callback to an awaitable result (line 42) | runs on its own |
| `examples/02_try-it-yourself.py` | Try it yourself (line 504) | runs on its own |
