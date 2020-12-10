from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('library', views.library, name = 'library'),
    path('staff', views.staff, name = 'staff'),
    path('services', views.services, name = 'services'),
    path('about', views.about, name = 'about')
]
