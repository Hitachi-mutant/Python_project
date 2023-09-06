from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
    path('greatings/', views.classroom_task, name='hello_neighbours'),
    path('templates/', views.my_landing_page, name='my_landing_page')
]
