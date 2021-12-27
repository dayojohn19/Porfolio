from django.db import models

# Create your models here.


class Investor(models.Model):
    investor_name = models.CharField(max_length=64)
    investor_contact = models.CharField(max_length=64)

    invested_percentage = models.IntegerField()
    invested_amount = models.IntegerField()
    reinvested = models.DateTimeField(auto_now=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Total_Investment(models.Model):
    amount = models.IntegerField()
    average = models.IntegerField(blank=True, default=0)
    quantity = models.IntegerField(blank=True, default=0)
    stock = models.CharField(max_length=64)
