import ast
import dis
import py_compile
from importlib.util import cache_from_source
from pathlib import Path

# 1
Path("mymodule.py").write_text('print("loading")\n', encoding="utf-8")
cached = cache_from_source("mymodule.py")
py_compile.compile("mymodule.py", doraise=True)
before = Path(cached).read_bytes()
Path("mymodule.py").write_text('print("loading")\nprint("a longer file now")\n', encoding="utf-8")
py_compile.compile("mymodule.py", doraise=True)
after = Path(cached).read_bytes()
print("cache file exists:", Path(cached).exists())
print("cache changed after the source changed:", after != before)

# 2
print(eval("2 ** 10"))
namespace = {}
exec("answer = 6 * 7", namespace)
print(namespace["answer"])
print(ast.literal_eval("[1, 2, {'three': 3}]"))
try:
    ast.literal_eval("__import__('os').getcwd()")
except ValueError:
    print("literal_eval rejects a call")

# 3
def seconds_in_a_day():
    return 24 * 60 * 60

print(86400 in seconds_in_a_day.__code__.co_consts)
print(any(item.opname == "BINARY_OP" for item in dis.get_instructions(seconds_in_a_day)))

# 4
plain = {}
exec("def f(x: int): pass", plain)
future = {}
exec("from __future__ import annotations\ndef f(x: int): pass", future)
print(plain["f"].__annotations__)
print(future["f"].__annotations__)
