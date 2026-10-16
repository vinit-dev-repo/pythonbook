def process(data, steps=()):
    return [apply_all(item, steps) for item in data]

def apply_all(item, steps):
    for step in steps:
        item = step(item)
    return item

CLEAN = (str.strip, str.lower)
SLUG = (str.strip, str.lower, lambda s: s.replace(" ", "_"))

print(process(["  Hello World  ", " BYE "], CLEAN))
print(process(["  Hello World  "], SLUG))
