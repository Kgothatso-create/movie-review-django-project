from django.db import models

# Create your models here.
class MovieChat(models.Model):
    """
    A model class to represent a movie chat object in the database.
    Returns a string representation of the MovieChat object.
    """
    username = models.CharField(max_length=100)
    movie_chat = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.username} {self.movie_chat}'
