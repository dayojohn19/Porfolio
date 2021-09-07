from django.db import models
from django.contrib.auth.models import User
from django.conf import settings




# Create your models here.
class Book(models.Model):
    price = models.IntegerField()
    instructor = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=500)
    link = models.URLField()
    
class Student(models.Model):
    user = models.CharField(max_length=64)
    courses = models.ManyToManyField(Book, blank=True, related_name="enrollee")

    def __str__(self):
        return f"{self.user} {self.courses}"
