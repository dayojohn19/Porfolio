from django.db import models
# from mail import User as User
# from app_mail import models as mail
# Create your models here.
class Point(models.Model):
    place = models.CharField(max_length=64)
    place_lat = models.CharField(max_length=64)
    place_long = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.place} "
from user.models import Mypigeons
class Race(models.Model):
    racename = models.CharField(max_length=64)
    price = models.IntegerField()
    started = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.racename}"


class Lap(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="L")
    release = models.ForeignKey(Point, on_delete=models.CASCADE, related_name="LL")
    
    release_lat = models.CharField(max_length=64)
    release_long = models.CharField(max_length=64)

    released = models.BooleanField(default=False)
    release_time = models.IntegerField(blank=True,default=1)
    char_time = models.CharField(blank=True,max_length=64)
    loading_cost= models.IntegerField()

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

    release_time = models.IntegerField(default=1)
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
#class Pigeons(models.Model):
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
            "id":self.id,
            "user":self.user,
            "ring": self.ring,
            "name": self.name,
            "code": self.code,
            #"time": self.time,
            "time": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "link":self.link,
            "linkimage":self.linkimage
        }

class Record(models.Model):
    entry = models.ManyToManyField(to='user.Mypigeons', blank=True, related_name="entry")
    ring = models.CharField(max_length=50)
    pigeon_name = models.CharField(max_length=64)
    lap_id = models.CharField(max_length=50)
    lap_name = models.CharField(max_length=64)
    race = models.CharField(max_length=64)
    race_name = models.CharField(max_length=64)

    # release = models.CharField(max_length=64)
    release = models.CharField(max_length=128, unique=True)
    time = models.DateTimeField()
    clock = models.DateTimeField()
    speed = models.CharField(max_length=50)
    distance = models.CharField(max_length=64)
    def serialize(self):
        return {
            "id":self.id,
            "entry":    self.entry,
            "speed":    self.speed,
            "ring":     self.ring,
            "lap":      self.lap,
            "release":  self.release,
            "clock":    self.clock
        }