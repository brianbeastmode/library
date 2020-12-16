from django.shortcuts import render
from django.contrib.auth import logout
from .models import Books
    

def index(request):

    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        return render(request, "index.html")

def library(request):
    book = Books.objects.all()

    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        return render(request, "library.html", {'books' : book})

def book(request, id):
    book = Books.objects.get(id=id)
    return render(request, "book.html", {'book': book})


def staff(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        return render(request, "staff.html")

def services(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        return render(request, "services.html")

def about(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    else:
        return render(request, "about.html")
