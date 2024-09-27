from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import BandListing, Message

# Form for creating and editing a Band Listing
class BandListingForm(forms.ModelForm):
    class Meta:
        model = BandListing
        # Fields to be included in the form
        fields = ['band_name', 'photo', 'description', 'snippet']
        # Customize form widgets for description and snippet fields
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'snippet': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Example: Post-punk band from New York, New York'}),
        }

    def __init__(self, *args, **kwargs):
        # Initialize the form and set up crispy forms helper
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'  # Form will use POST method
        self.helper.form_enctype = 'multipart/form-data'  # Enable file uploads for the photo field
        self.helper.add_input(Submit('submit', 'Create Listing'))  # Add a submit button

        # Ensure the 'photo' field is optional
        self.fields['photo'].required = False

# Form for sending a message to a band listing owner
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # Only the message body is needed in this form
        fields = ['message_body']
        # Customize the message body widget
        widgets = {
            'message_body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your message here...'}),
        }

    def __init__(self, *args, **kwargs):
        # Initialize the form and set up crispy forms helper
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'  # Form will use POST method
        self.helper.add_input(Submit('submit', 'Send Message'))  # Add a submit button
