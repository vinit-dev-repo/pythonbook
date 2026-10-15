# fake_transport.py
class FakeResponse:
    def __init__(self, body=b"", *, status_error=None, body_error=None, events=None):
        self._body = body
        self._status_error = status_error
        self._body_error = body_error
        self._events = events

    def raise_for_status(self):
        if self._events is not None:
            self._events.append("status")
        if self._status_error is not None:
            raise self._status_error

    @property
    def content(self):
        if self._events is not None:
            self._events.append("body")
        if self._body_error is not None:
            raise self._body_error
        return self._body


class QueueTransport:
    def __init__(self, outcomes, *, events=None):
        self._outcomes = iter(outcomes)
        self._events = events
        self.calls = []

    def __call__(self, url, *, timeout):
        if self._events is not None:
            self._events.append("transport")
        self.calls.append((url, timeout))
        outcome = next(self._outcomes)
        if isinstance(outcome, BaseException):
            raise outcome
        return outcome


def scripted_counter(samples, *, events=None):
    values = iter(samples)

    def counter():
        if events is not None:
            events.append("counter")
        value = next(values)
        counter.calls.append(value)
        if isinstance(value, BaseException):
            raise value
        return value

    counter.calls = []
    return counter
