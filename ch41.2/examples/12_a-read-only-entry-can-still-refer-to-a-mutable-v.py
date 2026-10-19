source = {"labels": ["new"]}
public = MappingProxyType(source)
public["labels"].append("checked")
print(source["labels"], public["labels"] is source["labels"])
try:
    public["labels"] = []
except TypeError:
    print("entry assignment blocked")
print(source["labels"])
