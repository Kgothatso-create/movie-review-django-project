from django.apps import AppConfig


class MovieZoneConfig(AppConfig):
    """
    This class represents the configuration for the 'movie_zone' app.
    It sets the default auto field to a big integer field and specifies the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie_zone'
