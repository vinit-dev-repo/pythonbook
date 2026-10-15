# controlled_clocks.py
from datetime import datetime, timezone


def scripted(samples, *, events=None, label='clock'):
    pending = list(samples)
    calls = []

    def clock():
        calls.append(None)
        if events is not None:
            events.append(label)
        value = pending.pop(0)
        if isinstance(value, Exception):
            raise value
        return value

    clock.calls = calls
    return clock


def utc(text):
    # Fixture text is a naive ISO date/time whose declared zone is UTC.
    value = datetime.fromisoformat(text)
    if value.tzinfo is not None:
        raise ValueError('fixture text must not already contain a timezone')
    return value.replace(tzinfo=timezone.utc)
