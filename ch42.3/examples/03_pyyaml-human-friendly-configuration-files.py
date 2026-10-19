import yaml
from yaml.constructor import ConstructorError

print(yaml.safe_load("") is None)
print(type(yaml.safe_load("when: 2000-05-01")["when"]).__name__)
try:
    yaml.safe_load("!!python/object:builtins.object {}")
except ConstructorError:
    print("python object tag refused:", True)
else:
    raise AssertionError("SafeLoader accepted a Python object tag")
