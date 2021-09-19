from django.urls import path
from . import views


app_name="index"
urlpatterns = [
    # path("<path:path>", views.path, name="path"),
    path("", views.index, name="index"),
    path("send", views.send, name="send"),
    path("social/", views.social, name="social"),
    path("colreg/", views.colreg, name="colreg"),
    path("games/", views.games, name="games"),
    path("s/", views.s, name="s"),
    path("fish/", views.fish, name="fish"),
    path("commerce/", views.commerce, name="commerce"),
]