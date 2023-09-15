from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('greatings/', views.classroom_task, name='hello_neighbours'),
    path('templates/', views.my_landing_page, name='my_landing_page'),
    path('categories/', views.category_list, name='category_list'),
    path('notes/', views.note_list, name='note_list'),
    path('master/', views.master, name='master'),
]
