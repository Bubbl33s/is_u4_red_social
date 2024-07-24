from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import usuarios.signals
