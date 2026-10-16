class Badge:
    def __init__(self, label, level):
        self.label = label
        self.level = level

badge = Badge("new", 1)
print(badge.label, badge.level)
