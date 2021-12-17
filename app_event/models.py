from django.db import models
# from djongo import models
# Create your models here.


class Events(models.Model):
    # _id = models.ObjectIdField()
    start_time = models.CharField(max_length=64)
    end_time = models.CharField(max_length=64)

    organizer = models.CharField(max_length=64)
    organizer_contact = models.CharField(max_length=64)
    organizer_image = models.URLField()

    event_type = models.CharField(max_length=64)
    event_description = models.CharField(max_length=500)
    event_name = models.CharField(max_length=64)
    event_image = models.URLField()
    event_cost = models.IntegerField(default=1)
    event_participants = models.ManyToManyField('Participants')

    timestamp = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['start_time']

    def __unicode__(self):
        return self.start_time


class Participants(models.Model):
    # _id = models.ObjectIdField()
    participant = models.CharField(max_length=64)
    participant_image = models.URLField()

    # def __str__(self):
    #     return self.participant


class Event_Chat(models.Model):
    chat_rooms = models.IntegerField(default=1)
    # chat_room = models.ForeignKey(Events, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    sender = models.CharField(max_length=64)
    sender_image = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Event_Picture(models.Model):
    image = models.ImageField(upload_to='event_images')
