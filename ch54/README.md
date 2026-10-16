# 54 - REST APIs, requests and Web Scraping

The code of the chapter **54 - REST APIs, requests and Web Scraping** of the Python tutorial (folder `10 - Web applications and production boundaries`), copied byte for byte from the chapter. The chapter explains every line. Each table below says where a file sits in the chapter: the section heading and the line where the code starts, so you can read the explanation next to it.

## What this chapter teaches

- What an API is and how REST APIs use URLs and HTTP methods
- How to call an API with the `requests` library, and read what comes back
- How to handle errors and set timeouts
- How to send query parameters and data safely
- How to work with dates and time zones using `dateutil` and `zoneinfo`
- The rules to check before you scrape a website
- How to pull data out of a real web page with `BeautifulSoup`

## Files the chapter asks you to save

Each file sits at the path the chapter gives it, so a demo that uses a folder such as `lazy_demo/` keeps that folder here.

| File | Where it is in the chapter | Note |
|---|---|---|
| `weather_client.py` | Complete example: an API client (line 208) |  |
| `test_weather_client.py` | Complete example: an API client (line 316) |  |
| `weather_demo.py` | Complete example: an API client › Independent transfer (line 528) |  |
| `quotes_sample.html` | Complete web-scraping example (line 812) |  |
| `quote_scraper.py` | Complete web-scraping example (line 839) |  |
| `test_quote_scraper.py` | Complete web-scraping example (line 922) |  |
| `quotes_changed.html` | Practice: a changed page layout (line 1005) |  |
| `exercise_quote_scraper.py` | Practice: a changed page layout (line 1037) |  |
| `fetch_live_quotes.py` | Optional: fetch a live page (line 1109) |  |
| `exercise_quote_scraper_answer5.py` | Try it yourself (line 1224) |  |
| `document_cache.py` | Try it yourself › Transfer lab: reuse an immutable JSON download across runs (line 1259) |  |
| `test_document_cache.py` | Try it yourself › Transfer lab: reuse an immutable JSON download across runs (line 1321) |  |
| `threaded_page_counts.py` | Try it yourself › Transfer lab: count text from several pages (line 1423) |  |
| `try_page_counts.py` | Try it yourself › Transfer lab: count text from several pages (line 1471) |  |
| `date_conversion_lab.py` | Try it yourself › Transfer lab: give imported dates an explicit meaning (line 1553) |  |
| `inspect_http_exchange.py` | Try it yourself › Transfer lab: inspect a complete HTTP exchange (line 1698) |  |

## Examples, in chapter order

Every other Python block of the chapter, numbered in reading order and named after its section. Run them in order in one session (or paste them into one file): an example marked *may use names from earlier examples* builds on the ones before it, as it does in the chapter.

| File | Where it is in the chapter | Note |
|---|---|---|
| `examples/01_the-requests-library.py` | The requests library (line 72) | runs on its own |
| `examples/02_query-parameters.py` | Query parameters (line 116) | runs on its own |
| `examples/03_sending-data.py` | Sending data (line 146) | runs on its own |
| `examples/04_sending-data.py` | Sending data (line 173) | may use names from earlier examples |
| `examples/05_dates-and-time-zones-pytz-zoneinfo-and-dateutil.py` | Dates and time zones: pytz, zoneinfo and dateutil (line 596) | may use names from earlier examples |
| `examples/06_dates-and-time-zones-pytz-zoneinfo-and-dateutil.py` | Dates and time zones: pytz, zoneinfo and dateutil (line 622) | may use names from earlier examples |
| `examples/07_dates-and-time-zones-pytz-zoneinfo-and-dateutil.py` | Dates and time zones: pytz, zoneinfo and dateutil (line 656) | may use names from earlier examples |
| `examples/08_dates-and-time-zones-pytz-zoneinfo-and-dateutil.py` | Dates and time zones: pytz, zoneinfo and dateutil (line 673) | may use names from earlier examples |
| `examples/09_fetching-a-page.py` | Fetching a page (line 715) | runs on its own |
| `examples/10_beautifulsoup.py` | BeautifulSoup (line 747) | may use names from earlier examples |
| `examples/11_beautifulsoup.py` | BeautifulSoup (line 779) | may use names from earlier examples |
| `examples/12_try-it-yourself.py` | Try it yourself (line 1181) | runs on its own |
