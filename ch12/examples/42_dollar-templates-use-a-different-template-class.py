from string import Template

message = Template("${name}: $count items; fee $$2")
print(message.substitute(name="West", count=6))
try:
    message.substitute(name="West")
except KeyError as error:
    print("missing:", error.args[0])
print(message.safe_substitute(name="West"))
