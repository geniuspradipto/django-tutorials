from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=10)
    mob = models.CharField(max_length=15)

#don't forget to register the model after creation
