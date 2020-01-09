import datetime
from django import forms
from django.forms import ModelForm
# from django.forms.widgets import TextInput
from main.models import Image


class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('description', 'image_address', 'whitelist', 'file_name',)

form = UploadForm()