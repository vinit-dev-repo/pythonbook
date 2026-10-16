by_day = pd.DataFrame({"day": ["Mon", "Tue", "Wed"], "sales": [100, 150, 120]})
by_day = by_day.set_index("day")
print(by_day)
print(by_day.reset_index())
