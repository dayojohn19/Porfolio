from django.urls import path
from . import views

app_name = "ubx"
urlpatterns = [
    path("", views.index, name="index"),
    path("add_new", views.add_ubx, name="add_new")
]
