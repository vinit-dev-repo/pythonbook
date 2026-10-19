# report.py
# Final version
def category_total(rows, wanted):
    total = 0
    for row in rows:
        if row["category"] == wanted:
            total += row["quantity"]
    return total

def summarize_naive(rows, categories):
    return {category: category_total(rows, category) for category in categories}

def summarize_indexed(rows, categories):
    totals = {category: 0 for category in categories}
    for row in rows:
        category = row["category"]
        if category in totals:
            totals[category] += row["quantity"]
    return totals

if __name__ == "__main__":
    rows = [
        {"category": "books", "quantity": 2},
        {"category": "pens", "quantity": 7},
        {"category": "books", "quantity": 3},
    ]
    print(category_total(rows, "books"))
