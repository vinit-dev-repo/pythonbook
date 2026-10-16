import sys

print("switch interval (seconds):", sys.getswitchinterval())
print("GIL enabled:", sys._is_gil_enabled() if hasattr(sys, "_is_gil_enabled") else "n/a on this build")
