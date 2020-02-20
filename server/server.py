"""
Server module
"""

import uvicorn

from .app import configure_app
from .config import (
    APP_HOST,
    APP_PORT,
    LOG_LEVEL,
)


def main():
    """Run server."""
    app = configure_app()
    uvicorn.run(app, host=APP_HOST, port=APP_PORT, log_level=LOG_LEVEL)


if __name__ == '__main__':
    main()
