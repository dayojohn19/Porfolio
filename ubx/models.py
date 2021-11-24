from django.db import models

# Create your models here.


class ubx_Item(models.Model):
    first = models.CharField(max_length=64)

    def __str__(self):
        return self.first
