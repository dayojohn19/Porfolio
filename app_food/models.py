from django.db import models

# Create your models here.
class Food(models.Model):
    date = models.TextField(max_length=64)
    cook = models.TextField(max_length=64)
    umaga = models.TextField(max_length=64)
    tanghali = models.TextField(max_length=64)
    gabi = models.TextField(max_length=64)

    u_cost = models.TextField(max_length=64)
    t_cost = models.TextField(max_length=64)
    g_cost = models.TextField(max_length=64)


class Tally(models.Model):
    user = models.TextField(max_length=64)
    am = models.TextField(max_length=64,blank=True, null=True)
    pm = models.TextField(max_length=64,blank=True, null=True)
    eve = models.TextField(max_length=64,blank=True, null=True)

    cost = models.TextField(max_length=64)

