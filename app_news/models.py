from django.db import models
from datetime import datetime
# Create your models here.
class Article(models.Model):
    date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=64)
    link = models.CharField(max_length=6464)
    content = models.TextField(blank=True)
    section = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    def __str__(self):
        return self.title