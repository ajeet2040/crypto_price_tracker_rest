from django.apps import AppConfig


class PriceTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'price_tracker'

    def ready(self):
        from price_tracker.scheduler import start_job
        start_job()