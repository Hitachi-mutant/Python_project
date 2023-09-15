from django.db import models
from django.utils import timezone

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title


def create_initial_data():
    category1 = Category.objects.create(title='Work')
    category2 = Category.objects.create(title='Personal')

    # Create notes and associate them with categories
    note1 = Note.objects.create(title='Meeting with client', text='Meeting at 2:00 PM', reminder=timezone.now(), category=category1)
    note2 = Note.objects.create(title='Hangout with friends', text='Meeting at the cafe', reminder=timezone.now(), category=category2)
    note3 = Note.objects.create(title='Finish the project', text='Complete an important project', category=category1)


create_initial_data()
