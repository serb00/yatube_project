from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Contact

User = get_user_model()

# creating own form class based on standard user creation form class


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # set up model for our form
        model = User
        # set up fields and their order on the form
        fields = ("first_name", "last_name", "username", "email")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "body")
