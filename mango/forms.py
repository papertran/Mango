from django import forms
from django.contrib.auth.forms import UserCreationForm
from mango.models import userAccount

class registrationForm(UserCreationForm):
    email = forms.EmailField(max_length=128, help_text="Required. Add a valid email addresss")

    class Meta:
        model = userAccount
        fields = ("email", "username","first_name", "last_name", "password1", "password2")