import os
import subprocess
import sys
import logging
from decouple import config


# Django fixture
def start():

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", config("DJANGO_SETTINGS_MODULE"))
    try:
        import django

        django.setup()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    collectstatic_command = [
        "django-admin",
        "collectstatic",
        "--noinput",
    ]
    gunicorn_command = [
        "gunicorn",
        "--workers",
        f"{config('WEBSERVER_WORKERS')}",
        "--bind",
        f"0.0.0.0:{config('WEBSERVER_PORT')}",
        "src.wsgi:application",
    ]

    print(f"Running command: {' '.join(gunicorn_command)}")

    try:
        subprocess.run(collectstatic_command, check=True)
        subprocess.run(gunicorn_command, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred: {e}", file=sys.stderr)


def dev():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", config("DJANGO_SETTINGS_MODULE"))
    collectstatic_command = [
        "django-admin",
        "collectstatic",
        "--noinput",
    ]
    try:
        subprocess.run(collectstatic_command, check=True)
        subprocess.run(["django-admin", "runserver", "0.0.0.0:8080"], check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred: {e}", file=sys.stderr)


def worker():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", config("DJANGO_SETTINGS_MODULE"))
    try:
        subprocess.run(
            ["celery", "-A", "config", "worker", "--loglevel=info"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred: {e}")
