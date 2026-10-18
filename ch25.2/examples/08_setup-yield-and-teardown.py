import pytest

@pytest.fixture
def open_log_file(tmp_path):
    path = tmp_path / "log.txt"
    file = open(path, "w", encoding="utf-8")
    yield file                 # the test runs here, using `file`
    file.close()                # teardown after pytest resumes this fixture

def test_can_write_to_log(open_log_file):
    open_log_file.write("started\n")
    assert not open_log_file.closed
