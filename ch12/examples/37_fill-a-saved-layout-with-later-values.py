layout = "{station}: {count} samples"
print(layout.format(station="West", count=6))
print(layout.format(station="East", count=9))
print("{1} follows {0}; {1} stops".format("read", "write"))
print("{} / {}".format("read", "write"))
