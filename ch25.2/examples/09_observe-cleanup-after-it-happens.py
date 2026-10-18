import pytest

@pytest.fixture
def lifecycle():
    state = {"file": None, "events": []}
    yield state
    file = state["file"]
    if file is None:
        return
    print("closed after resource teardown:", file.closed)
    print("events:", state["events"])
    try:
        assert file.closed
        assert state["events"] == ["opened", "test", "closed"]
    finally:
        file.close()  # rescue cleanup if the observed fixture was broken

@pytest.fixture
def tracked_log_file(lifecycle, tmp_path):
    file = open(tmp_path / "log.txt", "w", encoding="utf-8")
    lifecycle["file"] = file
    lifecycle["events"].append("opened")
    yield file
    file.close()
    lifecycle["events"].append("closed")

def test_write_then_close(tracked_log_file, lifecycle):
    lifecycle["events"].append("test")
    tracked_log_file.write("started\n")
    assert not tracked_log_file.closed
