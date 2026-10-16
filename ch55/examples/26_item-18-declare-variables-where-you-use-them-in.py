for i in range(3):
    pass
print(i)          # the loop variable leaks past the loop

try:
    raise ValueError("boom")
except Exception as e:
    print("inside:", e)

try:
    print(e)      # Python deletes 'e' when the except block ends
except NameError as err:
    print("after the block:", err)
