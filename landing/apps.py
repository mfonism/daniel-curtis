from django.apps import AppConfig


class LandingConfig(AppConfig):
    name = "landing"

    def ready(self):
        from . import signals  # noqa

        super().ready()
