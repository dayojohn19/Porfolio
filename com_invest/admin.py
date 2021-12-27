from django.contrib import admin

# Register your models here.
from .models import Investor, Total_Investment

admin.site.register(Investor)
admin.site.register(Total_Investment)
