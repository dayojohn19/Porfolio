from django.urls import path

from . import views
app_name="food"
urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("cook", views.cook, name="cook")
]
