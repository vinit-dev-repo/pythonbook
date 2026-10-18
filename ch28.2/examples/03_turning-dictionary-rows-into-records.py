from collections import namedtuple

Record = namedtuple("Record", "name score")
first = {"name": "Ada", "score": 10}
reordered = {"score": 20, "name": "Grace"}

wrong = Record(*reordered.values())
right = Record(**reordered)
print("first name:", Record(**first).name)
print("fields:", Record._fields)
print("wrong:", wrong)
print("right score:", right.score)
