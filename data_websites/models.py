from django.db import models

# Create your models here.


class WebsiteMessages(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    sender = models.CharField(max_length=64)
    needAction = models.BooleanField(default=True)

    def serialize(self):
        return {
            "id": self.id,
            "message": self.message,
            "sender": self.sender,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "needAction": self.needAction,
        }
