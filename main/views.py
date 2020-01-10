from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from main.forms import UploadForm
from main.models import Image
from google.cloud import vision
from google.cloud.vision import types
import json
from google.cloud.vision import ImageAnnotatorClient

def detect_web(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.web_detection(image=image)
    annotations = response.web_detection


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
            response = detect_web("https://pbs.twimg.com/media/DXgQoJMVMAAkYrm.jpg")
            print(response)
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



