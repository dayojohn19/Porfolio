from django.contrib import admin
from .models import Race, Point, Lap, Loaded, Code, Record, Measurement, Standing, LoadingStation

# Register your models here.
admin.site.register(Race)
admin.site.register(Point)
admin.site.register(Lap)
admin.site.register(Loaded)
admin.site.register(Code)
admin.site.register(Record)
admin.site.register(Measurement)
admin.site.register(Standing)
admin.site.register(LoadingStation)
