class Message:
    def store(self, value):
        """Store a value; this is the setter's own documentation."""
        self._text = value

    def fetch(self):
        """Read the stored text."""
        return self._text

    incoming = property(fset=store, doc="Assign incoming text.")
    text = property(fget=fetch)

message = Message()
message.incoming = "ready"
print(message.text)
try:
    print(message.incoming)
except AttributeError as error:
    print(type(error).__name__)
print(Message.incoming.__doc__)
print(Message.text.__doc__)
