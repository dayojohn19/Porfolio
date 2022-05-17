from django.urls import path

from . import views
app_name = "ship_san_diego"
urlpatterns = [
    path("", views.index, name="index"),
    path("newPost", views.newPost, name="post"),
    path("readPost", views.readPost, name="read"),
    path("editPost", views.editPost, name="edit"),

    path("gallery", views.gallery, name="gallery"),
    path("gallery/comment/<int:id>", views.comment, name="comment"),
    path("view/<int:id>", views.view, name="view")
]
