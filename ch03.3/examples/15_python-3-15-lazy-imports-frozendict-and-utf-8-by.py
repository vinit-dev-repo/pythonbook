settings = frozendict(debug=False, level=3)
print(settings)
try:
    settings["debug"] = True
except TypeError as error:
    print("TypeError:", error)
