renamed = sales.rename(columns={"units": "units_renamed"})
print("units_renamed" in renamed.columns, "units" in sales.columns)
smaller = sales.drop(columns=["price_band"])
sales["order_id"] = sales["order_id"].astype(str)   # change a column's dtype
print(sales["city"].str.upper().head(3))            # .str reaches string methods per row
sales["city"] = sales["city"].replace({"Nairobi": "NBO"})
sales["order_id"] = sales["order_id"].astype(int)
