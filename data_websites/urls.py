from django.urls import path
from . import views

app_name = "data_websites"

urlpatterns = [
    path("", views.index, name="index"),
    path("postMessage/", views.postMessage, name="sendMessage")
]
