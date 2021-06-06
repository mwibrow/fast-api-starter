"""
Configuration
"""
import os

import toml


with open(os.path.join(os.path.dirname(__file__), "..", "pyproject.toml"), "r") as file_in:
    PYPROJECT = toml.loads(file_in.read())


APP_NAME = PYPROJECT["tool"]["poetry"]["name"]
APP_VERSION = PYPROJECT["tool"]["poetry"]["version"]
APP_HOST = os.environ.get("APP_HOST", "0.0.0.0")
APP_PORT = int(os.environ.get("APP_PORT", 8100))

LOG_LEVEL = "debug"
