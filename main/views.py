from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from main.forms import UploadForm
from main.models import Image


def index(request):
    return HttpResponse("INDEX")


class UploadImage(forms.Form):

    model = Image
    fields = '__all__'

def upload(request):

    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('/upload/')
        else:
            print("Upload failed")

    else:
        form = UploadForm()
    return render(request, 'upload.html', {form: form})

def results(request):
    return HttpResponse("RESULTS")

def profile(request):
    return HttpResponse("PROFILE")
