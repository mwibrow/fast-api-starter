"""
Configure app
"""
from fastapi import FastAPI


def configure_app():
    """Configure application."""
    app = FastAPI()

    @app.get('/')
    async def root():
        return {'message': 'Hello World'}

    return app
