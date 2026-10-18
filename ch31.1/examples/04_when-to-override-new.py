class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating the one and only instance")
            cls._instance = super().__new__(cls)
        else:
            print("Reusing the existing instance")
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)
