# 54b - Project - Loading a Consistent Resource Snapshot

The code of the chapter **54b - Project - Loading a Consistent Resource Snapshot** of the Python tutorial (folder `10 - Web applications and production boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- Load a response only when its body, size or duration is first needed.
- Keep those values together so that they describe one successful load.
- Distinguish a URL change from an explicit refresh, and preserve a usable snapshot when refresh fails.
- Check the behavior offline with controlled responses and elapsed-time samples.

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `fake_transport.py` | Load one consistent resource snapshot › Give the dependencies a small, visible interface (line 61) |  |
| `resource_cache.py` | Load one consistent resource snapshot › Build one candidate, then publish it (line 127) |  |
| `test_resource_cache.py` | Load one consistent resource snapshot › Test the contract and a known bad refresh (line 243) |  |
| `cache_demo.py` | Load one consistent resource snapshot › Follow a complete load, refresh and URL change (line 472) |  |
| `cache_transfer.py` | Try it yourself (line 552) |  |
