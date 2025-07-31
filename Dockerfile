FROM python:3.12-alpine

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