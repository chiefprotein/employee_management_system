from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'myapp/login.html')
def home(request):
    return HttpResponse('home')
def add_emp(request):
    return render(request, 'myapp/ADd.html')