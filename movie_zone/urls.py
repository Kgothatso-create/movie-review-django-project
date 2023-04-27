from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),

    # Define URL pattern for the index view with name 'index'
    path('poll/', views.poll, name='poll'),

    # Define URL pattern for the detail view with name 'detail'
    path('<int:question_id>/', views.detail, name='detail'),

    # Define URL pattern for the vote view with name 'vote'
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # Define URL pattern for the results view with name 'results'
    path('<int:question_id>/results/', views.results, name='results'),

]