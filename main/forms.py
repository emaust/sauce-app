import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import Image
from main.models import Profile



class SearchForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'image_address', 'file_name',)

form = SearchForm()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar', 'instagram', 'twitter', 'youtube', 'website', 'patreon']

class ReportForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['results']