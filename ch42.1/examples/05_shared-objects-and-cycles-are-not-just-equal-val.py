import json
import pickle

shared = ["draft"]
original = [shared, shared]
from_pickle = pickle.loads(pickle.dumps(original))
from_json = json.loads(json.dumps(original))
print("pickle shares:", from_pickle[0] is from_pickle[1])
print("JSON shares:", from_json[0] is from_json[1])
from_pickle[0].append("checked")
print(from_pickle[1], shared)

cycle = []
cycle.append(cycle)
restored = pickle.loads(pickle.dumps(cycle))
print("restored cycle:", restored[0] is restored)
try:
    json.dumps(cycle)
except ValueError:
    print("JSON cycle refused")
