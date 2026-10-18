incoming = []
outgoing = []
make_callback = lambda destination: lambda message="ready": destination.append(message)
receive = make_callback(incoming)
send = make_callback(outgoing)

print("before calls:", incoming, outgoing)
receive()
send("sent")
original_incoming = incoming
incoming = []
receive("again")
print("captured list:", original_incoming)
print("new list:", incoming)
print("other callback:", outgoing)
