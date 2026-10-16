sales = pd.read_csv("sales.csv")
print(sales.groupby("city")["price"].mean())
