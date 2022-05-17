from django.contrib import admin

# Register your models here.
from app_Car.models import Places, PlaceSchedule
admin.site.register(Places)
admin.site.register(PlaceSchedule)
