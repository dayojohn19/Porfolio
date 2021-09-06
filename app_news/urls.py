from django.urls import path

from . import views
app_name="news"
urlpatterns = [
    path("", views.index, name="index"),
    path("publish/", views.publish, name="publish"),
    path("section/<int:x>", views.section, name="section"),
]
