
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('new_page', views.new_page, name="new_page"),
    path('register', views.register, name="register"),
]
