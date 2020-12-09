from django.shortcuts import render
from django.contrib.auth import logout

def index(request):

    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        return render(request, "index.html")

def library(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        return render(request, "library.html")

def staff(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        return render(request, "staff.html")
