from django.db import models
from django.utils import timezone
from django import forms

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Collapse(models.Model):
    title = models.CharField(max_length=200)
    first_button = models.CharField(max_length=30)
    second_button = models.CharField(max_length=30)
    text_field = models.TextField()
    
    def __str__(self):
        return self.title
    
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
    category3 = Category.objects.create(title='Hobby')

#     # Create notes and associate them with categories
#     note1 = Note.objects.create(title='Meeting with client', text='Meeting at 2:00 PM', reminder=timezone.now(), category=category1)
#     note2 = Note.objects.create(title='Hangout with friends', text='Meeting at the cafe', reminder=timezone.now(), category=category2)
#     note3 = Note.objects.create(title='Finish the project', text='Complete an important project', category=category1)

def collapse_element_initial_data():
    collapse_element_instance = Collapse.objects.create(title='Collapse element', first_button='Button 1', second_button='Button 2', text_field='These elements has been retrieved from the data base')



# Because it is a test, I have to execute these functions once to populate the database
# create_initial_data()
# collapse_element_initial_data()


        
        