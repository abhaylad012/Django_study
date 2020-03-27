from django.shortcuts import render


# Create your views here.

def home(request):
    name = ['abhay' , 'shubham', 'vidhya']
    return render(request, "home.html", {'name': name})

def new_page(request):
    return render(request, "new_page.html", {})

def register(request):
    print("i am printing")
    res = request.body

    # for r in res:
    #     print("Printing body elemeent ",r)
    print(request.body)

    name = request.POST.get('name')
    email = request.POST.get('email')
    data = {'name': name, 'email': email}
    return render(request, "new_page.html",{'data': data})
    # return render(request, "new_page.html",data)