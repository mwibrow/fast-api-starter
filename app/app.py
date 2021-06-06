"""
Configure app
"""
from fastapi import FastAPI
from .config import APP_NAME, APP_VERSION


class Application(FastAPI):
    """Application class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_event_handler("startup", self.startup)
        self.add_event_handler("shutdown", self.shutdown)

    async def startup(self):
        """Start up."""

    async def shutdown(self):
        """Shutdown."""


def get_app() -> FastAPI:
    """Configure application."""
    app = Application()

    @app.get("/status")
    async def status():
        return {"app": APP_NAME, "version": APP_VERSION, "message": "healthy"}

    return app
