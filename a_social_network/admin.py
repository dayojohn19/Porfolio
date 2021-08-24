from django.contrib import admin

# Register your models here.

from .models import Name, Profile, Like, Follow
# Register your models here.
admin.site.register(Name)
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Follow)
# admin.site.register(User)