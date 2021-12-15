from django.urls import path

from . import views
app_name = "freedive"
urlpatterns = [
    path("", views.index, name="index"),
    path("events", views.events, name="events"),
    path("socials", views.socials, name="socials"),
    path("home", views.home, name="home"),
    path("community", views.community, name="community"),
]
