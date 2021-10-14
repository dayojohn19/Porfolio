from django.contrib import admin
from .models import Chain, Mypigeons, Image, Userimage

# Register your models here.
admin.site.register(Chain)
admin.site.register(Mypigeons)
admin.site.register(Image)
admin.site.register(Userimage)
