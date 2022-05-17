from django.core.files.storage import FileSystemStorage
from django.db import models
from datetime import datetime
import datetime
# Create your models here.
fs = FileSystemStorage(location='sandiego')


class MySandiegoGallery(models.Model):
    poster_id = models.IntegerField(default=0)
    poster_name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    value = models.IntegerField()
    location = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True, editable=True)


class Comment(models.Model):
    user = models.CharField(max_length=64)
    user_picture = models.URLField(blank=True)
    contact = models.CharField(max_length=64)
    say = models.TextField()
    stamp = models.DateTimeField(auto_now_add=True)


class MySanDiegoDays(models.Model):

    poster_id = models.IntegerField(default=1)
    poster = models.CharField(max_length=64, blank=True)

    title = models.CharField(max_length=24, blank=True)  # this
    feeling = models.TextField(blank=True)  # this
    date = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    dateNow = models.DateField(default=datetime.datetime.now())

    country = models.CharField(max_length=64, blank=True)
    vicinity = models.CharField(max_length=64, blank=True)

    courseTrue = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)

    DutiesAndEvents = models.TextField(blank=True)

    image = models.ImageField(upload_to='san_diego')
    activity = models.TextField(blank=True, null=True)
    # SHIPraces = models.ManyToManyField(
    #     to='g_pigeon_race.Race', blank=True, related_name="registered")

    latitude = models.CharField(max_length=64, blank=True)
    longitude = models.CharField(max_length=64, blank=True)

    comments = models.ManyToManyField(
        Comment, blank=True, related_name="comments")

    def serialize(self):
        return {
            "id": self.id,
            "poster": self.poster,
            "title": self.title,
            "feeling": self.feeling,
            "date": self.date,
            "time": self.time,
            "country": self.country,
            "courseTrue": self.courseTrue,
            "activity": self.activity,
            "dateNow": self.dateNow

            # "time": self.time,
        }

    def __str__(self):
        return f"{self.title} --- {self.dateNow} --- {self.date}"
        # return self.title + self.dateNow
