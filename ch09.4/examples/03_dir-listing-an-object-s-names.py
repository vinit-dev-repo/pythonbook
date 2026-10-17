public = [name for name in dir("hello") if not name.startswith("_")]

print(len(public), "public string methods")
print(public[:8])
