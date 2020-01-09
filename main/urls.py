from django.contrib import admin
from django.urls import path
from .views import index
from .views import upload
from .views import results
from .views import profile


app_name = 'main'

urlpatterns = [
  path("", index),
  path('upload/', upload),
  path('results/', results),
  path('profile/', profile),
]