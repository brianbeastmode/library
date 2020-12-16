from django.db import models

class Books(models.Model):
    bookTitle = models.CharField(max_length=100)
    bookAuthor = models.CharField(max_length=100)
    bookDescription = models.TextField()
    bookCategory = models.CharField(max_length=100, blank=True)
    yearPublished = models.IntegerField()
    bookFile = models.FileField(upload_to='books', blank=True)
    bookImage = models.ImageField(upload_to='covers', blank=True)
    isbn = models.IntegerField(blank=True)
    pages = models.IntegerField()

    
