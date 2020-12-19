from django.shortcuts import render
from django.contrib.auth import logout
from .models import Books
    

def index(request):

    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return render(request, "login.html")

def library(request):
    book = Books.objects.all()

    if request.user.is_authenticated:
        return render(request, "library.html", {'books' : book})
    else:
        return render(request, "login.html")

def book(request, id):
    book = Books.objects.get(id=id)
    return render(request, "book.html", {'book': book})


def staff(request):
    if request.user.is_authenticated:
        return render(request, "staff.html")
    else:
        return render(request, "login.html")

def services(request):
    if request.user.is_authenticated:
        return render(request, "services.html")
    else:
        return render(request, "login.html")

def about(request):
    if request.user.is_authenticated:
        return render(request, "about.html")
    else:
        return render(request, "login.html")
