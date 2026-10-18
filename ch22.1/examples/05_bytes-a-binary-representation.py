class Message:
    def __init__(self, text):
        self.text = text

    def __bytes__(self):
        return self.text.encode("utf-8")

message = Message("café")
encoded = bytes(message)
print(encoded)
print(type(encoded).__name__)
