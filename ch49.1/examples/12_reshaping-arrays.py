try:
    flat.reshape(5, 5)   # 12 numbers can't fill 25 slots
except ValueError as e:
    print("Error:", e)
