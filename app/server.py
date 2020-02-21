"""
Server module
"""
import hupper
import uvicorn

from .app import get_app
from .config import Config


def run():
    """Run server."""
    app = get_app()
    uvicorn.run(app, host=Config.APP_HOST, port=Config.APP_PORT, log_level=Config.LOG_LEVEL)


def watch():
    """Watch files/"""
    reloader = hupper.start_reloader('app.server.run')

    # monitor an extra file
    reloader.watch_files(['app/**/*.py'])


if __name__ == '__main__':
    run()
