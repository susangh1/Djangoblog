from django.db import models


# Create your models here.
class Contact(models.Model):
    email= models.CharField(max_length=122)
    Name = models.CharField(max_length=122)
    Phone = models.CharField(max_length=20)
    Description = models.TextField()
    date = models.DateField()

