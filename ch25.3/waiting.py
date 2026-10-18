# waiting.py
def seconds_left(started_at, now, wait):
    return max(0, wait - (now - started_at))
