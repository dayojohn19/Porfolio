from django.db import models

# Create your models here.
class Race(models.Model):
    code = models.CharField(max_length=64)
    host = models.CharField(max_length=64)

class Room(models.Model):
    room_code = models.IntegerField(blank=True)
    player1 = models.CharField(max_length=64, blank=True)
    player2 = models.CharField(max_length=64, blank=True)
    full = models.BooleanField(default=False)

    sticker1 = models.CharField(max_length=64, blank=True)
    sticker2 = models.CharField(max_length=64, blank=True)
from django.utils import timezone
from django.conf import settings
class Chat(models.Model):
    chat_id = models.IntegerField()
    player = models.CharField(max_length=64, blank=True)
    message = models.CharField(max_length=64, blank=True)
    time = models.DateTimeField(auto_now_add=timezone.now)

    def serialize(self):
        return {
            "id": self.id,
            "sender": self.player,
            "message": self.message,
            "time":self.time.strftime("%h %d, %I:%M%p ")
        }
class Player(models.Model):
    room = models.CharField(max_length=64, blank=True)
    player = models.CharField(max_length=64, blank=True)
    user = models.CharField(max_length=64, blank=True)
    sticker = models.CharField(max_length=64, blank=True)
