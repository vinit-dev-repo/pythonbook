print(sales.sort_values("price", kind="stable"))
print(sales.sort_values(["city", "units"], ascending=[True, False]))
print(sales.nlargest(2, "price"))
print(sales.nsmallest(2, "units"))
