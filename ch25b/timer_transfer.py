# timer_transfer.py
from controlled_clocks import scripted, utc
from timer import Timer


if __name__ == '__main__':
    counter = scripted([10.0, 15.0, 14.0, 18.0])
    wall = scripted([
        utc('2026-01-03T00:30:00'), utc('2026-01-03T00:30:05'),
        utc('2026-01-03T00:30:04'), utc('2026-01-03T00:30:08'),
    ])
    timer = Timer(counter=counter, wall_clock=wall)
    old_zone = Timer._display_zone
    try:
        Timer.set_display_offset(0, 'UTC')
        timer.start()
        timer.stop()
        before = (timer.state, timer.start_time, timer.end_time, timer.elapsed)
        try:
            timer.stop()
        except ValueError as error:
            assert (timer.state, timer.start_time, timer.end_time, timer.elapsed) == before
            assert (len(counter.calls), len(wall.calls)) == (3, 3)
            print('failed repeated stop:', type(error).__name__, timer.elapsed)
        else:
            raise AssertionError('backward stop unexpectedly succeeded')
        Timer.set_display_offset(-60, 'west')
        assert timer.state == 'stopped' and timer.elapsed == 5.0
        assert timer.end_time.isoformat() == '2026-01-02T23:30:05-01:00'
        print('same end, new display:', timer.end_time.isoformat())
        assert timer.stop() is None
        assert timer.elapsed == 8.0
        assert timer.end_time.isoformat() == '2026-01-02T23:30:08-01:00'
        assert timer.start_time == before[1]
        assert (len(counter.calls), len(wall.calls)) == (4, 4)
        print('retry:', timer.elapsed, timer.end_time.isoformat())
    finally:
        Timer._display_zone = old_zone
