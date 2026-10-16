# 1
subscribed = {"news", "sports"}
available = {"news", "sports", "weather", "tech"}
print(sorted(available - subscribed))  # ['tech', 'weather'] - sorted() so the order is fixed

# 2
visits = ["home", "about", "home", "contact", "about"]
ordered_unique = list(dict.fromkeys(visits))
print(ordered_unique)                  # ['home', 'about', 'contact']

# 3
monday = {"Amy", "Ben", "Cara"}
tuesday = {"Ben", "Dan"}
print(sorted(monday & tuesday))        # ['Ben'] - both days
print(sorted(monday - tuesday))        # ['Amy', 'Cara'] - only Monday

# 4
# {1, [1, 2]} raises TypeError: cannot use 'list' as a set element (unhashable type: 'list').
# A set stores elements in a hash table, so every element must be hashable.
# Lists are mutable, so Python refuses to hash them - the same rule as dict keys.

# 5
roles = frozenset({"admin", "editor"})
descriptions = {roles: "Can manage and publish content"}
print(descriptions[frozenset({"admin", "editor"})])
