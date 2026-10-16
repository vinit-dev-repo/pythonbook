big_london_orders = sales[(sales["city"] == "London") & (sales["units"] > 4)]
print(big_london_orders)
