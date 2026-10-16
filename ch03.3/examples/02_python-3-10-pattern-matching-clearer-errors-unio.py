def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On the x-axis at {x}"
        case (0, y):
            return f"On the y-axis at {y}"
        case (x, y):
            return f"Point at ({x}, {y})"

print(describe_point((0, 0)))
print(describe_point((5, 0)))
print(describe_point((3, 4)))
