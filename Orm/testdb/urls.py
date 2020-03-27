from django.urls import path, include

from todo_list import views
from . import views

urlpatterns = [
    path('show', views.show, name="show" ),
]