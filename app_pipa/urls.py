from django.urls import path

from . import views
app_name = "pipa"
urlpatterns = [
    path("", views.index, name="index"),
]
