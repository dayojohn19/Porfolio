
from django.urls import path
from . import views

# from django.conf.urls import url
app_name = 'social_network'
urlpatterns = [
    path("", views.index, name="index"),


    ###
    path("in2", views.index2, name="index2"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("submit", views.postit, name="submit"),
    path("<str:username>", views.upost, name="users"),

    path("<str:post_id>/delete", views.delete, name="delete"),
    ## path("<int:postid>", views.liked_post, name="like-post"),
    path("<int:post_id>/like", views.like, name="likes"), 
    path("following/<int:post_id>/like", views.like, name="likes"), 
    path("posts/<int:post_id>/edit", views.edit, name="edit"),
    path("following/<str:username>", views.following, name="following")

]
