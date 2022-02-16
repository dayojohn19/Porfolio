from django.urls import path
from . import views

app_name = "trade"
urlpatterns = [
    path('', views.index, name="index"),
    path('fetch_old_data/<str:old_file>', views.fetch_old_data, name="fetch_data"),
    path('live', views.live_chart, name="live"),
    path('new_data/<str:what_coin>/<str:what_interval>',
         views.new_data, name="new_data"),
    path('primary', views.primary_chart, name="primary_chart"),
    path('primary_Live', views.primary_live, name="primary_live")

]
