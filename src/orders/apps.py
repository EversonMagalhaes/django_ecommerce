from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
    # Importa o arquivo signals.py para garantir que os receivers sejam conectados
        import orders.signals