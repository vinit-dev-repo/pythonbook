try:
    b"\xff".decode("utf-8")
except ValueError:
    print("Caught it via ValueError, even though the real error is UnicodeDecodeError")
