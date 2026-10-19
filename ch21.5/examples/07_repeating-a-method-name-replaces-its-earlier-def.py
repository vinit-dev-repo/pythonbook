class RepeatedFormatter:
    def caption(self, label):
        return label

    def caption(self, label, detail):
        return f"{label}: {detail}"


broken = RepeatedFormatter()
try:
    broken.caption("dock")
except TypeError:
    print("the one-argument version was replaced")
print(broken.caption("dock", "ready"))


class FlexibleFormatter:
    def caption(self, label, detail=None):
        return label if detail is None else f"{label}: {detail}"


fixed = FlexibleFormatter()
print(fixed.caption("dock"))
print(fixed.caption("dock", "ready"))
