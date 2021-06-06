"""
Server module
"""

import hupper
import uvicorn


from .app import get_app
from .config import APP_HOST, APP_PORT, LOG_LEVEL


def run():
    """Run server."""
    app = get_app()

    try:
        uvicorn.run(app, host=APP_HOST, port=APP_PORT, log_level=LOG_LEVEL)
    except KeyboardInterrupt:

        pass


def watch():
    """Watch files/"""
    reloader = hupper.start_reloader("app.server.run")

    reloader.watch_files(["app/**/*.py"])


if __name__ == "__main__":
    run()
