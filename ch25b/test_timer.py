# test_timer.py
import unittest
from datetime import datetime, timedelta, timezone
from math import isfinite

from controlled_clocks import scripted, utc
from timer import Timer, TimerStateError


BASE = utc('2026-01-01T00:00:00')


class ClockFailure(RuntimeError):
    pass


class FaultyTimer(Timer):
    # Deliberate bad stage: the first assignment survives a wall-clock failure.
    def start(self):
        self._start_counter = self._counter_sample(self._counter())
        self._start_wall = self._wall_sample(self._wall_clock())
        self._end_counter = self._end_wall = self._duration = None
        self._state = 'running'


class TimerTests(unittest.TestCase):
    def setUp(self):
        old_zone = Timer._display_zone
        self.addCleanup(setattr, Timer, '_display_zone', old_zone)
        Timer.set_display_offset(0, 'UTC')

    def make(self, counters, walls, timer_type=Timer):
        events = []
        counter = scripted(counters, events=events, label='counter')
        wall = scripted(walls, events=events, label='wall')
        return timer_type(counter=counter, wall_clock=wall), counter, wall, events

    def public_snapshot(self, timer):
        values = [timer.state]
        for name in ('start_time', 'end_time'):
            try:
                values.append(getattr(timer, name))
            except TimerStateError:
                values.append('unavailable')
        if timer.state == 'stopped':
            values.append(timer.elapsed)
        return tuple(values)

    def test_constructor_checks_callables_without_sampling(self):
        timer, counter, wall, events = self.make([], [])
        self.assertEqual(timer.state, 'idle')
        self.assertEqual(events, [])
        self.assertEqual(counter.calls, [])
        self.assertEqual(wall.calls, [])
        for options in ({'counter': 1}, {'wall_clock': None}):
            with self.subTest(options=options), self.assertRaises(TypeError):
                Timer(**options)

    def test_idle_errors_consume_no_samples_and_preserve_fields(self):
        timer, counter, wall, events = self.make([], [])
        before = vars(timer).copy()
        for action in (timer.stop, lambda: timer.elapsed,
                       lambda: timer.start_time, lambda: timer.end_time):
            with self.assertRaises(TimerStateError):
                action()
            self.assertEqual(vars(timer), before)
        self.assertEqual(events, [])
        self.assertEqual((len(counter.calls), len(wall.calls)), (0, 0))

    def test_all_successful_transitions_and_query_consumption(self):
        timer, counter, wall, events = self.make(
            [100.0, 102.0, 105.0, 108.0, 200.0, 300.0, 303.0],
            [BASE + timedelta(seconds=n) for n in (0, 5, 8, 20, 30, 33)])
        self.assertIsNone(timer.start())
        self.assertEqual(self.public_snapshot(timer), ('running', BASE, 'unavailable'))
        before = vars(timer).copy()
        self.assertEqual(timer.elapsed, 2.0)
        self.assertEqual(vars(timer), before)
        self.assertEqual(events, ['counter', 'wall', 'counter'])
        self.assertIsNone(timer.stop())
        self.assertEqual(timer.elapsed, 5.0)
        self.assertIsNone(timer.stop())
        expected = ('stopped', BASE, BASE + timedelta(seconds=8), 8.0)
        self.assertEqual(self.public_snapshot(timer), expected)
        calls = events[:]
        self.assertEqual(self.public_snapshot(timer), expected)
        self.assertEqual(events, calls)
        self.assertIsNone(timer.start())  # restart from stopped
        self.assertEqual(self.public_snapshot(timer), ('running', BASE + timedelta(seconds=20), 'unavailable'))
        self.assertIsNone(timer.start())  # restart while already running
        self.assertEqual(self.public_snapshot(timer), ('running', BASE + timedelta(seconds=30), 'unavailable'))
        self.assertIsNone(timer.stop())
        self.assertEqual(self.public_snapshot(timer), ('stopped', BASE + timedelta(seconds=30), BASE + timedelta(seconds=33), 3.0))
        self.assertEqual((len(counter.calls), len(wall.calls)), (7, 6))
        self.assertEqual(events, ['counter', 'wall', 'counter'] + ['counter', 'wall'] * 5)

    def test_clock_failures_at_each_transition_preserve_complete_state(self):
        cases = [('idle', 'start'), ('running', 'start'), ('stopped', 'start'),
                 ('running', 'stop'), ('stopped', 'stop')]
        for state, method in cases:
            for failed_clock in ('counter', 'wall'):
                with self.subTest(state=state, method=method, failed_clock=failed_clock):
                    prefix = [] if state == 'idle' else [10.0]
                    if state == 'stopped':
                        prefix.append(15.0)
                    failure = ClockFailure('sample failed')
                    counters = prefix + [failure if failed_clock == 'counter' else 20.0]
                    walls = [BASE] * len(prefix)
                    if failed_clock == 'wall':
                        walls.append(failure)
                    timer, counter, wall, events = self.make(counters, walls)
                    if state != 'idle':
                        timer.start()
                    if state == 'stopped':
                        timer.stop()
                    public_before = self.public_snapshot(timer)
                    fields_before = vars(timer).copy()
                    calls_before = len(events)
                    with self.assertRaises(ClockFailure) as caught:
                        getattr(timer, method)()
                    self.assertIs(caught.exception, failure)
                    self.assertEqual(self.public_snapshot(timer), public_before)
                    self.assertEqual(vars(timer), fields_before)
                    self.assertEqual(events[calls_before:], ['counter'] if failed_clock == 'counter' else ['counter', 'wall'])
                    self.assertEqual(len(counter.calls), len(prefix) + 1)
                    self.assertEqual(len(wall.calls), len(prefix) + (failed_clock == 'wall'))

    def test_invalid_counter_samples_at_start_stop_and_query(self):
        bad_values = [(True, TypeError), (1, TypeError), ('1.0', TypeError),
                      (None, TypeError), (float('nan'), ValueError),
                      (float('inf'), ValueError), (-float('inf'), ValueError)]
        for value, error in bad_values:
            for operation in ('start', 'stop', 'elapsed'):
                with self.subTest(value=value, operation=operation):
                    counters = [value] if operation == 'start' else [1.0, value]
                    walls = [] if operation == 'start' else [BASE]
                    timer, counter, wall, events = self.make(counters, walls)
                    if operation != 'start':
                        timer.start()
                    before = vars(timer).copy()
                    public_before = self.public_snapshot(timer)
                    call_count = len(wall.calls)
                    with self.assertRaises(error):
                        if operation == 'elapsed':
                            timer.elapsed
                        else:
                            getattr(timer, operation)()
                    self.assertEqual(vars(timer), before)
                    self.assertEqual(self.public_snapshot(timer), public_before)
                    self.assertEqual(len(wall.calls), call_count)

    def test_invalid_wall_samples_preserve_start_or_stop_state(self):
        for value in (None, '2026-01-01', datetime(2026, 1, 1)):
            for state in ('idle', 'running', 'stopped'):
                with self.subTest(value=value, state=state):
                    prefix = [] if state == 'idle' else [1.0]
                    if state == 'stopped':
                        prefix.append(2.0)
                    timer, counter, wall, events = self.make(prefix + [3.0], [BASE] * len(prefix) + [value])
                    if state != 'idle':
                        timer.start()
                    if state == 'stopped':
                        timer.stop()
                    before = vars(timer).copy()
                    public_before = self.public_snapshot(timer)
                    with self.assertRaises(TypeError):
                        timer.start() if state == 'idle' else timer.stop()
                    self.assertEqual(vars(timer), before)
                    self.assertEqual(self.public_snapshot(timer), public_before)
                    self.assertEqual(events[-2:], ['counter', 'wall'])

    def test_backward_candidates_and_overflow_leave_fields_unchanged(self):
        for start, candidate, error in ((3.0, 2.0, 'backward'), (-1e308, 1e308, 'finite')):
            for operation in ('stop', 'elapsed'):
                with self.subTest(start=start, operation=operation):
                    timer, counter, wall, events = self.make([start, candidate], [BASE, BASE])
                    timer.start()
                    before = vars(timer).copy()
                    with self.assertRaisesRegex(ValueError, error):
                        if operation == 'elapsed':
                            timer.elapsed
                        else:
                            timer.stop()
                    self.assertEqual(vars(timer), before)
                    self.assertEqual(self.public_snapshot(timer), ('running', BASE, 'unavailable'))
                    self.assertEqual(len(wall.calls), 2 if operation == 'stop' else 1)
        timer, counter, wall, events = self.make([10.0, 15.0, 14.0], [BASE] * 3)
        timer.start()
        timer.stop()
        before = self.public_snapshot(timer)
        with self.assertRaisesRegex(ValueError, 'backward'):
            timer.stop()
        self.assertEqual(self.public_snapshot(timer), before)

    def test_running_query_clock_exception_preserves_fields(self):
        failure = ClockFailure('query failed')
        timer, counter, wall, events = self.make([1.0, failure, 4.0], [BASE])
        timer.start()
        before = vars(timer).copy()
        with self.assertRaises(ClockFailure) as caught:
            timer.elapsed
        self.assertIs(caught.exception, failure)
        self.assertEqual(vars(timer), before)
        self.assertEqual(timer.elapsed, 3.0)
        self.assertEqual(events, ['counter', 'wall', 'counter', 'counter'])

    def test_zero_negative_origin_backward_wall_and_utc_normalization(self):
        east = timezone(timedelta(hours=5, minutes=30), 'east')
        wall_start = datetime(2026, 1, 1, 5, 30, tzinfo=east)
        timer, counter, wall, events = self.make([-2.0, -2.0, 3.0], [wall_start, BASE, BASE - timedelta(seconds=1)])
        timer.start()
        self.assertEqual(timer.start_time, BASE)
        self.assertEqual(timer.start_time.utcoffset(), timedelta(0))
        self.assertIs(timer._start_wall.tzinfo, timezone.utc)
        timer.stop()
        self.assertEqual(timer.elapsed, 0.0)
        timer.stop()
        self.assertEqual(timer.elapsed, 5.0)
        self.assertLess(timer.end_time, timer.start_time)
        self.assertEqual(timer.end_time, BASE - timedelta(seconds=1))

    def test_independent_timers_share_only_display_configuration(self):
        a, ac, aw, ae = self.make([100.0, 108.0, 300.0], [BASE] * 3)
        b, bc, bw, be = self.make([200.0, 203.0], [BASE + timedelta(minutes=1)] * 2)
        a.start()
        a.stop()
        self.assertEqual(b.state, 'idle')
        self.assertEqual(be, [])
        b.start()
        b.stop()
        for minutes, expected in ((0, '2026-01-01T00:00:00+00:00'),
                                  (330, '2026-01-01T05:30:00+05:30'),
                                  (-240, '2025-12-31T20:00:00-04:00')):
            Timer.set_display_offset(minutes, 'display')
            self.assertEqual(a.start_time.isoformat(), expected)
            self.assertEqual(b.start_time, a.start_time + timedelta(minutes=1))
            self.assertEqual(b.start_time.utcoffset(), timedelta(minutes=minutes))
            self.assertEqual((a.elapsed, b.elapsed), (8.0, 3.0))
        self.assertEqual((len(ac.calls), len(aw.calls), len(bc.calls), len(bw.calls)), (2, 2, 2, 2))
        before_b = self.public_snapshot(b)
        a.start()
        self.assertEqual(a.state, 'running')
        self.assertEqual(self.public_snapshot(b), before_b)
        future, counter, wall, events = self.make([1.0], [BASE])
        future.start()
        self.assertEqual(future.start_time.utcoffset(), timedelta(hours=-4))

    def test_offset_boundaries_and_failed_settings_preserve_display(self):
        timer, counter, wall, events = self.make([1.0, 2.0], [BASE] * 2)
        timer.start()
        timer.stop()
        for minutes in (-1439, 1439):
            Timer.set_display_offset(minutes, 'edge')
            self.assertEqual(timer.start_time.utcoffset(), timedelta(minutes=minutes))
            self.assertEqual(timer.elapsed, 1.0)
        for minutes, name, error in ((True, 'bad', TypeError), (1.0, 'bad', TypeError),
                                     (0, None, TypeError), (-1440, 'bad', ValueError),
                                     (1440, 'bad', ValueError), (10**100, 'bad', ValueError)):
            with self.subTest(minutes=minutes, name=name):
                before = (timer.start_time.isoformat(), timer.end_time.isoformat(), timer.elapsed)
                zone = Timer._display_zone
                with self.assertRaises(error):
                    Timer.set_display_offset(minutes, name)
                self.assertIs(Timer._display_zone, zone)
                self.assertEqual((timer.start_time.isoformat(), timer.end_time.isoformat(), timer.elapsed), before)

    def assert_restart_regression(self, timer_type):
        timer, counter, wall, events = self.make(
            [100.0, 105.0, 200.0, 208.0],
            [BASE, BASE, ClockFailure('restart wall failed'), BASE], timer_type)
        timer.start()
        timer.stop()
        before = self.public_snapshot(timer)
        with self.assertRaises(ClockFailure):
            timer.start()
        self.assertEqual(self.public_snapshot(timer), before)
        timer.stop()
        # Failed restart must not change the original 100.0 counter anchor.
        self.assertEqual(timer.elapsed, 108.0)

    def test_public_regression_detects_assignment_before_second_sample(self):
        self.assert_restart_regression(Timer)
        with self.assertRaisesRegex(AssertionError, r'8\.0 != 108\.0'):
            self.assert_restart_regression(FaultyTimer)

    def test_default_clocks_smoke_without_fixed_duration(self):
        timer = Timer()
        timer.start()
        timer.stop()
        self.assertEqual(timer.state, 'stopped')
        self.assertTrue(isfinite(timer.elapsed))
        self.assertGreaterEqual(timer.elapsed, 0.0)
        self.assertIsNotNone(timer.start_time.utcoffset())
        self.assertIsNotNone(timer.end_time.utcoffset())


if __name__ == '__main__':
    unittest.main()
