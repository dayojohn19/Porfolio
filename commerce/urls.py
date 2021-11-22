from django.urls import path
from . import views

app_name = "commerce"
urlpatterns = [
    path('', views.commerce, name="commerce"),
    path('auction', views.auction, name="auction"),
    path('sale', views.sale, name="sale"),
    path('load', views.load, name="load")
]
