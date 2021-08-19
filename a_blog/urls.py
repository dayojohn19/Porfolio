from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path("", views.index, name="index"),
    path('new_blog/', views.save_blog, name="new_blog"),
    path("get_blog/", views.get_blog, name="get_blog")
]