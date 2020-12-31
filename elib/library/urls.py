from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('library', views.library, name = 'library'),
    path('staff', views.staff, name = 'staff'),
    path('services', views.services, name = 'services'),
    path('about', views.about, name = 'about'),
    path('library/<int:id>/author-<str:bookAuthor>', views.authorSearch, name='author_search'),
    path('library/<int:id>', views.book, name = 'library_preview'),
    path('library/<int:id>/<str:bookTitle>', views.userManual, name = 'render_view'),
    
    
]
