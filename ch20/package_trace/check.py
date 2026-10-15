# package_trace/check.py
import sys
import myapp.utils.numbers

print(myapp.utils.numbers.shout_number(42))
print("caller:", "myapp" in globals(), "numbers" in globals())
print("cached:", sorted(name for name in sys.modules if name == "myapp" or name.startswith("myapp.")))
print("parent link:", myapp.utils.numbers is sys.modules["myapp.utils.numbers"])
print("unused cached:", "myapp.utils.unused" in sys.modules)
for module in (myapp, myapp.utils, myapp.utils.numbers):
    spec = module.__spec__
    print(spec.name, spec.parent, spec.submodule_search_locations is not None)
