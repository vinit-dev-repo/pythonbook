import math
import subprocess
import sys
from math import sqrt
from timeit import repeat

# 1
source = "base = 20\ndef total(v):\n    return base + v\n"
code = compile(source, "<lesson>", "exec")
namespace = {}
exec(code, namespace)
print(namespace["total"](22))                  # 42
namespace["base"] = 30
print(namespace["total"](22))                  # 52

# 2
for function in (lambda: math.sqrt(81), lambda: sqrt(81)):
    print(repeat(function, number=20000, repeat=3))

# 3
result = subprocess.run([sys.executable, "-I", "-c", "import sys; print(sys.flags.isolated)"],
                        capture_output=True, text=True, check=True)
print(result.stdout.strip())                   # 1
