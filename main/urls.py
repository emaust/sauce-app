from django.contrib import admin
from django.urls import path, include
from .views import index
from .views import upload
from .views import results
from .views import profile
from .views import register



app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register),
    path("", index),
    path('upload/', upload),
    path('results/', results),
    
    
]