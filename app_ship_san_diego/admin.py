from django.contrib import admin

# Register your models here.
from .models import MySanDiegoDays, Comment
admin.site.register(MySanDiegoDays)
admin.site.register(Comment)
