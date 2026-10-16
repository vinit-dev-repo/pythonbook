class LookupRobot:
    def __str__(self):
        return "type method"

robot = LookupRobot()
robot.__str__ = lambda: "instance attribute"
print(robot.__str__())
print(str(robot))
