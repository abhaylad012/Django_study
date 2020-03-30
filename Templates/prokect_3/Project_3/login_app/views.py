from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List
from .forms import ListForm
from django.contrib import messages


# Create your views here.

def login_form(request):
    return render(request, "login_form.html")

def success(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()

            all_items = List.objects.all
            messages.success(request, ('Item has been added to List'))
            return render(request, 'success.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'success.html', {'all_items': all_items})


# return render(request, "login_form.html")

#
# def success(request):
#     return

