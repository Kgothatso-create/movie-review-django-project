from django import forms
from .models import MovieChat

class MovieChatForm(forms.ModelForm):
    class Meta:
        model = MovieChat
        fields = ['username', 'movie_chat']
        widgets = {
            'username': forms.TextInput(attrs={'max_length': 100, 'required': True}),
            'movie_chat': forms.Textarea(attrs={'max_length': 500, 'required': True}),
        }
