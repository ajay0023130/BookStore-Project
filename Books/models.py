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
    ImageUrl = models.CharField(max_length=600)

    def __str__(self):
        return f'Book :{self.title} author-name :  {self.author}'
        # return self.id


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Date:{self.date}"

    
