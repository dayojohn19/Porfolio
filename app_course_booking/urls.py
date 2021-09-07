from django.urls import path

from . import views
app_name="course_booking"
urlpatterns = [
    path("home/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("create_course/", views.create_course, name="create_course"),
    path("enroll/", views.enroll, name="enroll")
]
