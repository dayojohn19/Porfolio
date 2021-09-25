from django.urls import path
from . import views

app_name="sale"
urlpatterns = [
    path('', views.index, name="index"),
    path('order/<int:item_id>/<str:hashed>/<int:i_price>', views.order, name="order"),
    path('create', views.create, name="create"),
    path('item/<int:id>', views.item, name="item"),
    # path('load', views.load, name="load"),
    path('mylist', views.mylist, name="mylist"),
    path('myorder', views.myorder, name="myorder"),
    path('mybuyer', views.mybuyer, name="mybuyer"),
    path('sale/register', views.register_view, name="register"),
    path('sale/login', views.login_view, name="login"),
    path('sale/logout', views.logout_view, name="logout"),
    path('sale/<int:category>', views.category, name="category"),
    path('<int:id>/<str:csrf_token>/update_create', views.update_create, name="update_create"),
]
