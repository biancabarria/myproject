from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return render(response, "main/home.html", {})

def form(response):
    return render(response, "main/form.html", {})

# Create your views here.
