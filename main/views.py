from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from main.forms import UploadForm
from main.forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import Image
from google.cloud import vision
from google.cloud.vision import types
import json
import os
from google.cloud.vision import ImageAnnotatorClient

def detect_web(uri):
    client = vision.ImageAnnotatorClient()
    print(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.web_detection(image=image)
    annotations = response.web_detection
    return response

def index(request):
    return render(request, "index.html")


class UploadImage(forms.Form):

    model = Image
    fields = '__all__'

def upload(request):

    if request.method == 'POST':

        form = UploadForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['image_address']
            form.save()
            print(url)
            response = detect_web(url)
            print(response)
            return redirect('/upload/')
        else:
            print("Upload failed")

    else:
        form = UploadForm()
    return render(request, 'upload.html', {form: form})

def results(request):
    return render(request, "results.html")


def profile(request):
    return HttpResponse("PROFILE")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/results/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
