from django.urls import path

from . import views

app_name= "bank"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:csrf_token>/a", views.account, name="account"),
    path("<str:csrf_token>/s", views.schedule, name="schedule"),
    path("<str:csrf_token>/m", views.manager, name="manager"),
    path("<str:csrf_token>", views.client, name="client"),
]
