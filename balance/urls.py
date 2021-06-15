from django.urls import path
from . import views as as_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', as_views.index, name='index'),
    path('register/', as_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
]