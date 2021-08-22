from django.urls import path
from . import views
from . import earthquake
from . import calendar_print


app_name="application"
urlpatterns = [
    path("", views.application, name="application"),
    path("mail/", views.app_mail, name="mail"),
    path("earthquake/", earthquake.main, name="earthquake"),
    path("calendar/", calendar_print.calendar_print , name="calendar"),
    path("calendar/<int:y>", calendar_print.calendar_get , name="calendar_y"),

]