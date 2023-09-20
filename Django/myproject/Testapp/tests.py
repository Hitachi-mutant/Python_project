from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from Testapp.models import Collapse, collapse_element_initial_data, Category, Note
from Testapp.forms import NoteForm
from Testapp.views import organiser_app, delete_note, filter_notes_by_category

class CollapseModelTestCase(TestCase):
    def test_collapse_model_creation(self):
        # Test that a Collapse object can be created
        collapse = Collapse.objects.create(
            title='Test Collapse',
            first_button='Test Button 1',
            second_button='Test Button 2',
            text_field='Test Text'
        )
        self.assertEqual(collapse.title, 'Test Collapse')
        self.assertEqual(collapse.first_button, 'Test Button 1')
        self.assertEqual(collapse.second_button, 'Test Button 2')
        self.assertEqual(collapse.text_field, 'Test Text')

    def test_collapse_element_initial_data(self):
        # Test the collapse_element_initial_data function
        collapse_element_initial_data()  # Create a Collapse instance

        # Verify that an instance with the expected data exists in the database
        collapse = Collapse.objects.get(title='Collapse element')
        self.assertEqual(collapse.first_button, 'Button 1')
        self.assertEqual(collapse.second_button, 'Button 2')
        self.assertEqual(collapse.text_field, 'These elements has been retrieved from the data base')


class NoteFormTestCase(TestCase):
    def test_valid_note_form(self):
        form_data = {
            'title': 'Test Note',
            'text': 'This is a test note.',
            'category': Category.objects.create(title='Test Category').id
        }
        form = NoteForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_note_form(self):
        form_data = {}
        form = NoteForm(data=form_data)
        self.assertFalse(form.is_valid())

class OrganiserAppTestCase(TestCase):
    def test_organiser_app(self):
        response = self.client.get(reverse('organiser_app'))
        self.assertEqual(response.status_code, 200)  # Check if the page loads successfully

class DeleteNoteTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='Test Category')
        self.note = Note.objects.create(title='Test Note', text='This is a test note.', category=self.category)

    def test_delete_note(self):
        response = self.client.post(reverse('delete_note', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)                      # Check if the response is a redirect
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())  # Check if the note has been deleted

class FilterNotesByCategoryTestCase(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(title='Category 1')
        self.category2 = Category.objects.create(title='Category 2')
        self.note1 = Note.objects.create(title='Note 1', text='This is note 1.', category=self.category1)
        self.note2 = Note.objects.create(title='Note 2', text='This is note 2.', category=self.category2)

    def test_filter_notes_by_category(self):
        response = self.client.get(reverse('filter_notes_by_category'), {'category': self.category1.id})
        self.assertEqual(response.status_code, 200)  # Check if the page loads successfully
        self.assertContains(response, 'Note 1')      # Check if 'Note 1' is in the filtered notes
        self.assertNotContains(response, 'Note 2') 
        