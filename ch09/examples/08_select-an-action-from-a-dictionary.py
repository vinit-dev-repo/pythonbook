def manifest_count(codes):
    return len(codes)

def manifest_line(codes):
    return ", ".join(codes)

actions = {"count": manifest_count, "line": manifest_line}
parcel_codes = ["K7", "M2", "K7"]
for command in ["line", "count", "remove"]:
    action = actions.get(command)
    if action is None:
        print(command, "unknown command")
    else:
        print(command, action(parcel_codes))
