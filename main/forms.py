import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import Image


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'image_address', 'whitelist', 'file_name',)

form = UploadForm()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']