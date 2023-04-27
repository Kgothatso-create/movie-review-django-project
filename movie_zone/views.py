from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .form import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 

# Create your views here.
def index(request):
    return render(request, 'index.html')


# Creating user authentication views here.
# User register view
def register(request):
    """
    A view function that handles user registration.

    If the request method is 'POST', this function validates the form data,
    checks if the username already exists in the database, and creates a new user
    object with the given credentials. If the user is successfully registered,
    they are redirected to the index page with a success message. If the form is
    invalid or the registration is unsuccessful, an error message is displayed.
    
    If the request method is 'GET', this function instantiates a new form and renders
    the registration page with the form.

    Args:
        request (HttpRequest): The HTTP request object sent by the user.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template
        with the form, success message, or error message, depending on the status
        of the registration process.
    """
    form = NewUserForm()  # Instantiate the form
    if request.method == 'POST':

        # Handle form submission
        form = NewUserForm(request.POST)
        if form.is_valid():

             # Process form data and save user
            first_name = form.cleaned_data['first_name']
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

        # Check if the username already exists in the database
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please choose a different username.")
                return render(request, 'register.html', {'form': form})
            
             # Check if password1 and password2 match
            if password1 != password2:
                messages.error(request, "Passwords do not match. Please enter the same password in both fields.")
                return render(request, 'register.html', {'form': form})
            
            # Create user object
            user = User.objects.create_user(first_name=first_name,username=username, password=password1)

            # Process form data and save user
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, 'register.html', {'form': form})


# User login view
def user_login(request):
    """
    Logs in a user with a given username and password.

    If the request method is POST, the function initializes an AuthenticationForm with request and POST data. If the form is
    valid, it gets the username and password from the POST data and authenticates the user. If the user is authenticated,
    the function logs in the user and redirects to the index page. If the username or password is invalid, the function
    shows an error message. If the form is invalid, the function shows an error message.

    If the request method is not POST, the function creates an instance of AuthenticationForm and renders the login.html
    template with the request and form data.

    Args:
        request: A Django request object.
    Returns:
        A rendered HTML response.
    """
     # Check if request method is POST
    if request.method == 'POST':

         # Initialize AuthenticationForm with request and POST data
        form = AuthenticationForm(request, data=request.POST)

        # Check if form is valid
        if form.is_valid():

            # Get username from POST data
            username = request.POST['username']
            # Get password from POST data
            password = request.POST['password']
            # Authenticate user
            user = authenticate(request, username=username, password=password)

            # If user is authenticated log in the user
            if user is not None:
                login(request, user)  
                messages.success(request, 'Login successful.')
                return redirect('index') 
            
            # Show error message for invalid username or password
            else:
                messages.error(request, 'Invalid username or password.')

        # Show error message for invalid form
        else:
            messages.error(request,"Invalid username or password.")

    # Create an instance of AuthenticationForm
    form = AuthenticationForm()
    # Render login.html template with request and form data
    return render(request, 'login.html')  


# User logout view
def user_logout(request):

    # Log out the user
    logout(request)

    # Show info message for successful logout
    messages.info(request, "You have successfully logged out.") 

    # Get the URL for the login page using URL reverse
    login_url = reverse('login')

    # Redirect to the login page
    return redirect(login_url)

# The login_required decorator to ensure only logged-in users can access this view
@login_required(login_url ='login')
# Poll views here
def poll(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "poll.html", context)

# The login_required decorator to ensure only logged-in users can access this view
@login_required(login_url ='login')
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

# The login_required decorator to ensure only logged-in users can access this view
@login_required(login_url ='login')
def vote(request, question_id):
    """
    View function that handles voting on a particular question.

    Args:
        request: HTTP request object containing the POST data.
        question_id: ID of the question being voted on.

    Returns:
        HttpResponseRedirect: Redirects to the results page for the question.

    Raises:
        None.

    This function retrieves the selected choice from the POST data, increments its
    vote count, and redirects the user to the results page for the question.
    If the user does not select a choice, it displays an error message and
    redisplay the voting form.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully
        # dealing with POST data. This prevents data from being
        # posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('results', args=(question_id,))
        )

# The login_required decorator to ensure only logged-in users can access this view
@login_required(login_url ='login')
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})