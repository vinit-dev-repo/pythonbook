ALLOWED_SORT = {"name", "price"}

def sort_query(user_choice):
    column = user_choice if user_choice in ALLOWED_SORT else "name"
    # safe: `column` can only ever be one of OUR two words
    return f"SELECT * FROM products ORDER BY {column}"

print(sort_query("price"))
print(sort_query("price; DROP TABLE products--"))
