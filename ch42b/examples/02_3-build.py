import json
from datetime import datetime
from pathlib import Path

def save_profile(profile, path):
    payload = {
        "name": profile["name"],
        "joined": profile["joined"].isoformat(),   # dates go out as ISO text
        "tags": sorted(profile["tags"]),           # sets go out as a SORTED list
    }
    Path(path).write_text(json.dumps(payload), encoding="utf-8")

def load_profile(path):
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    return {
        "name": raw["name"],
        "joined": datetime.fromisoformat(raw["joined"]),
        "tags": set(raw["tags"]),
    }

original = {"name": "Amara", "joined": datetime(2026, 3, 1, 9, 30), "tags": {"admin", "beta"}}
save_profile(original, "profile.json")
loaded = load_profile("profile.json")
print(loaded == original)
print(loaded["tags"] == original["tags"], type(loaded["joined"]).__name__)
