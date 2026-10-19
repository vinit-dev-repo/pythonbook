from contextlib import closing

class OldStyleConnection:
    """Has .close() but is NOT a context manager on its own."""
    def close(self):
        print("connection closed")

with closing(OldStyleConnection()) as conn:
    print("using the connection")
