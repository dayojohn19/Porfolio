from django.urls import path

from . import views
app_name = "freedive"
urlpatterns = [
    path("", views.index, name="index"),
    path("events", views.events, name="events"),
    path("socials", views.socials, name="socials"),
    path("home", views.home, name="home"),
    path("community", views.community, name="community"),

    path("add_event", views.add_event, name="add_event"),
    path("room/<int:room_id>", views.room, name="room"),
    path("JoinRoom/<int:room_id>",  views.join, name="join"),
    path("Participate/<str:side>/<int:room_id>",
         views.participate_chat, name="participate_chat"),
    path("Send/<int:room_id>", views.send, name="send")
]
