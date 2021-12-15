from django.urls import path
from . import views


app_name = "user"
urlpatterns = [
    path("", views.index, name="index"),
    path("l/", views.login_view, name="login"),
    path("lo/", views.logout_view, name="logout"),
    path("r/", views.register, name="register"),

    # add image
    path("upload/", views.pictures, name="upload"),
    path("uploaduser/", views.userpictures, name="uploaduser"),

    path("submit/", views.addpigeon, name="submit"),
    path("loadpigeon/<int:id>/", views.load_pigeon, name="loadpigeon"),

    path("player/<str:username>/", views.player, name="player"),
    path("pigeon/view_record/<int:pid>", views.view_record, name="view_record"),

    # coin
    path('last_name', views.last_name, name="last_name"),
    # print TRADING

    path('print', views.printit, name="printit"),
    path('userpage', views.user_page, name="userpage"),
    #
    path('order_it', views.Order_it, name="order_it"),
    path('js_order_it', views. Js_Order_it, name="js_order_it"),
    path('cancel_it', views.Cancel_it, name="cancel_it")
]
