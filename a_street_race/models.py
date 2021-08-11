from django.db import models

# Create your models here.
class Race(models.Model):
    code = models.CharField(max_length=64)
    host = models.CharField(max_length=64)

class Room(models.Model):
    room_code = models.IntegerField()
    player1 = models.CharField(max_length=64, blank=True)
    player2 = models.CharField(max_length=64, blank=True)
    full = models.BooleanField(default=False)

class Chat(models.Model):
    chat_id = models.IntegerField()
    player = models.CharField(max_length=64, blank=True)
    message = models.CharField(max_length=64, blank=True)
