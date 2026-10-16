def category_total(rows, wanted):
    total = 0
    for row in rows:
        if row["category"] == wanted:
            total += row["quantity"]
    return total
