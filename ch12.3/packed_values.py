# packed_values.py
from array import array
from pathlib import Path
from tempfile import TemporaryDirectory

readings = array("d", [1.25, -3.5, 6.0])
with TemporaryDirectory() as folder:
    path = Path(folder) / "readings.bin"
    with path.open("wb") as stream:
        readings.tofile(stream)
    restored = array(readings.typecode)
    with path.open("rb") as stream:
        restored.fromfile(stream, len(readings))
    print("same values:", restored == readings)
    print("expected byte count:", path.stat().st_size == len(readings) * readings.itemsize)
    partial = array(readings.typecode)
    with path.open("rb") as stream:
        try:
            partial.fromfile(stream, len(readings) + 1)
        except EOFError:
            print("short read retained:", partial.tolist())

raw = readings.tobytes()
rebuilt = array(readings.typecode)
rebuilt.frombytes(raw)
print("byte round trip:", rebuilt == readings)
rebuilt.byteswap()
rebuilt.byteswap()
print("two swaps restore bytes:", rebuilt.tobytes() == raw)
print("sorted copy:", array(readings.typecode, sorted(readings)).tolist())
