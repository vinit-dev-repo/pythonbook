try:
    "€".encode("ascii")
except UnicodeEncodeError as e:
    print("UnicodeEncodeError:", e)
