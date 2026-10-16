defaults = {"theme": "light", "font_size": 12}
overrides = {"font_size": 16}

merged = defaults | overrides       # a brand NEW dict
print(merged)

defaults |= overrides               # updates defaults IN PLACE
print(defaults)
