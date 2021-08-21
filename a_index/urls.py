from django.urls import path
from . import views
from . import earthquake

app_name="index"
urlpatterns = [
    path("", views.index, name="index"),
    path("social/", views.social, name="social"),
    path("colreg/", views.colreg, name="colreg"),
    path("blog/", views.blog, name="blog"),
    path("map/", views.map, name="map"),
    path("games/", views.games, name="games"),
    path("application/", views.application, name="application"),
    path("application/mail", views.app_mail, name="mail"),
    path("application/earthquake", earthquake.main, name="earthquake")
]