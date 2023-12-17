from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Invalid username or password"))
            return redirect('loginuser')

    else:
        return render(request, 'myapp/login.html')
def home(request):
    return render(request, 'myapp/Home.html')
def add_emp(request):
    return render(request, 'myapp/ADd.html')
def view_emp(request):
    return HttpResponse('view_emp')
def grievances(request):
    return HttpResponse('grievances')
def manager_info(request):
    return HttpResponse('manager_info')
def department(request):
    return render(request, 'myapp/departm.html')
