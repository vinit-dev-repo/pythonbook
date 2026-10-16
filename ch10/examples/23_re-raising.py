def load_settings():
    try:
        return 1 / 0
    except ZeroDivisionError:
        print("Logging the problem before it crashes the program...")
        raise            # re-raise the SAME exception

load_settings()
