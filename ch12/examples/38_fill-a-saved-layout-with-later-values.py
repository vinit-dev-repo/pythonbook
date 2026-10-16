import sys

record = {"name": "West", "count": 6}
print("{row[name]} runs Python {runtime.version_info.major}".format(row=record, runtime=sys))
print("{name}: {count}".format(**record))
print("{{{0[1]}}}".format(["red", "green"]))
