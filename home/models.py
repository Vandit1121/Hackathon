from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=15)
    complain=models.TextField()
    date=models.DateField()