from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.blog, name="index"),
    path("new_blog", views.index, name="post_blog"),
    path('new_blog/', views.save_blog, name="new_blog"),
    path("get_blog/", views.get_blog, name="get_blog")
]
