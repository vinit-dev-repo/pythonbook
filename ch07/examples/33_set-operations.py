python_fans = {"amara", "ravi", "sam"}
java_fans   = {"ravi", "lee", "priya"}

print(sorted(python_fans | java_fans))   # union
print(sorted(python_fans & java_fans))   # intersection
print(sorted(python_fans - java_fans))   # difference
print(sorted(python_fans ^ java_fans))   # symmetric difference
