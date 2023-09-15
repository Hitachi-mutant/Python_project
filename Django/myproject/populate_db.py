import os
import django
from Testapp.models import Category, Note
from django.utils import timezone

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Initialize Django
django.setup()

def create_initial_data():
    # Create categories
    category1 = Category.objects.create(title='Work')
    category2 = Category.objects.create(title='Personal')

    # Create notes and associate them with categories
    note1 = Note.objects.create(title='Meeting with client', text='Meeting at 2:00 PM', reminder=timezone.now(), category=category1)
    note2 = Note.objects.create(title='Hangout with friends', text='Meeting at the cafe', reminder=timezone.now(), category=category2)
    note3 = Note.objects.create(title='Finish the project', text='Complete an important project', category=category1)

if __name__ == "__main__":
    create_initial_data()
