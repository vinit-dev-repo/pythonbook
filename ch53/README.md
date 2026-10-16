# 53 - Flask - Your First Web App

The code of the chapter **53 - Flask - Your First Web App** of the Python tutorial (folder `10 - Web applications and production boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- How a browser and a web server exchange requests and responses
- What `Flask` is, and how to write the smallest possible web app
- How to add more pages, including pages with a changing part in the URL
- How templates keep HTML in separate files instead of Python strings
- The difference between `GET` and `POST`, and how to handle a form
- How to build a small JSON API that another program can call
- What HTTP status codes mean, in plain words

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `app.py` | Install Flask and make a small app (line 69) |  |
| `routes_app.py` | Dynamic URLs (line 161) |  |
| `template_app.py` | Templates: separating HTML from Python (line 252) |  |
| `templates/home.html` | Templates: separating HTML from Python (line 280) |  |
| `templates/base.html` | One base template, many pages: `{% block %}` (line 315) |  |
| `templates/about.html` | One base template, many pages: `{% block %}` (line 327) |  |
| `templates/sign.html` | HTTP verbs: GET vs POST (line 381) |  |
| `todo_api.py` | Building a small JSON API (line 412) |  |
| `test_flask_responses.py` | Check the routes without starting a server (line 592) |  |
| `exercise_flask_responses.py` | Practice: observe the unchanged notes app (line 688) |  |
| `templates/greet.html` | Try it yourself (line 840) |  |
| `parcel_app.py` | Transfer lab: turn a form into a result URL (line 863) |  |
| `templates/parcel_form.html` | Transfer lab: turn a form into a result URL (line 907) |  |
| `templates/parcel_result.html` | Transfer lab: turn a form into a result URL (line 925) |  |
| `check_parcel_app.py` | Transfer lab: turn a form into a result URL (line 960) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_more-pages-routes.py` | More pages: routes (line 126) | runs on its own |
| `examples/02_returning-html.py` | Returning HTML (line 232) | may use names from earlier examples |
| `examples/03_http-verbs-get-vs-post.py` | HTTP verbs: GET vs POST (line 360) | may use names from earlier examples |
| `examples/04_building-a-small-json-api.py` | Building a small JSON API (line 507) | may use names from earlier examples |
| `examples/05_connecting-to-a-real-database.py` | Connecting to a real database (line 750) | may use names from earlier examples |
| `examples/06_try-it-yourself.py` | Try it yourself (line 798) | may use names from earlier examples |
