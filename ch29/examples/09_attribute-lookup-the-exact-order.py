class Fallback:
    def __getattr__(self, name):
        return f"made up {name}"

print(Fallback().anything)
