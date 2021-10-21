from django.db import models

# Create your models here.


class Blog_Item(models.Model):
    title = models.CharField(max_length=64)
    sub_title = models.CharField(max_length=64)
    paragraph = models.TextField()
    picture_link = models.CharField(max_length=1000)
