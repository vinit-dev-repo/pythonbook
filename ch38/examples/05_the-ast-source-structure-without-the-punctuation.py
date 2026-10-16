import ast

source = "total = price * 3\nprint(total)\n"
tree = ast.parse(source)
print(ast.dump(tree, indent=2))
