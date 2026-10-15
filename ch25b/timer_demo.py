# timer_demo.py
from controlled_clocks import scripted, utc
from timer import Timer, TimerStateError


if __name__ == '__main__':
    counter_a = scripted([100.0, 102.0, 105.0, 108.0, 300.0])
    wall_a = scripted([
        utc('2026-01-01T00:00:00'),
        utc('2026-01-01T00:00:02'),
        utc('2025-12-31T23:59:59'),
        utc('2026-01-02T00:00:00'),
    ])
    a = Timer(counter=counter_a, wall_clock=wall_a)
    b = Timer(counter=scripted([200.0, 203.0]), wall_clock=scripted([
        utc('2026-01-01T00:01:00'), utc('2026-01-01T00:01:03'),
    ]))
    old_zone = Timer._display_zone
    try:
        Timer.set_display_offset(0, 'UTC')
        a.start()
        print('running A:', a.state, a.elapsed)
        a.stop()
        print('first stop A:', a.elapsed)
        a.stop()
        print('repeated stop A:', a.elapsed, a.end_time < a.start_time)
        b.start()
        b.stop()
        print('independent durations:', a.elapsed, b.elapsed)
        print('UTC starts:', a.start_time.isoformat(), b.start_time.isoformat())
        Timer.set_display_offset(330, 'east')
        print('east starts:', a.start_time.isoformat(), b.start_time.isoformat())
        print('unchanged durations:', a.elapsed, b.elapsed)
        Timer.set_display_offset(-240, 'west')
        print('west starts:', a.start_time.isoformat(), b.start_time.isoformat())
        a.start()
        try:
            a.end_time
        except TimerStateError:
            print('restart clears A end:', a.state, 'B remains', b.state, b.elapsed)
        else:
            raise AssertionError('restart retained an end')
    finally:
        Timer._display_zone = old_zone
