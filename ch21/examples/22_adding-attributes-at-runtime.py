class Badge:
    labels = ["new"]

class_view = vars(Badge)
Badge.kind = "member"
print(class_view["kind"])
try:
    class_view["kind"] = "admin"
except TypeError as error:
    print(type(error).__name__)
class_view["labels"].append("featured")
print(Badge.labels)
