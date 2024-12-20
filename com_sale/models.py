from django.db import models
import datetime
# Create your models here.
class Item(models.Model):
    notavailable = models.BooleanField(default=False)
    listing_date = models.DateTimeField()
    paid_date = models.IntegerField()
    expiration_date = models.DateTimeField()

    title = models.CharField(max_length=64)
    owner = models.CharField(max_length=64)
    time = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    link2 = models.URLField(blank=True)
    link3 = models.URLField(blank=True)
    link4 = models.URLField(blank=True)
    link5 = models.URLField(blank=True)
    link6 = models.URLField(blank=True)
    link7 = models.URLField(blank=True)
    link8 = models.URLField(blank=True)
    link9 = models.URLField(blank=True)
    link10 = models.URLField(blank=True)
    description = models.CharField(max_length=64)
    price = models.IntegerField()
    category = models.CharField(max_length=64)
    orders = models.ManyToManyField('app_mail.User', default=None, blank=True, related_name="item_order")
    bought = models.IntegerField(default=0)
    
    @property
    def num_order(self):
        return self.orders.all().count()
    def __str__(self):
        return f"{self.title}"

class Order(models.Model):
    i_id = models.CharField(max_length=64)
    i_price = models.IntegerField(default=1)
    i_total_price = models.IntegerField(default=2)
    owner = models.CharField(max_length=64)
    user = models.ForeignKey('app_mail.User', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    select = models.URLField(blank=True)
    delivered = models.BooleanField(default=False)
    del_time = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField()
    qty = models.IntegerField()



class Wishlist(models.Model):
    user = models.ForeignKey('app_mail.User', on_delete=models.CASCADE)
    wish = models.ForeignKey('Item', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.wish)

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fancier')
    def __str__(self):
        return self.name


class Userimage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fancier_profiles')
    def __str__(self):
        return self.name
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location='/user/pigeons/')
