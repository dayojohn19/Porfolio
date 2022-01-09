from django.urls import path
from . import views
from . import earthquake
from . import calendar_print, qrcode, speech


app_name = "application"
urlpatterns = [
    path("", views.application, name="application"),
    path("mail/", views.app_mail, name="mail"),
    path("earthquake/", earthquake.main, name="earthquake"),
    path("calendar/", calendar_print.calendar_print, name="calendar"),
    path("calendar/<int:y>", calendar_print.calendar_get, name="calendar_y"),
    # path("speech/", speech.main, name="speech"),
    path("qrcode/", qrcode.main, name="qrcode"),
    path("news/", views.news, name="news"),
    path("app_course_booking/", views.course_booking, name="course_booking"),
    # path("blog", views.blog, name="blog")
    # SENDING EMAIL  from STATIC/CONTACT_DEV/EMAIL.JS
    path("send/<str:contact>/<str:user_name>/<str:message>",
         views.sendit, name="sendit")
]
