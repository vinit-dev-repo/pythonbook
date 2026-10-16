import ast

tree = ast.parse("return 1")
print("parsed:", type(tree.body[0]).__name__)
try:
    compile(tree, "<outside-function>", "exec")
except SyntaxError:
    print("compile: SyntaxError")
