jobs = {"scan": [1], "send": [2]}
live = jobs.keys()
snapshot = list(live)
preview = jobs.copy()
preview["scan"].append(3)
preview["send"] = [9]
print(jobs["scan"], jobs["send"])
del jobs["scan"]
jobs["scan"] = [4]
print(list(live))
print(snapshot)
