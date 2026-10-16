# Bad style — a comprehension used only for its side effect, the result is thrown away
[print(n) for n in [1, 2, 3]]

# Good style — just loop
for n in [1, 2, 3]:
    print(n)
