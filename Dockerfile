FROM python:3.14-alpine@sha256:faee120f7885a06fcc9677922331391fa690d911c020abb9e8025ff3d908e510

WORKDIR /app

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

RUN apk add --no-cache build-base jpeg-dev zlib-dev libpng-dev

COPY . .

RUN uv sync --locked

EXPOSE 8000

CMD ["uv", "run", "python", "src/server.py"]