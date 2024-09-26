from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image
from ..forms import BandListingForm, MessageForm

# Create your tests here.
class BandListingFormTest(TestCase):

    def test_valid_bandlisting_form_with_all_fields(self):
        # Create an image in memory for the test
        image = BytesIO()
        Image.new('RGB', (100, 100)).save(image, format='JPEG')
        image.seek(0)
        
        photo = SimpleUploadedFile(name='test_image.jpg', content=image.getvalue(), content_type='image/jpeg')
        
        form_data = {
            'band_name': 'Test Band',
            'photo': photo,
            'description': 'This is a test description.',
            'snippet': 'Post-punk band from New York, New York',
        }
        form = BandListingForm(data=form_data, files={'photo': photo})
        self.assertTrue(form.is_valid())  # Form should be valid with a valid photo

    def test_bandlisting_with_photo(self):
        # Create an image in memory for the test
        image = BytesIO()
        Image.new('RGB', (100, 100)).save(image, format='JPEG')
        image.seek(0)

        photo = SimpleUploadedFile(name='test_image.jpg', content=image.getvalue(), content_type='image/jpeg')

        form_data = {
            'band_name': 'Band With Photo',
            'description': 'A description',
            'snippet': '',  # Optional snippet
        }
        
        # Include the photo in the files dictionary
        form = BandListingForm(data=form_data, files={'photo': photo})
        
        # Check if the form is valid and print errors if not
        if not form.is_valid():
            print(form.errors)  # Print the errors to diagnose the issue

        self.assertTrue(form.is_valid())  # Form should be valid with an optional photo

    def test_invalid_bandlisting_form_no_band_name(self):
        # Test case where 'band_name' is missing (invalid)
        form_data = {
            'band_name': '',  # Invalid because band_name is required
            'description': 'A valid description',
            'snippet': 'Valid snippet',
        }
        form = BandListingForm(data=form_data)
        self.assertFalse(form.is_valid())  # Form should be invalid
        self.assertIn('band_name', form.errors)  # Error should be related to 'band_name'

    def test_invalid_bandlisting_form_no_snippet(self):
        # Test case where 'snippet' is optional
        form_data = {
            'band_name': 'Valid Band',
            'description': 'A description',
            'snippet': '',  # Optional snippet
        }
        form = BandListingForm(data=form_data)
        self.assertTrue(form.is_valid())  # Form should be valid with optional snippet


class MessageFormTest(TestCase):

    def test_valid_message_form(self):
        # Test case with valid data
        form_data = {
            'message_body': 'This is a test message.',
        }
        form = MessageForm(data=form_data)
        self.assertTrue(form.is_valid())  # Form should be valid

    def test_invalid_message_form_empty_body(self):
        # Test case where 'message_body' is empty (invalid)
        form_data = {
            'message_body': '',  # Invalid because message_body is required
        }
        form = MessageForm(data=form_data)
        self.assertFalse(form.is_valid())  # Form should be invalid
        self.assertIn('message_body', form.errors)  # Error should be related to 'message_body'

    def test_message_form_with_long_message(self):
        # Test case with a very long message (valid)
        long_message = 'This is a long test message.' * 100
        form_data = {
            'message_body': long_message,
        }
        form = MessageForm(data=form_data)
        self.assertTrue(form.is_valid())  # Form should be valid even with a long message
