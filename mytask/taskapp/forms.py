from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    Class Meta:
        model = Contact
        fields = '__all__'