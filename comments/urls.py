from django.urls import path
from .views import movie_chat_view

urlpatterns = [
    path('', movie_chat_view, name='moviechat'),
]
