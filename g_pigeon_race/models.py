from user.models import Mypigeons
from django.db import models
# from mail import User as User
# from app_mail import models as mail
# Create your models here.


class LoadingStation(models.Model):
    lap = models.IntegerField()
    place = models.CharField(max_length=64)
    price = models.IntegerField()
    time = models.CharField(max_length=64)


class Standing(models.Model):
    race_id = models.IntegerField()
    pigeon_id = models.IntegerField()
    pigeon_name = models.CharField(max_length=64)
    tspeed = models.IntegerField(default=0)

    class Meta:
        ordering = ["-tspeed"]

    def __str__(self):
        return f"{self.pigeon_name} Speed: {self.tspeed}"


class Point(models.Model):
    place = models.CharField(max_length=64)
    place_lat = models.CharField(max_length=64)
    place_long = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.place} "


class Race(models.Model):
    racename = models.CharField(max_length=64)
    price = models.IntegerField()
    started = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.racename}"


class Lap(models.Model):
    num_load = models.ManyToManyField(
        'Loaded', blank=True, related_name="load_count")
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="L")
    release = models.ForeignKey(
        Point, on_delete=models.CASCADE, related_name="LL")

    release_lat = models.CharField(max_length=64)
    release_long = models.CharField(max_length=64)

    released = models.BooleanField(default=False)
    release_time = models.IntegerField(blank=True, default=1)
    char_time = models.CharField(blank=True, max_length=64)
    loading_cost = models.IntegerField()

    @property
    def num_loaded(self):
        return self.num_load.all().count()

#    release_time
#   released


class Code(models.Model):
    code = models.CharField(max_length=64)
    hcode = models.CharField(max_length=64)

    ring_code = models.CharField(max_length=64, blank=True)
    pigeon_id = models.CharField(max_length=65, blank=True)


class Measurement(models.Model):
    uid = models.IntegerField()
    latitude = models.CharField(max_length=64)
    longitude = models.CharField(max_length=64)


class Loaded(models.Model):
    isLoaded = models.BooleanField(default=True)
    race_id = models.CharField(max_length=64)
    race_name = models.CharField(max_length=64)
    lap = models.CharField(max_length=64)
    lap_name = models.CharField(max_length=64)

 #   lap_lat
 #   lap_long

    pigeon_id = models.CharField(max_length=65)
    pigeon_name = models.CharField(max_length=64)
    pigeon_ring = models.CharField(max_length=64, blank=True)
    pigeon_hcode = models.CharField(blank=True, max_length=64)

    pigeon_lat = models.CharField(max_length=64)
    pigeon_long = models.CharField(max_length=64)
    pigeon_loader = models.CharField(max_length=64)

    release_lat = models.CharField(max_length=64)
    release_long = models.CharField(max_length=64)

    release_time = models.IntegerField(blank=True, null=True, default=1)
    clock_time = models.IntegerField(default=1)

#    def __str__(self):
#        return str(self.lap)
#    def __str__(self):
#        return str(self.loaded_pigeons.count())

    def serialize(self):
        return {
            "id": self.loaded_pigeons,
            "lap": self.lap
        }
# class Pigeons(models.Model):
#    x = models.CharField(max_length=12)
#    y = models.CharField(max_length=12)
#    races = models.ManyToManyField(Race, blank=True, related_name="registered")


class Entries(models.Model):
    name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    ring = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    linkimage = models.CharField(max_length=100)
    #time = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "ring": self.ring,
            "name": self.name,
            "code": self.code,
            # "time": self.time,
            "time": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "link": self.link,
            "linkimage": self.linkimage
        }


class Record(models.Model):
    pigeon_id = models.IntegerField(default=1, blank=True)
    entry = models.ManyToManyField(
        to='user.Mypigeons', blank=True, related_name="entry")
    ring = models.CharField(max_length=50, blank=True)
    pigeon_name = models.CharField(max_length=64, blank=True)
    lap_id = models.CharField(max_length=50, blank=True)
    lap_name = models.CharField(max_length=64, blank=True)
    race = models.CharField(max_length=64, blank=True)
    race_name = models.CharField(max_length=64, blank=True)

    # release = models.CharField(max_length=64)
    release = models.CharField(max_length=64, blank=True)
    # release2 = models.DateTimeField(auto_now_add=True)
    time = models.CharField(max_length=64, blank=True)
    clock = models.CharField(max_length=64, blank=True)
    speed = models.DecimalField(max_digits=20, decimal_places=2)
    distance = models.CharField(max_length=64, blank=True)

    class Meta:
        ordering = ["-speed"]

    def serialize(self):
        return {
            "rid": self.id,
            "id": self.pigeon_id,
            "pigeon_name": self.pigeon_name,
            "lap_name": self.lap_name,
            "speed":    self.speed,
            "ring":     self.ring,
            "release":  self.release,
            "clock":    self.clock,
            "distance": self.distance
        }
