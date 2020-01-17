from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django import forms
from main.forms import UploadForm
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.models import Image
from google.cloud import vision
from google.cloud.vision import types
import json
import os
import argparse
from google.cloud.vision import ImageAnnotatorClient

def annotate(path):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = path

    web_detection = client.web_detection(image=image).web_detection
    return web_detection

def page_matches(annotations):

    if annotations.pages_with_matching_images:
        for page in annotations.pages_with_matching_images:
            yield('Url  : {}'.format(page.url))

def image_matches(annotations):
    if annotations.full_matching_images:
        yield('\n{} Full Matches found: '.format(
            len(annotations.full_matching_images)))
    
        for image in annotations.full_matching_images:
            yield('Url  : {}'.format(image.url))

def partial_images(annotations):
    if annotations.partial_matching_images:
        yield('\n{} Partial Matches found: '.format(
            len(annotations.partial_matching_images)))

        for image in annotations.partial_matching_images:
            yield('Url  : {}'.format(image.url))


    # if annotations.web_entities:
    #     print('\n{} Web entities found: '.format(
    #     len(annotations.web_entities)))

    #     for entity in annotations.web_entities:
    #         print('Score      : {}'.format(entity.score))
    #         print('Description: {}'.format(entity.description))


    if __name__ == '__main__':
        parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.RawDescriptionHelpFormatter)
        path_help = str('The image to detect, can be web URI, '
            'Google Cloud Storage, or path to local file.')
        parser.add_argument('image_url', help=path_help)
        args = parser.parse_args()

        report(annotate(args.image_url))



def index(request):
    return render(request, "index.html", {'title': 'Home'})


class UploadImage(forms.Form):

    model = Image
    fields = '__all__'

def upload(request):

    if request.method == 'POST':

        form = UploadForm(request.POST)
        if form.is_valid():
            if request.user == True:
                upload = form.save(commit=False)
                upload.user=request.user
                url = form.cleaned_data['image_address']
                form.save()
            else:
                upload = form.save(commit=False)
                url = form.cleaned_data['image_address']
            annotated = annotate(url)
            results = page_matches(annotated)
            print(form)
            return render(request, 'results.html', {"results": results})

    else:
        form = UploadForm()
    return render(request, 'upload.html', {form: form})


def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid(): 
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account for {username} has been created. Log in to continue.')
      return redirect('login')
  else:
    form = UserRegistrationForm()

  return render(request, "register.html", {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Profile updated')
            return redirect('profile')
        else:
            print("error")
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)


def results(request):
    return render(request, "results.html")


