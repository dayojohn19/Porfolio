
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class User(AbstractUser):
#     pass

# try upload images
from django.core.files import storage


class Chain(models.Model):
    chain = models.CharField(max_length=64, default=1231)
    value = models.CharField(max_length=64, blank=True)


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fancier')

    def __str__(self):
        return self.name


class Userimage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fancier_profiles')

    def __str__(self):
        return self.name


fs = FileSystemStorage(location='/user/pigeons/')


class Mypigeons(models.Model):
    owner = models.CharField(max_length=64)
    name = models.CharField(max_length=24)
    ring = models.CharField(max_length=24)
    time = models.CharField(max_length=64)
    link = models.ImageField(storage=fs, max_length=64,
                             default=None, blank=True, null=True)

    loaded = models.BooleanField(default=False)
    loads = models.CharField(max_length=64, blank=True)
    races = models.ManyToManyField(
        to='g_pigeon_race.Race', blank=True, related_name="registered")

    my_lat = models.CharField(max_length=64)
    my_long = models.CharField(max_length=64)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "ring": self.ring,
            "name": self.name,
            "owner": self.owner,
            "loads": self.loads,
            "loaded": self.loaded

            # "time": self.time,
        }

    def __str__(self):
        return self.name
