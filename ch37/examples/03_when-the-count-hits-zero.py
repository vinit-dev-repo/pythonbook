class Greeting:
    def __init__(self, text):
        self.text = text
    def __del__(self):
        print(f"Goodbye from: {self.text}")

message = Greeting("hello")
message = "something else"      # the tag moves; refcount of Greeting object hits 0
