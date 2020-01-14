from django.contrib import admin 
from django.contrib.auth import views as auth_views
from django.urls import path, include
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', main_views.register, name='register'),
    path("", main_views.index, name='index'),
    path('upload/', main_views.upload, name='upload'),
    path('results/', main_views.results, name='results'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)