from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=420)
    subtitle=models.CharField(max_length=420)
    description = models.TextField()
    pages= models.IntegerField()
    publisher= models.CharField(max_length=420)
    published= models.DateField()
    author= models.CharField(max_length=420)
    # ImageUrl = models.CharField(max_length=600)

    def __str__(self):
        return f'Book :{self.title} author-name :  {self.author}'
