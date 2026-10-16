from delegate_record import Client, ClientView

target = Client("Noor")
view = ClientView(target)
view.name = "label"
target.name = "Iris"
print(view.name)
print(view.greet())
print(target.name)
print(repr(view))
