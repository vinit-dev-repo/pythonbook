# array_file_worker.py
import sys
import numpy as np

mode, path = sys.argv[1:]
if mode not in {"r", "c", "r+"}:
    raise ValueError("choose r, c or r+")
mapped = np.load(path, mmap_mode=mode, allow_pickle=False)
if mapped.shape != (3, 2) or mapped.dtype != np.dtype("float64"):
    raise ValueError("expected three pairs of float64 readings")

if mode == "r":
    try:
        mapped[0, 1] = 99.0
    except ValueError:
        print("r: write rejected")
    else:
        raise AssertionError("read-only write succeeded")
else:
    mapped[:, 1] += 0.5
    mapped.flush()
    print(mode + ": " + str(mapped[:, 1].tolist()))
