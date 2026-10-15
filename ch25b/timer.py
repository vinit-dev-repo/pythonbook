# timer.py
from datetime import datetime, timedelta, timezone
from math import isfinite
from time import perf_counter


class TimerStateError(RuntimeError):
    pass


def utc_now():
    return datetime.now(timezone.utc)


class Timer:
    _display_zone = timezone.utc

    def __init__(self, *, counter=perf_counter, wall_clock=utc_now):
        if not callable(counter) or not callable(wall_clock):
            raise TypeError('counter and wall_clock must be callable')
        self._counter = counter
        self._wall_clock = wall_clock
        self._state = 'idle'
        self._start_counter = self._start_wall = None
        self._end_counter = self._end_wall = self._duration = None

    @staticmethod
    def _counter_sample(value):
        if type(value) is not float:
            raise TypeError('counter sample must be a built-in float')
        if not isfinite(value):
            raise ValueError('counter sample must be finite')
        return value

    @staticmethod
    def _wall_sample(value):
        if not isinstance(value, datetime) or value.utcoffset() is None:
            raise TypeError('wall sample must be an aware datetime')
        return value.astimezone(timezone.utc)

    def _samples(self):
        counter = self._counter_sample(self._counter())
        wall = self._wall_sample(self._wall_clock())
        return counter, wall

    @property
    def state(self):
        return self._state

    @property
    def start_time(self):
        if self._state == 'idle':
            raise TimerStateError('timer has not started')
        return self._start_wall.astimezone(Timer._display_zone)

    @property
    def end_time(self):
        if self._state != 'stopped':
            raise TimerStateError('timer has not stopped')
        return self._end_wall.astimezone(Timer._display_zone)

    @property
    def elapsed(self):
        if self._state == 'idle':
            raise TimerStateError('timer has not started')
        if self._state == 'stopped':
            return self._duration
        candidate = self._counter_sample(self._counter())
        if candidate < self._start_counter:
            raise ValueError('counter moved backward')
        duration = candidate - self._start_counter
        if not isfinite(duration):
            raise ValueError('duration must be finite')
        return duration

    def start(self):
        counter, wall = self._samples()
        self._start_counter, self._start_wall = counter, wall
        self._end_counter = self._end_wall = self._duration = None
        self._state = 'running'

    def stop(self):
        if self._state == 'idle':
            raise TimerStateError('timer has not started')
        counter, wall = self._samples()
        if counter < self._start_counter:
            raise ValueError('counter moved backward')
        if self._end_counter is not None and counter < self._end_counter:
            raise ValueError('counter moved backward')
        duration = counter - self._start_counter
        if not isfinite(duration):
            raise ValueError('duration must be finite')
        self._end_counter, self._end_wall, self._duration = counter, wall, duration
        self._state = 'stopped'

    @classmethod
    def set_display_offset(cls, minutes, name):
        if type(minutes) is not int or not isinstance(name, str):
            raise TypeError('minutes must be a built-in int and name a string')
        if not -1440 < minutes < 1440:
            raise ValueError('offset must be strictly between -1440 and 1440 minutes')
        candidate = timezone(timedelta(minutes=minutes), name)
        Timer._display_zone = candidate
