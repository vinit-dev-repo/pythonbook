# 53.2 - Templates, GET and POST, a JSON API and Status Codes

The code of the chapter **53.2 - Templates, GET and POST, a JSON API and Status Codes** of the Python tutorial (folder `10 - Web applications and production boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How templates keep HTML in separate files instead of Python strings
- The difference between `GET` and `POST`, and how to handle a form
- How to build a small JSON API that another program can call
- What HTTP status codes mean, in plain words

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `template_app.py` | Templates: separating HTML from Python (line 45) |  |
| `templates/home.html` | Templates: separating HTML from Python (line 71) |  |
| `templates/base.html` | Templates: separating HTML from Python › One base template, many pages: `{% block %}` (line 104) |  |
| `templates/about.html` | Templates: separating HTML from Python › One base template, many pages: `{% block %}` (line 116) |  |
| `templates/sign.html` | HTTP verbs: GET vs POST (line 173) |  |
| `todo_api.py` | Building a small JSON API (line 206) |  |
| `templates/greet.html` | Try it yourself (line 401) |  |
| `parcel_app.py` | Try it yourself › Transfer lab: turn a form into a result URL (line 422) |  |
| `templates/parcel_form.html` | Try it yourself › Transfer lab: turn a form into a result URL (line 466) |  |
| `templates/parcel_result.html` | Try it yourself › Transfer lab: turn a form into a result URL (line 484) |  |
| `check_parcel_app.py` | Try it yourself › Transfer lab: turn a form into a result URL (line 518) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_http-verbs-get-vs-post.py` | HTTP verbs: GET vs POST (line 152) | runs on its own |
| `examples/02_building-a-small-json-api.py` | Building a small JSON API (line 304) | may use names from earlier examples |
| `examples/03_try-it-yourself.py` | Try it yourself (line 371) | may use names from earlier examples |
