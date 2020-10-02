from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    sex=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    def __str__(self):
         return self.name

class token(models.Model):
    name=models.CharField(max_length=30)
    tokenno= models.CharField(max_length=40)
    def __str__(self):
         return self.name

