# driver_demo.py
from boundaries import safe_call


def record(label, *, events):
    events.append(label)


def check_total(events, *, expected):
    events.append("checked")
    assert sum([2, 3]) == expected, "total should match expected"


def check_after(events):
    assert events == ["recorded", "checked"]
    events.append("later")


def main():
    events = []
    outcomes = [
        safe_call(record, "recorded", events=events),
        safe_call(check_total, events, expected=6),
        safe_call(check_after, events),
    ]
    successes = sum(1 for ok, value in outcomes if ok)
    print("invocation successes:", successes)
    print("invocation failures:", len(outcomes) - successes)
    print("events:", events)
    print("first value:", outcomes[0][1])
    print("second value type:", type(outcomes[1][1]).__name__)
    return events, outcomes


if __name__ == "__main__":
    main()
