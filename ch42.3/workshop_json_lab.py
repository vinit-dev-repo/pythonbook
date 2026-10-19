# workshop_json_lab.py
import json
from dataclasses import dataclass
from datetime import date, datetime, timezone
from decimal import Decimal

@dataclass
class CutPlan:
    day: date
    metres: Decimal

@dataclass
class MachineReport:
    recorded_at: datetime
    waste: Decimal

class WorkshopEncoder(json.JSONEncoder):
    def default(self, value):
        if type(value) is CutPlan:
            tag, payload = "plan", {"day": value.day, "metres": value.metres}
        elif type(value) is MachineReport:
            tag, payload = "report", {"recorded_at": value.recorded_at, "waste": value.waste}
        elif type(value) is datetime:
            tag, payload = "timestamp", value.isoformat()
        elif type(value) is date:
            tag, payload = "date", value.isoformat()
        elif type(value) is Decimal:
            tag, payload = "decimal", str(value)
        else:
            return super().default(value)
        return {"$workshop": tag, "value": payload}

BUILDERS = {
    "plan": lambda payload: CutPlan(**payload),
    "report": lambda payload: MachineReport(**payload),
    "timestamp": datetime.fromisoformat,
    "date": date.fromisoformat,
    "decimal": Decimal,
}

def restore_workshop(mapping):
    if "$workshop" not in mapping:
        return mapping
    tag = mapping["$workshop"]
    if set(mapping) != {"$workshop", "value"} or type(tag) is not str or tag not in BUILDERS:
        raise ValueError("unknown or malformed workshop envelope")
    return BUILDERS[tag](mapping["value"])

class WorkshopDecoder(json.JSONDecoder):
    def __init__(self, **options):
        for name in ("object_hook", "object_pairs_hook"):
            if options.pop(name, None) is not None:
                raise TypeError("WorkshopDecoder owns its object hook")
        super().__init__(object_hook=restore_workshop, **options)

document = {
    "plans": [CutPlan(date(2026, 4, 12), Decimal("12.3400"))],
    "reports": [MachineReport(datetime(2026, 4, 12, 8, 5, 9, 1200, tzinfo=timezone.utc), Decimal("0.0070"))],
}
if __name__ == "__main__":
    text = json.dumps(document, cls=WorkshopEncoder)
    restored = json.loads(text, cls=WorkshopDecoder)
    print("equal:", restored == document)
    print("same record:", restored["plans"][0] is document["plans"][0])
    print(type(restored["plans"][0].day).__name__, type(restored["reports"][0].recorded_at).__name__)
    print(restored["plans"][0].metres.as_tuple().exponent, restored["reports"][0].waste.as_tuple().exponent)
    try:
        json.loads('{"$workshop": "plugin", "value": "anything"}', cls=WorkshopDecoder)
    except ValueError:
        print("unknown tag refused")
