# pylint: disable=missing-docstring
from django.apps import AppConfig


class Example1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "example1"
