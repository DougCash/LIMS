from django import forms
from .models import Contacts, Locations

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = "__all__"

class LocationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = "__all__"