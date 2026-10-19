class Button:
    def __init__(self):
        self.listeners = []
    def on_click(self, fn):
        self.listeners.append(fn)
    def forget(self, fn):
        self.listeners.remove(fn)

class Screen:
    def __init__(self, data):
        self.data = data
    def handle(self):
        pass

button = Button()
screen = Screen(["a lot of data"] * 1000)
button.on_click(screen.handle)
print("listeners still held:", len(button.listeners))

button.forget(screen.handle)
print("after forgetting:", len(button.listeners))
