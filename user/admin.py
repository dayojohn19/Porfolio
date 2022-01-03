from django.contrib import admin
from .models import Chain, Mypigeons, Image, Userimage, Transaction_History, Order, User_Coins, User_visitor

# Register your models here.
admin.site.register(Chain)
admin.site.register(Mypigeons)
admin.site.register(Image)
admin.site.register(Userimage)
admin.site.register(Transaction_History)
admin.site.register(Order)
admin.site.register(User_Coins)
admin.site.register(User_visitor)
