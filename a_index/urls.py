from django.urls import path
from . import views

app_name="index"
urlpatterns = [
    path("", views.index, name="index"),
    path("social/", views.social, name="social"),
    path("colreg/", views.colreg, name="colreg"),
    path("blog/", views.blog, name="blog"),
]