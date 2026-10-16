class Methods:
    def __init__(self, balance):
        self.balance = balance

    def report(self):
        return f"old function, balance={self.balance}"

method_account = Methods(100)
saved_report = method_account.report
method_account.balance = 125

def replacement(self):
    return f"new function, balance={self.balance}"

Methods.report = replacement
print(saved_report())
print(method_account.report())
print(saved_report.__self__ is method_account)
print(saved_report.__func__.__name__)
