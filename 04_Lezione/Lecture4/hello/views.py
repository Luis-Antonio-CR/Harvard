from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def luis(request):
    return HttpResponse("Hello, Luis!")

def pablo(request):
    return HttpResponse("Hello, Pablo!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

