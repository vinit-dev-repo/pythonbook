limited = GoodLowerDict()
limited["ZONE"] = 4
limited.update({"AREA": 6})
limited |= {"ZONE": 9}
print(dict(limited))
print(limited["zone"], limited["ZONE"])
print("AREA" in limited, "area" in limited)
