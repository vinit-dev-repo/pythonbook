n = 10
before = id(n)
n = n + 1                  # 10 is unchanged; bind n to the result, 11
print("same object as before?", id(n) == before)
