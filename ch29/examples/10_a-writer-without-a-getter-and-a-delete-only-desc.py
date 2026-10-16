class WriteOnly:
    def __set__(self, instance, value):
        instance.__dict__["last_write"] = value

class DeleteOnly:
    def __delete__(self, instance):
        instance.__dict__.pop("removable", None)

class Channel:
    outgoing = WriteOnly()
    removable = DeleteOnly()

channel = Channel()
assert channel.outgoing is Channel.outgoing
channel.__dict__["outgoing"] = "local read"
channel.outgoing = "sent"
print(channel.outgoing, channel.last_write)
channel.__dict__["removable"] = "local value"
try:
    channel.removable = "replacement"
except AttributeError:
    print("delete-only assignment refused")
print(channel.removable)
del channel.removable
print(channel.removable is Channel.removable)
