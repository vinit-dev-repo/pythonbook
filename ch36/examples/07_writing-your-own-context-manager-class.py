try:
    with ToyDatabase() as db:
        print(db.query("DROP TABLE users"))
except ValueError as e:
    print("caught:", e)
