from django.apps import AppConfig


class DireccionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.direccion'
    
    def ready(self):
        import apps.direccion.signals  # Importar las señales de la aplicación correcta
