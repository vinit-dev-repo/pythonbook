events = []

def trace(label):
    events.append("evaluate " + label)
    def decorate(func):
        events.append("apply " + label)
        def wrapper():
            events.append("enter " + label)
            result = func()
            events.append("leave " + label)
            return result
        return wrapper
    return decorate

@trace("outer")
@trace("inner")
def work():
    events.append("body")
    return 7

print(events)
events.clear()
print(work())
print(events)
