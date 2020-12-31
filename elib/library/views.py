from django.shortcuts import render
from django.contrib.auth import logout
from django.db.models import Q
from .models import Books
from .filters import BookFilter


# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from django.http import HttpResponse, FileResponse, Http404, HttpResponseNotFound



def is_query_valid(param):
    return param != '' and param is not None


def index(request):

    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return render(request, "login.html")


def library(request): #filter and display books
    qs = Books.objects.all()
    if request.user.is_authenticated:
        title_author_query = request.GET.get('title_author')
        category_query = request.GET.get('category')
        isbn_query = request.GET.get('isbn')
        min_year_query = request.GET.get('min_year')
        max_year_query = request.GET.get('max_year')
        file_available_query = request.GET.get('file_available')
        file_unavailable_query = request.GET.get('file_unavailable')
        
        
        
        if is_query_valid(title_author_query):
            qs = qs.filter(Q(bookTitle__icontains=title_author_query) | Q(bookAuthor__icontains=title_author_query)).distinct()

        if is_query_valid(category_query):
            qs = qs.filter(bookCategory__icontains=category_query)
        
        if is_query_valid(isbn_query):
            qs = qs.filter(isbn__iexact=isbn_query)

        if is_query_valid(min_year_query):
            qs = qs.filter(yearPublished__gte=min_year_query)

        if is_query_valid(max_year_query):
            qs = qs.filter(yearPublished__lte=max_year_query)

        if file_available_query =='on' :
            qs = qs.filter(bookFile__istartswith='books')
        
        if file_unavailable_query =='on':
            qs = qs.filter(bookFile='')


        context = {
            'queryset': qs
        }

        return render(request, "library.html", context)
    else:
        return render(request, "login.html")


def authorSearch(request, id, bookAuthor): #search for all same author queries
    book = Books.objects.get(id=id, bookAuthor=bookAuthor)
    qs = Books.objects.all()
    if request.user.is_authenticated:
        author_query = bookAuthor
    
        if is_query_valid(author_query): #if author is not none or blank filter all books with this author
            qs = qs.filter(bookAuthor__iexact=author_query)
        
        context = {
            'queryset': qs,
            'book': book
        }

        return render(request, "library.html", context)
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

def userManual(request, id, bookTitle):
    book = Books.objects.get(id=id, bookTitle = bookTitle)
    if request.user.is_authenticated:
        return render(request, "book-view.html", {'bookTitle': book.bookTitle, 'bookFile': book.bookFile})
    else:
        return render(request, "login.html")
# def userManual(request, id, title):
#     book = Books.objects.get(id=id, bookTitle=title)
#     file_location = './media/books/Queueing.v3.pdf'

#     try:    
#         with open(file_location, 'r') as f:
#            file_data = f.read()

#         # sending response 
#         response = HttpResponse(file_data, content_type='application/pdf')
#         # response['Content-Disposition'] = ' filename="report.pdf"'

#     except IOError:
#         # handle file not exist case here
#         response = HttpResponseNotFound('<h1>File not exist</h1>')

#     return response

