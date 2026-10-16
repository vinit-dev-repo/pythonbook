by_city = sales.set_index("city")

print(by_city.loc["Tokyo"])       # rows labelled "Tokyo"
print(sales.iloc[0])              # the row at position 0
print(sales.iloc[0, 2])           # row 0, column at position 2
print(sales.loc[0, "product"])    # row labelled 0, column "product"
