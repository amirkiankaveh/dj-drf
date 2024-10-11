ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as base

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app



# Copy the source code into the container.
COPY . .
RUN python -m pip install poetry
RUN poetry install

# Expose the port that the application listens on.
EXPOSE 8080

CMD [ "poetry", "run", "start" ]

