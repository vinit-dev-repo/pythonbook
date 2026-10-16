commands = {}

def command(name, *, enabled=True):
    def decorate(func):
        if enabled:
            if name in commands:
                raise ValueError("duplicate command name")
            commands[name] = func
        return func
    return decorate

@command("status")
def status():
    return "ready"

@command("preview", enabled=False)
def preview():
    return "draft"

print(sorted(commands))
print(commands["status"] is status)
print(commands["status"]())
print(preview())
try:
    command("status")(preview)
except ValueError:
    print("duplicate rejected")
print(commands["status"] is status)
