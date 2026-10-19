renamed_input = pd.read_csv(
    "sales.csv", header=0,
    names=["id", "place", "item", "quantity", "unit_price"],
)
print(renamed_input.shape)
print(renamed_input.columns.tolist())
