from datetime import date

class DatedLabel:
    def __init__(self, day):
        self.day = day

    def __str__(self):
        return "friendly date"

    def __format__(self, spec):
        return "Date: " + format(self.day, spec)

dated = DatedLabel(date(2026, 9, 20))
print(str(dated))
print(format(dated, "%Y-%m-%d"))
print(f"{dated}")
