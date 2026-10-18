# import_practice/check_nested.py
import nested_module
import nested_from

for client in (nested_module, nested_from):
    print(client.__name__, "library" in client.__dict__, "label_pair" in client.__dict__)
print(nested_module.library.label_pair("red", "blue"))
print(nested_from.label_pair("red", "blue"))
