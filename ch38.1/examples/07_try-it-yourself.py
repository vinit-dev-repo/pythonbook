import ast
import io
import tokenize

# 1
source = 'print("first")\nprint("missing bracket"\n'
try:
    exec(compile(source, "<test>", "exec"))
except SyntaxError as error:
    print("SyntaxError before anything ran:", error.msg)

# 2
source = "x = [1,\n     2]\n"
for token in tokenize.generate_tokens(io.StringIO(source).readline):
    if token.type in (tokenize.NEWLINE, tokenize.NL):
        print(tokenize.tok_name[token.type], repr(token.string))

# 3
node = ast.parse("total = price * 3").body[0]
print(type(node).__name__, type(node.targets[0].ctx).__name__, type(node.value.op).__name__)

# 4
tree = ast.parse("return 1")
print("parsed:", type(tree.body[0]).__name__)
try:
    compile(tree, "<outside>", "exec")
except SyntaxError:
    print("compile: SyntaxError")
