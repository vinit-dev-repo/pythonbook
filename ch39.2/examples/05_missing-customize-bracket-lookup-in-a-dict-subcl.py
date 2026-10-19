class MissingLabelDict(dict):
    def __missing__(self, key):
        return f"<{key} missing>"

labels = MissingLabelDict(active="ready")
print(labels["active"])
print(labels["paused"])
print(labels.get("paused"))
print("paused" in labels)
