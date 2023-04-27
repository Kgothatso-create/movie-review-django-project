from django.shortcuts import render, redirect
from .models import MovieChat
from .form import MovieChatForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# The login_required decorator to ensure only logged-in users can access this view
@login_required(login_url ='login')
def movie_chat_view(request):
    """
    Display a form to allow users to submit a movie chat message and display all movie chat messages.

    :param request: The HTTP request object.
    :type request: ~django.http.HttpRequest
    :return: The rendered HTML template for the movie chat page.
    :rtype: ~django.http.HttpResponse
    """
    form = MovieChatForm()
    movie_chats = MovieChat.objects.all() # Fetch all MovieChat objects from the database
    if request.method == 'POST':
        # If form is submitted
        form = MovieChatForm(request.POST)
        if form.is_valid():
            # If form data is valid
            username = form.cleaned_data['username']
            movie_chat = form.cleaned_data['movie_chat']
            # Create and save a new MovieChat object
            movie_chat_obj = MovieChat(username=username, movie_chat=movie_chat)
            movie_chat_obj.save()
           
            return redirect('moviechat')
    else:  
        
        return render(request, 'moviechat.html', {'form': form, 'movie_chats': movie_chats})

