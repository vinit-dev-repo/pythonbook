try:
    raise ValueError("plain, not a group")
except* ValueError as group:
    print("caught:", type(group).__name__, [str(e) for e in group.exceptions])
