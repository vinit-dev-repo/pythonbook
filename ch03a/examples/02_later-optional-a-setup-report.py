import sys

print("interpreter:", sys.executable)
print("version:", ".".join(str(n) for n in sys.version_info[:3]))
print("in a virtual environment:", sys.prefix != sys.base_prefix)
try:
    import requests
    print("requests: available")
except ImportError:
    print("requests: import failed in this interpreter")
