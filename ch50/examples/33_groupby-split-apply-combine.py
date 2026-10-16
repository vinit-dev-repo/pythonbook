print(sales.groupby(["city", "product"])["units"].sum())
