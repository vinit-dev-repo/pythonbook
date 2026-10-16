import pickle

data = {"name": "Amy", "scores": [90, 85, 88]}

with open("data.pkl", "wb") as f:      # "wb" = write bytes
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:      # "rb" = read bytes
    restored = pickle.load(f)

print(restored)
