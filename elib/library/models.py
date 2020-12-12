from django.db import models

class Books(models.Model):
    bookName = models.CharField(max_length=100)
    bookAuthor = models.CharField(max_length=100)
    bookDescription = models.TextField()
    bookCategory = models.CharField(max_length=100, blank=True)
    yearPublished = models.IntegerField()
    bookImage = models.ImageField(upload_to='covers', blank=True)
    isbn = models.IntegerField(blank=True)
    pages = models.IntegerField()

    
