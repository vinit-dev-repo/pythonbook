import pytest

@pytest.fixture
def cleanup_observer():
    state = {"file": None, "events": []}
    yield state
    file = state["file"]
    if file is None:
        return
    print(state["case"], "closed before observer:", file.closed)
    print(state["case"], "events:", state["events"])
    try:
        assert file.closed is state["expected_closed"]
        assert state["events"] == state["expected_events"]
    finally:
        file.close()  # closes the intentionally leaked file after observing it

@pytest.fixture
def yield_only(cleanup_observer, tmp_path):
    state = cleanup_observer
    state["case"] = "yield-only"
    state["expected_closed"] = False
    state["expected_events"] = ["opened"]
    file = open(tmp_path / "yield-only.txt", "w", encoding="utf-8")
    state["file"] = file
    state["events"].append("opened")
    raise RuntimeError("setup stopped before yield")
    yield file
    file.close()
    state["events"].append("closed")

@pytest.fixture
def registered_cleanup(cleanup_observer, tmp_path, request):
    state = cleanup_observer
    state["case"] = "registered"
    state["expected_closed"] = True
    state["expected_events"] = ["opened", "closed"]
    file = open(tmp_path / "registered.txt", "w", encoding="utf-8")
    state["file"] = file
    state["events"].append("opened")

    def close_file():
        file.close()
        state["events"].append("closed")

    request.addfinalizer(close_file)
    raise RuntimeError("setup stopped after registering cleanup")
    return file

def test_yield_only_stops_before_test(yield_only):
    raise AssertionError("This test body should not run")

def test_registered_stops_before_test(registered_cleanup):
    raise AssertionError("This test body should not run")
