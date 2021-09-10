from django.urls import path
from . import views

app_name="commerce"
urlpatterns = [
    path('', views.commerce, name="commerece"),
    path('auction', views.auction, name="auction"),
    path('last_name', views.last_name, name="last_name"),

]
