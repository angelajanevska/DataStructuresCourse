from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
