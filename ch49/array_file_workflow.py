# array_file_workflow.py
from pathlib import Path
import subprocess
import sys
import tempfile
import numpy as np

worker = Path(__file__).with_name("array_file_worker.py")
original = np.array([[0.0, 1.25], [1.0, 2.5], [2.0, 3.75]])
with tempfile.TemporaryDirectory() as folder:
    text_path = Path(folder) / "readings.txt"
    array_path = Path(folder) / "readings.npy"
    np.savetxt(text_path, original, fmt="%.2f")
    from_text = np.loadtxt(text_path, dtype="float64")
    assert np.array_equal(from_text, original)
    np.save(array_path, from_text, allow_pickle=False)
    restored = np.load(array_path, allow_pickle=False)
    print("restored:", restored.shape, restored.dtype)

    for mode in ("r", "c", "r+"):
        result = subprocess.run(
            [sys.executable, str(worker), mode, str(array_path)],
            check=True, capture_output=True, text=True,
        )
        print(result.stdout.strip())
        on_disk = np.load(array_path, allow_pickle=False)
        expected = original.copy()
        if mode == "r+":
            expected[:, 1] += 0.5
        assert np.array_equal(on_disk, expected)
        print("disk:", on_disk[:, 1].tolist())
    assert original[:, 1].tolist() == [1.25, 2.5, 3.75]
