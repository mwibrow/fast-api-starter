"""
Configuration
"""
import os


class Config:
    """Configuration class."""

    APP_HOST = os.environ.get("APP_HOST", "0.0.0.0")
    APP_PORT = os.environ.get("APP_PORT", 8100)

    LOG_LEVEL = "debug"
