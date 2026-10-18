# cleanup_unittest_demo.py
import tempfile
import unittest

class OpenThenFail(unittest.TestCase):
    def setUp(self):
        self.events = []
        self.file = tempfile.TemporaryFile(mode="w+", encoding="utf-8")
        self.events.append("opened")
        self.addCleanup(self.close_file)
        raise RuntimeError("deliberate setup failure")

    def close_file(self):
        self.file.close()
        self.events.append("closed")

    def tearDown(self):
        self.events.append("tearDown")

    def test_body(self):
        self.events.append("test")
        self.fail("test body should not run")

if __name__ == "__main__":
    case = OpenThenFail("test_body")
    result = unittest.TestResult()
    case.run(result)
    try:
        print("setup errors:", len(result.errors))
        print("assertion failures:", len(result.failures))
        print("closed before rescue:", case.file.closed)
        print("events:", case.events)
        assert len(result.errors) == 1 and not result.failures
        assert "RuntimeError: deliberate setup failure" in result.errors[0][1]
        assert case.file.closed
        assert case.events == ["opened", "closed"]
    finally:
        case.file.close()  # rescue only after inspecting the state
