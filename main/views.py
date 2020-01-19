from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from main.forms import SearchForm
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from urllib.parse import urlencode
from main.models import Image
from google.cloud import vision
from google.cloud.vision import types
from google.cloud.vision import ImageAnnotatorClient
import os
import argparse


def annotate(path):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = path

    web_detection = client.web_detection(image=image).web_detection
    return web_detection

def page_matches(annotations):
    urls = []
    if annotations.pages_with_matching_images:
        for page in annotations.pages_with_matching_images:
            urls.append(format(page.url))
    return urls

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


class SearchImage(forms.Form):

    model = Image
    fields = '__all__'

def search(request):

    if request.method == 'POST':

        form = SearchForm(request.POST)
        if form.is_valid():
                upload = form.save(commit=False)
                anon = request.user.is_anonymous
                if anon == False:
                    upload.user=request.user
                    address = form.cleaned_data['image_address']
                    annotated = annotate(address)
                    results = page_matches(annotated)
                    upload.results = results
                    upload.save()
                    image = Image.objects.all().get(image_address=address)
                    base_url = reverse('results')
                    query_string = urlencode({'image': image.id})
                    url = '{}?{}'.format(base_url, query_string)
                    return redirect(url)
                else:
                    address = upload.image_address
                    annotated = annotate(address)
                    results = page_matches(annotated)
                    return render(request, 'results.html', {"results": results})

    else:
        form = SearchForm()
    return render(request, 'search.html', {form: form})


def results(request):
    iid = request.GET.get('image')
    display_image = Image.objects.all().get(id=iid)
    return render(request, "results.html")

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





