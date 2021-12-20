from django.db import models

# Create your models here.


class Blog_item(models.Model):
    title = models.CharField(max_length=64)
    sub_title = models.CharField(max_length=64)
    paragraph = models.TextField()
    picture_link = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField(max_length=64, default='user')

    def __str__(self):
        return self.title
