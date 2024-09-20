from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import BandListing, Message

class BandListingForm(forms.ModelForm):
    class Meta:
        model = BandListing
        fields = ['band_name', 'photo', 'description', 'snippet']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'snippet': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create Listing'))

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message_body']
        widgets = {
            'message_body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your message here...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send Message'))
