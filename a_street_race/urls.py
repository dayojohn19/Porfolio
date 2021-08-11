from django.urls import path
from . import views

app_name="street_race"
urlpatterns = [
    path("", views.index, name="index"),
    path("race", views.race, name="race"),
    path("create", views.create, name="create"),
    path("join", views.join, name="join"),
    path("fetch", views.fetch, name="fetch"),
    path("send", views.send, name="send")
    ]