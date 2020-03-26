from django.shortcuts import render

from .models import Test


# Create your views here.

def show(request):
    test1 = Test.objects.all()

    return render(request, "show.html", {'test1':test1})