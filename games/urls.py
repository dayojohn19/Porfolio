from django.urls import path
from . import views

app_name="games"
urlpatterns = [
    path("", views.index, name="index"),
    path("games/addition/", views.addition, name="addition"),
    path("games/color_game/", views.color_game, name="color_game"),
]