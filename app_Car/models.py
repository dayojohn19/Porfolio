from django.db import models

# Create your models here.


class PlaceSchedule(models.Model):
    dateN = models.IntegerField(null=True, blank=True)
    monthN = models.IntegerField(blank=True)
    yearN = models.IntegerField(blank=True)
    # adjust to dateTime FIeld
    timeDeparture = models.CharField(max_length=94, blank=True)
    departFrom = models.CharField(max_length=84)
    arriveTo = models.ForeignKey(
        'app_Car.Places', on_delete=models.CASCADE, related_name='goingTo', null=True)
    contactNumber = models.CharField(max_length=94)
    otherDetails = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"From: {self.departFrom} {self.contactNumber} - {self.otherDetails} "

    def serialize(self):
        return {
            "dateN": self.dateN,
            "monthN": self.monthN,
            "timeDeparture": self.timeDeparture,
            "departFrom": self.departFrom,
            "contactNumber": self.contactNumber,
            "arriveTo": self.arriveTo,
            "otherDetails": self.otherDetails,
            "timeDeparture": self.timeDeparture,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
        }


class placeEvent(models.Model):
    # departure Date
    dateN = models.IntegerField(null=True, blank=True)
    monthN = models.IntegerField(blank=True)
    yearN = models.IntegerField(blank=True)

    meetPlace = models.CharField(max_length=64, blank=True)
    meetTime = models.CharField(max_length=12, blank=True)

    endDate = models.CharField(max_length=64, blank=True)
    eventTitle = models.CharField(max_length=94)
    eventCost = models.CharField(max_length=64)
    eventDetails = models.TextField(blank=True)
    eventPlace = models.ForeignKey(
        'app_Car.Places', on_delete=models.CASCADE, related_name='PlaceOfEvent', null=True)

    # add contact Number
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.meetPlace} {self.eventTitle} - {self.eventDetails} - {self.eventCost} "


class Places(models.Model):
    placename = models.CharField(max_length=64)
    placeSchedule = models.ManyToManyField(
        PlaceSchedule, blank=True, related_name="scheds")
    placeEvent = models.ManyToManyField(
        placeEvent, blank=True, related_name='events')

    def __str__(self):
        return f"{self.placename}"

    @property
    def SchedList(self):
        return self.placeSchedule.all()

    def SchedListCount(self):
        return self.placeSchedule.count()

    def EventList(self):
        return self.placeEvent.all()

    def EventListCount(self):
        return self.placeEvent.count()
