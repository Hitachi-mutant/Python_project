from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Note, Person, Collapse
from .forms import NoteForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# classroom tasks - start
def hello_view(request):
    return HttpResponse('Say Hello to my little Test app!')

def classroom_task(request):
    return HttpResponse('Hello my neighbours! F*ck you too!!!')

def master(request):
    persons = Person.objects.all()  
    return render(request, 'master.html', {'persons': persons})

def collapse_element(request):
    element_data = Collapse.objects.all()
    return render(request, 'collapse_element.html', {'element_data': element_data})

# classroom tasks - end


@login_required
def organiser_app(request):
    categories = Category.objects.all()
    notes = Note.objects.all()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organiser_app')
    else:
        form = NoteForm()

    return render(request, 'organiser_app.html', {'categories': categories, 'notes': notes, 'form': form})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        note.delete()
    
    return redirect('organiser_app') 

@login_required
def filter_notes_by_category(request):
    categories = Category.objects.all()

    # Get the selected category from the request
    selected_category_id = request.GET.get('category', None)

    # Filter notes by category if a category is selected
    if selected_category_id:
        selected_category = Category.objects.get(id=selected_category_id)
        notes = Note.objects.filter(category=selected_category)
    else:
        notes = Note.objects.all()

    return render(request, 'organiser_app.html', {'categories': categories, 'notes': notes})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect('organiser_app')  # Redirect to organiser_app page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('organiser_app')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()
    return redirect('organiser_app') 




