sales["price_band"] = sales["price"].apply(lambda p: "cheap" if p < 15 else "pricey")
print(sales[["price", "price_band"]])
