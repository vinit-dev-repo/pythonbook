from collections import OrderedDict

d = OrderedDict()
d["first"] = 1
d["second"] = 2
d["third"] = 3

d.move_to_end("first")           # move a key to the back
print(d)

d.popitem(last=False)            # remove and return the FRONT item
print(d)
