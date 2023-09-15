from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Note, Person

def hello_view(request):
    return HttpResponse('Say Hello to my little Test app!')
# in the browser go to the address - http://localhost:8000/Testapp/hello/

def classroom_task(request):
    return HttpResponse('Hello my neighbours! F*ck you too!!!')

def my_landing_page(request):
    return render(request, 'landing_page.html')



def category_list(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'category_list.html', {'categories': categories})

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes})

def master(request):
    persons = Person.objects.all()  # Query the Person objects from the database
    return render(request, 'master.html', {'persons': persons})
