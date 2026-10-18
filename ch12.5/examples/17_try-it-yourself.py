from string import Template

layout = "{station}: {count} samples"
print(layout.format(station="West", count=6))      # West: 6 samples
print("{:>8.1f}".format(7.25))                     # "     7.2" (ties round to even)
message = Template("$name: $count samples")
print(message.substitute(name="West", count=6))    # West: 6 samples
