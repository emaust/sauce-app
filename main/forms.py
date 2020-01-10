import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from main.models import Image
from main.models import Users


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'image_address', 'whitelist', 'file_name',)

form = UploadForm()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']