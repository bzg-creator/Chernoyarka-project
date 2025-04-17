from django.apps import AppConfig

class ZonesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zones_app'

    def ready(self):
        import zones_app.signals
