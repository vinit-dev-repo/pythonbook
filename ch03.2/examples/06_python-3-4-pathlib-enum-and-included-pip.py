from pathlib import Path

config = Path("settings") / "app.toml"
print(config.as_posix())
print(config.suffix, config.stem)
