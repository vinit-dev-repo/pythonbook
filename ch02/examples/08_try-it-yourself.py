# 1
# python --version
# (Prints something like: Python 3.15.0)

# 2
# python
# >>> 144 / 12
# 12.0
# >>> exit()

# 3
# mkdir practice
# cd practice
# python -m venv .venv

# 4
# .venv\Scripts\Activate.ps1        (Windows)
# source .venv/bin/activate         (Mac/Linux)
# python -m pip install requests
# python -m pip list
# Installed names and versions depend on the selected environment.

# 5
# hello.py contains:
print("My workshop is ready!")
# Open a terminal whose current directory is first-run.
# Run with: python hello.py
# Output: My workshop is ready!

# 6
# Share source and pyproject.toml plus poetry.lock or uv.lock.
# For uv also share .python-version. Exclude .venv and secrets.
# pipx isolates a command-line tool; its libraries are not project dependencies.
