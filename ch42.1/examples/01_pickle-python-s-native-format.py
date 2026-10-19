import pickle

data = {"name": "Amy", "scores": [90, 85, 88]}

# serialize to bytes
raw = pickle.dumps(data)
print(type(raw))

# deserialize back to a live object
restored = pickle.loads(raw)
print(restored)
