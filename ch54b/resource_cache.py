# resource_cache.py
from collections import namedtuple
from math import isfinite
from time import perf_counter


snapshot = namedtuple("snapshot", "source_url body size duration")


class Resource:
    def __init__(self, url, *, transport, counter=perf_counter):
        self._url = self._validate_url(url)
        if not callable(transport):
            raise TypeError("transport must be callable")
        if not callable(counter):
            raise TypeError("counter must be callable")
        self._transport = transport
        self._counter = counter
        self._snapshot = None

    @staticmethod
    def _validate_url(value):
        if type(value) is not str:
            raise TypeError("url must be a string")
        value = value.strip()
        if not value:
            raise ValueError("url must not be blank")
        return value

    @staticmethod
    def _validate_counter_sample(value):
        if type(value) is not float:
            raise TypeError("counter sample must be a float")
        if not isfinite(value):
            raise ValueError("counter sample must be finite")
        return value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        normalized = self._validate_url(value)
        if normalized != self._url:
            self._url = normalized
            self._snapshot = None

    @property
    def snapshot(self):
        return self._snapshot

    @property
    def body(self):
        return self._load_if_absent().body

    @property
    def size(self):
        return self._load_if_absent().size

    @property
    def duration(self):
        return self._load_if_absent().duration

    def refresh(self):
        return self._load()

    def _load_if_absent(self):
        if self._snapshot is None:
            return self._load()
        return self._snapshot

    def _load(self):
        requested_url = self.url
        start = self._validate_counter_sample(self._counter())
        response = self._transport(requested_url, timeout=(3, 10))
        response.raise_for_status()
        body = response.content
        if type(body) is not bytes:
            raise TypeError("response content must be bytes")
        end = self._validate_counter_sample(self._counter())
        duration = end - start
        if not isfinite(duration):
            raise ValueError("duration must be finite")
        if duration < 0:
            raise ValueError("counter must not move backwards")
        candidate = snapshot(requested_url, body, len(body), duration)
        self._snapshot = candidate
        return candidate
