class ToyDatabase:
    """Pretends to open and close a database connection."""

    def __enter__(self):
        print("connection opened")
        return self

    def query(self, sql):
        if "DROP" in sql:
            raise ValueError("that query is not allowed here")
        return f"ran: {sql}"

    def __exit__(self, exc_type, exc_value, traceback):
        print("connection closed")

with ToyDatabase() as db:
    print(db.query("SELECT * FROM users"))
