from django.apps import AppConfig


class CommentsConfig(AppConfig):
    """
    Configuration class for the `comments` app.

    Attributes:
        default_auto_field (str): The name of the auto-generated primary key field.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'
