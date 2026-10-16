with open("dispatch.data", "w", encoding="utf-8", newline="") as file:
    result = print("ready", 3, sep=":", file=file, flush=True)
print("return:", result)
with open("dispatch.data", encoding="utf-8") as file:
    print("saved:", repr(file.read()))
print("back on standard output")
