import itertools

daily_sales = [100, 150, 80, 200]
running_total = itertools.accumulate(daily_sales)
print(list(running_total))
