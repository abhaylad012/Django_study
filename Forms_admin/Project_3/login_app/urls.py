from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_form, name='login_form'),
    path('home', views.home, name='home'),
]