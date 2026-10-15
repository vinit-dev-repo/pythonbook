# nested_config_lab.py
import json
from collections import ChainMap
from pathlib import Path
from tempfile import TemporaryDirectory

def nested_overlay(overrides, defaults):
    if type(overrides) is not dict or type(defaults) is not dict:
        raise TypeError("configuration roots must be dictionaries")
    view = ChainMap({}, overrides, defaults)
    for key in overrides.keys() | defaults.keys():
        chosen = overrides[key] if key in overrides else defaults[key]
        if type(chosen) is dict:
            front = overrides.get(key, {})
            back = defaults.get(key, {})
            if type(back) is not dict:
                back = {}
            view.maps[0][key] = nested_overlay(front, back)
    return view

def read_config(directory, name):
    with (directory / f"{name}.json").open(encoding="utf-8") as stream:
        value = json.load(stream)
    if type(value) is not dict:
        raise ValueError("configuration file must contain an object")
    return value

fixtures = {
    "common": {"printer": {"copies": 1, "page": {"width": 210, "height": 297}}, "formats": ["pdf"]},
    "dev": {"printer": {"copies": 2, "page": {"width": 100}}, "formats": ["preview"]},
    "prod": {"printer": {"copies": 8}, "spool": True},
}
with TemporaryDirectory() as folder:
    directory = Path(folder)
    for name, payload in fixtures.items():
        (directory / f"{name}.json").write_text(json.dumps(payload), encoding="utf-8")
    common = read_config(directory, "common")
    dev = nested_overlay(read_config(directory, "dev"), common)
    prod = nested_overlay(read_config(directory, "prod"), common)
    print(dev["printer"]["copies"], dev["printer"]["page"]["width"], dev["printer"]["page"]["height"])
    print(prod["printer"]["copies"], prod["printer"]["page"]["width"], prod["spool"])
    print(dev["formats"])
    common["printer"]["page"]["height"] = 300
    print("live default:", dev["printer"]["page"]["height"])
    dev["printer"]["copies"] = 4
    print("local write:", dev["printer"]["copies"], common["printer"]["copies"])
    del dev["printer"]["copies"]
    print("fallback:", dev["printer"]["copies"])
