class Reminder:
    def __call__(self, message: str) -> str:
        return f"remember: {message}"

reminder = Reminder()
print(callable(reminder))
try:
    print(reminder())
except TypeError as error:
    print("Missing argument:", error)
print(reminder("milk"))
