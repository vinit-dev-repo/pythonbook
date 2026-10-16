import json
from datetime import date

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)   # let the base class raise its normal error

data = {"birthday": date(2000, 5, 1)}
text = json.dumps(data, cls=MyEncoder)
print(text)
