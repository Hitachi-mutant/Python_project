from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# in the browser go to the address - http://localhost:8000/Testapp/hello/

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('greatings/', views.classroom_task, name='hello_neighbours'),
    path('master/', views.master, name='master'),                               # adding Bootstrap 5 elements
    path('collapse_element/', views.collapse_element, name='collapse_element'), # adding Bootstrap 5 elements for testing
    path('organiser_app/', views.organiser_app, name='organiser_app'),          # homework tasks
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('filter_notes/', views.filter_notes_by_category, name='filter_notes_by_category'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
