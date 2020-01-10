from django.contrib import admin 
from django.contrib.auth import views as auth_views
from django.urls import path, include
# from .views import index
# from .views import upload
# from .views import results
# from .views import profile
# from .views import register
from main import views as main_views




app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', main_views.register, name='register'),
    path("", main_views.index, name='index'),
    path('upload/', main_views.upload, name='upload'),
    path('results/', main_views.results, name='results'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
]