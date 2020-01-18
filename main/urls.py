from django.contrib import admin 
from django.contrib.auth import views as auth_views
from django.urls import path, include
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('register/', main_views.register, name='register'),
    path("", main_views.index, name='index'),
    path('search/', main_views.search, name='search'),
    path('results/', main_views.results, name='results'),
    path("<int:id>", main_views.results, name="")
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)