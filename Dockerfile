FROM python:3.9-slim
LABEL MAINTAINER "Mark Wibrow"

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.6

RUN pip install poetry==${POETRY_VERSION}

RUN adduser --system app
RUN mkdir -p /usr/src/app
RUN chown app /usr/src/app
WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml /usr/src/app/
RUN poetry env use system && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
USER app

COPY . /usr/src/app
