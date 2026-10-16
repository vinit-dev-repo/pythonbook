class Account:
    def __init__(self, balance):
        self._balance = balance      # convention: internal
        self.__pin = "1234"          # name-mangled

acc = Account(100)
print(acc._balance)
print(acc._Account__pin)   # the REAL name after mangling
