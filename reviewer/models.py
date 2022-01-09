from django.db import models

# Create your models here.


class User_score(models.Model):
    ip = models.CharField(max_length=64)
    score = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    tries = models.IntegerField(default=0)
