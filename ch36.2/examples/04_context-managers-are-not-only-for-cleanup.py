import contextlib
import io

# 1. Temporarily send print() output somewhere else
buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    print("this goes into the buffer, not the screen")

print("captured:", buffer.getvalue().strip())
