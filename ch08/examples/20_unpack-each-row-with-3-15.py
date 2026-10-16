tags = [{"red", "blue"}, {"blue", "green"}]
print(sorted({*group for group in tags}))

settings = [{"size": "S", "colour": "red"}, {"size": "M"}]
print({**s for s in settings})
