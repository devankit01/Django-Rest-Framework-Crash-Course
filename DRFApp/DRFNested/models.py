from unicodedata import name
from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email

class Course(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')
