from django.urls import path
# from django.urls import include
# from login_app import views

from . import views
urlpatterns = [
    path('home', views.home, name = 'home'),
]