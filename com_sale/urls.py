from django.urls import path
from . import views

app_name="sale"
urlpatterns = [
    path('', views.index, name="index"),
    path('order/<int:item_id>/<str:hashed>/<int:i_price>', views.order, name="order"),
    path('create', views.create, name="create"),
    path('item/<int:id>', views.item, name="item"),
    path('load', views.load, name="load")
]
