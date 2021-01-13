from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Books(models.Model):
    bookTitle = models.CharField(max_length=100)
    bookAuthor = models.CharField(max_length=100)
    bookDescription = models.TextField()
    bookCategory = models.CharField(max_length=50, blank=True)
    yearPublished = models.IntegerField(validators=[MaxValueValidator(9999)])
    bookFile = models.FileField(upload_to='books', null=True, blank=True)
    bookImage = models.ImageField(upload_to='covers', blank=True)
    isbn = models.IntegerField(blank=True)
    pages = models.IntegerField(validators=[MaxValueValidator(10000), MinValueValidator(0)])
    featured = models.BooleanField()

    
