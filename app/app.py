"""
Configure app
"""
from fastapi import FastAPI

import asyncio


class Application(FastAPI):
    """Application class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_event_handler('startup', self.startup)
        self.add_event_handler('shutdown', self.shutdown)

    async def startup(self):
        """Start up."""
        for i in range(10):
            print('start', i)
            await asyncio.sleep(0.5)

    async def shutdown(self):
        """Shutdown."""
        for i in range(10):
            print('stop', i)
            await asyncio.sleep(0.5)


def get_app():
    """Configure application."""
    app = Application()

    @app.get('/')
    async def root():
        return {'message': 'Hello World'}

    return app
