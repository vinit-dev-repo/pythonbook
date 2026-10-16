import ast

print(ast.literal_eval("[1, 2, {'three': 3}]"))
print(ast.literal_eval("__import__('os').getcwd()"))
