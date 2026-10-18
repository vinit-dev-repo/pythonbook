# path_file_lab.py
from pathlib import Path
import site
import sys
import tempfile

with tempfile.TemporaryDirectory() as folder:
    root = Path(folder)
    library = root / "library"
    library.mkdir()
    (root / "lesson.pth").write_text(
        "# local experiment\nlibrary\nlibrary\nmissing\n"
        "import sys; print('path hook runs')\n", encoding="utf-8")
    before = list(sys.path)
    try:
        sys.path.append(str(root))
        print("after append:", str(library) in sys.path)
        site.addsitedir(str(root))
        print("after site:", str(library) in sys.path)
        print("copies:", sys.path.count(str(library)))
        print("missing added:", str(root / "missing") in sys.path)
    finally:
        sys.path[:] = before
