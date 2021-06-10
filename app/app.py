"""
Configure app
"""
from typing import Awaitable, Callable
from fastapi import FastAPI
from .config import APP_NAME, APP_VERSION


def get_app() -> FastAPI:
    """Configure application."""
    app = FastAPI()
    app.add_event_handler("startup", on_startup(app))
    app.add_event_handler("shutdown", on_shutdown())

    app.get("/status")(status)

    return app


def on_startup(app: FastAPI) -> Callable[[], Awaitable[None]]:
    """Return a handler executed when the `startup` event is triggered."""

    async def startup():
        """Do something on start up."""
        app.state.some_attribte = None

    return startup


def on_shutdown() -> Callable[[], Awaitable[None]]:
    """Return a handler executed when the `shutdown` event is triggered."""

    async def shutdown():
        """Do something on shutdown."""

    return shutdown


async def status():
    """Status handler."""
    return {"app": APP_NAME, "version": APP_VERSION, "message": "healthy"}
