from django.urls import path

from . import views
app_name = "app_car"
urlpatterns = [
    path("", views.index, name="index"),
    path("refresh", views.refreshSchedules, name="refreshSchedule"),
    path("destination", views.destinations, name="destinations"),
    path("departure", views.departures, name="departure"),
    path("departureJSON", views.departuresJSON, name="departureJSON"),
    path("place/<int:id>/<int:currentMonth>/", views.place, name="place"),
    path("event/<int:id>/<int:currentMonth>/",
         views.PlaceAddEvent, name="event"),

    # PlaceAddEvent

]
