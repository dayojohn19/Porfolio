from django.urls import path
from . import views

app_name = "trade"
urlpatterns = [
    path('', views.index, name="index"),
    path('fetch_data', views.fetch_datas, name="fetch_data"),
]
