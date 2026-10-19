import pathlib
pathlib.Path("greeter.py").write_text(
    'print("greeter.py is running its top-level code")\n'
    '\n'
    'def greet(name):\n'
    '    return f"Hello, {name}"\n'
)
print("wrote greeter.py")
