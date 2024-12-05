from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def education(request):
    return render(request, "education.html")