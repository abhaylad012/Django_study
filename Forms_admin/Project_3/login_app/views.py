from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List
from .forms import ListForm
from django.contrib import messages


# Create your views here.

def login_form(request):
    return render(request, "login_form.html")

def home(request):
    if request.method == 'POST':
        print("in post")
        form = ListForm(request.POST or None)
        print("printing form:", form)

        if form.is_valid():
            print("in form if")
            form.save()

            all_items = List.objects.all
            print(all_items)
            messages.success(request, ('Item has been added to List'))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        print("in else")
        all_items = List.objects.all
        print(all_items)
        return render(request, 'home.html', {'all_items': all_items})


# return render(request, "login_form.html")

#
# def success(request):
#     return

