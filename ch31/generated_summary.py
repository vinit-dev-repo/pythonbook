# generated_summary.py
def summary_for(fields):
    fields = tuple(fields)
    def summary(self):
        return tuple(getattr(self, name) for name in fields)
    return summary

class SummaryMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        updated = dict(namespace)
        if "summary_fields" in updated and "summary" not in updated:
            updated["summary"] = summary_for(updated["summary_fields"])
        return super().__new__(mcs, name, bases, updated, **kwargs)

def add_summary(cls):
    local = vars(cls)
    if "summary_fields" in local and "summary" not in local:
        cls.summary = summary_for(local["summary_fields"])
    return cls

class Place(metaclass=SummaryMeta):
    summary_fields = ("name", "capacity")
    name, capacity = "studio", 4

@add_summary
class Delivery:
    summary_fields = ("code",)
    code = "R8"

print(Place().summary(), Delivery().summary())
place = Place()
place.capacity = 7
print(place.summary())

class Custom(Place):
    summary_fields = ("missing",)
    def summary(self):
        return "kept"

print(Custom().summary())
