# manual_namespace/check_failure.py
import sys
from loader import prepare, run_registered

name = "lesson_broken"
caller = {}
try:
    code = prepare("def broken(:\n    pass\n", name)
    caller["lesson"] = run_registered(name, code)
except SyntaxError:
    print("compile failure:", name in sys.modules, "lesson" in caller)

source = "created = 1\nraise ValueError('body failed')\n"
try:
    code = prepare(source, name)
    caller["lesson"] = run_registered(name, code)
except ValueError:
    print("execution failure:", name in sys.modules, "lesson" in caller)
