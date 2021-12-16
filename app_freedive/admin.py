from django.contrib import admin

# Register your models here.

from .models import Events, Participants, Event_Chat

# Register your models here.
admin.site.register(Events)
admin.site.register(Participants)

admin.site.register(Event_Chat)
