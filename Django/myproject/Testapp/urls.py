from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView, LogoutView



# in the browser go to the address - http://localhost:8000/Testapp/organiser_app/

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('greatings/', views.classroom_task, name='hello_neighbours'),
    path('master/', views.master, name='master'),                               # adding Bootstrap 5 elements
    path('collapse_element/', views.collapse_element, name='collapse_element'), # adding Bootstrap 5 elements for testing
    path('organiser_app/', views.organiser_app, name='organiser_app'),          # homework tasks
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('filter_notes/', views.filter_notes_by_category, name='filter_notes_by_category'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # it will redirect to the login page
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),

]

