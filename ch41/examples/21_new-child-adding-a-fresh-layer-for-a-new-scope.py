del settings["language"]
print(settings["language"], defaults["language"])
try:
    del settings["language"]
except KeyError:
    print("no first-map override")
