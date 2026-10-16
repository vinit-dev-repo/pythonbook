from datetime import date

class Event:
    def __init__(self, name, day):
        self.name = name
        self.day = day

    @classmethod
    def today(cls, name):
        return cls(name, date.today())

    @classmethod
    def from_string(cls, name, iso_date):
        return cls(name, date.fromisoformat(iso_date))

e1 = Event.from_string("Launch", "2026-09-01")
print(e1.name, e1.day)
