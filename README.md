# FastAPI starter

Simple starter using [FastAPI](https://fastapi.tiangolo.com/) and [uvicorn](https://www.uvicorn.org/)
inside [docker](https://www.docker.com/).

Uses [hupper](https://docs.pylonsproject.org/projects/hupper/en/latest/)
and [Watchdog](https://pythonhosted.org/watchdog/) to restart
the server when source-code changes.

## Usage

Simply run `docker-compose up -d --build server` at the project root.
