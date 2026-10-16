def risky():
    raise ExceptionGroup("two things went wrong", [
        ValueError("bad value"),
        TypeError("bad type"),
    ])

try:
    risky()
except* ValueError as group:
    print("caught ValueErrors:", [str(e) for e in group.exceptions])
except* TypeError as group:
    print("caught TypeErrors :", [str(e) for e in group.exceptions])
