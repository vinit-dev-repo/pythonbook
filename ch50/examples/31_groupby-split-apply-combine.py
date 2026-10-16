print(sales.groupby("city")["units"].agg(["mean", "sum", "count"]))
