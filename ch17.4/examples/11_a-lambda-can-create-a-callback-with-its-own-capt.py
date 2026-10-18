def make_receiver(destination):
    def receive(message="ready"):
        destination.append(message)
    return receive

delivered = []
handler = make_receiver(delivered)
pending = [lambda: handler("opened"), lambda: handler("closed")]
print("registered:", delivered)
for action in pending:
    action()
print("dispatched:", delivered)
