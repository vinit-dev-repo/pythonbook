latin1_source = b'# coding: latin-1\nword = "caf\xe9"\n'
namespace = {}
exec(compile(latin1_source, "<latin1>", "exec"), namespace)
print(ascii(namespace["word"]))

bad_source = b'word = "caf\xe9"\n'
try:
    compile(bad_source, "<default-utf8>", "exec")
except SyntaxError as error:
    print(type(error).__name__)
