from django.apps import AppConfig


class TagsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tags'

    def ready(self):
        # AQUI É ONDE SEU SIGNALS.PY É GARANTIDO DE SER CARREGADO
        import tags.signals

