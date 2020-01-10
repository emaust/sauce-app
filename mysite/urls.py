
from django.contrib import admin
from main import views as main_views
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('main.urls')),
    path('register/', main_views.register, name='register'),
    path("", main_views.index, name='index'),
    path('upload/', main_views.upload, name='upload'),
    path('results/', main_views.results, name='results'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
]
